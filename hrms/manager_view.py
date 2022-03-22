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



import datetime





# print(datetime.date.today().month)











# Manager Route

# Manager login
class Manager_Login_View(LoginView):
    # model = get_user_model()
    # model = Manager
    form_class = LoginForm
    template_name = 'hrms/managerReg/login.html'

    def get_success_url(self):
        url = resolve_url('hrms:manager_dashboard')
        return url


class Manager_Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:manager_login',permanent=True)




# Manager Board   
class Manager_Dashboard(LoginRequiredMixin,ListView):
    # queryset = Employee.objects.select_related('position')
    # queryset = Employee.objects.get(id=emp_id)
    template_name = 'hrms/manager/managerdashboard.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        # context['emp_total'] = Employee.objects.all().count()
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        context['task_total'] = MKPD.objects.all().count()
        context['skpd_count'] = SKPD.objects.all().count()
        staff = Employment.objects.filter(department=user)
        skpd  = Employment.objects.filter(department=user).annotate(Count("staff",distinct=True))
        # kpis = KPIScorePenalty.objects.all()
        # print(kpis[0])

        context["manager"] = user

        context['staff_total'] = Employment.objects.filter(department=user).count()
        context["staffs"] = Employment.objects.filter(department=user)
        context['tasks'] = MKPD.objects.order_by('-mkpd_id')
        context['projects'] = KPI_Evalutation.objects.order_by('id')
        return context


# Manager Board   
class Manager_KPD(LoginRequiredMixin,ListView):
  
    template_name = 'hrms/manager/manager_kpd.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        # context['emp_total'] = Employee.objects.all().count()
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        context["manager"] = user
        context['kpds'] = KPD.objects.filter(Q(dept_id__dept_name=user)& Q(period__month=datetime.date.today().month)).order_by("kpd_id")
        context['projects'] = KPI_Evalutation.objects.order_by('id')
        return context



# Manager Board   
class Manager_Employee_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/members.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['task_total'] = MKPD.objects.all().count()
        context['skpd_count'] = SKPD.objects.all().count()
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        context["manager"] = user
        context['staff_total'] = Employment.objects.filter(department=user).count()
        context["staffs"] = Employment.objects.filter(department=user)
        context['tasks'] = MKPD.objects.order_by('-mkpd_id')
        context['projects'] = KPI_Evalutation.objects.order_by('id')
        return context
    
    
    
    
# Manager Board   
class Manager_Message_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/messages.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['staff_total'] = MKPD.objects.all().count()
        context['skpd_count'] = SKPD.objects.all().count()
        context['tasks'] = MKPD.objects.order_by('-mkpd_id')
        context['projects'] = KPI_Evalutation.objects.order_by('id')
        return context





#   Create Project
# class Create_Project_View(LoginRequiredMixin,CreateView):
#     model = SKPD
#     form_class  = SKPDForm
#     manager_url = 'hrms:manager_login'
#     template_name = 'hrms/manager/skpd/create-project.html'
#     success_url = reverse_lazy('hrms:manager_dashboard')
   
#     # def dispatch(self,*args,**kwargs):
#     #     return super(Create_Project_View,self).dispatch(*args,**kwargs)
    
#     def get_form_kwargs(self):
#         kwargs = super(Create_Project_View,self).get_form_kwargs()
#         kwargs['request'] = self.request
#         # kwargs.update({"user":self.request.user})
#         return kwargs
    
    # def get_form(self,form_class=None):
    #         form = super(Create_Project_View,self).get_form()
    #         user = get_object_or_404(Department,head_of_dept__user=self.request.user)
    #         form.fields["employee"] = Employment.objects.filter(department=user)
    #         # self.fields['employee'].widget = form.Select()
    #         return form

class Assign_Rating_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/assign-rating-table.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        # context['projects'] = KPI_Evalutation.objects.order_by('-mkpd_id')
        context['projects'] = KPI_Evalutation.objects.filter(Q(employee__employ_id=self.kwargs["pk"]) & Q(period__month=datetime.date.today().month)).order_by("week")
        return context


      


class Rating_View(LoginRequiredMixin,DetailView):
    model = MKPD
    template_name = 'hrms/manager/project_detail.html'
    login_url = 'hrms:manager_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = MKPD.objects.get(mkpd_id=self.object.pk)
            context["project"] = query
            return context
        except ObjectDoesNotExist:
            return context


class Employee_Report_View(LoginRequiredMixin,DetailView):
    model = Employment
    template_name = 'hrms/manager/employee-report.html'
    form_class = KPI_EvalutationForm
    login_url = 'hrms:manager_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = MKPD.objects.get(mkpd_id=self.object.pk)
            context["project"] = query
            return context
        except ObjectDoesNotExist:
            return context

