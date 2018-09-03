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

   file_lists = glob.glob(MEDIA_ROOT + '/model_data/*')
   for file_list in file_lists:
       file_list=os.path.basename(file_list)
       print(file_list)

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
       'model_fd': mf
   }

   return render(request,'KT1/ks_admin.html',admin_data)
