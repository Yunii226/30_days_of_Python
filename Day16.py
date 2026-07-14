from datetime import datetime 
#1
now=datetime.now()
print(datetime.now())
print(datetime.now().timestamp())


#2
format_date=now.strftime("%B/%d/%Y, %H:%M:%S")
print(format_date)

#3
date= "5 December, 2019"
print(datetime.strptime(date,"%d %B, %Y"))

#4
new_year=datetime(2027,1,1,0,0,0)
diff=new_year-now
print(diff)

#5
given_date=datetime(1970,1,1)
print(now-given_date)