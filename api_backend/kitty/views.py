from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from kitty.forms import KittyForm, UserForm
from kitty.models import Kitty
from kitty.serializers import KittySerializer
from django.middleware.csrf import get_token
# Create your views here.


def get_all_kitties():
    kitties = Kitty.objects.all().order_by('name')
    kitties_serializers = KittySerializer(kitties, many=True)
    return kitties_serializers.data


def index(request):
    kitties = get_all_kitties()
    return render(request, 'index.html', {'kitties': kitties})


def kitties_rest(request):
    kitties = get_all_kitties()
    return JsonResponse(kitties, safe=False)


def users_rest(request):
    return JsonResponse("Ok", safe=False)


def add_kitty_view(request):
    
     if request.method == 'POST':
         kitty_form = KittyForm(request.POST)
         if kitty_form.is_valid():
             kitty = kitty_form.save()
             return redirect('kitties')
     if request.method == 'GET':
         kitty_form = KittyForm()
         csrf_token = get_token(request)
         html_form = f"""
             <form method="post">
             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                 {kitty_form.as_p()}
                 <button type="submit">Submit</button>
             </form>
         """
         return HttpResponse(html_form)


class NewKittyView(CreateView):
    form_class = KittyForm
    template_name = 'form_kitty.html'
    success_url = '/index_kitties/'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_kitty.html'
    success_url = '/'