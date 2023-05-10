# initialize current position
x, y = 0, 0

# process instructions
while True:
    # get next instruction
    instruction = input("Enter instruction (UP/DOWN/LEFT/RIGHT steps or STOP): ")
    if instruction == "STOP":
        break

    # parse instruction
    direction, steps = instruction.split()
    steps = int(steps)

    # update position
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

# print final position
print("Final position: ({}, {})".format(x, y))
