from django.contrib.auth import get_user_model
from .models import ( Employee,Department,Kin,Attendance, Leave,Unit,EmployeeType,
                    SBU_Directorate,Unit,Designation,Complaint,
                    # GradeLevel,
                    Position,Station,Bank,EmployeeType,KPIScorePenalty,
                    SKPD,MKPD,KPI_Evalutation,KPD,KPIScoreRange,Employment)
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.core import validators
from django.utils import timezone
from django.db.models import Q
import time
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django import forms
PERCENTAGE_VALIDATOR = [MinValueValidator(0),MaxValueValidator(100)]
from django.shortcuts import  get_object_or_404


class RegistrationForm (UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Confirm Password'}))
    # thumb = forms.ImageField(label='Attach a Passport Photograph',required=True,widget=forms.FileInput(attrs={'class':'form-control mt-2'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1', 'password2')

class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'Username Here'}))
#    email = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder':'Email'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'********'}))


class EmployeeTypeForm(forms.ModelForm):

    class Meta: 
        model = EmployeeType
        fields = "__all__"
        widgets={
            'employeetype_id': forms.TextInput(attrs={"placeholder":"Employee Type ID"}),
            'employeetype':forms.TextInput(),
        }

class DirectorateForm(forms.ModelForm):

    class Meta:
        model = SBU_Directorate
        fields = "__all__"
        widgets={
            'sbu_id': forms.TextInput(attrs={"placeholder":"SBU ID"}),
            'sbu_name': forms.TextInput(attrs={"placeholder":"SBU Name"}),
            'sbu_email': forms.EmailInput(attrs={"placeholder":"SBU Email"}),
            # 'director_of_service': forms.TextInput(attrs={"placeholder":"Director of service"}),
        "    director_of_service": forms.Select()
        }


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = '__all__'
        widgets={
            'dept_id': forms.TextInput(attrs={"placeholder":"Department ID"}),
            'dept_name': forms.TextInput(attrs={"placeholder":"Department Name"}),
            # 'head_of_dept': forms.TextInput(attrs={"placeholder":"HOD Name"}),
           " head_of_dept": forms.Select(),
            'description': forms.Textarea(attrs={"placeholder":"Department Description"}),
            'sbu_id':forms.Select(),
        }  


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"
        widgets={
            'unit_id': forms.TextInput(attrs={"placeholder":"Unit ID"}),
           ' head_of_unit': forms.Select(),
            'dept_id':forms.Select(),
            'unit_name': forms.TextInput(attrs={"placeholder":"Unit Name"}),
        } 

class DesignationForm(forms.ModelForm):
    # design_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Design ID'}))
    # designation = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Designation'}))
    class Meta:
        model = Designation
        fields = "__all__"
        widgets={
            'design_id': forms.TextInput(attrs={"placeholder":"Design ID"}),
            'designation': forms.Textarea(attrs={"placeholder":"Designation"}),
        } 

# class GradeLevelForm(forms.ModelForm):
#     # gradelevel_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'GradeLevel ID'}))
#     # gradelevel = forms.IntegerField( min_value=1,max_value=17 ,required=False,widget=forms.NumberInput())
#     class Meta:
#         model = GradeLevel
#         fields = "__all__"
#         widgets={
#             'gradelevel_id': forms.TextInput(attrs={"placeholder":"GradeLevel ID"}),
#             'gradelevel': forms.NumberInput(),
#         } 

class PositionForm(forms.ModelForm):
  
    class Meta:
        model = Position
        fields = "__all__"
        widgets={
            'position_code': forms.TextInput(attrs={"placeholder":"Position Code"}),
            'position': forms.TextInput(attrs={"placeholder":"Position"}),
            'description': forms.Textarea(attrs={"placeholder":"Position Description"}),
        } 

class StationForm(forms.ModelForm):

    class Meta:
        model = Station
        fields = '__all__'
        widgets={
            'station_id': forms.TextInput(attrs={"placeholder":"Station ID"}),
            'station_name': forms.TextInput(attrs={"placeholder":"Station Name"}),
            # 'station_manager': forms.TextInput(attrs={"placeholder":"Station Manager"}),
            'station_manager': forms.Select(),
            'station_email_address': forms.EmailInput(attrs={"placeholder":"Email Address"}),
            'station_location': forms.Textarea(attrs={"placeholder":"Station Location"}),
            'station_address': forms.Textarea(attrs={"placeholder":"Station Address"}),
        }  


