from django import forms
from .models import JsonData,Jockey
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
    FOOD_CHOICES = (
        ('apple', 'りんご'),
        ('beef', '牛肉'),
        ('bread', 'パン'),
    )

    D_TEST =[
             ['penis','ペニス'],
             ['chimpo','ちんぽ']
            ]

    file_lists = glob.glob(MEDIA_ROOT + '/model_data/*')
    for file_list in file_lists:
        file_list = os.path.basename(file_list)

        print(file_list)

    model_file = forms.ChoiceField(
        label='データファイルリスト',
        widget=forms.CheckboxSelectMultiple,
        choices=D_TEST,
        required=True,)

#class KeibajouForm(forms.ModelForm):

#    class Meta:
#      model = Keibajou
       #SelectBox=forms.ChoiceField(empty_label='選択してください'),
       #InputJSON=forms.FileField(label= "Select a JSON File" )
