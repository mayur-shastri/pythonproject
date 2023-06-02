from scrapper import scrapperFuncN
import random
from stay_output import stayOutput
from tkinter import *

# Do, Stay, Eat, new_eat_price, stay_price, ratings, image_links
def packageMaker(root,destination, budget, stayDuration, numPeople):

    scrapperOutput = scrapperFuncN(destination)
    Hotels = scrapperOutput[1]
    Restaurants = scrapperOutput[2]
    Restaurant_expense = scrapperOutput[3]
    Hotel_prices = [price * 80 for price in scrapperOutput[4]]  # Convert hotel prices to rupees
    for price in Hotel_prices:
        if price == 0:
            Hotel_prices.remove(price)
    ratings = scrapperOutput[5]
    image_links = scrapperOutput[6]

    num_packages = 5
    packages = []

    def calculate_score(hotel_price, restaurant_cost):
        return hotel_price * stayDuration - sum(restaurant_cost)

    def get_random_eat_price(cost, hotel_price):
        if hotel_price > 1000:
            # User chose an expensive hotel, prefer Mid-range or Fine Dining
            if cost == 'Mid-range':
                return random.randint(600, 1100) * numPeople
            elif cost == 'Fine Dining':
                return random.randint(1500, 2500) * numPeople
        else:
            # User chose a cheaper hotel, prefer Cheap Eats
            if cost == 'Cheap Eats':
                return random.randint(100, 600) * numPeople

        # Default case: Randomly choose any price range
        return random.randint(100, 1000) * numPeople

    adjusted_budget = budget * numPeople

    selected_hotels = set()  # Set to store selected hotel indices

    max_attempts = 100  # Maximum attempts to find unique hotels
    attempts = 0

    while len(packages) < num_packages and attempts < max_attempts:
        remaining_budget = adjusted_budget
        hotel_index = random.randint(0, len(Hotels) - 1)
        restaurant_images=[]
        if hotel_index in selected_hotels:
            attempts += 1
            continue  # Skip if the hotel has already been selected
        
        selected_hotels.add(hotel_index)  # Add the hotel index to selected hotels set
        attempts = 0  # Reset the attempts counter
        
        hotel_name = Hotels[hotel_index]
        hotel_price = Hotel_prices[hotel_index] * stayDuration * numPeople
        hotel_rating = ratings[hotel_index + 10]
        hotel_image = image_links[hotel_index + 10]
        if hotel_price*stayDuration*numPeople > remaining_budget:
            continue  # Skip the hotel if its price exceeds the remaining budget

        restaurant_list = []
        restaurant_cost = []
        restaurant_ratings = []
        temp_restaurants = Restaurants.copy()  # Create a copy of Restaurants
        temp_ratings = ratings.copy()
        temp_image_links = image_links.copy()
        while remaining_budget > 0 and temp_restaurants:  # Use the copied list for iteration
            restaurant_index = random.randint(0, len(temp_restaurants) - 1)
            ratings_index = restaurant_index + 20
            image_index = restaurant_index + 20
            restaurant_name = temp_restaurants[restaurant_index]
            restaurant_expense = Restaurant_expense[restaurant_index]
            eat_price = get_random_eat_price(restaurant_expense, hotel_price)

            if remaining_budget >= eat_price:
                remaining_budget -= eat_price
                restaurant_list.append(restaurant_name)
                restaurant_cost.append(eat_price)
                restaurant_ratings.append(temp_ratings[ratings_index])
                restaurant_images.append(temp_image_links[image_index])
                #print(temp_image_links[image_index])
            else:
                break  # Break the loop if remaining budget is insufficient

            temp_restaurants.remove(restaurant_name)  # Remove from the copied list
            temp_ratings.remove(temp_ratings[ratings_index])
            temp_image_links.remove(temp_image_links[image_index])
        if restaurant_list:
            package_score = calculate_score(hotel_price, restaurant_cost)
            packages.append((hotel_name, hotel_price, hotel_rating, restaurant_list, restaurant_cost, restaurant_ratings, package_score,hotel_image,restaurant_images))

    # Sort the packages based on the score in descending order
    packages.sort(key=lambda x: x[6], reverse=True)

    if len(packages) < num_packages:
        print(f"Only {len(packages)} packages available instead of {num_packages}. Consider adjusting the parameters.")
    # placeName,hotelName,stars,reviews,hotel_image,hotel_price
    # print(destination.title(),packages[0][0],packages[0][7],packages[0][1])
    print('-------------------------------------')
    print("Hotel name = ",packages[0][0])
    print('-------------------------------------')
    print("Image Link = ",packages[0][7])
    print('-------------------------------------')
    print("Hotel Price = ",packages[0][1])
    print('-------------------------------------')
    
    root.withdraw()  # Hide the root window

    stayOutput(root, destination, packages[0][0], packages[0][7], packages[0][1])

    root.mainloop()
# packageMaker('pondicherry', 600000, 3, 2)