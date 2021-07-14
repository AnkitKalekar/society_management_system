#amount

import pandas as pd
import numpy as np
import os, pickle
import new_data, modification

dfa=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])



def run():
    f=open("entry.dat",'rb')
    obj=pickle.loads(f.read())
    df=obj
    rooms=new_data.rooms_info(df)
    return opt(rooms, df, dfm)


class Hidem:
    def __init__(self,lst):
        self.room_no=lst[0]
        self.jan=lst[1]
        self.feb=lst[2]
        self.mar=lst[3]
        self.apr=lst[4]
        self.may=lst[5]
        self.jun=lst[6]
        self.jul=lst[7]
        self.aug=lst[8]
        self.sep=lst[9]
        self.oct=lst[10]
        self.nov=lst[11]
        self.dec=lst[12]

def show(dfm):
    global dfa
    dfm=dfa
    df1=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
    if len(dfm)>0:
        for i in range(len(dfm)):
            df1.loc[i]=[dfm.loc[i].room_no.room_no, dfm.loc[i].jan.jan, dfm.loc[i].feb.feb, dfm.loc[i].mar.mar, dfm.loc[i].apr.apr, \
                        dfm.loc[i].may.may, dfm.loc[i].jun.jun, dfm.loc[i].jul.jul, dfm.loc[i].aug.aug, dfm.loc[i].sep.sep, \
                        dfm.loc[i].oct.oct, dfm.loc[i].nov.nov, dfm.loc[i].dec.dec ]
        return df1

def show_recent(dfs):
    df1=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
    df1.loc[0]= [dfs.room_no.room_no, dfs.jan.jan, dfs.feb.feb, dfs.mar.mar, dfs.apr.apr, \
                    dfs.may.may, dfs.jun.jun, dfs.jul.jul, dfs.aug.aug, dfs.sep.sep, \
                    dfs.oct.oct, dfs.nov.nov, dfs.dec.dec ]
    print(df1)
    del df1

def single(room,dfm):
    df1=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
    for i in range(len(dfm)):
        df1.loc[i]=[dfm.loc[i].room_no.room_no, dfm.loc[i].jan.jan, dfm.loc[i].feb.feb, dfm.loc[i].mar.mar, dfm.loc[i].apr.apr, \
                    dfm.loc[i].may.may, dfm.loc[i].jun.jun, dfm.loc[i].jul.jul, dfm.loc[i].aug.aug, dfm.loc[i].sep.sep, \
                    dfm.loc[i].oct.oct, dfm.loc[i].nov.nov, dfm.loc[i].dec.dec ]
    lst=[]
    lst=df1.values.tolist()
    lst_room=df1.room_no.values.tolist()
    idx=lst_room.index(room)
    del df1
    df1=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])

    for i in range(len(lst)):
        df1.loc[i]=hidem(lst[i])
    dfa=df1
    return dfa

def room_info(dfm):
    lst=[]
    df1=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
    df1=show(df1)
    print(df1)
    lst=df1.room_no.tolist()
    print(lst)

def check(lst):
    count=0
    for i in lst:
        if i!=0:
            count+=1
    if count>11:
        return 'err_excess'
    
def fill(rooms,df,dfm):
    if len(df)==0:
        print('No room entries available')
        return dfm
    if len(dfm)==0:
        dfm=update_room(df,df1)
        
    room_id=input("Enter room number: ")
    if room_id in rooms:
        service_fee=int(input("Enter service fee: "))
        amount=int(input("Enter amount paid: "))

        lst=[]
        df1=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
        df1=show(dfm)
        
        room_list=show(dfm).room_no.values.tolist()
        idx=room_list.index(room_id)
        div=amount//service_fee
        lst=df1.loc[idx].values.tolist()
        if check(lst)!="err_excess":
            for i in range(1,13):
                if lst[i]==0:
                    lst[i]=service_fee
                    amount-=service_fee
                if amount==0:
                    break
                                
            dfa.loc[idx]=Hidem(lst)
            show_recent(dfa.loc[idx])
            del lst
            return dfa
        else:
            print("Amount exceeds this year's limit")
            return dfm
          
    else:
        print("This room does not exist")
        return dfm


def sort_arrange(dfm):
    global dfa
    if len(dfm)!=0:
        df1=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
        lst=[]
        lst=show(dfm).values.tolist()
        lst.sort()
        for i in range(len(lst)):
            df1.loc[i]=Hidem(lst[i])
        dfa=df1
        return dfa
    else:
        return dfa

def del_room(room_list, stored_room,dfm):
    global dfa
    df2=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
    df1=show(dfm)
    lst_df=df1.values.tolist()
    #print('lst_df', lst_df)
    if len(room_list)!=len(stored_room):
        lst=list( set(room_list).intersection(set(stored_room)) )
        lst=lst+list( set(room_list) - set(stored_room))
        idx=[]
        for i in range(len(lst)):
            for j in range(len(lst_df)):
                if lst[i] == lst_df[j][0]:
                    idx.append(j)
        for i in idx:
            df2.loc[len(df2)]=Hidem(lst_df[i])
        #print('dataframe' ,show(df2))
        dfm=df2
        dfa=df2
        return df2
    else:
        return dfm

    
def update_room(df,dfm):
    global dfa
    if len(dfm)>0:
        dfa=dfm
    room_list=new_data.rooms_info(df)
    if len(dfm)==0:
      for i in range(len(room_list)):
        dfa.loc[len(dfa)]=Hidem([room_list[i], 0, 0, 0, 0, 0, 0, \
                                 0, 0, 0, 0, 0, 0])
    else:
        
        stored_room= show(dfm).room_no.tolist()
        for i in range(len(room_list)):

            if room_list[i] not in stored_room:
                dfm.loc[len(dfm)]=Hidem([room_list[i], 0, 0, 0, 0, 0, 0,\
                                   0, 0, 0, 0, 0, 0])
                
    dfa=del_room(room_list, stored_room, dfm)
    dfm=dfa
    return dfa



        
def remove(rooms,dfm):
    global dfa
    if len(dfa)==0:
        update_room(dfa)
    print(show(dfm).room_no.values.tolist())       
    room_id=input("Enter room number: ")
    if room_id in rooms:
        print("Last paid amount will be removed")
        lst=[]
        df1=pd.DataFrame(columns=['room_no','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov', 'dec'])
        df1=show(dfm)
            
        room_list=show(dfm).room_no.values.tolist()
        idx=room_list.index(room_id)
        print(idx)
        lst=show(dfm).loc[idx].values.tolist()
        for i in range(1,13):
            if lst[i]==0:
                lst[i-1]=0
            elif i==12:
                lst[12]=0
                            
        dfm.loc[idx]=Hidem(lst)
        show_recent(dfm.loc[idx])
        del lst
    return dfm
    

def opt(rooms,df,dfm):
    global dfa
    while True:
        dfa=dfm
        update_room(df,dfm)
        dfm=sort_arrange(dfm)
        if len(df)==0:
            print('No entries avalible, first add new entries')
            return dfm
        ch=int(input("""Choose:
                            1. Make an entry
                            2. Remove an entry
                            3. Show
                            4. quite
                        
                Enter choice: """))
        
        if ch==1:
            print(rooms)
            return fill(rooms,df, dfm)
            
        elif ch==2:
            return remove(rooms, dfm)
            
        elif ch==3:
            print(show(dfa))
            return dfa
            
        elif ch==4:
            return dfa
       
