from django.shortcuts import render,redirect
from django.core import serializers

from KTest.settings import BASE_DIR,MEDIA_ROOT
from . import models
from . import forms
from . import ksyslib
import inspect
import glob
import os

from django.http import HttpResponse


# Create your views here.
def index(request):

    myapp_data = {
        'app_name':request.resolver_match.app_name,
        #'model_name':models.Jockey._meta.object_name,
        'class_names':list(map(lambda x:x[0],inspect.getmembers(models, inspect.isclass))),
        #'model_fields':Jockey._meta.get_fields(),

    }

    return render(request, 'KT1/index2.html',myapp_data)

def ks_admin(request):
   file_info={}
   file_mei=[]
   file_create_T=[]
   file_update_T=[]

   if request.method =='POST':
       if 'del_button' in request.POST:
           print("削除ボタンを押した")
           print(request.POST)
           result = models.JsonData.objects.filter(json_data__contains=request.POST['del_button'])
           count = models.JsonData.objects.filter(json_data__icontains=request.POST['del_button']).count()
           print("件数：",count)
           for instance in result:
               print("queryset test:",instance.json_data)


   file_lists = glob.glob(MEDIA_ROOT + '/model_data/*')
   for file_name in file_lists:
       print('file name:'+file_name)
       print('file create time:',ksyslib.file_create_time(file_name))
       print('file update time:', ksyslib.file_update_time(file_name))
       file_create_T.append(ksyslib.file_create_time(file_name))
       file_update_T.append(ksyslib.file_update_time(file_name))
       file_name = os.path.basename(file_name)
       file_mei.append(file_name)

      # file_update_T.append(ksyslib.file_update_time(file_name))
   mf = forms.ModelDataCrudForm()

   form = forms.ModelSelectForm(data=request.POST,files=request.FILES)
   if form.is_valid():
       form.save()
       print('VALID')
       return redirect('KT1:Ksadmin')

   print('NOT VALID')
   j_data = serializers.serialize("json",models.Jockey.objects.all())
   admin_data={
       'class_names': list(map(lambda x: x[0], inspect.getmembers(models, inspect.isclass))),
       'form': form,
       'json_d':j_data,#JSONアウトプットテスト
       'media_root': os.path.join(BASE_DIR,'media'),
       'model_fd': mf,
       'model_data':file_mei,
       'file_create_time':file_create_T,
       'file_update_time':file_update_T,
   }

   return render(request,'KT1/ks_admin.html',admin_data)
