
from django.shortcuts import render


from .form import ImageForm
from .models import Image
# Create your views here.
import json
def index(request):
    cale_json = 'image/static/users.json'

    with open(cale_json) as json_file:
        data = json.load(json_file)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'index.html', {'obj': obj, 'data': data[0]})
        else:
            img = Image.objects.all()
            return render(request, 'index.html', {'img': img, 'form': form, 'data': data[0]})
    else:  # For GET requests
        form = ImageForm()
        img = Image.objects.all()
        return render(request, 'index.html', {'img': img, 'form': form, 'data': data[0]})

def dataset(request):
    cale_json = 'image/static/users.json'

    with open(cale_json) as json_file:
        data = json.load(json_file)

    return render(request, 'dataset.html', {'data': data})
