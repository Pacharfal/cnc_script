#imports
import re



#funkce1 increments y by 10, where x is bigger than 50 and sort blocks in ascending order

def funkce1():
    # open a file
    with open("D327971_fc1.i", "r") as input_file:
        file_content = input_file.read()

    #split content to lines
    lines = file_content.splitlines()

    #Loop through each line
    for i in range(len(lines)):
        if "X" in lines[i]:
            x = float(lines[i].split("X")[1].split("Y")[0])
            if x > 50:
                y = float(lines[i].split("Y")[1])
                y += 10
                lines[i] = lines[i].replace("Y" + str(int(y - 10)), "Y" + str(int(y)))

    #join lines back together
    new_content = "\n".join(lines)

    # Open a new file for writing
    with open('cnc.txt', 'w') as output_file:
        # Write the modified contents to the new file
        output_file.write(new_content)
    return None


#funkce2 prints min/max values from x and y axes to console

def funkce2():
    return None
