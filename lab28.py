
class TRADE_DOCUMENT: #create superclass called TRADE_DOCUMENT 
    contacts_list= [] #create an empty array
    
    def __init__(self, Customer_name, Customer_addr1, Customer_addr2, Customer_addr3, Phone_number, Date, Product_name, Product_cost): #create a method called __init__
        self.Customer_name=Customer_name   #attributes                                                                                         
        self.Customer_addr1=Customer_addr1
        self.Customer_addr2=Customer_addr2
        self.Customer_addr3=Customer_addr3
        self.Phone_number=Phone_number
        self.Date=Date
        self.Product_name=Product_name
        self.Product_cost=Product_cost
        TRADE_DOCUMENT.contacts_list.append(self)#append the values for the attributes to contacts_list found in TRADE_DOCUMENT
    #END init
#END class


class SALES_ORDER(TRADE_DOCUMENT): #create a subclass called SALES_ORDER
    
    def __init__(self, order_number, Email_address, VAT_number): #create a method called __init__ 
        self.order_number=order_number #attributes
        self.Email_address=Email_address
        self.VAT_number=VAT_number
    #END init


    def Check_email(self, Email_address): #create a method called Check_Email()
        print("Checking {} is a valid email".format(Email_address)) #print message
    #END check_email

    def Calculate_cost(self,Total_cost, Product_cost, VAT_rate):#create a method to calculate the total cost
        Total_cost=Product_cost-(Product_cost*VAT_rate)
    #END Calculate_cost
#END class
class DISPATCH_NOTE(TRADE_DOCUMENT): #create a subclass called DESPATCH_NOTE
    
    def __init__(self, dispatch_number, Email_address, VAT_number, VAT_rate, Transport_number, Total_cost): #with these attributes
        self.dispatch_number=dispatch_number
        self.Email_address=Email_address
        self.VAT_number=VAT_number
        self.VAT_rate=VAT_rate
        self.Transport_number=Transport_number
        self.Total_cost=Total_cost
    # END init
    

    def Calculate_cost(self,Total_cost, Product_cost, VAT_rate):#create a method to calculate the total cost
        self.Total_cost=Product_cost-(Product_cost*VAT_rate)
    #END Calculate_cost

#END class   

class SALES_INVOICE(TRADE_DOCUMENT): 
    def __init__(self, invoice_number, VAT_rate, Transport_number, Total_cost): #with these attributes
        self.invoice_number=invoice_number
        self.VAT_rate=VAT_rate
        self.Transport_number=Transport_number
        self.Total_cost=0
    # END init
    def Send_invoice(self, Customer_name): #create a method called Send_invoice()
        print("Sending ", self.Customer_name, " an invoice")#print message
    #END Send_invoice
    def Calculate_cost(self, Total_cost, Product_cost, VAT_rate):#create a method to calculate the total cost
        self.Total_cost=Product_cost-(Product_cost*VAT_rate)
    #END Calculate_cost
#END class
        

    

c1 = TRADE_DOCUMENT ("John Smith", "19 MainStreet, ", "Newtown, ", "CoDown", "0857744551", "29/01/2017", "Red Earrings", 10.00)
c2 = TRADE_DOCUMENT ("Mary Brown", "44 HighStreet, ", "Oldham, ", "London", "0894483652", "30/01/2017", "Blue earrings", 12.00
                     )

s1 = SALES_ORDER ("441587", "johnsmith@gmail.com", "001568")
s2 = SALES_ORDER ("441588", "maryannbrown@yahoo.com", "152336")

d1 = DISPATCH_NOTE ("458555", "johnsmith@gmail.com", "001568", 0.2, "2215225325", 0) 
d1.Calculate_cost(d1.Total_cost, c1.Product_cost, d1.VAT_rate)

d2 = DISPATCH_NOTE ("558685", "maryannbrown@yahoo.com", "152336", 0.1, "54138453654", 0)
d2.Calculate_cost(d2.Total_cost, c2.Product_cost, d2.VAT_rate)

i1 = SALES_INVOICE ("232", 0.2, "2215225325", 0)
i1.Calculate_cost(i1.Total_cost, c1.Product_cost, i1.VAT_rate)

i2 = SALES_INVOICE ("249", 0.1, "54138453654", 0)
i2.Calculate_cost(i2.Total_cost, c2.Product_cost, i2.VAT_rate)

print("CUSTOMER DETAILS: ")
print("Our customers are:", c1.Customer_name, "and ", c2.Customer_name)
print("Our customers addresses are: ", c1.Customer_addr1, c1.Customer_addr2, c1.Customer_addr3,"and ", c2.Customer_addr1, c2.Customer_addr2, c2.Customer_addr3)
print("Our customers phone numbers are: ", c1.Phone_number, "and", c2.Phone_number)
print("Our customers date of first contact is: ", c1.Date, "and", c2.Date)
print("The products that our customers ordered are: ", c1.Product_name, "and", c2.Product_name)
print("The products that our customers ordered cost: ", c1.Product_cost, "and", c2. Product_cost)
print("")

print("SALES ORDERS: ")
print("Our sales orders numbers are:", s1.order_number, "and ", s2.order_number)
print("Our customers email addresses are:", s1.Email_address, "and ", s2.Email_address)
print("Our customers VAT numbers are: ", s1.VAT_number, "and", s2.VAT_number)
print(s1.Check_email(s1.Email_address))
print("")

print("DISPATCH NOTE DETAILS: ")
print("The dispatch numbers are: ", d1.dispatch_number, "and", d2.dispatch_number) 
print("The email addresses are: ", d1.Email_address, "and", d2.Email_address)
print("The VAT numbers are: ", d1.VAT_number, "and", d2.VAT_number)
print("The VAT rates are: ", d1.VAT_rate, "and", d2.VAT_rate)
print("The transport numbers are: ", d1.Transport_number, "and", d2.Transport_number)
print("The total cost is: ", d1.Total_cost, "and", d2.Total_cost)
print("")

print("SALES INVOICE DETAILS: ")
print("The sales invoice numbers are: ", i1.invoice_number, "and", i2.invoice_number)
print("The VAT rates are: ", i1.VAT_rate, "and", i2.VAT_rate)
print("The transport numbers are: ", i1.Transport_number, "and", i2.Transport_number)
print("The total cost is: ", i1.Total_cost, "and", i2.Total_cost)
