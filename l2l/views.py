from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import *


def index(request):
    now = datetime.now()
    template = loader.get_template('l2l/index.html')
    context = {
        'iso': now.strftime("%Y-%m-%dT%H:%M:%S"),
        'now': now
    }
    return HttpResponse(template.render(context, request))


def upload_file(request):
    if request.method == "POST":
        form = image_upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = image_upload()
    return render(request, "l2l/images.html", {'form':form})

def success(request):
    return HttpResponse("sucessfully uploaded")