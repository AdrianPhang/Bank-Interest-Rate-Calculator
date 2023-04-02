# -*- coding: utf-8 -*-
"""
@author: phang
"""
#Defining a conditional statement as InterestRateCalculator which calculates the interest rates based on the basis of DBS Multiplier account.

def interestRateCalculator ( ta , categoryHit , ab ):
    interestValue = 0
    print(categoryHit)
    print(ta)

#Accounting for Salary + 0 Transaction with less than $50,000 or $50,000 for Account Balance.

    if categoryHit == 0:
        if ta < 2000:
            interestValue = 0.0005/12 * ab
        if ta >= 2000 and ta < 2500:
            interestValue = 0.0005/12 * ab
        if ta >= 2500 and ta < 5000:
            interestValue = 0.0005/12 * ab
        if ta >= 5000 and ta < 15000:
            interestValue = 0.0005/12 * ab
        if ta >= 15000 and ta < 30000:
            interestValue = 0.0005/12 * ab
        if ta >= 30000:
            interestValue = 0.0005/12 * ab
        if ab >= 50000:
            interestValue2 = ab * (0.0005/12)
            return interestValue2
        if ab > 100000:
            interestValue3 = (ab - 100000) * (0.0005/12) + interestValue2 + interestValue
            return interestValue3
    
#Accounting for Salary + 1 Transaction with less than $50,000 or $50,000 for Account Balance.
    
    if categoryHit == 1:
        if ta < 2000:
            if ab <= 50000:
                interestValue = 0.0005/12 * ab
            if ab > 50000:
                interestValue = (ab - 50000) * (0.0005/12) + 0.0005/12 * 50000
        if ta >= 2000 and ta < 2500:
            if ab <= 50000:
                interestValue = 0.0155/12 * ab
            if ab > 50000:
                interestValue = (ab - 50000) * (0.0005/12) + 0.0155/12 * 50000
            
        if ta >= 2500 and ta < 5000:
            if ab <= 50000:
                interestValue = 0.0185/12 * ab
            if ab > 50000:
                interestValue = (ab - 50000) * (0.0005/12) + 0.0185/12 * 50000   
           
        if ta >= 5000 and ta < 15000:
            if ab <= 50000:
               interestValue = 0.0190/12 * ab
            if ab > 50000:
                interestValue = (ab - 50000) * (0.0005/12) +  0.0190/12 * 50000   
        if ta >= 15000 and ta < 30000:
            if ab <= 50000:
                interestValue = 0.02/12 * ab
            if ab > 50000:
                interestValue = (ab - 50000) * (0.0005/12) + 0.02/12 * 50000    
        if ta >= 30000:
            if ab <= 50000:
                interestValue = 0.0208/12 * ab
            if ab > 50000:
                interestValue = (ab - 50000) * (0.0005/12) + 0.0208/12 * 50000    
       
            
        return interestValue
       
        
#Accounting for Salary + 2 Transaction with less than $50,000 or $50,000 for Account Balance.
    
    elif categoryHit == 2:
        if ta < 2000:
            interestValue = 0.0005/12 * ab
        if ta >= 2000 and ta < 2500:
            interestValue = 0.018/12 * ab
        if ta >= 2500 and ta < 5000:
            interestValue = 0.02/12 * ab
        if ta >= 5000 and ta < 15000:
            interestValue = 0.022/12 * ab
        if ta >= 15000 and ta < 30000:
            interestValue = 0.023/12 * ab
        if ta >= 30000:
            interestValue = 0.035/12 * ab
        if ab >= 50000:
            interestValue2 = (ab - 50000) * (0.05/12) + interestValue

#Returning the variable InterestValue which as it is defined in interestRateCalculator   
       
        return interestValue2
        
