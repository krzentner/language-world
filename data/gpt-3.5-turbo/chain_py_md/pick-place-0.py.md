# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Move the gripper to the target location
    #  4. Release the puck
    # First, move the gripper above the puck
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # Once the gripper is above the puck, grab the puck
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.grab("the puck")
    # Move the gripper to the target location
    if check("the robot's gripper is holding the puck and is not near the target location"):
        robot.move("the gripper to the target location")
    # Release the puck
    if check("the robot's gripper is holding the puck and is at the target location"):
        robot.release("the puck")