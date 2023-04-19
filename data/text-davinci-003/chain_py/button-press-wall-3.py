
    # Steps:
    #  1. Line up gripper with button as viewed from the side
    #  2. Push down on the button (while avoiding the wall)
    # First, line up the robot's gripper with the button by moving it
    # horizontally (around the side of the wall).
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper with button horizontally")
    # Once the gripper is lined up with the button, start pushing down on the
    # button by moving the gripper in a downward direction.
    # This can be done by moving the gripper in a downward direction while
    # avoiding the wall.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button while avoiding wall")