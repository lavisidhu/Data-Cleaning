infile = open("digestive_illnesses.csv",'r')
new_file = open("cleaned_digestive_illnesses.csv",'w')
temp = []
for i,line in enumerate(infile):
    line = line.rstrip()
    line = line.split(",")

    if i%2!=0:
        temp = line
    else:
        temp = temp+line
        temp=str(temp)
        temp = temp.replace("  ","")
        temp=temp.replace("''","")
        temp = temp.replace(",,","")
        temp = temp.replace("'","")
        temp = temp.replace("[","")
        temp = temp.replace("]","")
        temp = temp.replace(",,",",")
        temp = temp.replace(", ,",",")
        temp = temp.replace(", ",",")
        temp = temp.replace(" ,",",")
        new_file.write(temp+'\n')
        temp = []
