from django.shortcuts import render, redirect
from clonegram.models import Image


# Create your views here.
def image_list(request):
    images = Image.objects.all().values()
    return render(request, 'authy.html', {'images': images})


def like_image(request, id):
    image = Image.objects.get(pk=id)
    image.likes += 1
    image.save()
    return redirect('image_list')
