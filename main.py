try:

   a=int(input("enter the first number:"))


   b=int(input("enter  the second number: "))
   print("what kind of opration do you want to perform.\n press + for addition" \
   " \n press - for subtracrion\npress for sicision\npress *for multiplicarion")
   O=input("enter opration :")
   match O:
    case "+":
    
       print(f"the result is: {a+b}")

    case "-":
        print(f"the result is:{a-b}")
    case "*":
        print(f"the result is:{a*b}")
    case "/":
        print(f"the result is:{a/b}")
    case default:
        print(f"there was an error")
except Exception as e:
 print("enter a valid value of a and b")

