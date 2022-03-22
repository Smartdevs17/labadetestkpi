from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Avg,Sum,Count,OuterRef
from django.contrib.auth import get_user_model
from .models  import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin




from hrms.components import *
from hrms.admin_view import *
from hrms.employee_view import *
from hrms.manager_view import *
from hrms.others import *
from hrms.auth import *
from datetime import datetime


# def index(request):
#     return render(request,"hrms/templates/hrms/home/home.html")

# Create your views here.