class EmployeeForm (forms.ModelForm):
    thumb = forms.ImageField(widget=forms.ClearableFileInput(attrs={}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    mobile = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Mobile Number'}))
    dob = forms.DateField()
    emergency = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=Employee.GENDER,widget=forms.Select(attrs={}))
    language = forms.ChoiceField(choices=Employee.LANGUAGE,widget=forms.Select(attrs={}))
    nationality = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nationality'}))
    state_origin = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'State of Origin'}))
    lga_of_origin = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'State of Origin'}))
    address = forms.CharField( widget=forms.Textarea(attrs={'placeholder':'Residential Address'}))
    state_of_residence = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'State of Residence'}))
    lga_of_residence= forms.CharField( widget=forms.TextInput(attrs={'placeholder':'LGA of Residence'}))
    account_no = forms.CharField( widget=forms.TextInput(attrs={"placeholder":"Account No"}))
    bank = forms.CharField( widget=forms.TextInput(attrs={"placeholder":"Bank"}))
   

    # class Meta:
    #     model = Employee
    #     fields = ('first_name', 'last_name', 'mobile','email','emergency','salary','gender','bank','language','thumb')
    #     widgets={
    #         'bank':forms.TextInput(attrs={}),
    #         'account_no':forms.TextInput(attrs={})
    #     }

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Valid Email'}))
    # Need to add one for password as well
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class NewEmployeeForm (forms.ModelForm):
  
    class Meta:
        model = Employee
        # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
        fields = ['first_name',"middle_name",'thumb', 'last_name',"dob", 'mobile','account_no','emergency','bank','language']
        widgets={
            # 'user':forms.TextInput(attrs={"placeholder":"Username"}),
            'first_name':forms.TextInput(attrs={"placeholder":"First Name"}),
            'middle_name':forms.TextInput(attrs={"placeholder":"Middle Name"}),
            'last_name':forms.TextInput(attrs={"placeholder":"Last Name"}),
            'mobile':forms.TextInput(attrs={"placeholder":"Mobile Number"}),
            'emergency':forms.TextInput(attrs={"placeholder":"Relative Mobile Number"}),
            'dob':forms.DateInput(attrs={"type": "date"}),
            'bank':forms.TextInput(attrs={"placeholder":"Bank Name"}),
            'account_no':forms.TextInput(attrs={"placeholder":"Account Number"}),
            "thumb":forms.FileInput(attrs={}),
            "language":forms.Select(attrs={}),
            "gender": forms.Select(attrs={}),
        }



class BankForm(forms.ModelForm):
    # gradelevel_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'GradeLevel ID'}))
    # gradelevel = forms.IntegerField( min_value=1,max_value=17 ,widget=forms.TextInput(attrs={'placeholder':'Designation'}))
    class Meta:
        model = Bank
        fields = "__all__"
        widgets={
            'bank_id': forms.TextInput(attrs={"placeholder":"Bank ID"}),
            'bank': forms.TextInput(attrs={"placeholder":"Bank Information"}),
        }       

class KinForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={}))
    address = forms.CharField(widget=forms.Textarea(attrs={}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={}))
    employee = forms.ModelChoiceField(Employee.objects.filter(kin__employee=None),required=False,widget=forms.Select(attrs={}))

    class Meta:
        model = Kin
        fields = '__all__'
    




class AttendanceForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Attendance.STATUS,widget=forms.Select(attrs={'class':'form-control w-50'}))
    staff = forms.ModelChoiceField(Employee.objects.filter(Q(attendance__status=None) | ~Q(attendance__date = timezone.localdate())), widget=forms.Select(attrs={'class':'form-control w-50'}))
    class Meta:
        model = Attendance
        fields = ['status','staff']

class LeaveForm (forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))

    class Meta:
        model = Leave
        fields = '__all__'

        widgets={
            'start': forms.DateInput(attrs={'type':'date'}),
            'end': forms.DateInput(attrs={'type':'date'}),
            'status':forms.Select(attrs={}),
            'employee':forms.Select(attrs={}),
        }


class EmploymentForm(forms.ModelForm):
  
    class Meta:
        model = Employment
        fields = "__all__"
        widgets={
            'employ_id':forms.TextInput(attrs={"placeholder":"Employee ID"}),
            'first_name':forms.TextInput(attrs={"placeholder":"First Name"}),
            'middle_name':forms.TextInput(attrs={"placeholder":"Middle Name"}),
            'last_name':forms.TextInput(attrs={"placeholder":"Last Name"}),
            "employee_type": forms.Select(),
            "employee": forms.Select(),
            "sbu_id": forms.Select(),
            "station": forms.Select(),
            "department": forms.Select(),
            "unit": forms.Select(),
            "designation": forms.Select(),
            "gradelevel": forms.Select(),
            "position": forms.Select(),
            "step": forms.Select(),
            "doe": forms.DateInput(),
        }



    
