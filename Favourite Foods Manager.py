favourite_foods = [] 

while True:
    print("\nFavourite Foods Manager")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View all favourite foods")
    
    choice = input("Choose an option: ")  
    
    if choice == "0":
        print("Thanks for using Favourite Foods Manager!")
        break
    elif choice == "1":
        food = input("Enter your favourite food name: ")
        if food in favourite_foods:
            print(f"{food} is already in your favourite foods list!")
        else:
            favourite_foods.append(food)
            print(f"{food} added successfully.")
    elif choice == "2":
        food = input("Enter a food name which you want to remove: ")
        if food in favourite_foods:
            favourite_foods.remove(food)
            print(f"{food} removed successfully.")
        else:
            print(f"{food} is not in your favourite foods list.")
    elif choice == "3":
        if favourite_foods:
            print("Your favourite foods: ")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}. {food}")
        else:
            print("Food list is empty or no foods added yet!")
    else:
        print("Invalid Choice!")
