# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
# Steps:
#   1. Detect the mug on the table
#   2. Move gripper above the mug
#   3. Close gripper to grab the mug
#   4. Move gripper to target location
#   5. Open gripper to release the mug
# Use object detection to find the mug on the table
def coffee_push(robot):
    if check("the mug is not detected on the table"):
        robot.detect("mug")
    # Move the gripper above the mug
    if check("the gripper is not above the mug"):
        robot.place("gripper above mug")
    # Close the gripper to grab the mug
    if check("the gripper is above the mug and open"):
        robot.close("gripper around mug")
    # Move the gripper to the target location
    if check("the gripper is closed and the mug is not at the target location"):
        robot.move("gripper to goal location")
    # Open the gripper to release the mug
    if check("the gripper is at the goal location and closed"):
        robot.open("gripper")