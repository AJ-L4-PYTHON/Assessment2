 # vending machine main menu or selection
 
a = {'number': 101, 'food': 'Iced Coffee','price': 5}
b = {'number': 102, 'food': 'Choocolate Milk','price': 4.5}
c = {'number': 103, 'food': 'Cold Milk','price': 2.5}
d = {'number': 104, 'food': 'Water','price': 1}
e = {'number': 105, 'food': 'Gatorade','price': 8}
f = {'number': 106, 'food': 'Pepsi','price': 5}
g = {'number': 107, 'food': 'Coca-Cola','price': 5.5}
h = {'number': 108, 'food': 'Sprite','price': 5.5}
i = {'number': 109, 'food': 'Galaxy','price': 4.5}
j = {'number': 110, 'food': 'Hershey Kisses','price': 15}
k = {'number': 111, 'food': 'Maltesers','price': 9.5}
l = {'number': 112, 'food': 'Skittles','price': 8.5}
m = {'number': 113, 'food': 'Gummy Bears','price': 6.5}
n = {'number': 114, 'food': 'Milky Way','price': 6.5}
o = {'number': 115, 'food': 'Mars','price': 4.5}
items = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
money = 0

# setting the price on each item
Iced_Coffee=5
Chocolate_Milk=4.512
Cold_Milk=2.5
Water=1
Gatorade=8
Pepsi=5
Coca_Cola=5.5
Sprite=5.5
Galaxy=4.5
Hershey_Kisees=15
Maltesers=9.5
Skittles=8.5
Gummy_Bears=6.5
Milky_Way=6.5
Mars=4.5





def show(items): # to print out the items available and their code and price when the code is activated
    print('\nitems available \n')
    print("------------------------")
    for item in items:
        print(item.get('number'), item.get('food'), item.get('price'))

print("")
money = float(input("Input money: "))    #this lets the user input the amount of money they want to use
PurchaseAgain = True     #this makes it so that the code is currently true on "Purchase Again"

while PurchaseAgain == True: 
    show(items) #this prints the codes inputed into the term "show(items)"
    print("------------------------")
    print("")
    Item_selection = input("Input number: ") 
    print("")

    if Item_selection == '101':      #if item code 101 is selected, the user will go through this path
        print("Item selected = Iced Coffee | Price = 5 ")      #this code prints the item that has been selected and its price
        if money < Iced_Coffee:                  #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds") 
        elif money >= Iced_Coffee:       #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Iced_Coffee       
            print('Change returned: ' + str(money) + "\nYour Iced Coffee has been dispensed.")             #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '102': 
        print("Item selected = Chocolate Milk | Price = 4.5 ") 
        if money < Chocolate_Milk: 
            print("Insufficient Funds")
        elif money >= Chocolate_Milk: 
            money -= Chocolate_Milk 
            print('Change returned: ' + str(money) + "\nYour Chocolate Milk has been dispensed.") 

    elif Item_selection == '103':
        print("Item selected = Cold Milk | Price = 2.5 ") 
        if money < Cold_Milk: 
            print("Insufficient Funds")
        elif money >= Cold_Milk: 
            money -= Cold_Milk 
            print('Change returned: ' + str(money) + "\nYour Cold Milk has been dispensed.") 
            
    elif Item_selection == '104': 
        print("Item selected = Water | Price = 1 ") 
        if money < Water: 
            print("Insufficient Funds")
        elif money >= Water: 
            money -= Water 
            print('Change returned: ' + str(money) + "\nYour Water has been dispensed.") 

    elif Item_selection == '105':
        print("Item selected = Gatorade | Price = 8 ") 
        if money < Gatorade: 
            print("Insufficient Funds")
        elif money >= Gatorade: 
            money -= Gatorade 
            print('Change returned: ' + str(money) + "\nYour Gatorade has been dispensed.") 

    elif Item_selection == '106':
        print("Item selected = Pepsi | Price = 5 ") 
        if money < Pepsi: 
            print("Insufficient Funds")
        elif money >= Pepsi: 
            money -= Pepsi 
            print('Change returned: ' + str(money) + "\nYour Pepsi has been dispensed.") 

    elif Item_selection == '107':
        print("Item selected = Coca-Cola | Price = 5.5 ") 
        if money < Coca_Cola: 
            print("Insufficient Funds")
        elif money >= Coca_Cola: 
            money -= Coca_Cola
            print('Change returned: ' + str(money) + "\nYour Coca-Cola has been dispensed.") 

    elif Item_selection == '108': 
        print("Item selected = Sprite | Price = 5.5 ") 
        if money < Sprite: 
            print("Insufficient Funds")
        elif money >= Sprite: 
            money -= Sprite 
            print('Change returned: ' + str(money) + "\nYour Sprite has been dispensed.") 

    elif Item_selection == '109': 
        print("Item selected = Galaxy | Price = 4.5 ") 
        if money < Galaxy: 
            print("Insufficient Funds")
        elif money >= Galaxy: 
            money -= Galaxy 
            print('Change returned: ' + str(money) + "\nYour Galaxy has been dispensed.")

    elif Item_selection == '110': 
        print("Item selected = Herchey Kisses | Price = 15 ") 
        if money < Hershey_Kisees: 
            print("Insufficient Funds")
        elif money >= Hershey_Kisees: 
            money -= Hershey_Kisees 
            print('Change returned: ' + str(money) + "\nYour Hershey Kisses has been dispensed.")       

    elif Item_selection == '111': 
        print("Item selected = Maltesers | Price = 9.5 ") 
        if money < Maltesers: 
            print("Insufficient Funds")
        elif money >= Maltesers: 
            money -= Maltesers 
            print('Change returned: ' + str(money) + "\nYour Maltesers has been dispensed.")

    elif Item_selection == '112': 
        print("Item selected = Skittles | Price = 8.5 ") 
        if money < Skittles: 
            print("Insufficient Funds")
        elif money >= Skittles: 
            money -= Skittles 
            print('Change returned: ' + str(money) + "\nYour Skittles has been dispensed.")         

    elif Item_selection == '113': 
        print("Item selected = Gummy Bears | Price = 6.5 ") 
        if money < Gummy_Bears: 
            print("Insufficient Funds")
        elif money >= Gummy_Bears: 
            money -= Gummy_Bears 
            print('Change returned: ' + str(money) + "\nYour Gummy Bears has been dispensed.") 

    elif Item_selection == '114': 
        print("Item selected = Milky Way | Price = 6.5 ") 
        if money < Milky_Way: 
            print("Insufficient Funds")
        elif money >= Milky_Way: 
            money -= Milky_Way 
            print('Change returned: ' + str(money) + "\nYour Milky Way has been dispensed.")

    elif Item_selection == '115': 
        print("Item selected = Mars | Price = 4.5 ") 
        if money < Mars: 
            print("Insufficient Funds")
        elif money >= Mars: 
            money -= Mars 
            print('Change returned: ' + str(money) + "\nYour Mark has been dispensed.")  


#if the code that the user inputted is not one of the product's codes, it will print "Invalid code"
    else:                      
        print('Invald Number')                  

    choice = input('Anything else? (yes/no):')         #this code gives the user the choice of if they want to purchase another item or not
    if choice == 'no':
        PurchaseAgain: False

        if money !=0:
            print(str(money) + ' money left')
            money = 0
            print(' Thank you for purchasing at Briize Vendings, come again soon!')
            break
        else:
            print('Thank you for purchasing at Briize Vendings, come again soon!')
            break
    else:
        continue
