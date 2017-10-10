import sys


folder_loc = sys.argv[1]
filename =sys.argv[2]
fileobj = open(folder_loc + filename);
flag=0
real_rev = open(folder_loc + "real_"+filename,"w+")
fake_rev = open(folder_loc + "fake_"+filename,"w+")

for line in fileobj:  
    for i in range(len(line)):
        if (line[i] == '[' and flag == 0):          #for beginning of real reviews
            flag = 1
       	elif (line[i-1]==']' and flag == 1):        #for end of real reviews
            flag = 2
        elif (line[i]=='[' and flag == 2):          #for beginning of fake reviews
            flag = 3
        elif (line[i-1] == ']' and flag == 3):      #for end of fake reviews
            flag = 4
        if(flag ==1):
            real_rev.write(line[i])
        elif(flag==3):
            fake_rev.write(line[i])
        
