print(f'Hello! Please tell what you need to complete before your trip:')

dic_task={}

for i in range(1,5):    
 dic_task[i]=input(f'Task {i}:...\t')
 

task=input(f'witch task you need help remembering?:....\t')

print('you need to : '+dic_task[int(task)])

print(f'you forgot an intermediate task?:....\t')

new_item=input(f'what was it?:....\t')

new_position=input(f'what position should you do this task?:....\t')

dic_task[new_position]=new_item

print("i will remind you to use the WC :*(\n\
       Here is all you have to do before the trip:\n {}".format(dic_task) )

print("By the way, you already did the 1st and 2nd task . Let's forget about those:")
dic_task.pop(1)
dic_task.pop(2)
print(dic_task)

print("tell me your name and password number and i will keep them safe!")
name=input(f'Name:....\t')
password=input(f'Pass:....\t')
my_tuple=(name,password)
print('this will be safely stored: {}'.format(my_tuple))

my_countries=input(f"countries you've been to:...\t")
a=set(my_countries.split())

friend_countries=input(f"countries your friend has been to:...\t")
b=set(friend_countries.split())




print("your friend has gone to {} but you haven't\n\
you have been to {} but your friend hasn't\n\
both have been to {}\n".format(" and ".join(b.difference(a))," and ".join(a.difference(b))," and ".join(a.intersection(b))))

dic_passengers={'G123456':{'seat':'12A','Flight':123},'G989494':{'seat':'27D','flight':1009}}

print("this is the system's information:\n{}".format(dic_passengers))


      
      
