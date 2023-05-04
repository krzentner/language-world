

To check the robot's state, you can use functions like these:

```
# check if the robot's gripper is in a particular state
def check(state):
    return True if state else False

# check if the robot's gripper is below something
def below(thing):
    return check("the robot's gripper is below the %s" % thing)

# check if the robot's gripper is above something
def above(thing):
    return check("the robot's gripper is above the %s" % thing)

# check if the robot's gripper is near something
def near(thing):
    return check("the robot's gripper is near the %s" % thing)

# check if the robot's gripper is holding something
def holds(thing):
    return check("the robot's gripper is holding the %s" % thing)

# check if the robot's gripper is aligned with something vertically
def vertical(thing):
    return check("the robot's gripper is vertically aligned with the %s" % thing)

# check if the robot's gripper is aligned with something from the front
def forward(thing):
    return check("the robot's gripper is forward aligned with the %s" % thing)

# check if the robot's gripper is aligned with something from the side
def horizontal(thing):
    return check("the robot's gripper is horizontally aligned with the %s" % thing)

# check if the robot's gripper is not near something
def far(thing):
    return not near(thing)

# check if the robot's gripper is not above something
def not_above(thing):
    return not above(thing)

# check if the robot's gripper is not below something
def not_below(thing):
    return not below(thing)

# check if the robot's gripper is not holding something
def not_holds(thing):
    return not holds(thing)

# check if the robot's gripper is not vertically aligned with something
def not_vertical(thing):
    return not vertical(thing)

# check if the robot's gripper is not aligned with something from the front
def not_forward(thing):
    return not forward(thing)

# check if the robot's gripper is not aligned with something from the side
def not_horizontal(thing):
    return not horizontal(thing)

# check if the robot's gripper is not horizontally left of something
def not_left(thing):
    return not check