from django.contrib.auth.models import User
from django import forms
from django.forms import fields

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username' : '아이디',
            'first_name' : '성',
            'last_name' : '이름',
            'email' : '이메일',    
            }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!')
        return cd['password2']

