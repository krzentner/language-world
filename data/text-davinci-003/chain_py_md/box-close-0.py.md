

# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put gripper above box lid
    #  2. Grab the box lid with the gripper
    #  3. Move the box lid above the box
    #  4. Place the box lid onto the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper isn't near the box lid, put the gripper around the box lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.grab("box lid")
    # If the gripper is near the box lid and open, close the gripper around it.
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # If the gripper is holding the box lid, move the box lid above the box.
    if check("the robot's gripper is above the box lid and the robot's gripper is closed"):
        robot.move("box lid above box")
    # If the box lid is above the box, place it on the box.
    if check("the box lid is above the box"):
        robot.place("box lid on box")