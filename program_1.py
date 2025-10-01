# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.
#Programmer: Devin Goshaw
#date: 9/30/2025
# Program: Kilometer to mile conversion program 


def kilometer_conversion(kilometers):    
    miles = 0.0
    ######################
    conversion=0.621372
    miles=kilometers*conversion
    print(kilometers,'kilometers')
    print(miles,'miles')
    ######################    


    # Return the variable to the calling function
    return miles
#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    kilometer_conversion(float(input("enter the kilometers:")))
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    print('in main')
    # Display the miles
