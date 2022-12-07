'''
Created on 21-Nov-2022

@author: Binita
'''
def make_amount(rupees_to_make,no_of_five,no_of_one):
    #five_needed=0
    #one_needed=0
    #amt=0
    five_needed=rupees_to_make//5
    #one_needed=rupees_to_make%5
    
    if(five_needed>no_of_five):
        five_needed=no_of_five
    one_needed=rupees_to_make-(five_needed*5)
    if(one_needed>no_of_one):
        print("-1")
    else:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    
    
make_amount(16,1,15)