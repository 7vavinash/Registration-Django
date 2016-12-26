from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#start your code here
class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		def save(self, commit=True):
			user = super(UserCreateForm, self).save(commit=False)
			user.email = self.cleaned_data('email')

			if commit:
				user.save()
			return user




class LogInForm(forms.Form):
	username = forms.CharField(label='User Name')
	password = forms.CharField(label='Password', widget = forms.PasswordInput())