import new_data
import numpy as np
import pandas as pd

def ip():
    a= input("Enter contact: ")
    return a

def digit(data,name, names, contacts):
    if data.isdigit():
        data=int(data)
        data= new_data.contact_verify(data, name, names, contacts)
        if data=="err_length":
            print("Contact lenght must be 6 or 8 for landline and 10 or 12 for mobile.")
        elif data=="err_unique":
            print("Entry already exists. This entered data has to be unique.")
        else:
            return data
    else:
        print("Entered data are not digits")

def sortarrange(df):
    df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
    df1=new_data.show(df)
    lst=df1.values.tolist()
    lst.sort()
    df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
    for i in range(len(lst)):
        df1.loc[i]=new_data.Hide(lst[i][0],lst[i][1],lst[i][2],lst[i][3],lst[i][4],lst[i][5],lst[i][6])
    return df1

def del_single(df):
    
    try:   
        a=new_data.show(df)
        print(a)
        lst=[]
        room=input("Enter room number to modify the derails: ")
        rooms=[]
        rooms=a.room_no.values.tolist()
        idx=rooms.index(room)

    except Exception as e:
        print(e)
        return df

    else:
        
        if room not in rooms:
            print("No such room number avaliable")
            
        else:         
            cho=input(f"Do you want to delete room number {room} from the record (yes / no): ").lower()
            if cho=="yes":
                df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
                lst=new_data.show(df).values.tolist()
                lst.pop(idx)
                for i in range(len(lst)):
                        df1.loc[i]=new_data.Hide(lst[i][0],lst[i][1],lst[i][2],lst[i][3],lst[i][4],lst[i][5],lst[i][6])
                return df1
            return df
        
def modify(df):
    print(new_data.show(df))
    lst=[]
    room=input("Enter room number to modify the derails: ")
    if room=="":
        return print("No changes made.")
   
                
    while True:

        try:   
            for i in df.room_no:
                lst.append(i.room_no)
            a=lst.index(room)
            #print(a)
            ch=int(input("""What do u want to modify:
                                1. Room number
                                2. Owner name
                                3. Owner contact
                                4. Rented
                                5. Tenent
                                6. Tenent contact
                                7. Complaint
                                8. Quite
                            Choose from above: """))

        except Exception as e:
            print(e)

        else:
            
            if ch==1:
                data= input("Enter room correct number: ")
                if data!="":
                    temp=[]
                    for i in df.room_no:
                        temp.append(i.room_no)
                    if data in temp:
                        print("this room number already exist")
                    else:
                        df.loc[a].room_no.room_no=data
                    del temp
            
            elif ch==2:
                data=input("Enter owner's name: ").title()
                if data!="":
                    df.loc[a].owner.owner=data
                    
            elif ch==3:
                data=input("Enter owner's contact")
                if data !="":
                    contacts=[]
                    owners=[]
                    contact=digit(data)
                    for i in df.owner_contact:
                        contacts.append(i.owner_contact)
                    for i in df.owner:
                        owners.append(i.owner)
                    data=digit(data, df.loc[a].owner, owners, contacts)
                    if type(data)==int:     
                        df.loc[a].owner_contact.owner_contact=data

            elif ch==4:
                rented=input("Rented status (Yes/ No): ").lower()
                if rented in ['yes','y','ye']:
                    df.loc[a].rented.rented=True
                    df.loc[a].tenent.tenent=input("Enter tenent's name:").title()
                    data=input("Enter tenent's contact: ")
                    if data !="":
                        contacts=[]
                        tenents=[]
                        for i in df.tenent_contact:
                            contacts.append(i.tenent_contact)
                        for i in df.owner:
                            tenents.append(i.tenent)
                        data=digit(data, df.loc[a].tenent, tenents, contacts)
                        if type(data)==int:     
                            df.loc[a].tenent_contact.tenent_contact=data
                        else:
                            print("Number must be 6 or 8 for landline and 10 or 12 for mobile.")
                else:
                    df.loc[a].rented.rented=False
                    df.loc[a].tenent.tenent= np.nan
                    df.loc[a].tenent_contact.tenent_contact= np.nan
           
            elif ch==5:
                if df.loc[a].rented.rented==False:
                    print("Change rented status first...")
                else:
                    df.loc[a].tenent.tenent=ip().title()
                    
            elif ch==6:
                if df.loc[a].rented.rented==False:
                    print("Change rented status first...")
                    if df.loc[a].tenent.tenent==np.nan:
                        print("Enter tenent's name first...")
                else:
                    contact=ip()
                    df.loc[a].tenent_contact.tenent_contact=new_data.contact_len(contact)

                    
            elif ch==7:
                df.loc[a].complaint.complaint=input("Enter your conplaint here: ")
                
            elif ch==8:
                break
            
            else:
                print("Invalid input")
            new_data.show_recent(df.loc[a])