#Accounting for Salary + 3 or more Transaction with less or more than $50,000 for Account Balance
    
    elif categoryHit == 3 or categoryHit == 4:
        interestValue1 = 0;
        if ab < 50000:
            
            if ta < 2000:
                interestValue = 0.0005/12 * ab 
            if ta >= 2000 and ta < 2500:
                interestValue = 0.018/12 * ab 
            if ta >= 2500 and ta < 5000:
                interestValue = 0.02/12 * ab
            if ta >= 5000 and ta < 15000:
                interestValue = 0.022/12 * ab 
            if ta >= 15000 and ta < 30000:
                interestValue = 0.023/12 * ab 
            if ta >= 30000:
                interestValue = 0.035/12 * ab
                
        if ab >= 50000:
            
            if ta < 2000:
                interestValue1 = 0.0005/12 * 50000 
            if ta >= 2000 and ta < 2500:
                interestValue1 = 0.018/12 * 50000 
            if ta >= 2500 and ta < 5000:
                interestValue1 = 0.02/12 * 50000
            if ta >= 5000 and ta < 15000:
                interestValue1 = 0.022/12 * 50000 
            if ta >= 15000 and ta < 30000:
                interestValue1 = 0.023/12 * 50000 
            if ta >= 30000:
                interestValue1 = 0.035/12 * 50000
         
            if ta < 2000:
                interestValue = 0.0005/12 * (ab -  50000)
            if ta >= 2000 and ta < 2500:
                interestValue = 0.02/12 * (ab -  50000) 
            if ta >= 2500 and ta < 5000:
                interestValue = 0.022/12 * (ab -  50000)
            if ta >= 5000 and ta < 15000:
                interestValue = 0.024/12 * (ab -  50000) 
            if ta >= 15000 and ta < 30000:
                interestValue = 0.025/12 * (ab -  50000) 
            if ta >= 30000:
                interestValue = 0.038/12 * (ab -  50000)

#Making sure that interest rate based the different categorization of less than or more than $50,000 is properly tabulated.
                
            interestValue = interestValue1 + interestValue 

#Returning the variable InterestValue which as it is defined in interestRateCalculator
        
        return interestValue
            
#Defining the categorization for each dbs transactions being made and triggering it the necessary inputs for interest rate calculator (line 9) to count the rates. 

def userInput( ab , sc , ccs , hli , ip , iid ):
    categoryHit = 0
    ta = 0        
    if ccs > 0:
        categoryHit +=1
    if hli > 0:
        categoryHit +=1
    if ip > 0:
        categoryHit +=1
    if iid > 0:
        categoryHit +=1
    if sc > 0:
            ta = sc + ccs + hli + ip + iid
#Returning the variable newV which as it is defined in userInput       
    newV= interestRateCalculator(ta , categoryHit, ab )
    print ( newV )
    return newV;

#Prompting User to enter their information.
#While preventing non-numerical inputs which will lead to syntax error by looping it till the user enters a float.
    
while True:
     try:
         Account_Balance = float(input(" What is your account balance? "))
         Salary_Credited = float(input(" How much salary per month will you be crediting? "))
         Credit_Card_Spending = float(input (" How much do you spend on your credit card transactions every month? If Nil, Please enter 0. "))
         Home_Loan_Instalment = float(input (" How much are you paying for your Home Loan Instalment every month? If Nil, Please enter 0. "))
         Insurance_Premium = float(input (" How much do you spend on your Insurance Premium every month with DBS? If Nil, Please enter 0. "))
         Investments_in_DBS = float(input (" How much do you contribute on your Investments every month with DBS? If Nil, Please enter 0. "))
         interestRate = userInput(Account_Balance, Salary_Credited, Credit_Card_Spending, Home_Loan_Instalment, Insurance_Premium, Investments_in_DBS)
         print("Your interest rate returns is $"+str(interestRate))
         break
     except ValueError:
         print(" Please input a valid number . Thank you! ")

#Showing the User on how much has he entered for the calculation of the interest rate.

print(f"Based on the inputs, You do have ${Salary_Credited} for your Salary Contribution every month \n${Credit_Card_Spending} for the Credit Card Spendings \n${Home_Loan_Instalment} financed for your Home Loan Instalment \n${Insurance_Premium} paid for your monthly instalment and ${Investments_in_DBS} contributed for your investment every month. ")



        
