from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Q
from .models import Work, FeedbackForm, User, Collection, CollectionWork
from .forms import (
    FeedbackFormForm,
    UserRegistrationForm,
    UserLoginForm,
    WorkUploadForm,
    CollectionForm,
    UserProfileForm,
)


# Create your views here.


def main(request):
    return render(request, "main.html")


def about(request):
    return render(request, "about.html")


def works(request):
    search_query = request.GET.get("q", "")
    view_type = request.GET.get("view", "works")

    if view_type == "collections":
        items_list = Collection.objects.all().order_by("-created_at")

        if search_query:
            items_list = items_list.filter(
                Q(name__icontains=search_query)
                | Q(description__icontains=search_query)
                | Q(tags__icontains=search_query)
                | Q(created_by__name__icontains=search_query)
                | Q(created_by__surname__icontains=search_query)
            )

        paginator = Paginator(items_list, 12)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "collections": page_obj,
            "search_query": search_query,
            "view_type": view_type,
        }
    else:
        items_list = Work.objects.all().order_by("-date_published")

        if search_query:
            items_list = items_list.filter(
                Q(name__icontains=search_query)
                | Q(short_description__icontains=search_query)
                | Q(long_description__icontains=search_query)
                | Q(author__name__icontains=search_query)
                | Q(author__surname__icontains=search_query)
                | Q(tags__icontains=search_query)
            )

        paginator = Paginator(items_list, 12)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "works": page_obj,
            "search_query": search_query,
            "view_type": view_type,
        }

    return render(request, "works.html", context)


def work_detail(request, work_id):
    try:
        work = Work.objects.get(id=work_id)
    except Work.DoesNotExist:
        messages.error(request, "Работа не найдена.")
        return redirect("works")

    if not request.user.is_authenticated or work.author != request.user:
        work.views += 1
        work.save(update_fields=["views"])

    collections = [
        cw.collection for cw in work.work_collections.select_related("collection").all()
    ]

    context = {
        "work": work,
        "collections": collections,
    }

    return render(request, "work_detail.html", context)


@login_required(login_url="register")
def edit_work(request, work_id):
    try:
        work = Work.objects.get(id=work_id)
    except Work.DoesNotExist:
        messages.error(request, "Работа не найдена.")
        return redirect("works")

    if work.author != request.user:
        messages.error(request, "У вас нет прав для редактирования этой работы.")
        return redirect("work_detail", work_id=work_id)

    if request.method == "POST":
        form = WorkUploadForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Работа успешно обновлена!")
                return redirect("work_detail", work_id=work_id)
            except Exception as e:
                messages.error(
                    request,
                    "Произошла ошибка при обновлении работы. Попробуйте еще раз.",
                )
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = WorkUploadForm(instance=work)

    context = {
        "form": form,
        "work": work,
        "is_edit": True,
    }

    return render(request, "edit_work.html", context)


@login_required(login_url="register")
def delete_work(request, work_id):
    try:
        work = Work.objects.get(id=work_id)
    except Work.DoesNotExist:
        messages.error(request, "Работа не найдена.")
        return redirect("works")

    if work.author != request.user:
        messages.error(request, "У вас нет прав для удаления этой работы.")
        return redirect("work_detail", work_id=work_id)

    if request.method == "POST":
        try:
            work_name = work.name
            work.delete()
            messages.success(request, f'Работа "{work_name}" успешно удалена.')
            return redirect("works")
        except Exception as e:
            messages.error(
                request, "Произошла ошибка при удалении работы. Попробуйте еще раз."
            )
            return redirect("work_detail", work_id=work_id)

    context = {
        "work": work,
    }

    return render(request, "delete_work.html", context)


@login_required(login_url="register")
def like_work(request, work_id):
    try:
        work = Work.objects.get(id=work_id)
    except Work.DoesNotExist:
        messages.error(request, "Работа не найдена.")
        return redirect("works")

    if work.author == request.user:
        messages.warning(request, "Вы не можете лайкнуть свою собственную работу.")
        return redirect("work_detail", work_id=work_id)

    work.likes += 1
    work.save(update_fields=["likes"])
    messages.success(request, "Спасибо за лайк!")

    return redirect("work_detail", work_id=work_id)


