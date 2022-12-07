'''
Created on 21-Nov-2022

@author: Binita
calculate food delivery charges for a person for veg or non veg food as per the distance for delivery.
'''
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    f=food_type
    q=quantity_ordered
    d=distance_in_kms
    a=invalid_entry(f,q,d)
    #print("value of a ",a)
    if(a==(-1)):
        bill_amount=-1
    else:
        bill_amount=0
        x=distance_in_kms
        y=delivery_charge(x)
        if(food_type=="V"):
            bill_amount=(120*quantity_ordered)+y  
        elif(food_type=="N"):
            bill_amount=(150*quantity_ordered)+y
        else:
            bill_amount=-1
    
    return bill_amount

def delivery_charge(distance_in_kms):
    d_charge=0
    if(distance_in_kms<=3):
        d_charge=0
    elif(3<distance_in_kms<=6):
        d_charge=(distance_in_kms-3)*3
    elif(6<distance_in_kms):
        d_charge=9+((distance_in_kms-6)*6)
    
    return d_charge
def invalid_entry(food_type,quantity_ordered,distance_in_kms):
    #bill_amount=0
    if((quantity_ordered<=0)or(distance_in_kms<=0)):
        bill_amount=-1
    #((food_type!="V")or(food_type!="N")):
       #or(quantity_ordered<0)or(distance_in_kms<0)):
        
    else:
        bill_amount=0
    
    return bill_amount
        
        
#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,8)
print(bill_amount)