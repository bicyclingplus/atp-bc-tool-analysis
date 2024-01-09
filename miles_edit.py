import json
import math

def calculate_distance(mode, proj_distance, proj_intersections, proj_volume, proj_connected):
    # -----------------------------------------------------------
    # function to estimate distance walked in a project
    #
    # Parameters:
    # -----------
    # proj_distance: Total path length of the project
    # proj_intersections: Total number of intersections within the project boundaries
    # proj_volume: Total intersection volume within the project boundaries
    #
    # Returns:
    # -----------
    # distance: Total distance walked within the project for the given intersection volume
    # -----------------------------------------------------------

    # Get data from the lookup table in config.json **EDIT: use the volume_to_miles instead, to test bicycling as well**
    f = open('volume_to_miles.json')
    config_data = json.load(f)
    miles_distribution = config_data[mode]

    # Calculating the average distance per intersection for the project
    proj_distance_per_intersection = proj_distance/proj_intersections

    # Convert miles into intersections
    intersection_distribution = {}
    distribution_den = 0
    for dist in miles_distribution:
        intersection_distribution[dist] = math.floor(float(dist)/proj_distance_per_intersection)
        print("miles distribution is",miles_distribution[dist])
        print("intersection distribution original is",intersection_distribution[dist])

        # If on average people walk more than the number of intersections in the project, then consider they have walked through all of the project intersections
        if intersection_distribution[dist] > proj_intersections:
            intersection_distribution[dist] = proj_intersections
        print("intersection distribution cut-off is",intersection_distribution[dist])

        # Distribution of people walking through intersections
        distribution_den += intersection_distribution[dist]*miles_distribution[dist] # number of intersections * % of people walking through them - weighted average # of intersections/ways each person is counted at
        adjusted_den = (distribution_den * proj_connected) # people staying in the project (proj_connected): travel the average.
        adjusted_den += (1-proj_connected)# People crossing (everyone else, 1 - proj_connected) travel 1 intersection.

    print("average intersections traveled is",distribution_den)
    print("adjusted average intersections traveled is",adjusted_den)
    print(adjusted_den/distribution_den)

    people = math.floor(proj_volume/distribution_den)
    people_adj = proj_volume/adjusted_den # total people/average intersections = unique people, not counted multiple times
    print("unique people is",people)
    print("adjusted unique people is",people_adj)

    # Calculating the distance walked in the project
    distance = 0
    for dist in miles_distribution:
        if (float(dist)>proj_distance):
            distance += proj_distance*miles_distribution[dist]*people
        else:
            distance += float(dist)*miles_distribution[dist]*people

    distance = round(distance, 2)

    return distance

if __name__ == "__main__":
    # Project data
    proj_intersections = 10
    proj_distance = 1.8
    proj_volume = 1234

    # Pass the data to the function calculate_distance()
    distance = calculate_distance(proj_distance, proj_intersections, proj_volume)
    print("The total distance travelled is: "+ str(distance)+ " miles")
