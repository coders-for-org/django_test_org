from django import forms  
from aboutus.models import Employee, Lyrics


class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"


class LyricsForm(forms.ModelForm):  
    class Meta:  
        model = Lyrics  
        fields = "__all__"