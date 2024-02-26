def main():
  print("This is monthly payment loan calculation ")
  print("")

  priciple = float(input("input the loan amount: "))
  apr = float(input("input the annual interest rate: "))
  years = int(input("input amount of year: "))
  

  monthly_interset_rate = apr / 1200
  amount_of_years = years * 12
  monthly_payment = priciple * monthly_interset_rate / (1- (1 + monthly_interset_rate) ** (-amount_of_years))

  print("The montly payment for this loan is: %.2f " % monthly_payment)

main()