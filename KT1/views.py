from django.shortcuts import render
from django.core import serializers
from . import models
from . import forms
import inspect

from django.http import HttpResponse


# Create your views here.
def index(request):

    myapp_data = {
        'app_name':request.resolver_match.app_name,
        #'model_name':models.Jockey._meta.object_name,
        'class_names':list(map(lambda x:x[0],inspect.getmembers(models, inspect.isclass))),
        #'model_fields':Jockey._meta.get_fields(),

    }

    return render(request, 'KT1/index.html',myapp_data)

def ks_admin(request):
   form = forms.ModelSelectForm()
   #J_data = serializers.serialize("json",models.Jockey.objects.all())
   j_data = serializers.serialize("json",models.Jockey.objects.all())
   admin_data={
       'class_names': list(map(lambda x: x[0], inspect.getmembers(models, inspect.isclass))),
       'form': form,
       'json_d':j_data,#JSONアウトプットテスト
   }

   return render(request,'KT1/ks_admin.html',admin_data)
