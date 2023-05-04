
    # Steps:
    #  1. Put gripper above the puck
    #  2. Close gripper on the puck
    #  3. Put the puck at the target location
    # First, put the gripper above the puck.
    # Because the robot's gripper opens horizontally, we need to grab the puck
    # from above.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # As long as the gripper is above the puck and open, we should close it on
    # the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is open"):
        robot.grab("the puck")
    # If the robot is holding the puck and the puck is not at the target location
    # we need to put the puck on the target location.
    if check("the robot is holding the puck and the puck is not at reach target"):
        robot.place("the puck at reach target")

# pick-place-topdown: pick up the puck and hold it at the target location
# This is topdown, so the gripper doesn't need to be above the puck.
def pick_place_topdown(robot):
    # Steps:
    #  1. Put gripper near the puck
    #  2. Close gripper on the puck
    #  3. Put the puck at the target location
    # First, put the gripper near the puck.
    if check("the robot's gripper is not near the puck"):
        robot.put("the gripper near the puck")
    # As long as the gripper is near the puck and open, we should close it on
    # the puck.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.grab("the puck")
    # If the robot is holding the puck and the puck is not at the target location
    # we need to put the puck on the target location.
    if check("the robot is holding the puck and the puck is not at reach target"):
        robot.place("the puck at reach target")

# pick-place-side: put the gripper near the puck to the side of it, then grab
# and place
def pick_