import colorama
colorama.init()
from stdiomask import getpass
from allfuctions1 import Adminfunctions,Userfunctions
class AdminActions(Adminfunctions):
    def execute(self,option):
        if option==1:           
            Adminfunctions.addfood(self)
        if option==2:            
            Adminfunctions.editfood(self)
        if option==3:            
            Adminfunctions.viewfood(self)
        if option==4:            
            Adminfunctions.removefood(self)

class UserActions(Userfunctions):
    def execute(self,choice):
        if choice=='a':            
            Userfunctions.register(self)
        if choice==1:           
            Userfunctions.placeneworder(self)
        if choice==2:
            Userfunctions.orderhistory(self)
        if choice==3:
            Userfunctions.updateprofile(self)

if __name__=='__main__':
    NameOfAdmin='admin'
    Password='123'
    adminact=AdminActions()
    useract=UserActions()
    while True:
        print(colorama.Fore.RED+'♥ '*7+"PROGRAMMER'S CAFE"+' ♥'*7+colorama.Fore.RESET)
        print('≈'*45)
        print("CHOICES:\n\n1.Admin\t\t2.Customer")
        print('≈'*45)
        choice=int(input("Enter your choice :"))
        if choice==1:
            name=input('Enter Admin name :').lower().strip()
            if name!=NameOfAdmin:
                print("You are not an authorised user.")
            else:
                print(f'welcome {name}!')
                key=getpass('Enter Password : ') #password is 123
                while name==NameOfAdmin and key==Password:
                    print('≈'*45)
                    print(colorama.Fore.YELLOW+' '*8+'♠ Welcome Admin ♠'+colorama.Fore.RESET)
                    print('\n1.Add fooditem\n2.Edit Fooditem\n3.View Menu\n4.Remove Fooditem\n5.Exit Admin Portal')
                    print('≈'*45)
                    option=int(input("Enter your option :"))
                    if option==5:
                        print('You are exiting Admin portal')
                        print('≈'*45)
                        break
                    adminact.execute(option)
                else:
                    print('Incorrect password')
        elif choice==2:
            print('≈'*45)
            print("A==>Register\n\nB==>Log in")
            print('≈'*45)
            key=input("Enter your choice :").lower()
            if key=='a':
                useract.execute('a')
            elif key=='b':
                name=input("Enter your Full Name :")
                P_word=getpass("Enter your password :")           
                if name in Userfunctions.Customerlist and Userfunctions.Customerlist[name].Password==P_word:
                    print(colorama.Fore.MAGENTA +'\n'+' '*7+f'♠ Welcome {name} ♠'+colorama.Fore.RESET)
                else:
                    print('invalid credentials')       
                while name in Userfunctions.Customerlist and Userfunctions.Customerlist[name].Password==P_word:
                    print('≈'*45)
                    print('1.Place new Order\n2.View Order History\n3.Update Profile\n4.Exit User portal')
                    print('≈'*45)
                    option=int(input('Enter your choice :'))
                    if option==4:
                        print("You are exiting User portal\n")
                        break 
                    useract.execute(option)
                            
               





