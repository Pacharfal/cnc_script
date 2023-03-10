#imports
import re

# function that sort blocks in ascending order

"""
def sort_blocks(content):
    # split content to lines
    lines = content.splitlines()

    # find indices of lines starting with T
    indices = [i for i in range(len(lines)) if re.match(r'^T\d+', lines[i])]

    # extract T values and sort indices based on T values
    indices.sort(key=lambda i: int(re.search(r'^T(\d+)', lines[i]).group(1)))

    # concatenate sorted blocks
    sorted_blocks = [lines[i] for i in indices]
    new_content = '\n'.join(sorted_blocks)

    return new_content
"""
#funkce1 increments y by 10, where x is bigger than 50

def funkce1(file_name):
    # open a file
    with open(file_name, "r") as input_file:
        file_content = input_file.read()

    # split content to lines
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

funkce1('D327971_fc1.i');

#funkce2 prints min/max values from x and y axes to console
def funkce2(filename):
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    with open(filename) as f:
        for line in f:
            if line.startswith('X'):
                x, y = line.split('Y')
                y = y.split('T')[0]  # remove any tool change commands
                x = float(x[1:])
                y = float(y)

                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    print("Minimum X value:", min_x)
    print("Minimum Y value:", min_y)
    print("Maximum X value:", max_x)
    print("Maximum Y value:", max_y)

funkce2("D327971_fc1.i");
