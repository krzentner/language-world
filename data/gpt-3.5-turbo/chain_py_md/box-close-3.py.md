# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Move gripper above the box lid
    #  2. Drop gripper around the box lid
    #  3. Close gripper around the box lid
    #  4. Move the box lid to the box
    # First, position the gripper above the box lid
    if check("the robot's gripper is not above the box lid"):
        robot.move("gripper to box lid")
    # Once the gripper is positioned above the box lid, drop the gripper around the box lid
    if check("the robot's gripper is not around the box lid"):
        robot.drop("gripper around the box lid")
    # With the gripper positioned around the box lid, close the gripper
    if check("the robot's gripper is around the box lid and the gripper is open"):
        robot.close("gripper around the box lid")
    # Once the box lid is securely held, move it to the box
    if check("the box lid is securely held by the gripper"):
        robot.place("the box lid on the box")