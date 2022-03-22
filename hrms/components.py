from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Avg,Sum,Count
from django.contrib.auth import get_user_model
from .models  import (Employee, Department,Kin, Attendance, Leave,SBU_Directorate,Station,Unit,MKPD,SKPD,KPI_Evalutation,
                      KPIScorePenalty,KPIScoreRange,EmployeeType,Designation,
                      Bank,
                    #   GradeLevel,
                      Position,Station,KPIScoreRange,
                      KPIScorePenalty,Employment,KPD)
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




#EmployeeType views
class EmployeeType_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/admin/component/employeetype/all-employtype.html'
    login_url = 'hrms:admin_login'
    model = EmployeeType
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employeetype_total'] = EmployeeType.objects.all().count()    
        context['employeetypes'] = EmployeeType.objects.order_by('-employeetype_id')
        return context

class EmployeeType_Detail(LoginRequiredMixin, DetailView):
    queryset = EmployeeType.objects.all()
    template_name = 'hrms/admin/component/employeetype/employtype_details.html'
    context_object_name = 'employeetype'
    login_url = 'hrms:admin_login'
    
class EmployeeType_New (LoginRequiredMixin,CreateView):
    model = EmployeeType
    template_name = 'hrms/admin/component/employeetype/add-employeetype.html'
    form_class = EmployeeTypeForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:employeetype_all')

class EmployeeType_Update(LoginRequiredMixin,UpdateView):
    model = EmployeeType
    template_name = 'hrms/admin/component/employeetype/add-employeetype.html'
    form_class = EmployeeTypeForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:employtype_all')


class EmployeeType_Delete(LoginRequiredMixin,DeleteView):
    model = EmployeeType
    template_name = 'hrms/admin/component/employeetype/employtype-delete.html'
    login_url = 'hrms:admin_login'   
    
    success_url = reverse_lazy('hrms:employeetype_all')
    pass





#SBU_DIRECTORATE views
class Directorate_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/sbu/all-sbu.html'
    login_url = 'hrms:admin_login'
    model = SBU_Directorate
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sbu_total'] = SBU_Directorate.objects.all().count()    
        context['sbus'] = SBU_Directorate.objects.order_by('-sbu_id')
        return context
    
    
class Directorate_Detail(LoginRequiredMixin, DetailView):
    queryset = SBU_Directorate.objects.all()
    template_name = 'hrms/admin/component/sbu/sbu_details.html'
    context_object_name = 'sbu'
    login_url = 'hrms:admin_login'
    
class Directorate_New (LoginRequiredMixin,CreateView):
    model = SBU_Directorate
    template_name = 'hrms/admin/component/sbu/add-sbu.html'
    form_class = DirectorateForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:sub_all')

class Directorate_Update(LoginRequiredMixin,UpdateView):
    model = SBU_Directorate
    template_name = 'hrms/admin/component/sbu/add-sbu.html'
    form_class = DirectorateForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:sbu_all')


class Directorate_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/sbu/sbu-delete.html'
    model = SBU_Directorate
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:sbu_all')
    pass


#Department views
class Department_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/dept/all-dept.html'
    login_url = 'hrms:admin_login'
    model = Department
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept_total'] = Department.objects.all().count()    
        context['depts'] = Department.objects.order_by('-dept_id')
        return context
    
    
class Department_Detail(LoginRequiredMixin,DetailView):
    queryset = Department.objects.all()
    template_name = 'hrms/admin/component/dept/dept_details.html'
    context_object_name = 'dept'
    login_url = 'hrms:admin_login'
    
class Department_New (LoginRequiredMixin,CreateView):
    model = Department
    template_name = 'hrms/admin/component/dept/add-dept.html'
    form_class = DepartmentForm
    login_url = 'hrms:admin_login'
    
    success_url = reverse_lazy('hrms:dept_all')

class Department_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/admin/component/dept/add-dept.html'
    form_class = DepartmentForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:dept_all')


class Department_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/dept/dept-delete.html'
    model = Department
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:dept_all')

