
    # Steps:
    #  1. Put gripper right of the plate
    #  2. Start pushing against the plate to slide it
    #  3. Push the plate harder
    # If the plate is left of the robot's gripper and the robot is not near the
    # plate, we should move the gripper near the plate to start pushing
    if check("the plate is left of the robot's gripper and the robot's gripper is not near the plate"):
        robot.move("the gripper to the right of the plate")
    # If the robot's gripper is near the plate, we can probably slide the plate
    # to the right by moving the gripper right.
    if check("the robot's gripper is near the plate"):
        robot.slide("the plate to the right")
    # If the robot's gripper is in front of the plate, push harder.
    if check("the robot's gripper is in front of the plate"):
        robot.push("the plate to the right harder")

# box-close: push the lid of the box onto the box
def box_close(robot):
    # Steps:
    #  1. Put gripper roughly above the box
    #  2. Lower the gripper onto the box
    #  3. Push the box closed harder
    # If the robot's gripper is not above the box as seen from above, move the
    # gripper above the box to push it closed.
    if check("the robot's gripper is not above the box and the robot's gripper is not below the box"):
        robot.move("gripper above box")
    # If the robot's gripper is vertically aligned with the box, lower the
    # gripper to press the lid closed.
    if check("the robot's gripper is below the box"):
        robot.push("gripper down onto box")
    # If the gripper is in front of the box, push harder.
    if check("the robot's gripper is in front of the box"):
        robot.push("box closed harder")

# box-open: pull the box open to the left
def box_open(robot):
    # Steps:
    #  1. Put gripper left of the box
    #  2. Start pulling the