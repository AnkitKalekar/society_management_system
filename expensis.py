import numpy as np
import pandas as pd
import amount, new_data, os, datetime


df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
dfa=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])

dfe=pd.DataFrame(columns=["date", "title","amount"])

lst1=[]


def run():
    dfo=pd.DataFrame(columns=["date", "title","amount"])
    return opt(dfo)




class Hide:
    def __init__(self, lst):
        self.date= lst[0]
        self.title= lst[1]
        self.amt= lst[2]
        
def entry(dfe):
    try:
        lst=[]
        
        print("Enter title for expensis: ")
        b=''
        while True:
            i=input()
            if i=="":
                break
            else:
                b+=i
        if b=="":
            raise Exception ("Cannot leave empty.")
        print("Enter date as day, month and year in numbers keep empty for current date")   
        day=input("Enter day (keep empty for current date): ")
        if day=="":
            print("Current date is entered for entry....")
            a=datetime.datetime.now().date()
            #date=date.strftime("%d-%m-%y")
        
        else:
            date=''
            month = input("Enter month (mm): ")
            year= input("Enter year (yy): ")
            date=day + "/" + month + "/" + year
            a = datetime.datetime.strptime(date, "%d/%m/%y").date()
            #date=date.strftime("%d-%m-%y")
        c =int(input("Enter amount: "))
        lst.append(a)
        lst.append(b)
        lst.append(c)
            
    except Exception as e:
        print(e)
        
    else:
        
        if len(dfe)==0:
            dfe.loc[0]=Hide(lst)
        else:
            dfe.loc[len(dfe)]=Hide(lst)
    return dfe


def show(dfe):
    dfs=pd.DataFrame(columns=["date", "title","amount"])
    for i in range(len(dfe)):
        dfs.loc[i]=[dfe.loc[i].date.date, dfe.loc[i].title.title, dfe.loc[i].amount.amt]
    return dfs

def sort(dfe):
    global lst1
    dfs=pd.DataFrame(columns=["date", "title","amount"])
    lst=show(dfe).values.tolist()
    lst=sorted(lst)
    lst1=lst.copy()
    for i in range(len(lst)):
        dfs.loc[i]=Hide(lst[i])
    return dfs
        
def del_entry(dfe):
    df1=pd.DataFrame(columns=["date", "title","amount"])
    lst=show(dfe).values.tolist()
    print("Choose a number from below: ")
    #print("Sr"," details")
    print(show(dfe))
    #for i in range(len(lst)):
    #   print(i,"-", lst[i][0], lst[i][1], lst[i][2])
    idx=int(input("Enter choice: "))
    lst.pop(idx)
    for i in range(len(lst)):
        df1.loc[i]=Hide(lst[i])
    return df1

def opt(dfo):
    global dfe
    if str(dfo)!='None':       
        dfe=dfo
    else:
        dfe=pd.DataFrame(columns=["date", "title","amount"])
        print("Cannot find old book, new entry book created")

    while True:
        try:
           ch=int(input("""Make a choice:
                            1. Enter expensis
                            2. View expensis
                            3. Delete entry
                            4. Quite
                        Enter your choice: """))
        except Exception as e:
            print(e)

        else:
            if ch==1:
                dfe=entry(dfe)

            elif ch==2:
                print(show(dfe))

            elif ch==3:
                dfe= del_entry(dfe)

            elif ch==4:
                return dfe
                print()
                break

            else:
                print("Invalid input")
            dfe=sort(dfe)  
