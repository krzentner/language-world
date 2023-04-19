# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid to the box
    # First, put the gripper roughly above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper is not around the box lid, put it around the box lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, close the gripper to pick up
    # the lid.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # If the gripper has successfully picked up the box lid, move it to the box.
    if check("the robot's gripper has closed around box lid and the box lid is moving towards the box"):
        robot.move("the box lid to the box")
    # If the box lid has reached the box, release the lid by opening the gripper.
    if check("the box lid is at the box location and the gripper is releasing it"):
        robot.open("gripper and release box lid")