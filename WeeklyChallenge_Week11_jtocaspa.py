
import re

f1=open("C:\\SCRIPTS\\Weekly_Challenge 11_log_sample.log","r+")
output=f1.read()
f2=open("C:\\SCRIPTS\\Weekly_Challenge 11_log_sample.log","r+")
output1=f2.readlines()


#1. When did the first warning occurred?

x=re.search(r"(?P<Fecha>(^(\d+[/:]){2}\d+)) (?P<Hora>(\d+[/:]){2}\d+) (?P<severity>(.WARNING.)) (.+ ){1,}",output)
print("the first event occurred on %s at %s"%(x.group("Fecha"),x.group("Hora")))

#2. Print the logs which does not match the standard format.
a=[]
severitylist=[]
print("logs below are not good :") 
for line in output1:
 x=re.findall(r"^(\d+[/:]){2}\d+ (\d+[/:]){2}\d+ \[\w+\] (\w+( |))+$",line)
 if x==a:
  print(line)
 objmatch=re.match(r"(?P<Fecha>(^(\d+[/:]){2}\d+)) (?P<Hora>(\d+[/:]){2}\d+) (?P<severity>(.\w+.)) (.+ ){1,}",line)
 if objmatch:
  severitylist.append(objmatch.group("severity"))
 

#3. List the different severities and its appearance count

temp=set(severitylist)
result={}
for i in temp:
 result[i]=severitylist.count(i)
print(result)

#4 After analyzing the logs, provide some log formatting recommendations to the
#customer (as comments at the beginning of your code)
print("the correct log format should be as:")
print(objmatch.group())






