#import new_data, modification, amount, expensis
import pandas as pd, pickle, os, sys

#append path for package pac
sys.path.append(sys.path[0]+ "\\pac\\")
print(sys.path[-1])
from pac import *


#dataframe
df=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
dfm=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
dfo=pd.DataFrame(columns=["date", "title","amount"])

#fee dataframe
#load
if os.path.isfile("pac/data/amt.dat"):
    file=open("pac/data/amt.dat", 'rb')
    obj = file.read()
    if len(obj)>0:
        obj= pickle.loads(obj)
        dfm=obj
        file.close()
#save amounts 
def savem(dfm):
    file=open('pac/data/amt.dat','wb')
    obj= pickle.dumps(dfm)
    file.write(obj)
    file.close()



#Expensis dataframe
#load
if os.path.isfile("pac/data/exp.dat"):
    file=open("pac/data/exp.dat", 'rb')
    obj = file.read()
    if len(obj)>0:
        obj= pickle.loads(obj)
        dfo=obj
        file.close()
#save        
def savex(dfm):
    file=open('pac/data/exp.dat','wb')
    obj= pickle.dumps(dfo)
    file.write(obj)
    file.close()



#load data from file
if os.path.isfile("pac/data/entry.dat"):
    file=open("pac/data/entry.dat", 'rb')
    obj = file.read()
    if len(obj)>0:
        obj= pickle.loads(obj)
        df=obj
    file.close()


# function to save data in file
def save(df):
    file=open("pac/data/entry.dat",'wb')
    obj=pickle.dumps(df)
    file.write(obj)
    
    file.close()    



def export(dfm, dfo,df):
    try:
        print("Data will be stored into your pc as csv in the downloads folder")
        d=amount.show(dfm)
        d.to_csv(os.path.expanduser("~"+ "\\Downloads\\")+"Maintanence.csv")
        del d

        d=expensis.show(dfo)
        d.to_csv(os.path.expanduser("~"+ "\\Downloads\\")+"Expensis.csv")
        del d

        d = new_data.show(df)
        d.to_csv(os.path.expanduser("~"+ "\\Downloads\\")+"Members info.csv")
        del d
    except:
        print("Close the file in excel while being saved.")
    

#menu
while True:
    #dfm=amount.update_room(df,dfm)
    try:
        print(""" Make a choice:
                1. New entry
                2. Modify an old entry
                3. View all data
                4. Delete single entry
                5. Delete all enteries
                6. Service fee details
                7. Expensis details
                8. Export all data
                9. Quite""")
        ch=int(input("Enter your choice: "))
        
    except Exception as e:
        print(e)
        
    else:
            
        if ch==1:
            a=new_data.new_entry(df)
            if type(a)!=str:
                df.loc[len(df)]=a
                new_data.show_recent(df.loc[len(df)-1])
                
        elif ch==2:
            if len(df)>0:
                modification.modify(df)
                save(df)
            else:
                print("No entry exists, file is empty.")
        elif ch==3:
            if len(df)>0:
                print(new_data.show(df))
            else:
                print("No entry exists, file is empty.")

        elif ch==4:
            df=modification.del_single(df)
            
        elif ch==5:
            print("This will cause you to loose all the data..")
            ch=input("Do you still want to delete all data (yes / no): ").lower()
            if ch=='yes':
                export(dfm, dfo,df)
                print("Delecting data now")
                if os.path.isfile("pac/data/entry.dat"):
                    os.remove("pac/data/entry.dat")
                    del df
                    df=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])

                if os.path.isfile('pac/data/amt.dat'):
                    os.remove('pac/data/amt.dat')
                    del dfm
                    dfm=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
                print("Data is deleted")
                    
            else:
                print("No changes made..")
        elif ch==6:
            rooms=new_data.rooms_info(df)
            dfm=amount.opt(rooms,df,dfm)

        elif ch==7:
            dfo=expensis.opt(dfo)

        elif ch==8:
              export(dfm, dfo,df)


        elif ch==9:
            del df
            break
        else:
            print("Invalid entry.")

##        #sort data
        if len(df)>0:
            df=modification.sortarrange(df)
##            
        #save data in external file    
        save(df)
        savem(dfm)
        savex(dfo)


