import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="select type of payment", action="store")
parser.add_argument("--interest", help="specify interest", type=float,action="store")
parser.add_argument("--payment", help="specify payment", type=float, action="store")
parser.add_argument("--principal", help="specify principal",type=float, action="store")
parser.add_argument("--periods", help="specify payment period",type=int, action="store")
args = parser.parse_args()

if args.type =="diff" and args.payment == None and args.periods !=None and args.principal != None and args.interest != None:
    interest = args.interest /1200
    principal =args.principal
    periods = args.periods

    for i in range(1,periods+1):
        print("Month",i,": paid out ",math.ceil(principal/periods + interest*(principal -(principal*(i-1))/periods)))
    total_pay = 0
    for j in range(1,periods+1):
        total_pay = total_pay + math.ceil(principal/periods + interest*(principal -(principal*(j-1))/periods))
    print("\nOverpayment =",math.ceil(total_pay - principal))


elif args.type =="diff" and args.payment != None:
    print("Incorrect parameters")

elif args.type == "annuity" and args.principal !=None and args.interest != None and args.periods != None and args.payment == None:
    interest = args.interest/1200
    periods = args.periods
    principal = args.principal
    annuity_payment = math.ceil(principal * (interest * math.pow(1+interest, periods))/(math.pow(1+interest, periods)-1))
    print("Your annuity payment =",(annuity_payment),"!")
    print("Overpayment =", math.ceil(periods * annuity_payment - principal))

elif args.type == "annuity" and args.principal ==None and args.interest != None and args.periods != None and args.payment != None:
    interest = args.interest/1200
    periods = args.periods
    principal = args.principal
    payment = args.payment
    credit_principal = payment / ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
    actual_pay = payment * periods
    print("Your credit principal =",math.ceil(credit_principal),"!")
    print("Overpayment =",math.ceil(actual_pay - credit_principal))

elif args.type == "annuity" and args.principal !=None and args.interest != None and args.periods == None and args.payment != None:
    interest = args.interest/1200
    principal = args.principal
    payment = args.payment
    number_of_payments = math.ceil(math.log((payment / (payment - interest * principal)), (1 + interest)))
    years_months = (math.modf(number_of_payments / 12))
    if years_months[1] != 0 and years_months[0]== 0:
        print("You need",math.ceil(years_months[1]),"years to repay this credit!")
    elif years_months[1]==0 and years_months[0]!=0:
        print("You need", math.ceil(years_months[0]*12), "months to repay this credit!")
    elif years_months[1] !=0 and years_months[0]!=0:
        print("You need", math.ceil(years_months[1]), "years and ",math.ceil(years_months[0]*12),"months to repay this credit!")
    actual_pay = number_of_payments*payment
    print("Overpayment =",math.ceil(actual_pay - principal))

else:
    print("Incorrect parameters")
