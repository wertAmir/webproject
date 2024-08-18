from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models

def home (request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def members(request):
  mymembers = models.Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = models.Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))