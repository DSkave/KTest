from django import forms
from django.apps import apps

from .models import JsonData,Jockey
from KTest.settings import BASE_DIR,MEDIA_ROOT
import glob
import os


class ModelSelectForm(forms.ModelForm):
      class Meta:
            model = JsonData
            fields = ('json_data',)
            labels = "ファイルアップロード"


class ModelDataCrudForm(forms.Form):
    #変数
    MODEL_NAME=[]
    RADIO_CHOICE=[
                  [0,"ファイルインポート"],
                  [1,"モデル操作"]
                  ]
    #モデル名取得
    app_models = apps.get_app_config('KT1').get_models()
    for i in app_models:
          MODEL_NAME.append([i.__name__,i.__name__])

    file_lists = glob.glob(MEDIA_ROOT + '/model_data/*')
    for file_list in file_lists:
        file_list = os.path.basename(file_list)

        print(file_list)

    model_list = forms.ChoiceField(
        label='モデル',
        widget=forms.Select,
        choices=MODEL_NAME,
        required=True,)

    radio_select = forms.ChoiceField(
        label="操作",
        widget=forms.RadioSelect,
        choices=RADIO_CHOICE,
        required=True,)



#class KeibajouForm(forms.ModelForm):

#    class Meta:
#      model = Keibajou
       #SelectBox=forms.ChoiceField(empty_label='選択してください'),
       #InputJSON=forms.FileField(label= "Select a JSON File" )
