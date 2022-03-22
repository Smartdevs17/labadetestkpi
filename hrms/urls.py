from django.urls import path
from . import views
app_name = 'hrms'


urlpatterns = [
    # Authentication Routes
    # path("",views.index,name="index"),
    path('', views.Index.as_view(), name='index'),
    path('employee_register/', views.Employee_Register_View.as_view(), name='employee_reg'),
    path('employee_login/', views.Employee_Login_View.as_view(), name='employee_login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/employee/new/', views.New_Employee_View.as_view(), name='employee_new'),
    path('dashboard/employee/<int:pk>/update/',views.Employee_Update.as_view(), name='employee_update'),



      # Admin Routes
    path('admin_login/', views.Admin_Login_View.as_view(), name='admin_login'),
    path('admin_dashboard/', views.Admin_Dashboard.as_view(), name='admin_dashboard'),
    path('admin_dashboard/settings', views.Admin_Setting.as_view(), name='admin_setting'),
    path('admin_logout/', views.Admin_Logout_View.as_view(), name='admin_logout'),
    path("admin_dashboard/report_complaint",views.Complaint_Report.as_view(), name ="report_complaint"),


     # Manager Routes
    path('manager_login/', views.Manager_Login_View.as_view(), name='manager_login'),
    path('manager_messages/', views.Manager_Message_View.as_view(), name='manager_message'),
    path('manager_dashboard/', views.Manager_Dashboard.as_view(), name='manager_dashboard'),
    path('manager_dashboard/kpd', views.Manager_KPD.as_view(), name='manager_kpd'),
    # path('manager_create_project/', views.Create_Project_View.as_view(), name='create_project'),
    path('manager_assgin_rating/<slug:pk>/', views.Assign_Rating_View.as_view(), name='assign_rating'),
    path('manager_dashboard/project_rating/<int:pk>/view/', views.Rating_View.as_view(), name='rating_view'),
    path('manager/kpi_evaluation/', views.Evaluation_View.as_view(), name='evaluation'),
    path('manager/report/', views.Report_View.as_view(), name='manager_report'),
    # path('manager_dashboard/<int:pk>/view/', views.Manager_Dashboard.as_view(), name='manager_dashboard'),
    path('manager_dashboard/settings', views.Manager_Setting.as_view(), name='manager_setting'),
    path('manager_logout/', views.Manager_Logout_View.as_view(), name='manager_logout'),
    path('manager_dashboard/members', views.Manager_Employee_View.as_view(), name='manager_members'),
  



# New Employee Routes
    path('employee_login/', views.Employee_Login_View.as_view(), name='employee_login'),
    path('employee_dashboard/', views.Employee_Dashboard.as_view(), name='employee_dashboard'),
    path('employee_dashboard/<int:pk>/project_detial/', views.Employee_Project_Detail.as_view(), name='project_detail'),
    path('employee_complete_task/', views.Complete_Project.as_view(), name='complete_task'),
    # path('employee_dashboard/project/<int:pk>/detial/', views.Project_Detail_View.as_view(), name='project_detail'),
    path('employee_report/<int:pk>/view/', views.Employee_Report_View.as_view(), name='report_view'),
    path('employee_logout/', views.Employee_Logout_View.as_view(), name='employee_logout'),
    path('employee_complaint/', views.Complaint_View.as_view(), name='employee_complaint'),



#SKPD Routes
    path('employee_dashboard/deliverable_report/<slug:pk>/add/', views.Project_New.as_view(), name='proj_new'),
    path('employee_dashboard/delivable_report/all/', views.Project_All.as_view(), name='proj_all'),
    path('employee_dashboard/delivable_report/<slug:pk>/', views.Project_Detail.as_view(), name='proj_detail'),
    path('employee_dashboard/skpddelivable_report/<slug:pk>/update/', views.Project_Update.as_view(), name='proj_update'),
    path('employee_dashboard/delivable_report/<slug:pk>/delete/', views.Project_Delete.as_view(), name='proj_delete'),
    # path('ajax/load-depts/', views.load_depts, name='ajax_load_depts'), 
    # path('ajax/load-units/', views.load_units, name='ajax_load_units'), 

# Employee Routes
    path('dashboard/employee/', views.Employee_All.as_view(), name='employee_all'),
    # path('dashboard/employee/new/', views.Employee_New.as_view(), name='employee_new'),
    path('dashboard/employee/<int:pk>/view/', views.Employee_View.as_view(), name='employee_view'),
    # path('dashboard/employee/<int:pk>/update/', views.Employee_Update.as_view(), name='employee_update'),
    path('dashboard/employee/<int:pk>/delete/', views.Employee_Delete.as_view(), name='employee_delete'),
    path('dashboard/employee/<int:id>/kin/add/', views.Employee_Kin_Add.as_view(), name='kin_add'),
    path('dashboard/employee/<int:id>/kin/<int:pk>/update/', views.Employee_Kin_Update.as_view(), name='kin_update'),


# #EmployeeType Routes
#     path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
#     path('dashboard/employeetype/add/', views.EmployeeType_New.as_view(), name='employeetype_new'),
#     path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),
#     path('dashboard/employee/<str:pk>/delete/', views.EmployeeType_Delete.as_view(), name='employee_delete'),


# #EmployeeType Routes
#     path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
#     path('dashboard/directorate/add/', views.Directorate_New.as_view(), name='directorate_new'),
#     path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),
#     path('dashboard/employee/<str:pk>/delete/', views.EmployeeType_Delete.as_view(), name='employee_delete'),

    # path('dashboard/employeetype/add/', views.EmployeeType_New.as_view(), name='employeetype_new'),
    # path('dashboard/directorate/add/', views.Directorate_New.as_view(), name='directorate_new'),
    # path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
    # path('dashboard/unit/add/', views.Unit_New.as_view(), name='unit_new'),
    # path('dashboard/designation/add/', views.Designation_New.as_view(), name='design_new'),
    # # path('dashboard/gradelevel/add/', views.GradeLevel_New.as_view(), name='grade_new'),
    # path('dashboard/position/add/', views.Position_New.as_view(), name='position_new'),
    # path('dashboard/station/add/', views.Station_New.as_view(), name='station_new'),
    # # path('dashboard/bank/add/', views.Bank_New.as_view(), name='bank_new'),
    # path('dashboard/employment/add/', views.Employment_New.as_view(), name='employment_new'),
    # path('dashboard/kpd/add/', views.KPD_New.as_view(), name='kpd_new'),
    # path('dashboard/kpiscorerange/add/', views.KPIScoreRange_New.as_view(), name='kpiscore_new'),





#Bank Routes
    path('dashboard/bank/add/', views.Bank_New.as_view(), name='bank_new'),
    path('dashboard/bank/all/', views.Bank_All.as_view(), name='bank_all'),
    path('dashboard/bank/<str:pk>/', views.Bank_Detail.as_view(), name='bank_detail'),
    path('dashboard/bank/<str:pk>/update/', views.Bank_Update.as_view(), name='bank_update'),
    path('dashboard/bank/<str:pk>/delete/', views.Bank_Delete.as_view(), name='bank_delete'),
    
    
#EmployeeType Routes
    path('dashboard/employeetype/add/', views.EmployeeType_New.as_view(), name='employeetype_new'),
    path('dashboard/employeetype/all/', views.EmployeeType_All.as_view(), name='employeetype_all'),
    path('dashboard/employeetype/<str:pk>/', views.EmployeeType_Detail.as_view(), name='employeetype_detail'),
    path('dashboard/employeetype/<str:pk>/update/', views.EmployeeType_Update.as_view(), name='employeetype_update'),
    path('dashboard/employeetype/<str:pk>/delete/', views.EmployeeType_Delete.as_view(), name='employeetype_delete'),


#Directorate Routes
    path('dashboard/sbu/add/', views.Directorate_New.as_view(), name='sbu_new'),
    path('dashboard/sbu/all/', views.Directorate_All.as_view(), name='sbu_all'),
    path('dashboard/sbu/<str:pk>/', views.Directorate_Detail.as_view(), name='sbu_detail'),
    path('dashboard/sbu/<str:pk>/update/', views.Directorate_Update.as_view(), name='sbu_update'),
    path('dashboard/sbu/<str:pk>/delete/', views.Directorate_Delete.as_view(), name='sbu_delete'),


#Department Routes
    path('dashboard/dept/add/', views.Department_New.as_view(), name='dept_new'),
    path('dashboard/dept/all/', views.Department_All.as_view(), name='dept_all'),
    path('dashboard/dept/<str:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
    path('dashboard/dept/<str:pk>/update/', views.Department_Update.as_view(), name='dept_update'),
    path('dashboard/dept/<str:pk>/delete/', views.Department_Delete.as_view(), name='dept_delete'),


#Unit Routes
    path('dashboard/unit/add/', views.Unit_New.as_view(), name='unit_new'),
    path('dashboard/unit/all/', views.Unit_All.as_view(), name='unit_all'),
    path('dashboard/unit/<str:pk>/', views.Unit_Detail.as_view(), name='unit_detail'),
    path('dashboard/unit/<str:pk>/update/', views.Unit_Update.as_view(), name='unit_update'),
    path('dashboard/unit/<str:pk>/delete/', views.Unit_Delete.as_view(), name='unit_delete'),
    
    
    
#Station Routes
    path('dashboard/station/add/', views.Station_New.as_view(), name='station_new'),
    path('dashboard/station/all/', views.Station_All.as_view(), name='station_all'),
    path('dashboard/station/<str:pk>/', views.Station_Detail.as_view(), name='station_detail'),
    path('dashboard/station/<str:pk>/update/', views.Station_Update.as_view(), name='station_update'),
    path('dashboard/station/<str:pk>/delete/', views.Station_Delete.as_view(), name='station_delete'),



#Designation Routes
    path('dashboard/design/add/', views.Designation_New.as_view(), name='design_new'),
    path('dashboard/design/all/', views.Designation_All.as_view(), name='design_all'),
    path('dashboard/design/<str:pk>/', views.Designation_Detail.as_view(), name='design_detail'),
    path('dashboard/design/<str:pk>/update/', views.Designation_Update.as_view(), name='design_update'),
    path('dashboard/design/<str:pk>/delete/', views.Designation_Delete.as_view(), name='design_delete'),



#Position Routes
    path('dashboard/position/add/', views.Position_New.as_view(), name='position_new'),
    path('dashboard/position/all/', views.Position_All.as_view(), name='position_all'),
    path('dashboard/position/<str:pk>/', views.Position_Detail.as_view(), name='position_detail'),
    path('dashboard/position/<str:pk>/update/', views.Position_Update.as_view(), name='position_update'),
    path('dashboard/position/<str:pk>/delete/', views.Position_Delete.as_view(), name='position_delete'),
    
    
#KPD Routes
    path('dashboard/kpd/add/', views.KPD_New.as_view(), name='kpd_new'),
    path('dashboard/kpd/all/', views.KPD_All.as_view(), name='kpd_all'),
    path('dashboard/kpd/<str:pk>/', views.KPD_Detail.as_view(), name='kpd_detail'),
    path('dashboard/kpd/<str:pk>/update/', views.KPD_Update.as_view(), name='kpd_update'),
    path('dashboard/kpd/<str:pk>/delete/', views.KPD_Delete.as_view(), name='kpd_delete'),
    

#KPISR Routes
    path('dashboard/kpisr/add/', views.KPISR_New.as_view(), name='kpisr_new'),
    path('dashboard/kpisr/all/', views.KPISR_All.as_view(), name='kpisr_all'),
    path('dashboard/kpisr/<str:pk>/', views.KPISR_Detail.as_view(), name='kpisr_detail'),
    path('dashboard/kpisr/<str:pk>/update/', views.KPISR_Update.as_view(), name='kpisr_update'),
    path('dashboard/kpisr/<str:pk>/delete/', views.KPISR_Delete.as_view(), name='kpisr_delete'),
   
#KPISP Routes
    path('dashboard/kpisp/add/', views.KPISP_New.as_view(), name='kpisp_new'),
    path('dashboard/kpisp/all/', views.KPISP_All.as_view(), name='kpisp_all'),
    path('dashboard/kpisp/<str:pk>/', views.KPISP_Detail.as_view(), name='kpisp_detail'),
    path('dashboard/kpisp/<str:pk>/update/', views.KPISP_Update.as_view(), name='kpisp_update'),
    path('dashboard/kpisp/<str:pk>/delete/', views.KPISP_Delete.as_view(), name='kpisp_delete'),
    
    
#Employment Routes
    path('dashboard/employment/add/', views.Employment_New.as_view(), name='employment_new'),
    path('dashboard/employment/all/', views.Employment_All.as_view(), name='employment_all'),
    path('dashboard/employment/<str:pk>/', views.Employment_Detail.as_view(), name='employment_detail'),
    path('dashboard/employment/<str:pk>/update/', views.Employment_Update.as_view(), name='employment_update'),
    path('dashboard/employment/<str:pk>/delete/', views.Employment_Delete.as_view(), name='employment_delete'), 
    path('dashboard/employee/search/', views.SearchView.as_view(),name = "search"),
    
    
    
#SKPD Routes
    path('dashboard/skpd/add/', views.SKPD_New.as_view(), name='skpd_new'),
    path('dashboard/skpd/all/', views.SKPD_All.as_view(), name='skpd_all'),
    path('dashboard/skpd/<slug:pk>/', views.SKPD_Detail.as_view(), name='skpd_detail'),
    path('dashboard/skpd/<slug:pk>/update/', views.SKPD_Update.as_view(), name='skpd_update'),
    path('dashboard/skpd/<slug:pk>/delete/', views.SKPD_Delete.as_view(), name='skpd_delete'),
    path('ajax/load-depts/', views.load_depts, name='ajax_load_depts'), 
    path('ajax/load-units/', views.load_units, name='ajax_load_units'), 
    
# #Department Routes
#     path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
#     path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
    path('dashboard/kpi_evaluation/<int:pk>/update/', views.Evaluation_Update.as_view(), name='evaluation_update'),
    
    
#SKPD Routes
    path('dashboard/mkpd/add/', views.Employee_SKPD.as_view(), name='employee_skpd'),
    path('dashboard/mkpd/<slug:pk>/all/', views.MKPD_All.as_view(), name='mkpd_all'),
    # path('dashboard/skpd/<slug:pk>/', views.SKPD_Detail.as_view(), name='skpd_detail'),
    # path('dashboard/skpd/<slug:pk>/update/', views.SKPD_Update.as_view(), name='skpd_update'),
    # path('dashboard/skpd/<slug:pk>/delete/', views.SKPD_Delete.as_view(), name='skpd_delete'),
    # path('ajax/load-depts/', views.load_depts, name='ajax_load_depts'), 
    # path('ajax/load-units/', views.load_units, name='ajax_load_units'), 
    
#Evalutation Routes
    path('dashboard/eva/<slug:pk>/add/', views.Evalutation_New.as_view(), name='eva_new'),
    path('dashboard/eva/all/', views.Evalutation_All.as_view(), name='eva_all'),
    path('dashboard/eva/all/<slug:pk>/details', views.Evalutation_All_Details.as_view(), name='eva_all_detail'),
    path('dashboard/eva/<str:pk>/', views.Evalutation_Detail.as_view(), name='eva_detail'),
    path('dashboard/eva/<str:pk>/update/', views.Evalutation_Update.as_view(), name='eva_update'),
    path('dashboard/eva/<str:pk>/delete/', views.Evalutation_Delete.as_view(), name='eva_delete'),

]
