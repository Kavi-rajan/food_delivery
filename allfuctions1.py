import time
import colorama
colorama.init()
from stdiomask import getpass
from allvariables1 import Adminvariables,Uservariables

class Adminfunctions:

    Menu={}
    Foodid=1
    def addfood(self):
        print('►'*7,"Add Food",'◄'*7)
        FoodID=self.Foodid
        self.Foodid+=1
        print("Food ID =",FoodID)
        Name=input('Enter Food name :')
        Quantity=input('Quantity :')
        Price=float(input('Price :Rs.'))
        Discount=int(input('Discount :'))
        Stock=int(input('Stock :'))
        food_obj=Adminvariables(FoodID,Name,Quantity,Price,Discount,Stock)
        self.Menu[FoodID]=food_obj
                
        print("Food item added succesfully !!\n")
        print('Added item :',self.Menu[FoodID])
        print('▒'*50)
    
    def editfood(self):
        print('►'*7,"Edit Food",'◄'*7)
        FoodID=int(input("Enter ID of the food you want to edit :"))
        
        if FoodID in self.Menu:
            Name=input('Enter Food name :')
            Quantity=input('Quantity :')
            Price=float(input('Price :Rs.'))
            Discount=int(input('Discount :'))
            Stock=int(input('Stock :'))

            self.Menu[FoodID].set_Name(Name)
            self.Menu[FoodID].set_Quantity(Quantity)
            self.Menu[FoodID].set_Price(Price)
            self.Menu[FoodID].set_Discount(Discount)
            self.Menu[FoodID].set_Stock(Stock)

            print('Food item edited sucessfully!!!\n')
            print('edited food item :',self.Menu[FoodID])
            
        else:
            print("Invalid ID")
        print('▒'*50)

    def viewfood(self):
        print('►'*7,"VIEW MENU",'◄'*7)
        for food in Adminfunctions.Menu.values():
            print(food)
        print("End of Menu")
        print('▒'*50)

    def removefood(self):
        print('►'*7,"Remove Food",'◄'*7)
        FoodId=int(input("Enter ID of the food you want to delete :"))
        
        if FoodId in self.Menu:
            print('Item removed successfully!!')
            del self.Menu[FoodId]
            
        else:
            print('Invalid ID')

        print('▒'*50) 

class Userfunctions:
    Customerlist={}
    Orderslist=[]

    def register(self):
        print('►'*7,'Register Yourself','◄'*7)
        Fullname=input("Enter your Full Name :")
        Phonenumber=int(input("Enter your Phonenumber :"))
        Email=input("Enter your mail :")
        Address=input("Enter your Address :")
        Password=input("Enter your password :")
        customer_obj=Uservariables(Fullname,Phonenumber,Email,Address,Password)
        self.Customerlist[Fullname]=customer_obj
        print('Your account has been registered succesfully!!\n')
                       
    def placeneworder(self):
        Adminfunctions.viewfood(self) 
        print('►'*7,'Place New Order','◄'*7)
        order=input("Enter the IDs of the food you want to order with comma in between :")
        order=order.split(',')
        order[:]=[int(i) for i in order]
        IDlist=list(Adminfunctions.Menu)
        if(all(x in IDlist for x in order)):
            for i in order[:]:
                for food in Adminfunctions.Menu.values():
                    if food.FoodID==i and food.Stock==0:
                        print(f'Sorry,{food.FoodID}.{food.Name} is out of stock.\nSo it is removed from order')
                        order.remove(i)
                    elif food.FoodID==i and food.Stock>0:
                        print(food)
            print(order)
            if len(order)>0:           
                print('1.Place the order\n2.Edit the Order\n') 
                choice=int(input("Enter your response :"))     
                if choice==1:
                    Fullname=input("Enter your Name to confirm the order :")
                    Password=getpass("Enter password to place the order :")
                    if Fullname in self.Customerlist and self.Customerlist[Fullname].Password==Password:
                        self.Orderslist.append([Fullname,order])
                        for i in order:
                            for food in Adminfunctions.Menu.values():
                                if food.FoodID==i:
                                    food.Stock-=1
                        print('Placing order...')
                        for i in range(51):
                            bar='█'*i+'-'*(50-i)
                            time.sleep(0.1)
                            print(colorama.Fore.CYAN+f"\r|{bar}|{2*i}%",end='\r'+colorama.Fore.RESET )
                        print("\norder Placed successfully!!")
                    else:
                        print('Invalid Credentials')
                elif choice==2:
                    self.placeneworder()         
        else:
            print('Id you entered is not in Menu')        
        
    def orderhistory(self):
        Fullname=input("Enter your Name to view your order history :")
        print('►'*7,'Order History','◄'*7)
        namelist=[i[0] for i in self.Orderslist]
        if Fullname in namelist:
            for term in self.Orderslist:
                if term[0]==Fullname:
                    print(term[1])
        else:
            print('No orders in given name')
        
    def updateprofile(self):
        print('►'*7,'Update Profile','◄'*7)
        name=input("Enter your Full Name :")
        P_word=getpass("Enter your present password :")
        if name in self.Customerlist and self.Customerlist[name].Password==P_word:
            Phonenumber=int(input("Enter your new Phonenumber :"))
            Email=input("Enter your new  mail :")
            Address=input("Enter your new Address :")
            Password=input("Enter your new password :")

            self.Customerlist[name].set_Phonenumber(Phonenumber)
            self.Customerlist[name].set_Email(Email)
            self.Customerlist[name].set_Address(Address)
            self.Customerlist[name].set_Password(Password)
            print('Profile updated Successfully')
        else:
            print('Invalid Credentials')

