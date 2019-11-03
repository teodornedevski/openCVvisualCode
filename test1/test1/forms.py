from django import forms 
from .models import *
  
  #create a form where the  image will be uploaded
class Image(forms.ModelForm): 
  
    class Meta: 
        model = insertImage 
        fields = ['imageToBeProcessed'] 