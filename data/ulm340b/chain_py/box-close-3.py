
    # Steps:
    #  1. Put gripper above the lid
    #  2. Put gripper near the lid
    #  3. Grab the lid with the gripper
    #  4. Move the lid to above the box
    # First, put the gripper above the lid.
    if check("the robot's gripper is not vertically aligned with lid and the robot's gripper is not near lid"):
        robot.put("gripper above lid")
    # If the gripper is above the lid, drop the gripper down near the lid.
    if check("the robot's gripper is vertically aligned with lid and the robot's gripper is not near lid"):
        robot.put("gripper near lid")
    # If the gripper is near the lid, try grabbing the lid.
    if check("the robot's gripper is near lid and the robot's gripper is open"):
        robot.close("gripper around lid")
    # As long as the gripper is closed around the lid, try putting the lid above
    # the box.
    if check("the robot's gripper is closed"):
        robot.move("lid above box")

# push-right: slide the puck to the right
def push_right(robot):
    # Steps:
    #  1. Put gripper left of the puck
    #  2. Move the gripper near the puck
    #  3. Push the gripper right into the puck
    # First, put the gripper left of the puck.
    if check("the robot's gripper is not left of the puck"):
        robot.put("gripper to left of puck")
    # Now that the gripper is left of the puck, put the gripper near the puck.
    if check("the robot's gripper is left of the puck"):
        robot.move("gripper to near puck")
    # If the gripper is already near the puck, just keep moving it right.
    if check("the robot's gripper is near puck"):
        robot.slide("gripper to right")

# pull-right: slide the puck to the right by pulling it with the gripper
def pull_right(robot):
    # Steps:
    #  1. Put gripper right of the puck
    #  2. Move