#Unit views
class Unit_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/unit/all-units.html'
    login_url = 'hrms:admin_login'
    model = Unit
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unit_total'] = Unit.objects.all().count()    
        context['units'] = Unit.objects.order_by('-unit_id')
        return context
    
  
class Unit_Detail(LoginRequiredMixin,DetailView):
    queryset = Unit.objects.all()
    template_name = 'hrms/admin/component/unit/unit_details.html'
    context_object_name = 'unit'
    login_url = 'hrms:admin_login'
    
class Unit_New (LoginRequiredMixin,CreateView):
    model = Unit
    template_name = 'hrms/admin/component/unit/add-unit.html'
    form_class = UnitForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:unit_all')

class Unit_Update(LoginRequiredMixin,UpdateView):
    model = Unit
    template_name = 'hrms/admin/component/unit/add-unit.html'
    form_class = UnitForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:unit_all')


class Unit_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/unit/unit-delete.html'
    model = Unit
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:unit_all')
    pass


#Station views
class Station_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/station/all-stations.html'
    login_url = 'hrms:admin_login'
    model = Station
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_total'] = Station.objects.all().count()    
        context['stations'] = Station.objects.order_by('-station_id')
        return context

  
class Station_Detail(LoginRequiredMixin,DetailView):
    queryset = Station.objects.all()
    template_name = 'hrms/admin/component/station/station_details.html'
    context_object_name = 'station'
    login_url = 'hrms:admin_login'
    
class Station_New (LoginRequiredMixin,CreateView):
    model = Station
    template_name = 'hrms/admin/component/station/add-station.html'
    form_class = StationForm
    login_url = 'hrms:admin_login'
    
    success_url = reverse_lazy('hrms:station_all')

class Station_Update(LoginRequiredMixin,UpdateView):
    model = Station
    template_name = 'hrms/admin/component/station/add-station.html'
    form_class = StationForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:station_all')



class Station_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/station/station-delete.html'
    model = Station
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:station_all')



#Designation views
class Designation_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/design/all-design.html'
    login_url = 'hrms:admin_login'
    model = Designation
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['design_total'] = Designation.objects.all().count()    
        context['designs'] = Designation.objects.order_by('-design_id')
        return context

  
class Designation_Detail(LoginRequiredMixin,DetailView):
    queryset = Designation.objects.all()
    template_name = 'hrms/admin/component/design/design_details.html'
    context_object_name = 'design'
    login_url = 'hrms:admin_login'
    

    
class Designation_New (LoginRequiredMixin,CreateView):
    model = Designation
    template_name = 'hrms/admin/component/design/add-design.html'
    form_class = DesignationForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:design_all')

class Designation_Update(LoginRequiredMixin,UpdateView):
    model = Designation
    template_name = 'hrms/admin/component/add-design.html'
    form_class = DesignationForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:design_all')


class Designation_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/design/design-delete.html'
    model = Designation
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:design_all')
    pass



# #GradeLevel views
# class GradeLevel_Detail(LoginRequiredMixin, ListView):
#     context_object_name = 'employees'
#     template_name = 'hrms/department/single.html'
#     login_url = 'hrms:login'
#     def get_queryset(self): 
#         queryset = GradeLevel.objects.filter(department=self.kwargs['pk'])
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["dept"] = Designation.objects.get(pk=self.kwargs['pk']) 
#         return context
    
# class GradeLevel_New (LoginRequiredMixin,CreateView):
#     model = GradeLevel
#     template_name = 'hrms/admin/component/add-gradelevel.html'
#     form_class = GradeLevelForm
#     login_url = 'hrms:manager_login'

#     success_url = reverse_lazy('hrms:admin_setting')

# class GradeLevel_Update(LoginRequiredMixin,UpdateView):
#     model = GradeLevel
#     template_name = 'hrms/department/edit.html'
#     form_class = GradeLevelForm
#     login_url = 'hrms:login'
#     success_url = reverse_lazy('hrms:dashboard')


# class GradeLevel_Delete(LoginRequiredMixin,DeleteView):
#     pass


#Position views
class Position_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/position/all-positions.html'
    login_url = 'hrms:admin_login'
    model = Position
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['position_total'] = Position.objects.all().count()    
        context['positions'] = Position.objects.order_by('-position_code')
        return context

  
