from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import loader
from .forms import *
import glob


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
    return redirect(show_image)

def show_image(request):
    image_list = []
    for filename in glob.glob("media/images/*.png"):
        image_list.append(filename)
    return render_to_response("l2l/show.html",{"images":image_list})