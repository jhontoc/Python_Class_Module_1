
#step 1
Sample=['Goblin', 'Creature', 'Troll', 'King/Queen', 'Witch/Warlock', 'Vampire', 'Guardian', 'Fairy', \
        'Knight', 'Elf', 'Assasin', 'Sorcerer/Sorceress', 'Giant', 'Warewolf', 'Wizard', 'Ogre', 'Goblin', \
        'Beast', 'Dragon', 'Ghost', 'Dwarf', 'Giant', 'Unicorn', 'Warrior', 'Spirit', 'Thief', 'Cyclops', 'Troll', \
        'Orc', 'Vampire']


Sample=list(set(Sample))

"""
2.Create dynamically a dictionary withletters from a to z and assign previous list to each letter.

alpha= {a :‘Goblin’ , b: ‘Creature’ ......... z:’Vampire’}

Hint: ord() can help you to convert letters into ascii 
"""
alpha=dict(enumerate(Sample,90))# 90 = a asci

"""
3.Convert the following string to a list:

string=’The Black,The Vengeful,The Dark,The Red,The Cursed,The Savage,The White,The Ugly,The Treacherous,The Blue,The Wicked,The Green’

"""

string = 'The Black,The Vengeful,The Dark,The Red,The Cursed,The Savage,The White,The Ugly,The Treacherous,The Blue,The Wicked,The Green'

str_list= string.split(',')


"""
From previous list assign one value to each key tothe following dictionary:
months={'Jan': '', 'Feb': '', 'Mar': '', 'Apr': '', 'May': '', 'Jun': '', 'Jul': '', 'Aug': '', 'Sep': '', 'Oct': '', 'Nov': '', 'Dec': ''}

"""

months={'Jan': '', 'Feb': '', 'Mar': '', 'Apr': '', 'May': '', 'Jun': '', 'Jul': '', 'Aug': '', 'Sep': '', 'Oct': '', 'Nov': '', 'Dec': ''}
c=0
for x in months:
    months[x]=str_list[c]
    c=c+1

months_number=dict(enumerate(months,1))

"""
5.That was the hard part! Now you only need to ask for Name and Month (number).
"""
while True: 
 try:
  data=input('please give me your name and Month(number):\n')
  name=data.split()[0][0].lower()
  N=data.split()[0]
  month=int(data.split()[1])
  print('Hola {}, Nacistes en el Mes de : {}\n'.format(N,months_number[month]))
  if ord(name) in alpha and months_number[month] in months:
   print("quiero decirte tu nombre de villano....!!!!\n\
         ques es ......\n\
      %s%s\n" % (alpha[ord(name)],months[months_number[month]]))
   print('gracias vuelve pronto')
   break
  else:
   print ('Values not estan en el rango permitido....please try again')
   continue

 except IndexError:
  print ('Minimo 2 Values....please try again')
  continue
 except ValueError:
  print ('ValueError....please try again')
  continue

"""
6.Based on first Letter of the name look into dictionary with letters which word corresponds and the same for the month.

"""

 
 
