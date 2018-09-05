from django.shortcuts import render,redirect
from django.core import serializers

from KTest.settings import BASE_DIR,MEDIA_ROOT
from . import models
from . import forms
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
#   tests = ['a','b','c']
#   for test in tests:
#       print(test)
   file_mei=[]
   #file_mei.append('a')
   file_lists = glob.glob(MEDIA_ROOT + '/model_data/*')
   for file_name in file_lists:
       file_name = os.path.basename(file_name)
       file_mei.append(file_name)

       print('test1:'+file_name)
   print(file_mei)
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
       'model_data':file_name,
   }

   return render(request,'KT1/ks_admin.html',admin_data)
