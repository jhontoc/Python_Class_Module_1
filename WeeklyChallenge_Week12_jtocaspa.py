import os


_dic={'0':"Menu", '1':"1.-Create a File", '2':"2.-Read a File", '3':"3.-Save a File", '4':"4.-Exit"}

def _filename(action):
 global cwd
 filename=input("Filename:")
 f=open(cwd+"\\"+filename,action)
 return f

while True:
  cwd=os.path.dirname(__file__) 
  script=os.path.basename(__file__)
  f=open(cwd+"\\"+script,'r')

  for option in _dic:
      print (_dic[option])
  try:
   option=str(input("Option:\t"))
   _dic[option]
   if option=='1':
    f=_filename('w')

   if option=='2':
    f=_filename('r')
    print("***File Output***")
    print(f.read())
    raise NameError()

   if option=='3':
    number1=input("Insert first number:")
    number2=input("Insert second number:")
    f=_filename('w')
    result=number1/number2
    f.write(str(result))
    
   if option=='4':
    raise KeyboardInterrupt()
    
 
  except KeyError:
   print("***Invalid Option***")
   pass
  except IOError as e:
   print("***File no found***",e)
   pass
  except ZeroDivisionError:
   print("Value saved on file: Invalido option",)
   f.write("Invalido option")
   pass
  
  except ValueError as e:
   print("***No-numeric data found***",e)
   pass
  except KeyboardInterrupt:
   print("***exiting program***")
   break
  except NameError:
   pass
  except TypeError:
   print("Numbers should interger") 
   pass
  except:
   pass
  else:
   print("file is create")
   
  finally:
   f.close()
   print("\n\n")
