from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import FeedbackForm, User, Work, Collection


class FeedbackFormForm(forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = ['name', 'email', 'phone', 'student_number', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш e-mail',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона',
                'required': True
            }),
            'student_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер, если есть'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Опишите ваш вопрос или предложение',
                'required': True
            })
        }
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'phone': 'Номер телефона',
            'student_number': 'Номер студента или преподавателя',
            'description': 'Описание'
        }
        help_texts = {
            'student_number': '(необязательно)'
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Basic phone validation - you can enhance this
        if phone and len(phone.replace(' ', '').replace('-', '').replace('+', '')) < 10:
            raise forms.ValidationError('Введите корректный номер телефона')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # You can add additional email validation here if needed
        return email


class WorkUploadForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['name', 'short_description', 'long_description', 'tags', 'cover_image', 'pdf_file']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название научной работы',
                'required': True
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание работы (до 300 символов)',
                'required': True,
                'maxlength': 300
            }),
            'long_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Полное описание работы, включая цели, методы, результаты и выводы',
                'required': True
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'математика, физика, исследование',
                'required': False
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'id': 'cover-upload'
            }),
            'pdf_file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf',
                'id': 'pdf-upload'
            })
        }
        labels = {
            'name': 'Название работы',
            'short_description': 'Краткое описание',
            'long_description': 'Полное описание',
            'tags': 'Теги/Категории',
            'cover_image': 'Обложка работы',
            'pdf_file': 'PDF файл'
        }
        help_texts = {
            'name': 'Укажите четкое и информативное название вашей научной работы',
            'short_description': 'Краткое описание для предварительного просмотра (максимум 300 символов)',
            'long_description': 'Подробное описание работы, включая цели, методы исследования, результаты и выводы',
            'tags': 'Введите теги через запятую для категоризации работы (например: математика, физика, исследование)',
            'cover_image': 'Загрузите изображение обложки (JPG, PNG, до 5 МБ)',
            'pdf_file': 'Загрузите PDF файл вашей работы (необязательно, максимум 10 МБ)'
        }

    def clean_short_description(self):
        short_description = self.cleaned_data.get('short_description')
        if len(short_description) > 300:
            raise forms.ValidationError('Краткое описание не должно превышать 300 символов')
        return short_description

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 10:
            raise forms.ValidationError('Название работы должно содержать минимум 10 символов')
        return name

    def clean_cover_image(self):
        cover_image = self.cleaned_data.get('cover_image')
        if cover_image:
            # Check file size (5MB limit)
            if cover_image.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError('Размер изображения не должен превышать 5 МБ')
            
            # Check file extension
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            file_extension = cover_image.name.lower()
            if not any(file_extension.endswith(ext) for ext in allowed_extensions):
                raise forms.ValidationError('Разрешены только изображения (JPG, PNG, GIF)')
        
        return cover_image

    def clean_pdf_file(self):
        pdf_file = self.cleaned_data.get('pdf_file')
        if pdf_file:
            # Check file size (10MB limit)
            if pdf_file.size > 10 * 1024 * 1024:  # 10MB in bytes
                raise forms.ValidationError('Размер файла не должен превышать 10 МБ')
            
            # Check file extension
            if not pdf_file.name.lower().endswith('.pdf'):
                raise forms.ValidationError('Разрешены только PDF файлы')
        
        return pdf_file


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description', 'cover_image', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название коллекции',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опишите коллекцию, её цели и содержание',
                'required': False
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'id': 'collection-cover-upload'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'математика, физика, исследование',
                'required': False
            })
        }
        labels = {
            'name': 'Название коллекции',
            'description': 'Описание',
            'cover_image': 'Обложка коллекции',
            'tags': 'Теги/Категории'
        }
        help_texts = {
            'name': 'Укажите четкое и информативное название коллекции',
            'description': 'Подробное описание коллекции, её целей и содержания',
            'cover_image': 'Загрузите изображение обложки (JPG, PNG, до 5 МБ)',
            'tags': 'Введите теги через запятую для категоризации коллекции (например: математика, физика, исследование)'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 5:
            raise forms.ValidationError('Название коллекции должно содержать минимум 5 символов')
        return name

    def clean_cover_image(self):
        cover_image = self.cleaned_data.get('cover_image')
        if cover_image:
            # Check file size (5MB limit)
            if cover_image.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError('Размер изображения не должен превышать 5 МБ')
            
            # Check file extension
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            file_extension = cover_image.name.lower()
            if not any(file_extension.endswith(ext) for ext in allowed_extensions):
                raise forms.ValidationError('Разрешены только изображения (JPG, PNG, GIF)')
        
        return cover_image


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'пароль',
            'required': True
        })
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'подтвердите пароль',
            'required': True
        })
    )

    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'student_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'имя',
                'required': True
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'фамилия',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e-mail',
                'required': True
            }),
            'student_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'номер студента',
                'required': True
            })
        }
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'email': 'Электронная почта',
            'student_number': 'Номер студента'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'e-mail',
            'required': True
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'пароль',
            'required': True
        })
    )

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if email and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Неверный email или пароль')
            else:
                self.confirm_login_allowed(self.user_cache)
        
        return self.cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'student_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'имя',
                'required': True
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'фамилия',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e-mail',
                'required': True
            }),
            'student_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'номер студента',
                'required': True
            })
        }
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'email': 'Электронная почта',
            'student_number': 'Номер студента'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if email is already taken by another user
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Этот email уже используется другим пользователем')
        return email 