def profile(request, user_id=None):
    profile_user = request.user
    if user_id:
        profile_user = User.objects.get(id=user_id)

    if (
        request.method == "POST"
        and request.user.is_authenticated
        and request.user.role == "administrator"
    ):
        if request.POST.get("action") == "set_manager_role":
            make_manager = request.POST.get("make_manager") == "1"
            try:
                if make_manager:
                    profile_user.role = "manager"
                else:
                    profile_user.role = "user"
                profile_user.save()
            except Exception:
                pass
            from django.urls import reverse

            return redirect(reverse("user_profile", args=[profile_user.id]))

    user_works = Work.objects.filter(author=profile_user).order_by("-date_published")
    total_works = user_works.count()
    total_views = user_works.aggregate(models.Sum("views"))["views__sum"] or 0
    total_likes = user_works.aggregate(models.Sum("likes"))["likes__sum"] or 0
    is_own_profile = request.user.is_authenticated and request.user == profile_user
    context = {
        "profile_user": profile_user,
        "user_works": user_works,
        "total_works": total_works,
        "total_views": total_views,
        "total_likes": total_likes,
        "is_own_profile": is_own_profile,
    }
    return render(request, "profile.html", context)


@login_required(login_url="register")
def edit_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Профиль успешно обновлен!")
                return redirect("profile")
            except Exception as e:
                messages.error(
                    request,
                    "Произошла ошибка при обновлении профиля. Попробуйте еще раз.",
                )
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        "form": form,
    }

    return render(request, "edit_profile.html", context)


def feedback(request):
    if request.method == "POST":
        form = FeedbackFormForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    "Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.",
                )
                return redirect("feedback")
            except Exception as e:
                messages.error(
                    request,
                    "Произошла ошибка при отправке сообщения. Попробуйте еще раз.",
                )
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = FeedbackFormForm()

    context = {
        "form": form,
    }

    return render(request, "feedback.html", context)


def contacts(request):
    return render(request, "contacts.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect("main")

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.name}!")
            return redirect("main")
        else:
            messages.error(request, "Неверный email или пароль.")
    else:
        form = UserLoginForm()

    context = {
        "form": form,
    }

    return render(request, "login.html", context)


def user_register(request):
    if request.user.is_authenticated:
        return redirect("main")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(
                    request, f"Аккаунт успешно создан! Добро пожаловать, {user.name}!"
                )
                return redirect("main")
            except Exception as e:
                messages.error(
                    request,
                    "Произошла ошибка при создании аккаунта. Попробуйте еще раз.",
                )
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }

    return render(request, "register.html", context)


