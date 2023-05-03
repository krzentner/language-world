# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location
    #  4. Open the gripper to release the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is lined up with the puck, grab it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is open"):
        robot.grab("puck")
    # Move the puck to the target location by sliding it.
    if check("the puck is in the gripper's grasp"):
        robot.slide("the puck to the goal")
    # Release the puck by opening the gripper.
    if check("the puck is at the goal"):
        robot.release("puck")