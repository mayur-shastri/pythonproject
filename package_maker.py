# # scrapperOutput is a tuple containing the following lists in the given order:
# #     # Do, Stay, Eat, new_eat_price, stay_price, ratings, image_links
# from scrapper import scrapperFuncN
# import random

# def packageMaker(destination, budget, stayDuration, numPeople):
#     scrapperOutput = scrapperFuncN(destination)
#     Hotels = scrapperOutput[1]
#     Restaurants = scrapperOutput[2]
#     Restaurant_expense = scrapperOutput[3]
#     Hotel_prices = [price * 80 for price in scrapperOutput[4]]  # Convert hotel prices to rupees
#     ratings = scrapperOutput[5]

#     num_packages = 5
#     packages = []

#     def calculate_score(hotel_price, restaurant_cost):
#         return hotel_price * stayDuration - sum(restaurant_cost)

#     def get_random_eat_price(cost, hotel_price):
#         if hotel_price > 1000:
#             # User chose an expensive hotel, prefer Mid-range or Fine Dining
#             if cost == 'Mid-range':
#                 return random.randint(1000, 1500) * numPeople
#             elif cost == 'Fine Dining':
#                 return random.randint(1500, 2500) * numPeople
#         else:
#             # User chose a cheaper hotel, prefer Cheap Eats
#             if cost == 'Cheap Eats':
#                 return random.randint(100, 600) * numPeople

#         # Default case: Randomly choose any price range
#         return random.randint(100, 1000) * numPeople

#     adjusted_budget = budget * numPeople

#     selected_hotels = set()  # Set to store selected hotel indices

#     max_attempts = 100  # Maximum attempts to find unique hotels
#     attempts = 0

#     while len(packages) < num_packages and attempts < max_attempts:
#         remaining_budget = adjusted_budget
#         hotel_index = random.randint(0, len(Hotels) - 1)
        
#         if hotel_index in selected_hotels:
#             attempts += 1
#             continue  # Skip if the hotel has already been selected
        
#         selected_hotels.add(hotel_index)  # Add the hotel index to selected hotels set
#         attempts = 0  # Reset the attempts counter
        
#         hotel_name = Hotels[hotel_index]
#         hotel_price = Hotel_prices[hotel_index] * stayDuration * numPeople
#         hotel_rating = ratings[hotel_index + 10]

#         if hotel_price*stayDuration*numPeople > remaining_budget:
#             continue  # Skip the hotel if its price exceeds the remaining budget

#         restaurant_list = []
#         restaurant_cost = []
#         restaurant_ratings = []
#         temp_restaurants = Restaurants.copy()  # Create a copy of Restaurants

#         while remaining_budget > 0 and temp_restaurants:  # Use the copied list for iteration
#             restaurant_index = random.randint(0, len(temp_restaurants) - 1)
#             restaurant_name = temp_restaurants[restaurant_index]
#             restaurant_expense = Restaurant_expense[restaurant_index]
#             eat_price = get_random_eat_price(restaurant_expense, hotel_price)

#             if remaining_budget >= eat_price:
#                 remaining_budget -= eat_price
#                 restaurant_list.append(restaurant_name)
#                 restaurant_cost.append(eat_price)
#                 restaurant_ratings.append(ratings[restaurant_index + 20])
#             else:
#                 break  # Break the loop if remaining budget is insufficient

#             temp_restaurants.remove(restaurant_name)  # Remove from the copied list

#         if restaurant_list:
#             package_score = calculate_score(hotel_price, restaurant_cost)
#             packages.append((hotel_name, hotel_price, hotel_rating, restaurant_list, restaurant_cost, restaurant_ratings, package_score))

#     # Sort the packages based on the score in descending order
#     packages.sort(key=lambda x: x[6], reverse=True)

#     # Print the available packages
#     count = 0
#     for package in packages:
#         count += 1
#         print(f"Package {count}:")
#         print("Hotel:", package[0])
#         print("Hotel Price (Rupees):", package[1])
#         print("Hotel Rating:", package[2])
#         print("Restaurants:")
#         for j in range(len(package[3])):
#             print(f"- {package[3][j]} (Cost: {package[4][j]})")
#             print("  Rating:", package[5][j])
#         print()

