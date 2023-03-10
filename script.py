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
            match = re.search(r"X([0-9.-]+)Y([0-9.-]+)", lines[i])
            if match:
                x = float(match.group(1))
                y = float(match.group(2))
                if x > 50:
                    y += 10
                    lines[i] = re.sub(r"Y[0-9.-]+", "Y" + str(y), lines[i])

    #join lines back together
    new_content = "\n".join(lines)

    # Open a new file for writing
    with open('cnc.txt', 'w') as output_file:
        # Write the modified contents to the new file
        output_file.write(new_content)

funkce1();

#funkce2 prints min/max values from x and y axes to console

def funkce2():
    pass