def user_logout(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы.")
    return redirect("main")


@login_required(login_url="register")
def upload(request):
    if request.method == "POST":
        form = WorkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                work = form.save(commit=False)
                work.author = request.user
                work.save()
                messages.success(request, "Ваша научная работа успешно опубликована!")
                return redirect("works")
            except Exception as e:
                messages.error(
                    request,
                    "Произошла ошибка при публикации работы. Попробуйте еще раз.",
                )
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = WorkUploadForm()

    context = {
        "form": form,
    }

    return render(request, "upload.html", context)


def faq(request):
    return render(request, "faq.html")


def is_manager(user):
    """Check if user is a manager or administrator"""
    return user.is_authenticated and (user.role in ["manager", "administrator"])


@login_required(login_url="register")
@user_passes_test(is_manager, login_url="main")
def manager_panel(request):
    """Manager panel for managing collections and feedback"""
    collections = Collection.objects.filter(created_by=request.user).order_by(
        "-created_at"
    )

    feedbacks = FeedbackForm.objects.filter(
        Q(status="new") | (Q(status="processing") & Q(processing_by=request.user))
    ).order_by("-date_submitted")

    if request.method == "POST":
        if request.POST.get("action") == "process_feedback":
            feedback_id = request.POST.get("feedback_id")
            try:
                feedback = FeedbackForm.objects.get(id=feedback_id, status="new")
                feedback.status = "processing"
                feedback.processing_by = request.user
                from django.utils import timezone

                feedback.processing_started_at = timezone.now()
                feedback.save()
                from django.urls import reverse

                return redirect(reverse("feedback_detail", args=[feedback.id]))
            except FeedbackForm.DoesNotExist:
                pass

    context = {
        "collections": collections,
        "feedbacks": feedbacks,
    }

    return render(request, "manager_panel.html", context)


@login_required(login_url="register")
@user_passes_test(is_manager, login_url="main")
def create_collection(request):
    """Create a new collection"""
    if request.method == "POST":
        form = CollectionForm(request.POST, request.FILES)
        selected_works = request.POST.getlist("works")

        if form.is_valid():
            try:
                collection = form.save(commit=False)
                collection.created_by = request.user
                collection.save()

                for work_id in selected_works:
                    try:
                        work = Work.objects.get(id=work_id)
                        CollectionWork.objects.get_or_create(
                            collection=collection, work=work, added_by=request.user
                        )
                    except Work.DoesNotExist:
                        pass

                messages.success(
                    request, f'Коллекция "{collection.name}" успешно создана!'
                )
                return redirect("manager_panel")
            except Exception as e:
                messages.error(request, "Произошла ошибка при создании коллекции.")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = CollectionForm()

    available_works = Work.objects.all().order_by("-date_published")

    context = {
        "form": form,
        "available_works": available_works,
    }

    return render(request, "create_collection.html", context)


@login_required(login_url="register")
@user_passes_test(is_manager, login_url="main")
def manage_collection(request, collection_id):
    """Manage a specific collection"""
    try:
        collection = Collection.objects.get(id=collection_id, created_by=request.user)
    except Collection.DoesNotExist:
        messages.error(request, "Коллекция не найдена.")
        return redirect("manager_panel")

    if request.method == "POST":
        action = request.POST.get("action")
        work_id = request.POST.get("work_id")
        selected_works = request.POST.getlist("selected_works")

        if action == "add_work":
            if selected_works:
                added_count = 0
                for work_id in selected_works:
                    try:
                        work = Work.objects.get(id=work_id)
                        CollectionWork.objects.get_or_create(
                            collection=collection, work=work, added_by=request.user
                        )
                        added_count += 1
                    except Work.DoesNotExist:
                        messages.error(request, f"Работа с ID {work_id} не найдена.")

                if added_count > 0:
                    if added_count == 1:
                        messages.success(request, f"1 работа добавлена в коллекцию.")
                    else:
                        messages.success(
                            request, f"{added_count} работ добавлено в коллекцию."
                        )
            else:
                messages.warning(
                    request, "Пожалуйста, выберите хотя бы одну работу для добавления."
                )

        elif action == "remove_work" and work_id:
            try:
                collection_work = CollectionWork.objects.get(
                    collection=collection, work_id=work_id
                )
                collection_work.delete()
                messages.success(request, "Работа удалена из коллекции.")
            except CollectionWork.DoesNotExist:
                messages.error(request, "Работа не найдена в коллекции.")

        elif action == "delete_collection":
            collection_name = collection.name
            collection.delete()
            messages.success(request, f'Коллекция "{collection_name}" удалена.')
            return redirect("manager_panel")

    collection_works = CollectionWork.objects.filter(
        collection=collection
    ).select_related("work")

    works_in_collection = [cw.work.id for cw in collection_works]
    available_works = Work.objects.exclude(id__in=works_in_collection).order_by(
        "-date_published"
    )

    context = {
        "collection": collection,
        "collection_works": collection_works,
        "available_works": available_works,
    }

    return render(request, "manage_collection.html", context)


def view_collection(request, collection_id):
    """Public view of a collection for all users"""
    try:
        collection = Collection.objects.get(id=collection_id)
    except Collection.DoesNotExist:
        messages.error(request, "Коллекция не найдена.")
        return redirect("works")

    collection_works = CollectionWork.objects.filter(
        collection=collection
    ).select_related("work")

    context = {
        "collection": collection,
        "collection_works": collection_works,
    }

    return render(request, "view_collection.html", context)


@login_required(login_url="register")
@user_passes_test(is_manager, login_url="main")
def edit_collection(request, collection_id):
    """Edit a collection"""
    try:
        collection = Collection.objects.get(id=collection_id, created_by=request.user)
    except Collection.DoesNotExist:
        messages.error(request, "Коллекция не найдена.")
        return redirect("manager_panel")

    if request.method == "POST":
        form = CollectionForm(request.POST, request.FILES, instance=collection)
        selected_works = request.POST.getlist("works")

        if form.is_valid():
            try:
                form.save()

                CollectionWork.objects.filter(collection=collection).delete()

                for work_id in selected_works:
                    try:
                        work = Work.objects.get(id=work_id)
                        CollectionWork.objects.get_or_create(
                            collection=collection, work=work, added_by=request.user
                        )
                    except Work.DoesNotExist:
                        pass

                messages.success(
                    request, f'Коллекция "{collection.name}" успешно обновлена!'
                )
                return redirect("manager_panel")
            except Exception as e:
                messages.error(request, "Произошла ошибка при обновлении коллекции.")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = CollectionForm(instance=collection)

    available_works = Work.objects.all().order_by("-date_published")

    selected_work_ids = [
        cw.work.id for cw in CollectionWork.objects.filter(collection=collection)
    ]

    context = {
        "form": form,
        "collection": collection,
        "available_works": available_works,
        "selected_work_ids": selected_work_ids,
    }

    return render(request, "edit_collection.html", context)


@login_required(login_url="register")
@user_passes_test(is_manager, login_url="main")
def manager_edit_work(request, work_id):
    """Manager can edit any work"""
    try:
        work = Work.objects.get(id=work_id)
    except Work.DoesNotExist:
        messages.error(request, "Работа не найдена.")
        return redirect("manager_panel")

    if request.method == "POST":
        form = WorkUploadForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Работа успешно обновлена!")
                return redirect("work_detail", work_id=work_id)
            except Exception as e:
                messages.error(request, "Произошла ошибка при обновлении работы.")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = WorkUploadForm(instance=work)

    context = {
        "form": form,
        "work": work,
        "is_manager_edit": True,
    }

    return render(request, "edit_work.html", context)


@login_required(login_url="register")
@user_passes_test(is_manager, login_url="main")
def manager_delete_work(request, work_id):
    """Manager can delete any work"""
    try:
        work = Work.objects.get(id=work_id)
    except Work.DoesNotExist:
        messages.error(request, "Работа не найдена.")
        return redirect("manager_panel")

    if request.method == "POST":
        try:
            work_name = work.name
            work.delete()
            messages.success(request, f'Работа "{work_name}" успешно удалена.')
            return redirect("manager_panel")
        except Exception as e:
            messages.error(request, "Произошла ошибка при удалении работы.")
            return redirect("work_detail", work_id=work_id)

    context = {
        "work": work,
        "is_manager_delete": True,
    }

    return render(request, "delete_work.html", context)


@login_required(login_url="register")
@user_passes_test(is_manager, login_url="main")
def feedback_detail(request, feedback_id):
    from django.shortcuts import get_object_or_404

    feedback = get_object_or_404(FeedbackForm, id=feedback_id)

    if request.method == "POST":
        if (
            request.POST.get("action") == "process_feedback"
            and feedback.status == "new"
        ):
            feedback.status = "processing"
            feedback.processing_by = request.user
            from django.utils import timezone

            feedback.processing_started_at = timezone.now()
            feedback.save()
            from django.urls import reverse

            return redirect(reverse("feedback_detail", args=[feedback.id]))
        if (
            request.POST.get("action") == "resolve_feedback"
            and feedback.status == "processing"
            and feedback.processing_by == request.user
        ):
            feedback.status = "resolved"
            from django.utils import timezone

            feedback.processing_ended_at = timezone.now()
            feedback.save()
            from django.contrib import messages

            messages.success(request, "Обращение отмечено как завершенное.")
            from django.urls import reverse

            return redirect(reverse("manager_panel"))

    context = {
        "feedback": feedback,
    }
    return render(request, "feedback_detail.html", context)


@login_required(login_url="register")
@user_passes_test(lambda u: u.role == "administrator", login_url="main")
def admin_panel(request):
    user_search = request.GET.get("user_search", "").strip()
    users = User.objects.all().order_by("surname", "name")
    if user_search:
        users = users.filter(
            Q(name__icontains=user_search)
            | Q(surname__icontains=user_search)
            | Q(email__icontains=user_search)
        )

    status_filter = request.GET.get("status")
    manager_filter = request.GET.get("manager")
    feedbacks = (
        FeedbackForm.objects.select_related("processing_by")
        .all()
        .order_by("-date_submitted")
    )
    if status_filter:
        feedbacks = feedbacks.filter(status=status_filter)
    if manager_filter:
        feedbacks = feedbacks.filter(processing_by_id=manager_filter)

    if request.method == "POST" and request.POST.get("action") == "set_manager_role":
        user_id = request.POST.get("user_id")
        make_manager = request.POST.get("make_manager") == "1"
        try:
            user = User.objects.get(id=user_id)
            if make_manager:
                user.role = "manager"
            else:
                user.role = "user"
            user.save()
        except User.DoesNotExist:
            pass
        from django.urls import reverse

        return redirect(reverse("admin_panel"))

    managers = User.objects.filter(role="manager")
    context = {
        "users": users,
        "feedbacks": feedbacks,
        "managers": managers,
        "status_filter": status_filter,
        "manager_filter": manager_filter,
        "user_search": user_search,
    }
    return render(request, "admin_panel.html", context)


@login_required(login_url="register")
@user_passes_test(lambda u: u.role == "administrator", login_url="main")
def admin_feedback_detail(request, feedback_id):
    from django.shortcuts import get_object_or_404

    feedback = get_object_or_404(FeedbackForm, id=feedback_id)
    context = {
        "feedback": feedback,
    }
    return render(request, "admin_feedback_detail.html", context)
