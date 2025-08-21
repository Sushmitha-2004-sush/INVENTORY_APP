from dataaccessobject.ProductDaoImple import ProductDaoImplementation
from dataaccessobject.AbstractProductDao import ProductDaoService
from models.product import Product
from datetime import datetime
class ProductManagementLib:
    'hnadles CRUD logic'
    dao_service: ProductDaoService = ProductDaoImplementation()

    @staticmethod
    def display_all():
        products = ProductManagementLib.dao_service.display_all_products()
        for product in products:
            print(product)
    @staticmethod
    def add_product():
        product = Product()
        productName = input("Enter the product name:")
        product.set_product_name(productName)
        unitprice = float (input("Enter unit price:"))
        product.set_unitprice(unitprice)
        categoryid = int(input("Enter category id:"))
        product.set_categoryid(categoryid)
        m_date = input("Enter manufacture Date(dd/MM/YYYY):")
        util_date = datetime.strptime(m_date, "%d/%M/%Y")
        conv_m_date = util_date.date()
        product.set_manufacture_date(conv_m_date)
        #product.set_is_active(is_active="Y")# instead of this is_active = input("Product available? (y/N)") nl product.set_is_active(is_active)
        if ProductManagementLib.dao_service.insert_products(product):
            print("Inserted successfully.....")
        else:
            print("Something went wrong")

    @staticmethod
    def update_product():
        searchid = int(input("Enter the product ID :"))
        #Create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not product:
            print("Product not found")
            return
        print(product)
        confirm = input("Do you want to edit this data:(y/n)")
        if confirm.lower()=='y':
            product.set_product_name(input("Enter new product name:"))
            product.set_unitprice(float(input("Enter New Unit Price:"))) #use menudriven for what ever we want to update using choice 1,2..
            #pass the object to dao update
            if ProductManagementLib.dao_service.update_product(product,searchid):
                print("Updated successfully...")
            else:
                print("Something went wrong....")
    @staticmethod
    def disable_product():
        searchid = int(input("Enter the product ID to disable:"))
        #Create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not product:
            print("Product not found")
            return
        print(product)
        confirm = input("Do you want to disable the product:(y/n)")
        if confirm.lower()=='y':
            product.set_is_active("N")
           
            #pass the object to dao update
            if ProductManagementLib.dao_service.disable_product(product,searchid):
                print("disabled successfully...")
            else:
                print("Something went wrong....")
    @staticmethod
    def apply_gst_to_product():
        product_id = int(input("Enter the product ID to apply GST:"))
        gst_percent = float(input("Emter the GST percentage to apply:"))
        if ProductManagementLib.dao_service.apply_gst(product_id,gst_percent):
            print(f"GST of {gst_percent} applied to productID {product_id}")
        else:
            print("failed to apply GST")

    
