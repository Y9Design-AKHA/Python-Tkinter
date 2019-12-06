# Author: Ali Khan
# Producing Comapany: UCC
# Development Supersivor: Alvin Jugoon
# Program: A Simplified Tax Return Calcualator

print("Ontario Tax Return Calculator \n") #Title

# Series of questions in order to return information for the tax refund.

Emplyoment_Income = int(input("How much gross employement income do you make anually?(Approx.) \n"))

Self_employement_Income = int(input("How much gross self-employement income do you make anually?(Approx.) \n"))

Capital_Gains = int(input("How much gross income have you made through stocks, bonds or real estate?(Approx.) \n"))

RRSP_Deductions = int(input("How much income has been deducted into an RRSP(Approx.) \n"))

Charity = int(input("Have much money have you given in charitable contributions(Approx.) \n"))

Taxes_Paid = int(input("How much income tax have you paid?(Approx.) \n"))

# This will take the information and calculate the tax refund.
income = Emplyoment_Income + Self_employement_Income + Capital_Gains

if (income >= 0) and (income <= 10400):
        Federal_tax = (0 * income)

elif (income > 10400) and (income <= 46605):
        Federal_tax = (0.15 * income)

elif (income > 46605) and (income <= 93208):
        Federal_tax = (0.205 * income)

elif (income > 93208) and (income <= 144489):
        Federal_tax = (0.26 * income)

elif (income > 144489) and (income <= 205842):
        Federal_tax = (0.29 * income)
else: 
        Federal_tax = (0.33 * income)

      	
if (income >= 0) and (income <= 10400):
        Provincial_tax = (0 * income)

elif (income > 10400) and (income <= 42963):
        Provincial_tax = (0.505 * income)

elif (income > 85920) and (income <= 149997):
        Provincial_tax = (0.915 * income)

elif (income > 149997) and (income <= 219997):
        Provincial_tax = (0.1116 * income)
else: 
        Provincial_tax = (0.1316 * income)

Total_tax = Federal_tax + Provincial_tax

After_Tax_income = income - Total_tax

Tax_Refund = 3606 + RRSP_Deductions + (Charity/2)

if (Taxes_Paid < Total_tax):

        Tax_Refund - (Total_tax - Taxes_Paid) 
elif  (Taxes_Paid >= Total_tax):
	    Tax_Refund + (Taxes_Paid - Total_tax)  


print ("Your Tax Refund is: \n" + str(round (Tax_Refund)))
print ("Your Total Income is: \n" + str(round (income)))
print ("Your Total Tax is: \n" + str(round (Total_tax)))
print ("Your after Tax income is: \n" + str(round(After_Tax_income)))



