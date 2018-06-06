infile = open("health_codes.csv",'r')
new_file = open("cleaned_health_codes.csv",'w')
header=[]
check=""
for i,line in enumerate(infile):
    index=0
    temp=[]
    temp1=[]
    line.strip()
    line.rstrip()
    line = line.replace("\n","")
    line=line.split(",")
    line.insert(0,"Description")
    line.insert(1,line.pop(-1))
    length=len(line)

    while length<8:
        line.append(check)
        length+=1

    for letter in line:
        if index%2==0:
            temp.append(letter)
        else:
            temp1.append(letter)

        index+=1

    if i==0:
        temp=str(temp)
        temp=temp.replace("''","")
        temp = temp.replace("'","")
        temp = temp.replace("[","")
        temp = temp.replace("]","")
        header=temp
        new_file.write(header+'\n')

    temp1=str(temp1)
    temp1 = temp1.replace("  ","")
    temp1=temp1.replace("''","")
    temp1 = temp1.replace("'","")
    temp1 = temp1.replace("[","")
    temp1 = temp1.replace("]","")
    temp1= temp1.replace(", ",",")
    new_file.write(temp1+'\n')
