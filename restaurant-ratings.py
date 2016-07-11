# your code goes here
import sys 

#Open the file containing restaurant names and ratings.
ratings_file = open(sys.argv[1])

#Initialize dictionary as empty.
restaurant_ratings = {}

#Loop over the restaurant ratings file
for line in ratings_file:

    #Create list containing one restaurant name and rating
    line = line.rstrip()
    line = line.split(":")

    #line[0] is the restaurant name; line[1] is the rating. 
    #Use the name as the key and the rating as the value.
    restaurant_ratings[line[0]] = line[1]

print restaurant_ratings

