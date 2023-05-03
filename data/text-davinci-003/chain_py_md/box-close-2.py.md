

# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put gripper near the box lid
    #  2. Grab the box lid with the gripper
    #  3. Move lid above box
    #  4. Drop lid onto the box
    # First, put the gripper near to the box lid.
    if check("the robot's gripper is not near the box lid"):
        robot.put("gripper near box lid")
    # If the gripper is near the box lid and the gripper is open, we can try to
    # grab the box lid.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.grab("box lid")
    # If the box lid is being held by the gripper, we can move it above the box.
    if check("the robot's gripper is holding box lid"):
        robot.move("lid above box")
    # Finally, if the box lid is above the box and the gripper is still closed,
    # we can drop it onto the box.
    if check("the robot's gripper is holding the box lid and the lid is above the box"):
        robot.drop("box lid onto the box")