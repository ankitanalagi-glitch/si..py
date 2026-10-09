def simple_interest(principal, interest, time):
    return (principal*interest*time)/100

if __name__=="__main__":
    principal = float(input("Enter principal amount: "))
    interest = float(input("Enter rate of interest: "))
    time = float(input("Enter time in time: "))

    print("Simple Interest =", simple_interest(principal, interest, time))
