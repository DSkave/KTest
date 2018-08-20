from django import forms

class ModelInputForm(forms.Form):
    formdata = {
       'InputJSON':forms.FileField(label= "Select a JSON File" ),
    }