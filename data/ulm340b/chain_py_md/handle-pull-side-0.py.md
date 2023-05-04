

# Step 1: Put gripper above handle
- Steps:
    - 1. Put gripper above handle
    - 2. Pull the handle up to goal height

# Step 2: Pull the handle up to goal height
- If the robot is above handle, pull up to goal height


# Step 3: Close gripper around handle

def handle_pull_side(robot):
    # Step 1: Put gripper above handle
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # Step 2: Pull the handle up to goal height
    if check("the robot's gripper is above handle"):
        robot.pull("handle up to goal height")
    # Step 3: Close gripper around handle
    if check("the robot's gripper is not around handle"):
        robot.close("gripper around handle")

"""
def handle_pull_side(robot):
    return




































































































































































































































































































































































