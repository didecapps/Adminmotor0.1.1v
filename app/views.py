# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext
#from models import User
from django.http import HttpResponse 

def home(recuest):
	#usuarios = User.object.all()
	template="index.html"
	return render_to_response(template,locals())
