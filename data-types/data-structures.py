spicy_foods = [
    {
        "name": "Chili Relleno",
        "cuisine": "Mexican",
        "heat_level": 5,
    }
    
]
# Define a function to get the names of spicy foods
def get_names(spicy_foods):
    # Returns a list of names of spicy foods
    return [food["name"] for food in spicy_foods]

# Call the function
get_names(spicy_foods)