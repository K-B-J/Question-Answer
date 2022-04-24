from django import forms
from .models import *
from .helper_functions import *
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.conf import settings


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
    dob = forms.DateField(
        widget=DatePickerInput(format="%d/%m/%Y"),
        input_formats=settings.DATE_INPUT_FORMATS,
        label="Date of Birth",
    )

    class Meta:
        model = UserInfo
        fields = ["first_name", "last_name", "mobile_no", "gender", "email", "dob"]

    def clean(self):
        cleaned_data = super().clean()
        dob = cleaned_data.get("dob")
        if dob != None and not valid_adult(str(dob)):
            raise forms.ValidationError(
                {"dob": "Only adults have access to the website"}
            )
        return cleaned_data


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["answer"]
