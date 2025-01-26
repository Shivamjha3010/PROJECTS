import time
import maskpass

print("Enter your card")

time.sleep(1)

balance = 10000
password = 3010

pin = int(maskpass.askpass(prompt="Enter Your 4-Digit Pin: ", mask="*"))

if pin == password:
    while True:
        print("""
            1. Check balance
            2. Withdraw Balance
            3. Deposit Balance
            4. Change Pin 
            5. Exit
        """)
        try:
            option = int(input("Enter your Choice-"))
        except ValueError:
              print("Enter valid option")
              continue
        
        if option == 1:
          print(f"Your Balance is-{balance}")

        elif option == 2:
            withdraw_amonut = int(input("Enter the amount-"))
            if balance>=withdraw_amonut:            
               balance=balance-withdraw_amonut
               print(f"withdraw amount is been debited from your account")
               print(f"Balance={balance}")
            else:
               print("Insufficent Balance")  

        elif option == 3:
            Deposit_amonut = int(input("Enter the amount-"))
            balance=balance+Deposit_amonut
            print(f"withdraw amount is been creadited from your account")
            print(f"Balance={balance}")  

        elif option == 4:
            a=int(maskpass.askpass(prompt="Enter Your 4-Digit Pin: ", mask="*"))  
            if a == password: 
               New_pin=int(maskpass.askpass(prompt="Enter Your New 4-Digit Pin: ", mask="*"))
               password=New_pin
               print("Pin Changed Sucessfully")
            else:
               print("Wrong Pin Try Again")

        elif option == 5:
          print("Thank You for using our services")
          break

        else:
           print("Invalid Option")
           

else:
     print("Wrong pin try again later")       