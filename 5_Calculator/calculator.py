def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return(n1-n2)
def mul(n1,n2):
    return(n1*n2)
def div(n1,n2):
    return(n1/n2)

operation={
    '+':add,
    '-' : sub,
    '*' : mul,
    '/' : div
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is 1st number?"))
    while should_accumulate:
        for sym in operation:
            print(sym)
        operation_symbol = input("Pick an operation:")
        num2 = float(input("What is next number?"))
        answer = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type yes to continue calculating with {answer}, otherwise no:")
        if choice == 'yes':
            num1 = answer
            # calculator()
        else:
            should_accumulate = False
            user_choice = input("Types yes if you want to calculate again, otehrwise no:")
            if user_choice == 'yes':
                print("\n" *20)
                calculator()
        
calculator()