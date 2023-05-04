

And then write some steps, as in the examples above.
Use `check` to evaluate conditions about the state of the world.
Here are the checks you can use.

```
# States that we can check:

# Is the robot's gripper aligned vertically with an object?
# (For example, if the gripper is above the object as viewed from above.)
def check("the robot's gripper is vertically aligned with {target}"):

# Is the robot's gripper aligned horizontally with an object?
# (For example, if the gripper is next to the object as viewed from the side.)
def check("the robot's gripper is horizontally aligned with {target}"):

# Is the robot's gripper near the object?
# (For example, if the object is right in front of the gripper.)
def check("the robot's gripper is near {target}"):

# Is the robot's gripper closed?
# (For example, if the gripper is holding an object.)
def check("the robot's gripper is closed"):

# Is the robot's gripper open?
# (For example, if the gripper is not holding an object.)
def check("the robot's gripper is open"):

# Is the robot's gripper around an object?
# (For example, if the robot is holding an object.)
def check("the robot's gripper is around {target}"):

# Is the robot's gripper in front of an object?
# (For example, if the robot is holding an object.)
def check("the robot's gripper is forward aligned with {target}"):

# Does an object have another object above it as viewed from above?
# (For example, if object 1 is above object 2.)
def check("{target1} is above {target2}"):

# Does an object have another object below it as viewed from above?
# (For example, if object 1 is below object 2.)
def check("{target1} is below {target2}"):

# Does an object have another object left of it as viewed from above?
# (For example, if object 1 is left of object 2.)
def check("{target1} is left of {target2}"):

# Does an object have another object right of it as viewed from above?
# (For example, if object 1 is right of object 2.)
def check("{target1} is right of {target2}"):

# Is an object on the top of the table?
# (For example,