class KPDForm(forms.ModelForm):
     
        class Meta:
            model = KPD
            fields = "__all__"
            widgets={
            'sub_id':forms.Select(),
            'dept_id':forms.Select(),
            'unit_id':forms.Select(),
            'kpd': forms.TextInput(attrs={"placeholder":"KPD "}),
            'description': forms.Textarea(attrs={"placeholder":" Description"}),
        }          

class KPIScoreRangeForm(forms.ModelForm):
 
    class Meta:
        model = KPIScoreRange
        fields = ["kpiscore_range_min","kpiscore_range_max","kpiscore_remark"]
        widgets={
            'kpiscore_range_min':forms.Select(),
            'kpiscore_range_max':forms.Select(),
            'kpiscore_remark': forms.TextInput(attrs={"placeholder":"KPD Remark"}),
        }  

class KPIScorePenaltyForm(forms.ModelForm):

    class Meta:
        model = KPIScorePenalty
        fields = ["kpiscore_range","percentage_penalty","paybenchmark"]
        widgets={
            'kpiscore_range':forms.Select(),
            'percentage_penalty': forms.NumberInput(),
            'paybenchmark': forms.TextInput(attrs={"placeholder":"No pay cut"}),
        }  

class SKPDForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop("request")
        super(SKPDForm,self).__init__(*args,**kwargs)
        admin = get_object_or_404(Employment,employee__user=self.request.user) 
        staff = get_object_or_404(Department,head_of_dept__user=self.request.user) 
        self.fields['dept'].queryset = Department.objects.filter(dept_name=staff)
        self.fields['employee'].queryset = Employment.objects.filter(department=staff)
        self.fields['kpd'].queryset = KPD.objects.filter(dept_id=admin.department)


    class Meta:
        model = SKPD
        # fields = ["sbu","week",'employee',"dept","kpd","weight","expected_time_of_delivery","unit"]
        fields = ["dept",'employee',"kpd","weight","expected_time_of_delivery","period"]

        widgets={
            # 'name': forms.TextInput(attrs={"placeholder": "Project Name"}),     
            # 'sbu': forms.Select(attrs={}),
            # 'unit': forms.Select(),
            "period": forms.Select(attrs={}),
            "dept": forms.Select(attrs={}),
            "kpd": forms.Select(attrs={}),
            "weight": forms.NumberInput(),
            "employee":forms.Select(),
            "expected_time_of_delivery": forms.TextInput(attrs={})

        }

class MKPDForm(forms.ModelForm):

    class Meta:
        model = MKPD
        fields = ["week","approved","description",'time_in','time_out',"date"]
    
 
        widgets={
            # "period": forms.Select(attrs={}),
            "skpd": forms.Select(attrs={}),
            "week": forms.Select(attrs={}),
            "approved": forms.Select(attrs={}),
            'time_in': forms.TextInput(),
            'time_out': forms.TextInput(),
            'description':forms.Textarea(attrs={  "placeholder":"Enter your remarks"}),
            "date": forms.DateInput(attrs={"type": "date"}),
        
        }




# class RatingForm(forms.ModelForm):
#     # project_rating= forms.IntegerField(required=False,widget=forms.NumberInput(),min_value=0,max_value=100)
#     # remark = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'No Pay Cut'}))
#     class Meta:
#         model = MKPD
#         fields = ("project_rating","remark")
#         widgets={
#             'remark': forms.TextInput(attrs={"placeholder": "Remark"}),
#            "project_rating": forms.NumberInput()
#         }

class KPI_EvalutationForm(forms.ModelForm):
    

    class Meta:
        model = KPI_Evalutation
        # fields = ["sbu","dept","mkpd","skpd","week","score","remark","approved","comment"]
        fields = ["score","remark","approved","comment"]

            

         
        widgets={
            'remark': forms.TextInput(),
            'comment': forms.Select(),
            # 'employee': forms.TextInput(attrs={"disbled": "True"}),
            # 'mkpd': forms.Select(),
            # 'period': forms.Select(),
            # "week": forms.Select(attrs={}),
            # "skpd": forms.Select(attrs={}),
            "score": forms.NumberInput(),
            'approved': forms.Select(),
        }




class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['approved','description']
        widgets={
            'approved': forms.Select(),
            'description': forms.Textarea(attrs={"placeholder":"Any complaint","required":False}),
        } 





