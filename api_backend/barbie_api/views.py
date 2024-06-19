from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from barbie_api.forms import BarbieForm, UserForm 
from barbie_api.models import Barbie
from barbie_api.serializers import BarbieSerializer
from django.middleware.csrf import get_token
# Create your views here.

def get_all_barbies():
    barbies = Barbie.objects.all().order_by('number')
    barbie_serializers = BarbieSerializer(barbies, many=True)
    return barbie_serializers.data


def index(request):
    barbies = get_all_barbies()
    return render(request, 'index.html', {'barbies': barbies})


def barbies_rest(request):
    barbies = get_all_barbies()
    return JsonResponse(barbies, safe=False)


def users_rest(request):
    return JsonResponse("Ok", safe=False)


def add_barbie_view(request):
    
     if request.method == 'POST':
         barbie_form = BarbieForm(request.POST)
         if barbie_form.is_valid():
             barbie = barbie_form.save()
             return redirect('barbies')
     if request.method == 'GET':
         barbie_form = BarbieForm()
         csrf_token = get_token(request)
         html_form = f"""
             <form method="post">
             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                 {barbie_form.as_p()}
                 <button type="submit">Submit</button>
             </form>
         """
         return HttpResponse(html_form)

class NewBarbieView(CreateView):
    form_class = BarbieForm
    template_name = 'form_barbie.html'
    success_url = '/index_barbies/'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_barbie.html'
    success_url = '/'
