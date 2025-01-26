import math
print("Looking To Split the cost of a Group Purchase? \nWelcome To Our Receipt Calculator. \nWe Will Ask a Few Question About Your Purchase(s) To Calculate Total Cost Per Person)")
price_all = eval(input("Please Enter The Cost Of Each Meal.\n(Eliminate The '$' Sign):"))
tax_p = float(input("What are The Sales Tax in your Area.\n(Elminate the '%' Sign):"))
split_p = float(input("How Many People are You Spitting The Bill With:"))
tip = int(input("What Percentage Would You Like To Give As a Tip.\n(Note:Eliminate The '%' Sign):"))
total_p = (price_all + (price_all*(tax_p/100)))+(price_all*(tip/100)/split_p)
final_P = round(total_p,2)
print("Your Total Bill is ₹",final_P,"\nThank You")