class Position_Detail(LoginRequiredMixin,DetailView):
    queryset = Position.objects.all()
    template_name = 'hrms/admin/component/position/position_details.html'
    context_object_name = 'position'
    login_url = 'hrms:admin_login'
    
class Position_New (LoginRequiredMixin,CreateView):
    model = Position
    template_name = 'hrms/admin/component/position/add-position.html'
    form_class = PositionForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:position_all')

class Position_Update(LoginRequiredMixin,UpdateView):
    model = Position
    template_name = 'hrms/admin/component/position/add-position.html'
    form_class = PositionForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:position_all')


class Position_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/position/position-delete.html'
    model = Position
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:position_all')
    pass



#Bank views
class Bank_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/bank/all-banks.html'
    login_url = 'hrms:admin_login'
    model = Bank
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bank_total'] = Bank.objects.all().count()    
        context['banks'] = Bank.objects.order_by('-bank_id')
        return context

  
class Bank_Detail(LoginRequiredMixin,DetailView):
    queryset = Bank.objects.all()
    template_name = 'hrms/admin/component/bank/bank-details.html'
    context_object_name = 'bank'
    login_url = 'hrms:admin_login'
    

  
class Bank_New (LoginRequiredMixin,CreateView):
    model = Bank
    template_name = 'hrms/admin/component/bank/add-bank.html'
    form_class = BankForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:bank_all')

class Bank_Update(LoginRequiredMixin,UpdateView):
    model = Bank
    template_name = 'hrms/admin/component/bank/add-bank.html'
    form_class = BankForm
    login_url = 'hrms:admin_login'
    
    success_url = reverse_lazy('hrms:bank_all')


class Bank_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/bank/bank_delete.html'
    model = Bank
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:bank_all')
    






#Position views
class KPD_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/kpd/all-kpd.html'
    login_url = 'hrms:admin_login'
    model = KPD
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kpd_total'] = KPD.objects.all().count()    
        context['kpds'] = KPD.objects.order_by('-kpd_id')
        return context

  
class KPD_Detail(LoginRequiredMixin,DetailView):
    queryset = KPD.objects.all()
    template_name = 'hrms/admin/component/kpd/kpd_details.html'
    context_object_name = 'kpd'
    login_url = 'hrms:admin_login'
    
class KPD_New (LoginRequiredMixin,CreateView):
    model = KPD
    template_name = 'hrms/admin/component/kpd/add-kpd.html'
    form_class = KPDForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:kpd_all')

class KPD_Update(LoginRequiredMixin,UpdateView):
    model = KPD
    template_name = 'hrms/admin/component/kpd/add-kpd.html'
    form_class = KPDForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:kpd_all')


class KPD_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/kpd/kpd-delete.html'
    model = KPD
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:kpd_all')


#KPIScoreRange  views
class KPISR_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/kpi/all-kpiSR.html'
    login_url = 'hrms:admin_login'
    model = KPIScoreRange
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kpisr_total'] = KPIScoreRange.objects.all().count()    
        context['kpisrs'] = KPIScoreRange.objects.order_by('-id')
        return context

  
class KPISR_Detail(LoginRequiredMixin,DetailView):
    queryset = KPIScoreRange.objects.all()
    template_name = 'hrms/admin/component/kpi/kpiSR_details.html'
    context_object_name = 'kpisr'
    login_url = 'hrms:admin_login'
    
class KPISR_New (LoginRequiredMixin,CreateView):
    model = KPIScoreRange
    template_name = 'hrms/admin/component/kpi/add-kpiscore-range.html'
    form_class = KPIScoreRangeForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:kpisr_all')

class KPISR_Update(LoginRequiredMixin,UpdateView):
    model = KPIScoreRange
    template_name = 'hrms/admin/component/kpi/add-kpiscore-range.html'
    form_class = KPIScoreRangeForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:kpisr_all')


class KPISR_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/kpi/kpiSR-delete.html'
    model = KPIScoreRange
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:kpisr_all')
    pass


