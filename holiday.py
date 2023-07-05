#T14 Beginner programming with Functions- Defining Your Own Functions - used lecture by Chris Joubert and accompanying pdf to complete task
import sys,time #Tutorial from replit.com
def delprint(text,delay_time): 
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)
  print("")

#Function to check for integer and reprompt if not - intially used ChatGPT to assist as function was initially not working as intended
def check_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Error: Please enter a valid integer.")
#User input for city they are flying to
city_flight = check_input("Will you be flying to:\n1. Dubrovnik, Croatia\n2. Cape Town, South Africa\n3. Jakarta, Bali\n4. Perth, Australia\nPlease select 1, 2, 3 or 4:\n")
        
#while other number entered = error
while city_flight < 1 or city_flight > 4:
    print("Error, try again.\n")
    city_flight = int(input("Will you be flying to:\n1. Dubrovnik, Croatia\n2. Cape Town, South Africa\n3. Jakarta, Bali\n4. Perth, Australia\nPlease select 1, 2, 3 or 4:\n"))

#User input - number of nights staying at hotel
num_nights = check_input("Enter the number of nights you plan to stay at the hotel:\n")

#User input - number of days renting a car
rental_days = check_input("Enter the number of days you will need to hire a rental car:\n")
    
#functions
#Hotel costs = num of nights * room cost per night
def hotel_cost():
    nights = num_nights
    costs ={
        1: 38, #Dubrovnik
        2: 13, #Cape Town
        3: 3, #Jakarta
        4: 30 #Perth
    }
    return costs.get(city_flight, 0) * nights

#define plane cost = cost of city_flight
def plane_cost():
    costs ={
        1: 200,
        2: 600,
        3: 900,
        4: 1200,
    } 
    return costs.get(city_flight, 0) 

#Define car rental cost = rental days * daily car cost (cheapest costs taken from travelsupermarket.com)
def car_rental():
    days = rental_days
    costs = {
        1: 4,#dubronik £4 
        2: 18,#Cape town avg £18
        3: 43,#Jakarta £43
        4: 68,#Perth £68
    }
    return costs.get(city_flight, 0) * days
    
#define holiday cost = hotel cost + plane cost + car rental, encountered issues stackoverflow.com
def holiday_cost(): 
    j = int(hotel_cost())
    k = int(plane_cost())
    r = int(car_rental())
    x = j + k + r
    return x

#Addtional function to easily print destination
def where():
    if city_flight == 1:
        return "Dubrovnik, Croatia"
    elif city_flight == 2:
        return "Cape Town, South Africa"
    elif city_flight == 3:
        return "Jakarta, Bali"
    elif city_flight == 4:
        return "Perth, Australia"


#final print out slow loading
delprint("         ...Loading...\n",.1)
print(f"""£{holiday_cost()} = Total Holiday Cost\n
          COST BREAKDOWN\n
£{plane_cost()} = flight to {where()}\n
£{hotel_cost()} = for {num_nights} nights in a hotel\n
£{car_rental()} = hiring a car for {rental_days} days in {where()}\n""")


