from checkbookprice.models import Photo
from django import forms

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
        widgets = {  # default값 변경시
            'image': forms.FileInput(attrs={'class': 'file','onchange':'imageView(this)'}),
        }
        labels = {
            'image':''
        }
