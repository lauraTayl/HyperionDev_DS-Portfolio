import math

#Capstone Project I —Variables and Control Structures used make example program of a finance calculator
#Realised I needed to use floats instead of integers from lecture on Using Variables
#Function to check for number and reprompt if not
def check_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return float(user_input)
        else:
            print("Error: Please enter a valid number.")

#2 options to choose from investment or bond, gives summary, option for input

print('''Investment: to calculate the amount of interest you'll earn on your investment \nBond: to calculate the amount you'll have to pay on a home loan.''')
invest_bond = input(("Enter either investment or bond to proceed: \n")).lower() 

#define bond and investment
#If investment, input for: amount deposited(P), interest rate(%)(r), no. of years(t), simple or compound
#A= total with interest
if invest_bond == "investment":
    if True:
      print("Investment chosen")
      P = check_input("How much money are you depositing?\n£ ")
      r_o = check_input("What is the interest rate? (%)\n")
      t = check_input("How many years do you plan to invest this money?\n")
      interest = input("Do you want to calculate simple or compound interest?\n").lower()
    
    if interest == "simple":
        r = r_o/100
        A = float(P * (1 + r*t))  #formula for simple interest
        print(f" If you invest £{P} at an interest rate of {r_o}% over {t} years, using {interest} interest.\n Your total investment will be £{A}")

    elif interest == "compound":
        r = r_o/100
        A = float(P * math.pow((1+r), t)) #formula for simple interest #something going wrong with this calculcation = fixed
        print(f"If you invest £{P} at an interest rate of {r_o}% over {t} years, using {interest} interest.\n Your total investment will be £{A}") #recorganise sentence to show input data
        
        
#If bond, input for: house value (P), interest rate (i), no of months to repay (n)
elif invest_bond == "bond":
    if True:
        print("Bond chosen")
        P = check_input("What is the value of your house\n£")
        i_o = check_input("What is the monthly interest rate? (%)\n")
        n = check_input("Number of months you expect to repay the bond over\n")
        i = (i_o /100)/12 
        repayment = float((i*P)/(1-(1+i)**(-n)))
        print(f"If the value of your home is £{P} and interest remains at {i_o}% and is repaid over the course of {n} months.\nYou will need to repay £{repayment} each month") #recorganise sentence to show input data
        
#If type isn't either bond or investment error message                 
else:
    print("Invalid data entered please try again") 

