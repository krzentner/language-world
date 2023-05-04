
    # Steps:
    #  1. Line up gripper to turn clockwise
    #  2. Turn dial clockwise
    # First, we need to move the gripper to roughly above the dial.
    if check("the robot's gripper is not forward aligned with the dial and the robot's gripper is not vertically aligned with the dial"):
        robot.put("the gripper near the dial")
    # Once the gripper is near the dial, we can start turning the dial
    # clockwise.
    if check("the robot's gripper is near the dial"):
        robot.turn("dial clockwise")

# lever-pull: pull the lever down
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above the lever handle
    #  2. Grab the lever handle
    #  3. Pull the lever handle down
    # First, move the gripper above the lever handle.
    if check("the robot's gripper is not vertically aligned with the lever handle"):
        robot.put("the gripper above the lever handle")
    # Next, grab the lever handle.
    if check("the robot's gripper is vertically aligned with the lever handle and the robot's gripper is not around the lever handle"):
        robot.grab("lever handle")
    # Next, pull the lever handle down.
    if check("the robot's gripper is around the lever handle and the robot's gripper is vertically aligned with the lever handle"):
        robot.pull("lever handle down")

# slider-pull: slide the slider to the right
def slider_pull(robot):
    # Steps:
    #  1. Put gripper above the slider handle
    #  2. Line up gripper right above the slider handle
    #  3. Grab the slider handle
    #  4. Pull the slider handle to the right
    # First, move the gripper above the slider handle.
    if check("the robot's gripper is not vertically aligned with the slider handle"):
        robot.put("the gripper above the slider handle")
    # Next, line up the gripper so that it's right above the slider handle.
    if check("the robot's gripper is vertically aligned with the slider handle and the robot's gripper is not right aligned with the slider handle"):
       