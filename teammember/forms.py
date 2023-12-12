from django import forms
from .models import Teammember

NUMS = [
        ('regular','Regular'),
        ('admin', 'Admin'),
        ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Teammember
        fields = "__all__"
        NUMS = forms.ChoiceField(widget=forms.RadioSelect(choices=NUMS))