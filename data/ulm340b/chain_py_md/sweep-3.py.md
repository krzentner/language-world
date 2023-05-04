

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move sideways into goal
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("cube to the goal")
```

Now I would like you to write the code to perform the task `insert`, which will insert the cube into the hole from above. Please copy and paste this as a starting point:

```
# insert: drop the cube into the hole
def insert(robot):
    # Steps:
    #  1. Place gripper above cube
    #  2. Grab cube
    #  3. Line up cube with hole
    #  4. Drop the cube in the hole
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("cube to the goal")
```

Can you write code to perform `screwdriver`, which turns a screwdriver counterclockwise 180 degrees?

```
# screwdriver: rotate the screwdriver counterclockwise 180 degrees
def screwdriver(robot):
    # Steps:
    #  1. Move gripper near the screwdriver
    #  2. Rotate screwdriver
    # Since the screwdriver has a very long handle, all the robot has