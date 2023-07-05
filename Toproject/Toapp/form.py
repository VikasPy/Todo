from django import forms
from .models import *

class todo_for(forms.ModelForm):
    class Meta:
      model=todo_box
      fields='__all__'
    