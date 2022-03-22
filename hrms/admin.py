from django.contrib import admin
# from django.contrib.auth import get_user_model
from .models import (Employee,Department,Station,SBU_Directorate,Unit,Employment,Kin,KPD,KPIScoreRange,Complaint
                    ,KPIScorePenalty,SKPD,MKPD,KPI_Evalutation,EmployeeType,Designation,
                    # GradeLevel,
                    Position,SMKPD,Bank)
# Register your models here.
# admin.site.register([Employee,Department,Attendance,Kin])
# admin.site.register(get_user_model())
admin.site.register([Bank,Employee,Department,Station,SBU_Directorate,Unit,Employment,Kin,KPD,KPIScoreRange,KPIScorePenalty,SKPD,MKPD,KPI_Evalutation,EmployeeType,Designation,
                    #  GradeLevel,
                     Position,SMKPD,Complaint])
