# your code goes here
import sys 

#Open the file containing restaurant names and ratings.
ratings_file = open(sys.argv[1])

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
sorted_restaurants = sorted(restaurants.items())

#Loop over sorted list.
for restaurant in sorted_restaurants:
    restaurant_name = restaurant[0]
    restaurant_rating = restaurant[1]

    print "{} is rated at {}.".format(restaurant_name, restaurant_rating)

