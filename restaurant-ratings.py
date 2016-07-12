# your code goes here
import sys, random

def make_restaurant_structure(filename):
    """Given a file of restaurants and related data, sort by restaurant name.

    filename: file that contains restaurant name and related data
    Each line of the file should be formatted as follows:
        restaurant:rating:other data:etc.
    Returns a list of tuples containing restaurant name, rating, other data, etc.
    """
    #Open the file containing restaurant names and ratings.
    restaurants_file = open(filename)

    #Initialize dictionary as empty.
    restaurants = {}

    #Loop over the restaurant ratings file
    for line in restaurants_file:

        #Create list containing one restaurant name and rating
        line = line.rstrip()
        line = line.split(":")

        #line[0] is the restaurant name; line[1] is the rating. 
        #Use the name as the key and the rating as the value.
        restaurants[line[0]] = int(line[1])

    #Convert dictionary into list of tuples.
    #Sort restaurants alphabetically.
    return restaurants


def add_restaurant(restaurant_structure):  
    print "Let's add another restaurant."
    new_restaurant_name = raw_input("What is the restaurant name? >>> ")
    new_restaurant_rating = int(raw_input("What is its rating? >>> "))

    restaurant_structure[new_restaurant_name] = new_restaurant_rating

    return restaurant_structure



def update_random_restaurant(restaurant_structure):
    username = raw_input("Hi! What's your name? >>> ")

    random_restaurant = random.sample(restaurant_structure, 1)
    print random_restaurant
    # print "{} is rated at {}.".format()

update_random_restaurant(make_restaurant_structure('scores.txt'))


def print_restaurant_ratings(filename):
    """Given file of restaurant data, prints sorted data.

    Prints restaurant info in the following format:
        "<Restaurant Name> is rated at <Restaurant Rating>."
    """
    restaurants = make_restaurant_structure(filename)

    sorted_restaurants = sorted(restaurants.items())

    #Loop over sorted restaurants.
    for restaurant in sorted_restaurants:
        restaurant_name = restaurant[0]
        restaurant_rating = restaurant[1]

        print "{} is rated at {}.".format(restaurant_name, restaurant_rating)

# print_restaurant_ratings(sys.argv[1])

