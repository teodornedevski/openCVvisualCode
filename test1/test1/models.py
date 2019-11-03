#insertImage definition
from django.db import models


class insertImage(models.Model): 
    imageToBeProcessed = models.ImageField(upload_to='images/') 