from django import forms
from .models import TodoModel,FormModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'description']

class FormNameForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['formname']