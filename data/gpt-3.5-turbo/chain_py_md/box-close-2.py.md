# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put the gripper above the box lid
    #  2. Drop the gripper around the box lid
    #  3. Close the gripper around the box lid
    #  4. Move the box lid to the box
    #  5. Release the box lid to close the box
    # First, put the gripper above the box lid
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the box lid to the box.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.place("box lid on box")
        # Release the box lid to close the box
        robot.open("gripper around box lid")