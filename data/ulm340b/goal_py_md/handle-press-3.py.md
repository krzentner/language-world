

### Step 1: Put the gripper to the left of the handle

# Handle-press: push down the handle
def handle_press(robot):
    # Steps:
    # 1. Put gripper to the left of the handle
    # 2. Push the handle to the right
    # 3. Put the gripper above the handle
    # 4. Push the handle down
    # 5. Line up the gripper as viewed from above
    # 6. Push down on the handle from the top
    
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")

    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("left of the handle")

### Step 2: Push the handle to the right

# Handle-press: push down the handle
def handle_press(robot):
    # Steps:
    # 1. Put gripper to the left of the handle
    # 2. Push the handle to the right
    # 3. Put the gripper above the handle
    # 4. Push the handle down
    # 5. Line up the gripper as viewed from above
    # 6. Push down on the handle from the top
    
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")

    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("left of the handle")

    if check("the robot's gripper is left of the handle"):
        robot.move_gripper("near the handle")

### Step 3: Put the gripper above the handle

# Handle-press: push down the handle
def handle_press(robot):
    # Steps:
    # 1. Put gripper to the left of the handle
    # 2. Push the handle to the right
    # 3. Put the gripper above the handle
    # 4. Push the handle down
    # 5. Line up the gripper as viewed from above
    # 6. Push down on the handle from the top
    
    if check("the robot's gripper is not vertically aligned