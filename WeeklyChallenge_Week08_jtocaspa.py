
import Packages.module_exchange as de
import Packages.subpackpage.module_graph as pic
import sys

coin_dic={'MXN':('Mexican Pesos',21),'BRL':('Real Brasileno',10),'ARS':('Peso Argentino',30),'PEN':('Sol Peruano',3.5),'EUR':('Euro',1.12)}
number=1
products=[]

'getting information from the user'
print(f'Select the initial currency (Just 3 letters code):\n')
for x, y in coin_dic.items():
 print("%s.- %s"%(x,y[0]))
 
while True:
 try:
  t_coin=input()
  print("Exchange rate: 1 %s equals %s USD\n"%(t_coin,coin_dic[t_coin][1]))
  break
 except KeyError:
  print("Oops!  That was no valid selection.  Try again...")   
     


print('Please introduce items')


while True:
 
 concept=str(input('concept {} ({}):'.format(number,t_coin)))
 amount=float(input('Amount {} ({}):'.format(number,t_coin)))
 ex_rate=de._exchange(t_coin)
 amoun_exchange=de._convert(ex_rate,amount)
 
 products.extend([[number,concept,amount,amoun_exchange]])
 number=number+1
 selection=input('do you want to add another item? (Yes/No):')
 
 if selection == 'Yes':
  continue    
 if selection == 'No':
  break
 if selection != 'Yes' or selection != 'No':
  print('Answer is not corret... ')
  print('Try again')
  sys.exit()
 

print("Expenses Report")
print("++++++++++++++++")
print("Concept\t Amount(%s)\t Amount(USD)"%(t_coin))
print("============================================")

item2=0
item3=0
for item in products:
 print("%s \t %s \t %s"%(item[1],item[2],item[3]))
 item2=item[2]+item2
 item3=item[3]+item3
print("============================================")
print("Total\t %s %s\t %s USD"%(item2,t_coin,item3))

pic.result(item3)




