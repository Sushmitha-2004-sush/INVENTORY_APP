from datetime import date
import re
class Product:
    'Python OOPs applied'
    def __init__(self,productid = None,productName=None,
                 unitprice=None,categoryid=None,
                 manufacturedate=None,
                 is_active="Y"):
        self.__productid=productid
        self.__productName=productName#vlidating productname
        self.__unitprice=unitprice
        self.__category_id=categoryid
        self.__manufacture_date= manufacturedate if manufacturedate else date.today()
        self.__is_active = is_active

        #---------------
        #GETTERS AND SETTERS
        #---------------
    def get_productid(self):
        return self.__productid
    def set_productid(self,productid):
        self.__productid = productid
    def get_productname(self):
        return self.__productName
    def set_product_name(self,productName):
        'validate product name before setting(2-30 alphabets / underscore)'
        pattern = re.compile(r"^[A-Za-z_]{2,30}$")

        while True:
            if pattern.match(productName):
                self.__productName = productName
                break
            else:
                print("\t\t Invalid product name must have only alphabets & _ min character 3!!....")
                productname=input("\t\t Enter Product name again:")
    def get_unitprice(self):
        return self.__unitprice
    def set_unitprice(self,unitprice):
        self.__unitprice = unitprice

    def get_categoryid(self):
        return self.__category_id
    def set_categoryid(self,categoryid):
        self.__category_id = categoryid

    def get_manufacture_date(self):
        return self.__manufacture_date 
    def set_manufacture_date(self,manufacturedate):
        if isinstance(manufacturedate,date):
            self.__manufacture_date = manufacturedate
        else:
            raise ValueError("Manufacture date must be data object")
        
    def get_is_active(self):
        return self.__is_active
    def set_is_active(self,is_active):
        self.__is_active = is_active

    #override __str__
    def __str__(self):
        return (
            f"productID :{str(self.get_productid()):<10}, "
            f"ProductName:{str(self.__productName or ''):<20}, "
            f"Categoryid:{str(self.__category_id or ''):<10}, "
            f"UnitPrice:{str(self.__unitprice or ''):<15}, "
            f"ManufactureDate:{str(self.__manufacture_date or ''):<15}, "
            f"Isactive:{str(self.__is_active or ''):<10}"
            )
 #<10,<15 are spacing 
         

        
        