
def eq_validation(val1,val2):
 if val1 == val2:
  return True
 else:
  print('Passwords are not the same, try again')
  return False
    


def ch_validation(password):
 forbidden_list={".","-"}
 pwd=password
 if not (forbidden_list.isdisjoint(set(pwd))):
  print('Incorrect password, (.) or (-) are not allowed\
        at the beginning nor at the end\n')
  return False

 else:
  return True 
 
  
  
 
     
