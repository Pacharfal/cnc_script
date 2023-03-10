
#funkce1 increments y by 10, where x is bigger than 50 and sort blocks in ascending order
def funkce1():
    # open a file
    with open("D327971_fc1.i", "r") as input_file:
        # Read the entire contents of the file into a string variable
        file_contents = input_file.read()

    # Make modifications to the contents of the file as needed
    modified_contents = file_contents.replace('X93.350Y116.850T01', 'Hello There !')

    # Open a new file for writing
    with open('cnc.txt', 'w') as output_file:
        # Write the modified contents to the new file
        output_file.write(modified_contents)
    return None


#funkce2 prints min/max values from x and y axes to console
def funkce2():
    return None
