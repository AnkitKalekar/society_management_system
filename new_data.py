#society management system
import pandas as pd, numpy as np, pickle

#class
class Hide:
    def __init__(self,room_no,owner, owner_contact, rented, tenent, tenent_contact, complaint):
        self.room_no=room_no
        self.owner=owner
        self.owner_contact=owner_contact
        self.rented=rented
        self.tenent=tenent
        self.tenent_contact=tenent_contact
        self.complaint=complaint
        
#function to add info


def new_entry(df):
    try:
        room_no=input("Enter room number / shop number: ")
        if room_no=="":
            raise Exception("err_empty")
        elif len(df)>=1:
            a=[]
            for i in df.room_no:
                a.append(i.room_no)
            if room_no in a:
                raise Exception("err_unique")
            del a
        
        owner=input("Enter owner name: ").title()
        if owner=="":
            raise Exception("err_empty")
        
        owner_contact=int(input("Enter contact info of owner: "))
        names=[];contacts=[]
        if len(df)>0:
            for i in df.owner:
                names.append(i.owner)
            for i in df.owner_contact:
                contacts.append(i.owner_contact)
        owner_contact = contact_verify(owner_contact, owner, names, contacts)
        if owner_contact=='error_unique':
            raise Exception("err_unique")
        elif owner_contact=='error_len':
            raise Exception("err_length")
        
        rented=input("Rented (yes / no): ").lower()
        if rented in ['yes','y','ye']:
            rented=True   
            if len(df)>0:
                for i in df.tenent:
                    names.append(i.tenent)
                for i in df.tenent_contact:
                    contacts.append(i.tenent_contact)
            if rented==True:
                    tenent=input("Enter tenent's name: ").title()
                    tenent_contact=int(input("Enter tenent's contact info: "))
                    tenent_contact=contact_verify(tenent_contact,tenent, names, contacts)
            if tenent_contact=='error':
                raise Exception("Contact must be unqiue...")
            elif tenent_contact=='error_len':
                raise Exception("err_length")

                    
        else:
            rented=False
            tenent=np.nan
            tenent_contact=np.nan
                
        complaint=input("Enter any compliant by the owner or tenent: ")
        if complaint =='':
            complaint=np.nan
        
    except Exception as e:
        e=str(e)
        if e=="err_empty":
            print("Cannot be left empty")
        elif e=="err_unique":
            print("Entry already exists. This entered data has to be unique.")
        elif e=="err_length":
            print("Contact lenght must be 6 or 8 for landline and 10 or 12 for mobile.")
        elif e=="invalid literal for int() with base 10:":
            print('incpm')
        return "entry_cancelled"
    else:
        return Hide(room_no,owner, owner_contact, rented, tenent, tenent_contact, complaint)
        #df.loc[len(df)]=[room_no,owner, owner_contact, rented, tenent, tenent_contact, complaint]
        #df.loc[len(df)]= Hide(room_no,owner, owner_contact, rented, tenent, tenent_contact, complaint)

        
    finally:
        print(" ")
        
#returns all existing entries       
def show(df):
    df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
    for i in range(len(df)):    
        df1.loc[i]=[df.loc[i].room_no.room_no, df.loc[i].owner.owner, df.loc[i].owner_contact.owner_contact,\
                    df.loc[i].rented.rented, df.loc[i].tenent.tenent, df.loc[i].tenent_contact.tenent_contact, df.loc[i].complaint.complaint]
          
    return df1


#returns recently added entry
def show_recent(a):
    if str(a)=="None":
        return 'None'
    else:
        df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
        q=[a.room_no.room_no, a.owner.owner, a.owner_contact.owner_contact,\
                a.rented.rented, a.tenent.tenent, a.tenent_contact.tenent_contact, a.complaint.complaint]
        df1.loc[0]=q
        print(df1)
        del df1

#checks length of number
def contact_len(contact):
    l=len(str(contact))
    if l==6 or l==8 or l==10 or l==12:
        return contact
    return 'error_len'

#check for repeatability
def contact_verify(contact,name,names,contacts):
    contact=contact_len(contact)
    if contact=='error_len':
        return 'error_len'
    else:
        if name in names:
            return contact
        else:
            if contact in contacts:
                return 'error_unique'
            else:
                return contact



def hide(df):
    df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])

    for i in range(len(df)):
        df1.loc[len(df)]=Hide(df.loc[i].room_no, df.loc[i].owner, df.loc[i].owner_contact, \
                              df.loc[i].rented, df.loc[i].tenent, df.loc[i].tenent_contact,df.loc[i].complaint )
    return df1


def rooms_info(df):
    df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
    df1=show(df)
    return df1.room_no.tolist()

#create a dataframe
##df=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
##df1=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
##new_entry(df)
##show(df)
##print('')
##new_entry()
##for i in range(len(df)):
##    q=[df.loc[i].room_no.room_no, df.loc[i].owner.owner, df.loc[i].owner_contact.owner_contact,\
##       df.loc[i].rented.rented, df.loc[i].tenent.tenent, df.loc[i].tenent_contact.tenent_contact, df.loc[i].complaint.complaint]
##    df1.loc[i]=q
##print(df1)
##del df1
