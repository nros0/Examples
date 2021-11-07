
# The following code calculates a taxi fare using a function assuming the following:
# Taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# The user can input how far they went in kilometers, then the fare will be calculated. 

taxi_fare = 4.00                   # defining taxi_fare 
ftaxi_fare = float(taxi_fare)      # setting taxi_fare to float so that it can be used in calculations with later values.

kilometer = 1000                   # defining distance of kilometer, which will be multiplied by the 
fkilometer = float(kilometer)      # number of kilometers the user states they went in order to find total meters travelled.

distance = input("How far did you go in kilometers?: ")    # User input for how many kilometers they travelled.
idistance = int(distance)                                  # turning user input string into integer
fdistance = float(idistance)                               # turning integer into float
kdistance = (fdistance) * 1000                             # multiplying by 1000 to get distance in meters

rate = 140                                                 # defining rate to have it later divide the kdistance
frate = float(rate)                                        # turning rate into float

amt = kdistance / frate                                    # calculation for the extra fare
amt_add = .25 * amt 
famt_add = round(amt_add, 2)                               # rounding to the first two decimal places


def fare_calculator(kms):
    kms = taxi_fare + famt_add
    print(f"${kms}")
    """This function takes the parameter of kilometers travelled as an added fare, adds it to the base
    taxi fare and prints the value."""
    
fare_calculator("{kms}")
