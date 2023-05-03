# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put the gripper directly above the box lid
    #  2. Grab the box lid
    #  3. Move the box lid above the box base
    #  4. Slowly lower the box lid onto the base
    # First, put the gripper directly above the box lid.
    if check("the robot's gripper is not directly above the box lid"):
        robot.place("gripper above box lid")
    # If the robot's gripper is above the box lid, drop the gripper around the lid.
    if check("the robot's gripper is above the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper encloses the lid, move it to above the box base.
    if check("the robot's gripper is around box lid and the robot's gripper is not above the box base"):
        robot.move("gripper above box base")
    # Once the gripper is above the box base, slowly lower the box lid onto the base.
    if check("the robot's gripper is above box base"):
        robot.put("box lid onto box base slowly")