#     if len(packages) < num_packages:
#         print(f"Only {len(packages)} packages available instead of {num_packages}. Consider adjusting the parameters.")

# # Example usage:
# packageMaker("pondicherry", 200000, 3, 2)


# from scrapper import scrapperFuncN
# import random

# def packageMaker(destination, budget, stayDuration, numPeople):
#     scrapperOutput = scrapperFuncN(destination)
#     Hotels = scrapperOutput[1]
#     Restaurants = scrapperOutput[2]
#     Restaurant_expense = scrapperOutput[3]
#     Hotel_prices = [price * 80 for price in scrapperOutput[4]]  # Convert hotel prices to rupees
#     ratings = scrapperOutput[5]
#     image_links = scrapperOutput[6]  # Image links list
    
#     num_packages = 5
#     packages = []

#     def calculate_score(hotel_price, restaurant_cost):
#         return hotel_price * stayDuration - sum(restaurant_cost)

#     def get_random_eat_price(cost, hotel_price):
#         if hotel_price > 1000:
#             # User chose an expensive hotel, prefer Mid-range or Fine Dining
#             if cost == 'Mid-range':
#                 return random.randint(1000, 1500) * numPeople
#             elif cost == 'Fine Dining':
#                 return random.randint(1500, 2500) * numPeople
#         else:
#             # User chose a cheaper hotel, prefer Cheap Eats
#             if cost == 'Cheap Eats':
#                 return random.randint(100, 600) * numPeople

#         # Default case: Randomly choose any price range
#         return random.randint(100, 1000) * numPeople

#     adjusted_budget = budget * numPeople

#     selected_hotels = set()  # Set to store selected hotel indices

#     max_attempts = 100  # Maximum attempts to find unique hotels
#     attempts = 0

#     while len(packages) < num_packages and attempts < max_attempts:
#         remaining_budget = adjusted_budget
#         hotel_index = random.randint(0, len(Hotels) - 1)
        
#         if hotel_index in selected_hotels:
#             attempts += 1
#             continue  # Skip if the hotel has already been selected
        
#         selected_hotels.add(hotel_index)  # Add the hotel index to selected hotels set
#         attempts = 0  # Reset the attempts counter
        
#         hotel_name = Hotels[hotel_index]
#         hotel_price = Hotel_prices[hotel_index] * stayDuration * numPeople
#         hotel_rating = ratings[hotel_index + 10]
#         hotel_image_link = image_links[hotel_index + 10]  # Hotel image link

#         if hotel_price * stayDuration * numPeople > remaining_budget:
#             continue  # Skip the hotel if its price exceeds the remaining budget

#         restaurant_list = []
#         restaurant_cost = []
#         restaurant_ratings = []
#         restaurant_image_links = []  # List to store restaurant image links
#         temp_restaurants = Restaurants.copy()  # Create a copy of Restaurants

#         while remaining_budget > 0 and temp_restaurants:  # Use the copied list for iteration
#             restaurant_index = random.randint(0, len(temp_restaurants) - 1)
#             restaurant_name = temp_restaurants[restaurant_index]
#             restaurant_expense = Restaurant_expense[restaurant_index]
#             eat_price = get_random_eat_price(restaurant_expense, hotel_price)

#             if remaining_budget >= eat_price:
#                 remaining_budget -= eat_price
#                 restaurant_list.append(restaurant_name)
#                 restaurant_cost.append(eat_price)
#                 restaurant_ratings.append(ratings[restaurant_index + 20])
#                 restaurant_image_links.append(image_links[restaurant_index + 20])  # Restaurant image link
#             else:
#                 break  # Break the loop if remaining budget is insufficient

#             temp_restaurants.remove(restaurant_name)  # Remove from the copied list

