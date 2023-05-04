

# Step 1:

## Step 1.1
The first step of bin picking is to put the gripper near the target object. You can use `robot.move` for this. Write the code to place the gripper near the target object and pass `check`.

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put the gripper near the cube
    #  2. Put gripper above cube
    #  3. Drop gripper around cube
    #  4. Close gripper around cube
    #  5. Drop cube into target bin
    # First, we need to move the gripper near the cube.
    if check("the robot's gripper is not near cube"):
        robot.move("the gripper near the cube")
```

## Step 1.2
The next step is to place the gripper above the object. Write the code to do this.

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put the gripper near the cube
    #  2. Put gripper above cube
    #  3. Drop gripper around cube
    #  4. Close gripper around cube
    #  5. Drop cube into target bin
    # First, we need to move the gripper near the cube.
    if check("the robot's gripper is not near cube"):
        robot.move("the gripper near the cube")
    # We need to put the gripper above the cube
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.place("gripper above cube")
```

## Step 1.3
Next, the gripper should be closed around the object. Write the code to place the gripper around the object and to close the gripper.

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put the gripper near the cube
    #  2. Put gripper above cube
    #  3. Drop gripper around cube
    #  4. Close gripper around cube
    #  5. Drop cube into