#KPIScorePenalty  views
class KPISP_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/kpi/all-kpiSP.html'
    login_url = 'hrms:admin_login'
    model = KPIScoreRange
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kpisr_total'] = KPIScorePenalty.objects.all().count()    
        context['kpisrs'] = KPIScorePenalty.objects.order_by('-id')
        return context

  
class KPISP_Detail(LoginRequiredMixin,DetailView):
    queryset = KPIScorePenalty.objects.all()
    template_name = 'hrms/admin/component/kpi/kpiSP_details.html'
    context_object_name = 'kpisp'
    login_url = 'hrms:admin_login'
    
class KPISP_New (LoginRequiredMixin,CreateView):
    model = KPIScorePenalty
    template_name = 'hrms/admin/component/kpi/add-kpiscore-penalty.html'
    form_class = KPIScorePenaltyForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:kpisp_all')

class KPISP_Update(LoginRequiredMixin,UpdateView):
    model = KPIScorePenalty
    template_name = 'hrms/admin/component/kpi/add-kpiscore-penalty.html'
    form_class = KPIScorePenaltyForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:kpisp_all')


class KPISP_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/kpi/kpiSP-delete.html'
    model = KPIScorePenalty
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:kpisp_all')
    pass

#Employmentviews
class Employment_All(LoginRequiredMixin, ListView):
    template_name = 'hrms/admin/component/employment/all-employment.html'
    login_url = 'hrms:admin_login'
    model = Employment
    context_object_name = 'qset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employment_total'] = Employment.objects.all().count()    
        context['employments'] = Employment.objects.order_by('-employ_id')
        return context

  
class Employment_Detail(LoginRequiredMixin,DetailView):
    queryset = Employment.objects.all()
    template_name = 'hrms/admin/component/employment/employment-details.html'
    context_object_name = 'employment'
    login_url = 'hrms:admin_login'
    
class Employment_New (LoginRequiredMixin,CreateView):
    model = Employment
    template_name = 'hrms/admin/component/employment/add-employment.html'
    form_class = EmploymentForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:employment_all')

class Employment_Update(LoginRequiredMixin,UpdateView):
    model = Employment
    template_name = 'hrms/admin/component/employment/add-employment.html'
    form_class = EmploymentForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:employment_all')

class Employment_Delete(LoginRequiredMixin,DeleteView):
    template_name = 'hrms/admin/component/employment/employment-delete.html'
    model = Employment
    login_url = 'hrms:admin_login'
    
    
    success_url = reverse_lazy('hrms:employment_all')

# class SearchView(LoginRequiredMixin,TemplateView):
#     template_name = "hrms/admin/dashboard/employee-search.html"
#     context_object_name = "worker"
    
#     def get(self,request,*args,**kwargs):
#         q = request.GET.get("q", "")
#         self.results = Employment.objects.get(employ_id=q)
#         return super().get(request,*args,**kwargs)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(results=self.results,**kwargs)
#         return context
    
class SearchView(LoginRequiredMixin,ListView)     :
    template_name = 'hrms/admin/dashboard/employee-search.html'
    model = Employment
    context_object_name = 'workers'
    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            context = self.model.objects.filter(employ_id=query)
        else:
            context = self.model.objects.none()
        return context
        

#Employmentviews
class Evaluation_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = KPI_Evalutation.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = KPI_Evalutation.objects.get(pk=self.kwargs['pk']) 
        return context
    
# class Evaluation_New (LoginRequiredMixin,CreateView):
#     model = Employment
#     template_name = 'hrms/admin/component/add-employment.html'
#     form_class = KPI_EvalutationForm
#     login_url = 'hrms:admin_login'

#     success_url = reverse_lazy('hrms:admin_setting')

class Evaluation_Update(LoginRequiredMixin,UpdateView):
    model = KPI_Evalutation
    me = 'hrms/manager/coomponents/edit-kpi.html'
    form_class = KPI_EvalutationForm
    login_url = 'hrms:manager_login'
    success_url = reverse_lazy('hrms:manager_dashboard')


class Evaluation_Delete(LoginRequiredMixin,DeleteView):
    pass