#   KPI EVALUATION
class Evaluation_View(LoginRequiredMixin,CreateView):
    model = KPI_Evalutation
    form_class  = KPI_EvalutationForm
    manager_url = 'hrms:manager_login'
    template_name = 'hrms/manager/kpi_evaluation.html'
    
    success_url = reverse_lazy('hrms:manager_dashboard')
    
    
    def get_form_kwargs(self):
        kwargs = super(Evaluation_View,self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs





class Report_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/reports.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        try:
            # leaders = SKPD.objects.filter(task_submission__approved="APPROVED").annotate(total=Sum("task_submission__score")).order_by("-total")
            leaders = Employment.objects.filter(report__approved="APPROVED").annotate(total=Sum("report__score"))
            tasks = Employment.objects.filter(report__approved="APPROVED").annotate(total=Sum("report__score"))
            # print(tasks[0].report.all())
            # ratings = MKPD.objects.filter(submissions__approved="APPROVED").annotate(Average=Sum("submissions__score"))
            # print(ratings)
            context["kpi_count"] = KPI_Evalutation.objects.all().count()
            kpis = KPIScorePenalty.objects.all()
            print(kpis[0])
            # leaders = User.objects.filter(~Q(submissions=None)).filter(submissions__status="approved").annotate(total=Sum("submissions__task__points")).order_by("-total")
            context["employees"] = leaders
            return context
        except ObjectDoesNotExist:
            return context


 # Admin Board   
class Manager_Setting(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/setting.html'
    login_url = 'hrms:manager_login'
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
        context['kpd_total'] = KPD.objects.all().count()
        return context



class Employee_Report_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/reports.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        try:
            leaders = SKPD.objects.filter(task_submission__approved="APPROVED").annotate(total=Sum("task_submission__score")).order_by("-total")
            # print(leaders)
            context["kpi_count"] = KPI_Evalutation.objects.all().count()
            # leaders = User.objects.filter(~Q(submissions=None)).filter(submissions__status="approved").annotate(total=Sum("submissions__task__points")).order_by("-total")
     
            context["employees"] = leaders
            return context
        except ObjectDoesNotExist:
            return context




class Employee_Evaluation(CreateView):
    model = KPI_Evalutation  
    form_class = KPI_EvalutationForm  
    # template_name = 'hrms/employee/create.html'
    
    success_url = reverse_lazy('hrms:manager_login')








class Manager_Employee_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/admin/dashboard/employee-all.html'
    model = Employee
    login_url = 'hrms:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['reg_total'] = Employment.objects.all().count()
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.all().count()
        context['workers'] = Employment.objects.order_by('employ_id')
        return context

class Manager_Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:manager_login',permanent=True)
    
    
    


#Employmentviews
class SKPD_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/skpd/all-skpd.html'
    login_url = 'hrms:manager_login'
    model = SKPD
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skpd_total'] = SKPD.objects.all().count()   
        admin = get_object_or_404(Employment,employee__user=self.request.user) 
        # print(admin.department)
        dept = SKPD.objects.filter(dept=admin.department).annotate(total=Count("kpd")).order_by('-employee')
        # print(dept[0].total)
        total = Employment.objects.filter(staff__employee__department=admin.department).annotate(total=Sum("staff__weight"))
        print(total[0].staff)
        # for items in list(total[0].staff):
        #     print(items)
        context['projects'] = SKPD.objects.filter(dept=admin.department).order_by('-employee')
        return context

  
class SKPD_Detail(LoginRequiredMixin,DetailView):
    queryset = SKPD.objects.all()
    template_name = 'hrms/manager/skpd/skpd-details.html'
    context_object_name = 'skpd'
    login_url = 'hrms:manager_login'
    
class SKPD_New(LoginRequiredMixin,CreateView):
    model = SKPD
    template_name = 'hrms/manager/skpd/add-skpd.html'
    form_class = SKPDForm
    # login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:employee_skpd')
    
    def get_form_kwargs(self):
        kwargs = super(SKPD_New,self).get_form_kwargs()
        kwargs['request'] = self.request
        # kwargs.update({"user":self.request.user})
        return kwargs

class SKPD_Update(LoginRequiredMixin,UpdateView):
    model = SKPD
    template_name = 'hrms/manager/skpd/add-skpd.html'
    form_class = SKPDForm
    login_url = 'hrms:manager_login'
    success_url = reverse_lazy('hrms:skpd_all')
    
    def get_form_kwargs(self):
        kwargs = super(SKPD_Update,self).get_form_kwargs()
        kwargs['request'] = self.request
        # kwargs.update({"user":self.request.user})
        return kwargs
    
class SKPD_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/manager/skpd/skpd-delete.html'
    model = SKPD
    login_url = 'hrms:manager_login'
    
    
    success_url = reverse_lazy('hrms:skpd_all')
    
    
# #Employmentviews
# class Evalutation_All(LoginRequiredMixin,ListView):
#     template_name = 'hrms/manager/evalutation/all-evaluation.html'
#     login_url = 'hrms:manager_login'
#     model = KPI_Evalutation 
#     context_object_name = 'qset'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = get_object_or_404(Department,head_of_dept__user=self.request.user)
#         skpd  = Employment.objects.filter(department=user).annotate(total=Count("staff",distinct=True))
#         # print(skpd[2])
#         context['skpd_total'] = Employment.objects.filter(department=user).annotate(total=Count("staff",distinct=True)).count()    
#         context['staffs'] = Employment.objects.filter(department=user).annotate(total=Count("staff",distinct=True)).order_by('-employ_id')
#         return context



#Employmentviews
class Evalutation_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/evalutation/all-evaluation.html'
    login_url = 'hrms:manager_login'
    model = KPI_Evalutation 
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        context['staffs'] = Employment.objects.filter(department=user)
        # context['staffs'] = MKPD.objects.filter(employee__department=user).order_by('-mkpd_id')
        return context
    
class Evalutation_All_Details(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/evalutation/eva-all-details.html'
    login_url = 'hrms:manager_login'
    model = KPI_Evalutation 
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        # print(skpd[2])
        context["staff"] = Employment.objects.get(employ_id=self.kwargs["pk"])
        staff =  Employment.objects.get(employ_id=self.kwargs["pk"])
        # print(staff)
        context['projects'] = MKPD.objects.filter(Q(employee__employ_id=self.kwargs["pk"]) & Q(period__month=datetime.date.today().month)).order_by("week")
        return context
      
    
      
class Evalutation_Detail(LoginRequiredMixin,DetailView):
    queryset = KPI_Evalutation .objects.all()
    template_name = 'hrms/manager/evaluation/evaluation-details.html'
    context_object_name = 'report'
    login_url = 'hrms:manager_login'
    
class Evalutation_New(LoginRequiredMixin,CreateView):
    model = KPI_Evalutation 
    template_name = 'hrms/manager/evalutation/add-evaluation.html'
    form_class = KPI_EvalutationForm
    # login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:eva_all')
    
    # def get_form_kwargs(self):
    #     kwargs = super(Evalutation_New,self).get_form_kwargs()
    #     kwargs['pk'] = self.object
    #     # kwargs.update({"user":self.request.user})
    #     return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        # print(skpd[2])
        context["staff"] = MKPD.objects.get(mkpd_id=self.kwargs["pk"])
        staff =   MKPD.objects.get(mkpd_id=self.kwargs["pk"])
        # print(staff.employee.employee.first_name)
        # context['projects'] = MKPD.objects.filter(Q(employee__employ_id=self.kwargs["pk"]) & Q(period__month=datetime.date.today().month)).order_by("week")
        return context
    
    def form_valid(self,form,**kwargs):
        staff =  MKPD.objects.get(mkpd_id=self.kwargs["pk"])
        form.instance.mkpd = staff
        form.instance.employee = staff.employee
        form.instance.skpd = staff.skpd
        form.instance.week = staff.week
        form.instance.period = staff.period
        return super().form_valid(form)
    
class Evalutation_Update(LoginRequiredMixin,UpdateView):
    model = KPI_Evalutation 
    template_name = 'hrms/manager/evalutation/add-evaluation.html'
    form_class = KPI_EvalutationForm
    login_url = 'hrms:manager_login'
    success_url = reverse_lazy('hrms:eva_all')

class Evalutation_Delete(DeleteView):
    template_name = 'hrms/manager/evalutation/evaluation-delete.html'
    model = KPI_Evalutation 
    login_url = 'hrms:manager_login'
    
    
    success_url = reverse_lazy('hrms:eva_all')
    
# class Evalutation_New(FormView):
#     model = KPI_Evalutation 
#     template_name = 'hrms/manager/skpd/add-skpd.html'
#     form_class = KPI_EvalutationForm
#     # login_url = 'hrms:manager_login'

#     success_url = reverse_lazy('hrms:eva_all')
    
    
#Employmentviews
class EvalutationView(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/evaluation/all-evaluation.html'
    login_url = 'hrms:manager_login'
    model = KPI_Evalutation 
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_total'] = KPI_Evalutation.objects.all().count()    
        context['reports'] = KPI_Evalutation.objects.order_by('-id')
        return context
    
def load_depts(request):
    sbu_id = request.GET.get('sbu_id')
    unit_id = request.GET.get('unit_id')
    # print(sbu_id)
    depts = Unit.objects.filter(dept_id=sbu_id).order_by('unit_id')
    # print(depts)
    return render(request, 'hrms/manager/dept_dropdown_list_options.html', {'depts': depts})
    # return JsonResponse(list(depts.values("unit_id","unit_name")),safe=False)
    
def load_units(request):
    unit_id = request.GET.get('unit_id')
    print(unit_id)
    units = Employment.objects.filter(unit=unit_id).order_by('employee')
    # print(depts)
    return render(request, 'hrms/manager/unit_dropdown_list_options.html', {'units': units})
    # return JsonResponse(list(depts.values("unit_id","unit_name")),safe=False)
    
    
# class MKPD_All(LoginRequiredMixin,ListView):
#     queryset = SKPD.objects.select_related('staff_kpd')
#     template_name = 'hrms/manager/mkpd/all-mkpd.html'
#     manager_url = 'hrms:manager_login'
#     context_object_name = 'qset' 
               
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs) 
#         try:
#             staff_kpd = SKPD.objects.filter(employee__employee=self.kwargs["pk"])
#             # staff_kpd = KPD.objects.filter(staff_kpd__employee__employee=self.kwargs["pk"]).annotate(total=Sum("staff_kpd__weight"))
#             staff_weight = KPD.objects.filter(staff_kpd__employee__employee=self.kwargs["pk"]).aggregate(total=Sum("staff_kpd__weight"))
#             # staff = Employment.objects.all().annotate(total=Count("staff__kpd"))
#             staff = Employment.objects.get(employee=self.kwargs["pk"])
#             # print(staff_kpd[0].expected_time_of_delivery)
#             # print(staff)
#             context["staff"] = Employment.objects.get(employee=self.kwargs["pk"])
#             context["projects"] =  SKPD.objects.filter(employee__employee=self.kwargs["pk"])
#             context["total"] = KPD.objects.filter(staff_kpd__employee__employee=self.kwargs["pk"]).aggregate(total=Sum("staff_kpd__weight"))
#             return context
#         except ObjectDoesNotExist:
#             return context
 
class MKPD_All(LoginRequiredMixin,ListView):
    queryset = SKPD.objects.select_related('staff_kpd')
    template_name = 'hrms/manager/mkpd/all-mkpd.html'
    manager_url = 'hrms:manager_login'
    context_object_name = 'qset' 
               
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        try:
            # staff_kpd = Employment.objects.filter(staff__employee=self.kwargs["pk"]).values()
            # staff_kpd = KPD.objects.filter(staff_kpd__employee__employee=self.kwargs["pk"]).annotate(total=Sum("staff_kpd__weight"))
            # staff_weight = KPD.objects.filter(staff_kpd__employee__employee=self.kwargs["pk"]).aggregate(total=Sum("staff_kpd__weight"))
            # staff = Employment.objects.all().annotate(total=Count("staff__kpd"))
            # staff = Employment.objects.get(employee=self.kwargs["pk"])
            # print(staff_kpd[0])
            # print(staff)
            context["staff"] = Employment.objects.filter(employee=self.kwargs["pk"])
            context["projects"] =  SKPD.objects.filter(employee__employee=self.kwargs["pk"])
            # context["projects"] =  Employment.objects.filter(staff__employee=self.kwargs["pk"])
            context["total"] = KPD.objects.filter(staff_kpd__employee__employee=self.kwargs["pk"]).aggregate(total=Sum("staff_kpd__weight"))
            return context
        except ObjectDoesNotExist:
            return context
        
                
# Manager Board   
class Employee_SKPD(LoginRequiredMixin,ListView):
    # queryset = Employee.objects.select_related('position')
    # queryset = Employee.objects.get(id=emp_id)
    template_name = 'hrms/manager/mkpd/mkpd-details.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        # context['emp_total'] = Employee.objects.all().count()
        context['task_total'] = MKPD.objects.all().count()
        context['skpd_count'] = SKPD.objects.all().count()
        # context['workers'] = Employee.objects.order_by('-id')
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        # print(user.dept_name)
        # print(get_object_or_404(Department,head_of_dept__user=self.request.user))
        # print(Employment.objects.filter(department__head_of_dept__user=self.request.user))
        context["manager"] = user
        # context["manager"] = Employment.objects.filter(employee__employee__user=self.request.user)
        # context['project_count'] = Project.objects.all().count()
        # staff = Employment.objects.filter(department=user)
        # print(staff)
        context['staff_total'] = Employment.objects.filter(department=user).count()
        context["staffs"] = Employment.objects.filter(department=user)
        context['tasks'] = MKPD.objects.order_by('-mkpd_id')
        context['projects'] = KPI_Evalutation.objects.order_by('id')
        return context
    
    
    
    
class Staff_Kpd_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/evalutation/home-eva.html'
    login_url = 'hrms:manager_login'
    model = KPI_Evalutation 
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        context['skpd_total'] = Employment.objects.filter(department=user)
        context['staffs'] = MKPD.objects.filter(employee__department=admin.department).order_by('-mkpd_id')
        return context

class Staff_Kpd_All_Detail(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/evalutation/all-evaluation.html'
    login_url = 'hrms:manager_login'
    model = KPI_Evalutation 
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        skpd  = Employment.objects.filter(department=user).annotate(total=Count("staff",distinct=True))
        # print(skpd[2])
        context["staff"] = Employment.objects.filter(employee=self.kwargs["pk"])
        context['projects'] = MKPD.objects.filter(employee__employee=self.kwargs["pk"])
        return context
    
# class Staff_Kpd_All(LoginRequiredMixin,ListView):
#     template_name = 'hrms/manager/evalutation/all-evaluation.html'
#     login_url = 'hrms:manager_login'
#     model = KPI_Evalutation 
#     context_object_name = 'qset'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = get_object_or_404(Department,head_of_dept__user=self.request.user)
#         skpd  = Employment.objects.filter(department=user).annotate(total=Count("staff",distinct=True))
#         # print(skpd[2])
#         context['skpd_total'] = Employment.objects.filter(department=user).annotate(total=Count("staff",distinct=True)).count()    
#         context['staffs'] = MKPD.objects.filter(employee__department=admin.department).annotate(total=Count("staff",distinct=True)).order_by('-employ_id')
#         return context
  
class Staff_Kpd_Detail(DetailView):
    queryset = KPI_Evalutation .objects.all()
    template_name = 'hrms/manager/evaluation/evaluation-details.html'
    context_object_name = 'report'
    login_url = 'hrms:manager_login'
    
class Staff_Kpd_New(CreateView):
    model = KPI_Evalutation 
    template_name = 'hrms/manager/evaluation/add-evaluation.html'
    form_class = KPI_EvalutationForm
    # login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:eva_all')
    
    def get_form_kwargs(self):
        kwargs = super(SKPD_New,self).get_form_kwargs()
        kwargs['request'] = self.request
        # kwargs.update({"user":self.request.user})
        return kwargs

class Staff_Kpd_Update(UpdateView):
    model = KPI_Evalutation 
    template_name = 'hrms/manager/evaluation/add-evaluation.html'
    form_class = KPI_EvalutationForm
    login_url = 'hrms:manager_login'
    success_url = reverse_lazy('hrms:eva_all')

class Staff_Kpd_Delete(DeleteView):
    template_name = 'hrms/manager/evaluation/evaluation-delete.html'
    model = KPI_Evalutation 
    login_url = 'hrms:manager_login'
    
    
    success_url = reverse_lazy('hrms:eva_all')
    
class Staff_Kpd_New(FormView):
    model = KPI_Evalutation 
    template_name = 'hrms/manager/skpd/add-skpd.html'
    form_class = KPI_EvalutationForm
    # login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:eva_all')
    
    
#Employmentviews
class EvalutationView(ListView):
    template_name = 'hrms/manager/evaluation/all-evaluation.html'
    login_url = 'hrms:manager_login'
    model = KPI_Evalutation 
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_total'] = KPI_Evalutation.objects.all().count()    
        context['reports'] = KPI_Evalutation.objects.order_by('-id')
        return context
    
def load_depts(request):
    sbu_id = request.GET.get('sbu_id')
    unit_id = request.GET.get('unit_id')
    # print(sbu_id)
    depts = Unit.objects.filter(dept_id=sbu_id).order_by('unit_id')
    # print(depts)
    return render(request, 'hrms/manager/dept_dropdown_list_options.html', {'depts': depts})
    # return JsonResponse(list(depts.values("unit_id","unit_name")),safe=False)
    
def load_units(request):
    unit_id = request.GET.get('unit_id')
    print(unit_id)
    units = Employment.objects.filter(unit=unit_id).order_by('employee')
    # print(depts)
    return render(request, 'hrms/manager/unit_dropdown_list_options.html', {'units': units})
    # return JsonResponse(list(depts.values("unit_id","unit_name")),safe=False)
    
    