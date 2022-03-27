from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Avg,Sum,Count,OuterRef
from django.contrib.auth import get_user_model
from .models  import (Employee, Department,Kin, Attendance, Leave,SBU_Directorate,
                    Station,Unit,MKPD,SKPD,
                    KPI_Evalutation,KPIScorePenalty,KPIScoreRange,Designation,
                    Employment,
                    # GradeLevel,
                    Position,Bank,EmployeeType,KPD,Complaint)
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from .forms import (
    RegistrationForm,
    LoginForm,
    EmployeeForm,
    KinForm,
    DepartmentForm,
    AttendanceForm, 
    LeaveForm,
    EmploymentForm,
    NewEmployeeForm,
    UserForm,
    MKPDForm,
    SKPDForm,
    KPDForm,
    # RatingForm,
    KPI_EvalutationForm,
    ComplaintForm
    )
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin
from datetime import datetime



# Admin View Route

class Admin_Login_View(LoginView):
    model = get_user_model()
    form_class = LoginForm
    template_name = 'hrms/admin/authorize/adminlogin.html'
    
    def get_success_url(self):
        url = resolve_url('hrms:admin_dashboard')
        return url


 # Admin Board   
class Admin_Dashboard(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    template_name = 'hrms/admin/dashboard/admindashboard.html'
    login_url = 'hrms:admin_login'
    model = get_user_model()
    context_object_name = 'qset'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['reg_total'] = Employment.objects.all().count()
        context['emp_total'] = Employee.objects.all().count()
        context['employeetype_total'] = EmployeeType.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['design_total'] = Designation.objects.all().count()
        context['manager_count'] = SBU_Directorate.objects.all().count()
        context['station_count'] = Station.objects.all().count()
        context['unit_total'] = Unit.objects.all().count()
        # context['grade_total'] = GradeLevel.objects.all().count()
        context['position_total'] = Position.objects.all().count()
        context['bank_total'] = Bank.objects.all().count()    
        context['workers'] = Employee.objects.order_by('-emp_id')
        return context 


 # Admin Board   
class Admin_Setting(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    template_name = 'hrms/admin/dashboard/add-component.html'
    login_url = 'hrms:admin_login'
    model = get_user_model()
    context_object_name = 'qset'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['reg_total'] = Employment.objects.all().count()
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['manager_count'] = SBU_Directorate.objects.all().count()
        context['station_count'] = Station.objects.all().count()
        context['unit_total'] = Unit.objects.all().count()
        # context['grade_total'] = GradeLevel.objects.all().count()
        context['position_total'] = Position.objects.all().count()
        context['bank_total'] = Bank.objects.all().count() 
        context['design_total'] = Designation.objects.all().count()
        context['employeetype_total'] = EmployeeType.objects.all().count()
        context['kpisr_total'] = KPIScoreRange.objects.all().count()
        context['kpisp_total'] = KPIScorePenalty.objects.all().count()
        context['kpd_total'] = KPD.objects.all().count()
        return context



class Complaint_Report(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    template_name = "hrms/admin/dashboard/report-all.html"
    login_url = "hrms:admin_login"
    model = get_user_model()
    context_object_name = 'qset'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['reports'] = Complaint.objects.order_by("-id")

class Admin_Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:admin_login',permanent=True)