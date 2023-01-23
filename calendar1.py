import calendar

yy=2022
mm=1
cal = []
cal_month = calendar.monthcalendar(yy, mm)
for week in cal_month:
    week_list=[]

    for day in week:
        if day==0:
            week_list.append("")
        else:
            week_list.append(day)
    cal.append(week_list)

print(cal)