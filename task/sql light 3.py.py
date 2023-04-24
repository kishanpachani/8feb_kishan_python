import sqlite3

print("press o for create table")
print("press 1 for insert data in table")
print("press 2 for update record in table")
print("press 3 for delete recrd in table")

try:
    dbcon=sqlite3.connect('nn.db')
    print("database connected")
except Exception as e:
        print(e)


a=int(input("enter number="))


if a==0:
    print("-------------------------------here create new table----------------------------------------------------")
    table=int(input("how many you are create table="))
    for i in range(table):
        print(i)
        sttnm=str(input("enter your table name="))
        stcl1=str(input("enter first column name="))
        stcl2=str(input("enter secouned column name="))
        stcl3=str(input("enter trd column name="))
        stcl4=str(input("enter fourth column name="))

        create_table=f"create table '{sttnm}' ('{stcl1}' integer primary key autoincrement, '{stcl2}' text,'{stcl3}' text, '{stcl4}' text )"
        try:
             dbcon.execute(create_table)
             print("Table created successfuly")
        except Exception as e:
             print(e)


elif a==1:
     print("-------------------------------here insert data in table----------------------------------------------------")
     sttnm=str(input("enter your table name="))
     """n=int(input("how many add values"))
     for i in range(n):
          print(i)"""
     #stid=(input("enter your id"))
     stnm=input("enter your  name=")
     stcy=input("enter your  city=")
     stnu=input("enter your  number=")

     insert_data=f"insert into '{sttnm}'(name,city,number) values('{stnm}','{stcy}','{stnu}')"
     try:
        dbcon.execute(insert_data)
        dbcon.commit()
        print(insert_data)
     except Exception as e:
      print(e)

elif a==2:
    print("-------------------------------here update data in table----------------------------------------------------")
    sttnm=str(input("enter your table name="))
    stnm=str(input("enter new name="))
    stcy=str(input("enter new city="))
    stwh=str(input("enter id="))

    
    update_data=f"update '{sttnm}' set name='{stnm}', city='{stcy}' where id='{stwh}'"
    try:
        dbcon.execute(update_data)
        dbcon.commit()
        print("updated new data")
    except Exception as e:
        print(e)

elif a==3:
    print("-------------------------------here delete record in table----------------------------------------------------")
    sttnm=str(input("enter your table name="))
    #stnm=str(input("enter new name="))
    #stcy=str(input("enter new city"))
    #stwh=str(input("enter id="))

    delete_data=f"delete from '{sttnm}'"
    try:
        dbcon.execute(delete_data)
        dbcon.commit()
        print("deleted data ")
    except Exception as e:
        print(e)

else:
    print("select proper nummber in list")

