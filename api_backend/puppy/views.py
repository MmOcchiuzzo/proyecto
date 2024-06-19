from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from puppy.forms import PuppyForm, UserForm
from puppy.models import Puppy
from puppy.serializers import PuppySerializer
from django.middleware.csrf import get_token
# Create your views here.


def get_all_puppies():
    puppies = Puppy.objects.all().order_by('name')
    puppies_serializers = PuppySerializer(puppies, many=True)
    return puppies_serializers.data


def index(request):
    puppies = get_all_puppies()
    return render(request, 'index_puppies.html', {'puppies': puppies})


def puppies_rest(request):
    puppies = get_all_puppies()
    return JsonResponse(puppies, safe=False)


def users_rest(request):
    return JsonResponse("Ok", safe=False)


def add_puppy_view(request):
    
     if request.method == 'POST':
         puppy_form = PuppyForm(request.POST)
         if puppy_form.is_valid():
             puppy = puppy_form.save()
             return redirect('puppies')
     if request.method == 'GET':
         puppy_form = PuppyForm()
         csrf_token = get_token(request)
         html_form = f"""
             <form method="post">
             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                 {puppy_form.as_p()}
                 <button type="submit">Submit</button>
             </form>
         """
         return HttpResponse(html_form)


class NewPuppyView(CreateView):
    form_class = PuppyForm
    template_name = 'form_puppy.html'
    success_url = '/index_puppies/'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_puppy.html'
    success_url = '/'
