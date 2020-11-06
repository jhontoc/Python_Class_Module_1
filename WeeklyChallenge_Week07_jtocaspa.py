import WeeklyChallenge_Week07_module_jtocaspa as pwd


myorder=['First','Second']

for x in myorder:
 pwd1, pwd2 = "", " "
 name=input("please type the %s user name: \t" % (x))
 while True:
  password=input("Type the new password:  \t")

  while not pwd.ch_validation(password):
   password=input("Type the new password:  \t")
  
  pwd1=password
  password=input("Type the new password again:  \t")
 
  while not pwd.ch_validation(password):
   password=input("Type the new password again:  \t")
  
  pwd2=password
  if pwd.eq_validation(pwd1,pwd2):
   break
  else:
   continue
   
 
 print('Thank you, your username: %s and password %s have saved \n' % (name,pwd2))




  
  
