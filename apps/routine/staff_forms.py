from django import forms
from .models import *


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['program', 'title', 'description', 'uploads', 'due_date']

