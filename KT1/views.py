from django.shortcuts import render
from . import models
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

#def model_edit(request):

