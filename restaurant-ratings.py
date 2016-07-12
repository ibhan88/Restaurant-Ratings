# your code goes here
import sys 

def sort_restaurants(filename):
    #Open the file containing restaurant names and ratings.
    ratings_file = open(filename)

    #Initialize dictionary as empty.
    restaurants = {}

    #Loop over the restaurant ratings file
    for line in ratings_file:

        #Create list containing one restaurant name and rating
        line = line.rstrip()
        line = line.split(":")

        #line[0] is the restaurant name; line[1] is the rating. 
        #Use the name as the key and the rating as the value.
        restaurants[line[0]] = line[1]

    #Convert dictionary into list of tuples.
    #Sort restaurants alphabetically.
    return sorted(restaurants.items())

def print_restaurant_ratings():

    sorted_restaurants = sort_restaurants(sys.argv[1])

    #Loop over sorted restaurants.
    for restaurant in sorted_restaurants:
        restaurant_name = restaurant[0]
        restaurant_rating = restaurant[1]

        print "{} is rated at {}.".format(restaurant_name, restaurant_rating)

print_restaurant_ratings()

