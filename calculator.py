while True:
    
    print("=== 1 For Addition ===")
    print("=== 2 For Substraction ===")
    print("=== 3 For Multiplication === ")
    print("=== 4 For Division ======")
    print("=== 5 For Module ====")
    print("=== 6 For Exit =====")
    choice= int(input("== Enter Your Choice : "))
    num1 = float(input("Enter First Number :"))
    num2 = float(input("Enter Second Number :"))
    
    if choice == 1 :
        print("--- Sum of ",num1, " and ",num2," is ",num1+num2)
    elif choice == 2 :
        print("--- Sub of ",num1, " and ",num2," is ",num1-num2)
    elif choice == 3 :
        print("--- Multi of ",num1, " and ",num2," is ",num1*num2)
    elif choice == 4 :
        print("--- Div of ",num1, " and ",num2," is ",num1/num2)
    elif choice == 5 :
        print("--- Mod of ",num1, " and ",num2," is ",num1%num2)
    elif choice == 6:
        exit
