from dataclasses import fields
from pyexpat import model
import uuid
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ticket_manager.models import Ticket



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = "__all__"
		ordering = ["-created"]


