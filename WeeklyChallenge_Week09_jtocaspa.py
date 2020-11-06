import csv

#reading

with open("Repository\\Weekly Challenge 9.csv","r") as f:
 readf= csv.reader(f,delimiter=',')
 file=[]
 for row in readf:
  file.append(row)


#logic
new_line=[]
plk_count,Bline_count,BBLF_count,Bspeed_count,c=0,0,0,0,0

for line in file[1:]:
    
 if line[2] =="":
  plk_count=int(line[4])
  c=file.index(line)
    
 if line[2] =="Line (ring)":
  Bline_count=Bline_count+1
  
 if line[2] =="BLF":
  BBLF_count=BBLF_count+1
  
 if line[2] =="Speed-dial":
  Bspeed_count=Bspeed_count+1


 if line == file[c+plk_count]:
  if (plk_count+Bline_count+Bspeed_count)>=5:
   cmodel='8851'
  else:
   cmodel='8841'  

  new_line.extend([[line[0],line[1],Bline_count,BBLF_count,Bspeed_count,cmodel]])
  plk_count,Bline_count,BBLF_count,Bspeed_count,c=0,0,0,0,0

##writing  

with open('Repository\\output.csv', mode='w',newline='') as ouputfile:
    output = csv.writer(ouputfile)

    output.writerow(['extension','name','#_line_buttons','#_blfs_buttons','#_speeddial_buttons','cisco_model'])
    output.writerows(new_line)
   


 
 
 
    




