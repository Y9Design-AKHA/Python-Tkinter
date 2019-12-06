# Author: Ali Khan
# Producing Comapany: UCC
# Development Supersivor: Alvin Jugoon
# Program: A Simplified Tax Return Calcualator

import tkinter as tk

def clicked():

	num1 = (income.get())
	num2 = (Capital_Gains.get())
	num3 = (Charitable_Contributions.get())
	num4 = (RRSP_Deductions.get())
	num5 = (Taxes_Paid.get())
	num6 =  3606
	Tax_Refund = int(num4)+int(num3)/2
	#labelAns.config(text="%d" % Tax_Refund)

	Total_income = int(num1)+int(num2)


	if (Total_income >= 0) and (Total_income <= 10400):
	    Federal_tax = (0 * Total_income)

	elif (Total_income > 10400) and (Total_income <= 46605):
	    Federal_tax = (0.15 * Total_income)

	elif (Total_income > 46605) and (Total_income <= 93208):
	    Federal_tax = (0.205 * Total_income)

	elif (Total_income > 93208) and (Total_income <= 144489):
	    Federal_tax = (0.26 * Total_income)

	elif (Total_income > 144489) and (Total_income <= 205842):
	    Federal_tax = (0.29 * Total_income)
	else: 
	    Federal_tax = (0.33 * Total_income)

	  	
	if (Total_income >= 0) and (Total_income <= 10400):
	    Provincial_tax = (0 * Total_income)

	elif (Total_income > 10400) and (Total_income <= 42963):
	    Provincial_tax = (0.505 * Total_income)

	elif (Total_income > 85920) and (Total_income <= 149997):
	    Provincial_tax = (0.915 * Total_income)

	elif (Total_income > 149997) and (Total_income <= 219997):
	    Provincial_tax = (0.1116 * Total_income)
	else: 
	    Provincial_tax = (0.1316 * Total_income)


	Total_tax = Federal_tax + Provincial_tax

	After_Tax_income = Total_income - Total_tax


	if ((int(num5)) < int(Total_tax)):

	        int(Tax_Refund) - (int(Total_tax) - int(entryNum5.get())) 
	elif  int(entryNum5.get()) >= Total_tax:
		    int(Tax_Refund) + int(entryNum5.get()) - (Total_tax) 
		   
	labelAns.config(text=Tax_Refund)


MyWindow = tk.Tk()
MyWindow.title("Ontario Tax Return Calculator")
MyWindow.geometry('600x400')
MyWindow.configure(background='#0d98ba')


income = tk.StringVar()
Capital_Gains = tk.StringVar()
Charitable_Contributions = tk.StringVar()
RRSP_Deductions = tk.StringVar()
Taxes_Paid = tk.StringVar()

# Series of questions in order to return information for the tax refund.
LabelTitle = tk.Label(MyWindow, text="Let's find your Tax refund!", font=("Arial",24,"bold"), fg="dark green")
LabelTitle.config(height = 2)
LabelNum1 = tk.Label(MyWindow, text="Annual income", fg="lime green")
LabelNum2 = tk.Label(MyWindow, text="Capital Gains", fg="lime green")
LabelNum3 = tk.Label(MyWindow, text="Charitable Contributions", fg="lime green")
LabelNum4 = tk.Label(MyWindow, text="RRSP Deductions", fg="lime green")
LabelNum5 = tk.Label(MyWindow, text="Taxes Paid", fg="lime green")
labelAns = tk.Label(MyWindow)


LabelTitle.grid(row=0, column=0)
LabelNum1.grid(row=2, column=0)
LabelNum2.grid(row=3, column=0)
LabelNum3.grid(row=4, column=0)
LabelNum4.grid(row=5, column=0)
LabelNum5.grid(row=6, column=0)
labelAns.grid(row=4, column=6)


entryNum1 = tk.Entry(MyWindow, textvariable=income)
entryNum1. grid(row=2, column=2)
entryNum2 = tk.Entry(MyWindow, textvariable=Capital_Gains)
entryNum2. grid(row=3, column=2)
entryNum3 = tk.Entry(MyWindow, textvariable=Charitable_Contributions)
entryNum3. grid(row=4, column=2)
entryNum4 = tk.Entry(MyWindow, textvariable=RRSP_Deductions)
entryNum4. grid(row=5, column=2)
entryNum5 = tk.Entry(MyWindow, textvariable=Taxes_Paid)
entryNum5. grid(row=6, column=2)

Total_income = 0


buttonCal = tk.Button(MyWindow, text="CALCULATE",command=clicked)
buttonCal.grid(row=11, column=2)

# Main Loop
MyWindow.mainloop()
