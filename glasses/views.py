from django.shortcuts import render, get_object_or_404
from .models import HomeModels, AboutModels, GalleryModels, BrandsModel, StoreModel, StoreGalleryModels, TechnologyModels, TechnologyDesModels
# Create your views here.

def home(request):
    query = HomeModels.objects.order_by('number')
    owl = BrandsModel.objects.order_by("number")[:8]
    gallery = GalleryModels.objects.all()[:6]

    context = {
        'query': query,
        'owl': owl,
        'gallery': gallery
    }

    return render(request, 'index.html', context)


def aboutus(request):
    query = get_object_or_404(AboutModels)
    context = {
        'query': query
    }
    return render(request, 'hakkimizda.html', context)

def brands(request):
    query = BrandsModel.objects.order_by("number")
    context = {
        'query': query
    }
    return render(request, 'markalarimiz.html', context)

def gallery(request):
    query = GalleryModels.objects.all()
    context = {
        'query': query
    }
    return render(request, 'galeri.html', context)

def store(request, id):
    query = get_object_or_404(StoreModel, id=id)
    store = StoreGalleryModels.objects.filter(magaza=id)

    context = {
        'query': query,
        'store': store,
    }
    return render(request, 'magazalarimiz.html', context)


def technology(request):
    query = TechnologyModels.objects.all()
    content = get_object_or_404(TechnologyDesModels)
    context = {
        'query': query,
        "content": content
    }

    return render(request, 'teknolojimiz.html',context)
