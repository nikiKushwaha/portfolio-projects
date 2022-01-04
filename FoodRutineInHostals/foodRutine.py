 import pandas as pd 
 import matplotlib.pyplot as plt
 from datetime import date 
 
 print("------------------WELCOME   TO  HOSTAL  ASSOCITION-----------------")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      def addNewfood():	
   foodid = int(input("Enter a food id : "))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        title = input("Enter Food title : ")
   Hostalfood = input("Enter the HostalName : ")   
   cost = int(input("Enter cost of all Foods : "))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  category = input("Enter category of foods : ")
   month = input("Enter Added month of foods : ")
   year = input("Enter Added year of food : ")
   bdf = pd.read_csv("D:\\Hostal\\EXEL FILES\\food.csv")
   n = bdf["foodid"].count()
   bdf.at[n] = [foodid,title,Hostalfood,cost,category]
   bdf.to_csv("D:\\Hostal\\EXEL FILES\\food.csv",index = False)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     print("New Food added  successfully")
   print(bdf)


 def searchFood():
     title = input("Enter a food name : ")
     bdf=pd.read_csv("D:\\Hostal\\EXEL FILES\\food.csv") 
     df = bdf.loc[bdf["title"]==title] 
     if df.empty:
         print("No food found with given  code") 
     else:
         print("Foods details are :")
         print(df)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  def deletefood():
      bookid = float(input("Enter a food id: "))
      bdf = pd.read_csv("D:\\Hostal\\EXEL FILES\\food.csv")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            bdf = bdf.drop(bdf[bdf["bookid"]== bookid].index)
      bdf.to_csv("D:\\Hostal\\EXEL FILES\\food.csv",index= False) 
      print("Food Deleted successfully")
      print(bdf)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

 def showFoods():
     bdf=pd.read_csv("D:\\Hostal\\EXEL FILES\\food.csv")
     print(bdf)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  def showCharts():
     print("Press 1 - food and their Cost")
     ch = int(input("Enter your choice : "))
     if ch == 1:
          df=pd.read_csv("D:\\Hostal\\EXEL FILES\\food.csv")
          df= df[["title","cost"]]
          df.plot("title","cost",kind='bar')
          plt.xlabel('title------->')
          plt.ylabel('cost-------->')
          plt.show()

    
 
 def login():
        uname = input("Enter Username : ")
        pwd = input("Enter password : ")
        df = pd.read_csv("D:\\Hostal\\EXEL FILES\\users.csv")
        df= df.loc[df["username"] == uname]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              if df.empty:
            print("Invalid Username given") 
            return False
         else:
             df = df.loc[df["password"] == pwd]
             if df.empty:
                   print("Invalid Password") 
                   return False
             else:
                   print("Username and Password matched successfully")
                   return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      def showMenu():
      print("-----------------------------") 
      print("---------Digital HostalAssociation---------")
      print("press 1 - Add a New Food")
      print("press 2 - Search for a Food")
      print("press 3 - Delete a  Food") 
      print("press 4 - Show All Foods")
      print("press 5 - Add a New Book")
      print("press 6 - To view charts Food") 
      print("press 7 - To exit")
      choice = int(input("Enter your choice : ")) 
        return choice
   if login():
         while True:
             ch = showMenu()
             if ch == 1:
                 addNewFood()
             elif ch == 2:
                  searchfood()
             elif ch == 3:
                   deletefood()
             elif ch == 4:
                   showfoods() 
             elif ch == 5:
                   showcharts()
             elif ch == 6:
                   break
              else:
                print("Invalid option Selected")
    
        print("THANKYOU FOR VISITING THE hOSTAL fOOD ROUTINE")                                                                                                                                                                                                                                                                                                  