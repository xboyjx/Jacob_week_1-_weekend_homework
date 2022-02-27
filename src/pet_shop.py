# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_list):
    pet_shop_name = pet_shop_list["name"]
    return pet_shop_name

def get_total_cash(pet_shop_list):
    total_cash = pet_shop_list["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash(pet_shop_list, amount):
    pet_shop_list["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop_list):
    pets_sold = pet_shop_list["admin"]["pets_sold"]
    return pets_sold

def increase_pets_sold(pet_shop_list, increase_amount):
    pet_shop_list["admin"]["pets_sold"] +=2

def get_stock_count(pet_shop_list):
    stock_count = len(pet_shop_list["pets"])
    return stock_count

def get_pets_by_breed(pet_shop_list, given_breed):
    total_pet_by_breed = []
    for pet in pet_shop_list["pets"]:
        if pet["breed"] == given_breed:
           total_pet_by_breed.append(pet) 
        
    return total_pet_by_breed

def find_pet_by_name(pet_shop_list, given_name):
    found_pet = ""
    for pet in pet_shop_list["pets"]:
        if pet["name"] == given_name:
            found_pet = pet
            break
        else:
            found_pet = None

    return found_pet

def remove_pet_by_name(pet_shop_list, name_to_remove):
    counter = 0
    for pet in pet_shop_list["pets"]:
        if pet["name"] == name_to_remove:
            pet_shop_list["pets"].pop(counter)
        counter +=1

def add_pet_to_stock(pet_shop_list, new_pet):
    pet_shop_list["pets"].append(new_pet)

def get_customer_cash(customer_list):
    cash = customer_list["cash"]
    return cash

def remove_customer_cash(customer, amount_to_remove):
    customer["cash"] -= amount_to_remove

def get_customer_pet_count(customer):
    pet_count = len(customer["pets"])
    return pet_count

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)