# #assign cost of one melon
# melon_cost = 1.00


# #assign customer name, how many  melons they bought and how much they paid
# #repeat for 6 individual customers
# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00


# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# #expected payment is the amount the customer owes for their melons
# customer1_expected = customer1_melons * melon_cost

# #if the customer pays the exact amount owed
# if customer1_expected != customer1_paid:
#     #print customer name, amount paid as a float with 2 decimals, and the amount expected as float with 2 decimals
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )
# #repeat for each customer
# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
    # print(f"{customer5_name} paid ${customer5_paid:.2f},",
    #       f"expected ${customer5_expected:.2f}"
    #       )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )


# define a function {what should i name it} that takes in a text file as the parameter
# parse the text file to reproduce output
# sample data from the file 2|Andrea Cruz|12|12.00

def customer_melon_payments(filename):
    
    #open the text file that was passed in
    data = open(filename)

    #for each line in the text file
    for line in data:
        #parse the customer data at the "|" and strip extra characters off the end
        customer_info = line.rstrip().split("|")
        #define variables at index (could also just put this in the f-string
        #Could do this in the f-string, but more readable broken out
        #convert to float to use : .2f (otherwise, float only giving one decimal place)
        customer_name = customer_info[1]
        expected = float(customer_info[2])
        paid = float(customer_info[3])

        #if the pay exactly the amount expected, print results
        if expected != paid:
            print(f"{customer_name} paid ${paid: .2f}, expected ${expected: .2f}")
       





customer_melon_payments("customer-orders.txt")