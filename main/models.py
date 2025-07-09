from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(
        self, email, name, surname, student_number=None, role="user", password=None
    ):
        if not email:
            raise ValueError("Необходимо указать электронную почту")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            surname=surname,
            student_number=student_number,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, password=None, **extra_fields):
        extra_fields.setdefault("role", "administrator")
        user = self.create_user(email, name, surname, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ("user", "Пользователь"),
        ("manager", "Менеджер"),
        ("administrator", "Администратор"),
    ]
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Электронная почта", unique=True)
    student_number = models.CharField(
        "Номер студента", max_length=30, blank=True, null=True
    )
    role = models.CharField("Роль", max_length=20, choices=ROLE_CHOICES, default="user")
    date_joined = models.DateTimeField("Дата регистрации", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.surname} {self.name} ({self.email})"

    def save(self, *args, **kwargs):
        if not self.pk and not self.date_joined:
            from django.utils import timezone

            self.date_joined = timezone.now()
        super().save(*args, **kwargs)


class Collection(models.Model):
    name = models.CharField("Название коллекции", max_length=200)
    description = models.TextField("Описание", blank=True)
    cover_image = models.ImageField(
        "Обложка коллекции",
        upload_to="collections/covers/",
        blank=True,
        null=True,
        help_text="Загрузите изображение обложки для коллекции (необязательно)",
    )
    tags = models.CharField(
        "Теги/Категории",
        max_length=500,
        blank=True,
        null=True,
        help_text="Введите теги через запятую (например: математика, физика, исследование)",
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="collections",
        verbose_name="Создатель",
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField("Название работы", max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="works", verbose_name="Автор"
    )
    date_published = models.DateTimeField("Дата публикации", auto_now_add=True)
    short_description = models.CharField("Краткое описание", max_length=300)
    long_description = models.TextField("Полное описание")
    likes = models.PositiveIntegerField("Лайки", default=0)
    views = models.PositiveIntegerField("Просмотры", default=0)
    tags = models.CharField(
        "Теги/Категории",
        max_length=500,
        blank=True,
        null=True,
        help_text="Введите теги через запятую (например: математика, физика, исследование)",
    )
    cover_image = models.ImageField(
        "Обложка работы",
        upload_to="works/covers/",
        blank=True,
        null=True,
        help_text="Загрузите изображение обложки для вашей работы (необязательно)",
    )
    pdf_file = models.FileField(
        "PDF файл",
        upload_to="works/pdfs/",
        blank=True,
        null=True,
        help_text="Загрузите PDF файл вашей работы (необязательно)",
    )

    class Meta:
        verbose_name = "Научная работа"
        verbose_name_plural = "Научные работы"

    def __str__(self):
        return self.name


class CollectionWork(models.Model):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name="collection_works",
        verbose_name="Коллекция",
    )
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name="work_collections",
        verbose_name="Работа",
    )
    added_at = models.DateTimeField("Дата добавления", auto_now_add=True)
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="added_works",
        verbose_name="Добавил",
    )

    class Meta:
        verbose_name = "Работа в коллекции"
        verbose_name_plural = "Работы в коллекциях"
        unique_together = ["collection", "work"]
        ordering = ["-added_at"]

    def __str__(self):
        return f"{self.work.name} в коллекции {self.collection.name}"


class FeedbackForm(models.Model):
    name = models.CharField("Имя", max_length=50)
    email = models.EmailField("Электронная почта")
    phone = models.CharField("Телефон", max_length=30)
    student_number = models.CharField(
        "Номер студента", max_length=30, blank=True, null=True
    )
    description = models.TextField("Описание")
    date_submitted = models.DateTimeField("Дата отправки", auto_now_add=True)

    STATUS_CHOICES = [
        ("new", "Новая"),
        ("processing", "В обработке"),
        ("resolved", "Завершена"),
    ]
    status = models.CharField(
        "Статус", max_length=20, choices=STATUS_CHOICES, default="new"
    )
    processing_by = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="processing_feedbacks",
        verbose_name="Обрабатывает менеджер",
    )
    processing_started_at = models.DateTimeField(
        "Начало обработки", null=True, blank=True
    )
    processing_ended_at = models.DateTimeField(
        "Окончание обработки", null=True, blank=True
    )

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"

    def __str__(self):
        return f"{self.name} — {self.email} ({self.date_submitted:%d.%m.%Y})"
