class Adminvariables:

    def __init__(self,FoodID=101,Name='x',Quantity='1 piece',Price=1,Discount=0,Stock=1):
        self.FoodID=FoodID
        self.Name=Name
        self.Quantity=Quantity
        self.Price=Price
        self.Discount=Discount
        self.Stock=Stock

    def __str__(self):
        return f'{self.FoodID}.{self.Name}({self.Quantity})[INR{self.Price}]\n'
                
    
    #setters for admin variables:

    def set_FoodID(self,FoodID):
        self.FoodID=FoodID
    def set_Name(self,Name):
        self.Name=Name
    def set_Quantity(self,Quantity):
        self.Quantity=Quantity
    def set_Price(self,Price):
        self.Price=Price
    def set_Discount(self,Discount):
        self.Discount=Discount
    def set_Stock(self,Stock):
        self.Stock=Stock


    #getters for admin variables:

    def get_FoodID(self):
        return self.FoodID
    def get_Name(self):
        return self.Name
    def get_Quantiy(self):
        return self.Quantity
    def get_Price(self):
        return self.Price
    def get_Discount(self):
        return self.Discount
    def get_Stock(self):
        return self.Stock

class Uservariables:

    def __init__(self,Fullname,Phonenumber,Email,Address,Password):
        self.Fullname=Fullname
        self.Phonenumber=Phonenumber
        self.Email=Email
        self.Address=Address
        self.Password=Password

    def __str__(self):
        return f'''
        Fullname :{self.Fullname}\n
        Phonenumber :{self.Phonenumber}\n
        Email : {self.Email}\n
        Address : {self.Address}\n
        Password :{self.Password}\n
        '''
    #setters for user variables

    def set_Fullname(self,Fullname):
        self.Fullname=Fullname
    def set_Phonenumber(self,Phonenumber):
        self.Phonenumber=Phonenumber
    def set_Email(self,Email):
        self.Email=Email
    def set_Address(self,Address):
        self.Address=Address
    def set_Password(self,Password):
        self.Password=Password

    #getters for user variables

    def get_Fullname(self):
        return self.Fullname
    def get_Phonenumber(self):
        return self.Phonenumber
    def get_Email(self):
        return self.Email
    def get_Address(self):
        return self.Address
    def get_Password(self):
        return self.Password
         
    



