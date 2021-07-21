import new_data, modification, amount, expensis
import pandas as pd, pickle, os

#dataframe
df=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])
dfm=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
dfo=pd.DataFrame(columns=["date", "title","amount"])

#fee dataframe load
if os.path.isfile("amt.dat"):
    file=open("amt.dat", 'rb')
    obj = file.read()
    if len(obj)>0:
        obj= pickle.loads(obj)
        dfm=obj
        file.close()

def savem(dfm):
    file=open('amt.dat','wb')
    obj= pickle.dumps(dfm)
    file.write(obj)
    file.close()


if os.path.isfile("exp.dat"):
    file=open("exp.dat", 'rb')
    obj = file.read()
    if len(obj)>0:
        obj= pickle.loads(obj)
        dfo=obj
        file.close()
        
def savex(dfm):
    file=open('exp.dat','wb')
    obj= pickle.dumps(dfo)
    file.write(obj)
    file.close()



#load data from file
if os.path.isfile("entry.dat"):
    file=open("entry.dat", 'rb')
    obj = file.read()
    if len(obj)>0:
        obj= pickle.loads(obj)
        df=obj
    file.close()


# function to save data in file
def save(df):
    file=open("entry.dat",'wb')
    obj=pickle.dumps(df)
    file.write(obj)
    
    file.close()    


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
                8. Quite""")
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
            print("This will cause you to all the data..")
            ch=input("Do you still want to delete all data (yes / no): ").lower()
            if ch=='yes':

                print("Data will be stored into ur pc as csv")
                d=amount.show(dfm)
                d.to_csv("Maintanence.csv")
                del d

                d=expensis.show(dfo)
                d.to_csv("Expensis.csv")
                del d

                d = new_data.show(df)
                d.to_csv("Menbers info.csv")
                del d

                print("Delecting data now")
                if os.path.isfile("entry.dat"):
                    os.remove("entry.dat")
                    del df
                    df=pd.DataFrame(columns=['room_no','owner','owner_contact','rented','tenent','tenent_contact','complaint'])

                if os.path.isfile('amt.dat'):
                    os.remove('amt.dat')
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
            
            print("Data will be stored into ur pc as csv")
            d=amount.show(dfm)
            d.to_csv("Maintanence.csv")
            del d

            d=expensis.show(dfo)
            d.to_csv("Expensis.csv")
            del d

            d = new_data.show(df)
            d.to_csv("Menbers info.csv")
            del d

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


