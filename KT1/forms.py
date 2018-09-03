from django import forms
from .models import JsonData
from KTest.settings import BASE_DIR,MEDIA_ROOT
import glob
import os



class ModelSelectForm(forms.ModelForm):
 #     json_file = forms.FileField()

      class Meta:
            model = JsonData
            fields = ('json_data',)
 #           excludes = ('json_data',)


class ModelDataCrudForm(forms.Form):
    file_lists = glob.glob(MEDIA_ROOT + '/model_data/*')
    for file_list in file_lists:
        file_list = os.path.basename(file_list)
        print(file_list)

    model_file = forms.ChoiceField(
        label='モデル用データファイル名',
        widget=forms.SelectMultiple,
#        choices=file_list,
        required=True,)

#class KeibajouForm(forms.ModelForm):

#    class Meta:
#      model = Keibajou
       #SelectBox=forms.ChoiceField(empty_label='選択してください'),
       #InputJSON=forms.FileField(label= "Select a JSON File" )
