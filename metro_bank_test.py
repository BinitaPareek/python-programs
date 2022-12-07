'''The Metro Bank provides various types of loans such as car loans, business loans and house loans to its account holders. Write a python program to implement the following requirements:

Initialize the following variables with appropriate input values:account_number, account_balance, salary, loan_type, loan_amount_expected and customer_emi_expected.

The account number should be of 4 digits and its first digit should be 1.

The customer should have a minimum balance of Rupees 1 Lakh in the account.

If the above rules are valid, determine the eligible loan amount and the EMI that the bank can provide to its customers based on their salary and the loan type they expect to avail.

The bank would provide the loan, only if the loan amount and the number of EMI’s requested by the customer is less than or equal to the loan amount and the number of EMI’s decided by the bank respectively.

Display appropriate error messages for all invalid data. If all the business rules are satisfied ,then display account number, eligible and requested loan amount and EMI’s.
'''

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    f=0

    
    if(account_balance>=100000):
        if(account_number//1000==1):
            #print("Account number:", account_number)
            
            if((loan_type=="Car")and(salary>25000)):
                eligible_loan_amount=500000
                bank_emi_expected=36
                if((loan_amount_expected<=eligible_loan_amount)and(customer_emi_expected<=bank_emi_expected)):
                    #display(eligible_loan_amount,bank_emi_expected,loan_amount_expected,customer_emi_expected)
                    f=1
                else:
                    print("The customer is not eligible for the loan")
            elif((loan_type=="House")and(salary>50000)):
                eligible_loan_amount=6000000
                bank_emi_expected=60
                if((loan_amount_expected<=eligible_loan_amount)and(customer_emi_expected<=bank_emi_expected)):
                    #display(eligible_loan_amount,bank_emi_expected,loan_amount_expected,customer_emi_expected)
                    f=1
                else:
                    print("The customer is not eligible for the loan")        
            elif((loan_type=="Business")and(salary>75000)):
                eligible_loan_amount=7500000
                bank_emi_expected=84
                if((loan_amount_expected<=eligible_loan_amount)and(customer_emi_expected<=bank_emi_expected)):
                    f=1
                    #display(eligible_loan_amount,bank_emi_expected,loan_amount_expected,customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")        
                    
            else:
                print("Invalid loan type or salary")
        else:
            print("Invalid account number")
    else:
        print("Insufficient account balance")  
    if(f==1):
        display(account_number,eligible_loan_amount, bank_emi_expected, loan_amount_expected, customer_emi_expected)
    
    
        
def display(account_number,eligible_loan_amount,bank_emi_expected,loan_amount_expected,customer_emi_expected):
    print("Account number:", account_number)
    print("The customer can avail the amount of Rs.", eligible_loan_amount)
    print("Eligible EMIs :", bank_emi_expected)
    print("Requested loan amount:", loan_amount_expected)
    print("Requested EMI's:",customer_emi_expected)   

calculate_loan(1001,70000,350000,"House",300000,20)






