from django import forms
from . import models


class ModelSelectForm(forms.Form):
      SelectBox = forms.ChoiceField()
      JSONFileField = forms.FileField()


#class KeibajouForm(forms.ModelForm):

#    class Meta:
#      model = Keibajou
       #SelectBox=forms.ChoiceField(empty_label='選択してください'),
       #InputJSON=forms.FileField(label= "Select a JSON File" )
