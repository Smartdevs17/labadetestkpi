from datetime import date
today = date.today()

# print("Curent year is ", today.year)
# print("Curent month is ", today.month)
# print("p:"+str(date.today().month)+":"+str(date.today().year)[-2:])
# print(type(("p:"+str(date.today().month)+":"+str(date.today().year)[-2:])))

# from datetime import datetime,timedelta

# now = datetime(datetime.now().year,datetime.now().month,1)
# ctr = datetime(2021,3,19)
# list = [ctr.strftime("%Y-%m-%d")]
# print(list)

# while ctr <= now:
#     ctr += timedelta(days=32)
#     list.append(datetime(ctr.year, ctr.month,1).strftime("%Y-%m-%d"))
#     print(list.append(datetime(ctr.year, ctr.month,1).strftime("%Y-%m-%d")))



# import datetime
# import pandas as pd

# start_date = datetime.date(2020,1,1)
# end_date = datetime.date(2026,2,1)

# date_range = pd.date_range(start_date,end_date)

# date_range = date_range[date_range.day==1]

# print(date_range)


# import datetime

# def range_of_months(start_date,end_date):
#     months = []
#     for i in range(start_date.year * 12 + start_date.month, end_date.year*12 + end_date.month + 1):
#         months.append(datetime.date((i-13) // 12 +1 , (i-1) % 12 + 1,30))
#     return(months)  
#     # for month in months:
#     #     print(month.month)
#     # return ("P:"+str(month.month)+ ":" +str(month.year))
  
# start_date = datetime.date.today()
# end_date = datetime.date(2022,12,12)
# date_period = range_of_months(start_date,end_date)
# # print(date_period)
# for month in date_period:
#     print(month)

from .models import SKPD

staff = SKPD.objects.all()
staff = SKPD.objects.filter(employee__employee__user="user4").annotate(total=Sum("weight"))
print(staff)