# OOP
inheritance OOP
1. Create a superclass called TRADE_DOCUMENT that has the following attributes:
•	Customer_name
•	Customer_addr1
•	Customer_addr2
•	Customer_addr3
•	Phone_number
•	Date
•	Product_name
•	Product_cost
And the following methods:
•	_ _init_ _( )
This is really a MIXIN class, as it is created to be inherited from.

2. Create a subclass SALES_ORDER that has the following attributes:
•	Order_number
•	Email_address
•	VAT_number
And the following methods:
•	Check_email() – just print out a message saying “Checking {} is a valid email”, self.Email_address

 
3. Create a subclass DISPATCH_NOTE has the following attributes:
•	Dispatch_number
•	Email_Address
•	VAT_number
•	VAT_rate
•	Transport_number
•	Total_cost
And the following methods:
•	Calcuate_cost() – populate the Total_cost attribute by taking the Product_cost and using the VAT_rate to calculate the net cost.



4. Create a subclass SALES_INVOICE has the following attributes:
•	Invoice_number
•	VAT_rate
•	Transport_number
•	Total_cost
And the following methods:
•	Send_invoice() – just print out a message saying “Sending {} an invoice”, self.customer_name
