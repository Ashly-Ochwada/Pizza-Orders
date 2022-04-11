print("Welcome to HB Pizza Deliveries")
size = input("What size of Pizza do you want? Small, Medium or Large ")
add_cheese = input("Do you want extra cheese? Yes or No ")
add_pepperoni = input("Do you want pepperoni? Yes or No ")
add_peppers = input("Do you want peppers? Yes or No ")
#Prices

bill = 0

if size == "S":
 bill += 1500 
elif size == "M":
  bill += 2750
else:
  bill += 3250

if add_cheese == "Yes":
   bill += 150

if add_pepperoni  == "Yes":
  if size == "S":
    bill += 200
  else:
    bill += 350

if add_peppers == "Yes":
   bill += 75

print(f"Your total bill is Ksh{bill}")