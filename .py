def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "charlotte" == city:
        return 220
    elif "tampa" == city:
        return 699
    elif "pittsburgh" == city:
        return 547
    elif "los angeles" == city:
        return 901
    
def rental_car_cost(days):
    if days>= 7
       return 40*days - 50
    elif days>= 3
       return 40*days - 20
    else :
        return 40*days
