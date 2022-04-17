from django import forms
from .models import *


class UserInfoForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        label="First Name",
    )
    last_name = forms.CharField(
        max_length=50,
        label="Last Name",
    )
    mobile_no = forms.CharField(
        max_length=20,
        label="Mobile Number",
    )
    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    email = forms.EmailField(label="Email ID")

    class Meta:
        model = UserInfo
        fields = ["first_name", "last_name", "mobile_no", "gender", "email"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