#         if restaurant_list:
#             package_score = calculate_score(hotel_price, restaurant_cost)
#             packages.append((hotel_name, hotel_price, hotel_rating, restaurant_list, restaurant_cost, restaurant_ratings, package_score, hotel_image_link, restaurant_image_links))

#     # Sort the packages based on the score in descending order
#     packages.sort(key=lambda x: x[6], reverse=True)

#     # Print the available packages
#     count = 0
#     for package in packages:
#         count += 1
#         print(f"Package {count}:")
#         print("Hotel:", package[0])
#         print("Hotel Price (Rupees):", package[1])
#         print("Hotel Rating:", package[2])
#         print("Hotel Image Link:", package[7])  # Print hotel image link
#         print("Restaurants:")
#         for j in range(len(package[3])):
#             print(f"- {package[3][j]} (Cost: {package[4][j]})")
#             print("  Rating:", package[5][j])
#             print("  Restaurant Image Link:", package[8][j])  # Print restaurant image link
#         print()

#     if len(packages) < num_packages:
#         print(f"Only {len(packages)} packages available instead of {num_packages}. Consider adjusting the parameters.")

# # Example usage:
# packageMaker("pondicherry", 50000, 3, 2)


from scrapper import scrapperFuncN
import random

def packageMaker(destination, budget, stayDuration, numPeople):
    scrapperOutput = scrapperFuncN(destination)
    Hotels = scrapperOutput[1]
    Restaurants = scrapperOutput[2]
    Restaurant_expense = scrapperOutput[3]
    Hotel_prices = [price * 80 for price in scrapperOutput[4]]  # Convert hotel prices to rupees
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
                return random.randint(1000, 1500) * numPeople
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
        
        if hotel_index in selected_hotels:
            attempts += 1
            continue  # Skip if the hotel has already been selected
        
        selected_hotels.add(hotel_index)  # Add the hotel index to selected hotels set
        attempts = 0  # Reset the attempts counter
        
        hotel_name = Hotels[hotel_index]
        hotel_price = Hotel_prices[hotel_index] * stayDuration * numPeople
        hotel_rating = ratings[hotel_index + 10]

        if hotel_price*stayDuration*numPeople > remaining_budget:
            continue  # Skip the hotel if its price exceeds the remaining budget

        restaurant_list = []
        restaurant_cost = []
        restaurant_ratings = []
        temp_restaurants = Restaurants.copy()  # Create a copy of Restaurants

        while remaining_budget > 0 and temp_restaurants:  # Use the copied list for iteration
            restaurant_index = random.randint(0, len(temp_restaurants) - 1)
            restaurant_name = temp_restaurants[restaurant_index]
            restaurant_expense = Restaurant_expense[restaurant_index]
            eat_price = get_random_eat_price(restaurant_expense, hotel_price)

            if remaining_budget >= eat_price:
                remaining_budget -= eat_price
                restaurant_list.append(restaurant_name)
                restaurant_cost.append(eat_price)
                restaurant_ratings.append(ratings[restaurant_index + 20])
            else:
                break  # Break the loop if remaining budget is insufficient

            temp_restaurants.remove(restaurant_name)  # Remove from the copied list

        if restaurant_list:
            package_score = calculate_score(hotel_price, restaurant_cost)
            packages.append((hotel_name, hotel_price, hotel_rating, restaurant_list, restaurant_cost, restaurant_ratings, package_score))

    # Sort the packages based on the score in descending order
    packages.sort(key=lambda x: x[6], reverse=True)

    # Print the available packages
    count = 0
    for package in packages:
        count += 1
        print(f"Package {count}:")
        print("Hotel:", package[0])
        print("Hotel Price (Rupees):", package[1])
        print("Hotel Rating:", package[2])
        print("Restaurants:")
        for j in range(len(package[3])):
            print(f"- {package[3][j]} (Cost: {package[4][j]})")
            print("  Rating:", package[5][j])
        print()

    if len(packages) < num_packages:
        print(f"Only {len(packages)} packages available instead of {num_packages}. Consider adjusting the parameters.")

# Example usage:
packageMaker("pondicherry", 200000, 3, 2)