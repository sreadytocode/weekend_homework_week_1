# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"] 

def add_or_remove_cash(pet_shop, num):
    pet_shop["admin"]["total_cash"] += num 
     
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    found_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_breed.append(breed)
    return found_breed 

def find_pet_by_name(pet_shop, name):
    found_name = None
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            found_name = pet
    return found_name

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet["name"] = None

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)
    len(pet_shop["pets"])
    
def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer_cash, num):
    customer_cash["cash"] -= num 

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
    len(customer["pets"])
    
def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True 
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):   
    
    if pet == find_pet_by_name(pet_shop, "Arthur") and customer_can_afford_pet(customer, pet) == True:
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
        remove_customer_cash(customer, 900)
        add_or_remove_cash(pet_shop, 900)

    else: 
        get_customer_pet_count(customer) 
        get_pets_sold(pet_shop)
        get_customer_cash(customer)
        get_total_cash(pet_shop)


