import csv
def read_file():
    with open("data.csv")as f1:
        data=csv.reader(f1,delimiter=",")
        li=[]
        i=0
        for row in data:
            if(i>0):
                li.append({"name":row[0],"city":row[1],"designation":row[2],"experience_in_year":row[3]})
            i=i+1
    f1.close()
    return(li)