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













# #Department views

# class Department_Detail(LoginRequiredMixin, ListView):
#     context_object_name = 'employees'
#     template_name = 'hrms/department/single.html'
#     login_url = 'hrms:login'
#     def get_queryset(self): 
#         queryset = Employee.objects.filter(department=self.kwargs['pk'])
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
#         return context
    
# class Department_New (LoginRequiredMixin,CreateView):
#     model = Department
#     template_name = 'hrms/department/create.html'
#     form_class = DepartmentForm
#     login_url = 'hrms:login'

# class Department_Update(LoginRequiredMixin,UpdateView):
#     model = Department
#     template_name = 'hrms/department/edit.html'
#     form_class = DepartmentForm
#     login_url = 'hrms:login'
#     success_url = reverse_lazy('hrms:dashboard')



#Attendance View
class Attendance_New (LoginRequiredMixin,CreateView):
    model = Attendance
    form_class = AttendanceForm
    login_url = 'hrms:login'
    template_name = 'hrms/attendance/create.html'
    success_url = reverse_lazy('hrms:attendance_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.localdate()
        pstaff = Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate())) 
        context['present_staffers'] = pstaff
        return context

class Attendance_Out(LoginRequiredMixin,View):
    login_url = 'hrms:login'

    def get(self, request,*args, **kwargs):

       user=Attendance.objects.get(Q(staff__id=self.kwargs['pk']) & Q(status='PRESENT')& Q(date=timezone.localdate()))
       user.last_out=timezone.localtime()
       user.save()
       return redirect('hrms:attendance_new')   

class LeaveNew (LoginRequiredMixin,CreateView, ListView):
    model = Leave
    template_name = 'hrms/leave/create.html'
    form_class = LeaveForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:leave_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leaves"] = Leave.objects.all()
        return context

class Payroll(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'hrms/payroll/index.html'
    login_url = 'hrms:login'
    context_object_name = 'stfpay'

# class RecruitmentNew (CreateView):
#     model = Recruitment
#     template_name = 'hrms/recruitment/index.html'
#     form_class = RecruitmentForm
#     success_url = reverse_lazy('hrms:recruitment')

# class RecruitmentAll(LoginRequiredMixin,ListView):
#     model = Recruitment
#     login_url = 'hrms:login'
#     template_name = 'hrms/recruitment/all.html'
#     context_object_name = 'recruit'

# class RecruitmentDelete (LoginRequiredMixin,View):
#     login_url = 'hrms:login'
#     def get (self, request,pk):
#      form_app = Recruitment.objects.get(pk=pk)
#      form_app.delete()
#      return redirect('hrms:recruitmentall', permanent=True)

class Pay(LoginRequiredMixin,ListView):
    model = Employee
    template_name = 'hrms/payroll/index.html'
    context_object_name = 'emps'
    login_url = 'hrms:login'
