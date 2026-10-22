#WAP to Get Book details uisng  keyword and default parameter (default para (4) and 10 over all parameters)

def book(title,author,price,Sr_no,shelf_no=23,category="Historic",Pages=500):
    print("Title :",title)
    print("Author :",author)
    print("Price :",price)
    print("Serial No :",Sr_no)
    print("Shelf :",shelf_no)
    print("Category :",category)
    print("Pages :",Pages)

title=input("Enter Title of Book :")
author=input("Enter Author of Book :")

book(title,author,price=1000,Sr_no=196)
