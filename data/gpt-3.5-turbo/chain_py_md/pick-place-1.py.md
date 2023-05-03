# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put the gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the gripper to the target location
    #  4. Release the puck
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.grab("puck")
    if check("the robot's gripper is not at the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is at the target location and the robot's gripper is closed around the puck"):
        robot.release("puck")