from pydoc import classname
from django import forms
from .models import News
import re #регулярные выражение
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',help_text='Максимум 150 символов', widget=forms.TextInput(attrs={"class": "form-control"}))    
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget= forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget= forms.PasswordInput(attrs={"class": "form-control"}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))    
    password = forms.CharField(label='Пароль', widget= forms.PasswordInput(attrs={"class": "form-control"}))

class NewsForm(forms.ModelForm):   #СВЯЗАННЫЕ С МОДЕЛЮ
    class Meta:
        model = News
        #fields = "__all__"
        fields = ['title', 'content', 'is_pablished', 'photo', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content' : forms.Textarea(attrs={"class": "form-control", "row": 8}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'photo': forms.FileInput()
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={"class": "form-control"}))  
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={"class": "form-control", "rows": 7}))  
    captcha = CaptchaField()


# from django import forms
# from .models import Category


# class NewsForm(forms.Form):   НЕ СВЯЗАННЫЕ С МОДЕЛЮ
#     title = forms.CharField(max_length=150, label='Назва ние ', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label="Описание ", required=False, widget=forms.Textarea(
#         attrs={
#             "class": "form-control",
#             "rows": 8,    
#         }))
#     is_pablished = forms.BooleanField(label="Опубликовано?", required=False, initial=True)
#     category = forms.ModelChoiceField(empty_label="Выберите категорию", label="Категория ", queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))