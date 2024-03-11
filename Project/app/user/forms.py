from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from user.models import User

class UserLoginForm(AuthenticationForm): #Рассширенная версия формы которая проверяет все данные для  авторизации пользователя 
    class Meta:
        model = User
        fields = ['username', 'password']



class UserRegistForm(UserCreationForm):
    class Meta:
        model = User
        fields = ( #Данные которые будут отоброжаются в форме регистрации 
            "first_Name",
            "last_Name",
            "username",
            "email",
            "password1",
            "password2",
        )
    
    first_Name = forms.CharField()
    last_Name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserProfileForm(UserChangeForm):
     
    image = forms.ImageField()
    first_Name = forms.CharField()
    last_Name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
     
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",)






        
    