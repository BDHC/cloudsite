#sigle upload forms.py
# from django import forms
# from .models import FileUpload

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = FileUpload
#         fields = ('file',)

#multiple upload forms.py
from django import forms
from django.forms import ClearableFileInput
from .models import FileUpload
class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('file',)
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }