
    # Steps:
    #  1. Put gripper above the knob
    #  2. Grab the knob with the gripper
    #  3. Line the knob up with the right
    #  4. Push the knob to the right
    # First, put the gripper above the knob.
    if check("the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    # If the knob becomes left of the gripper, go back to putting the gripper
    # above the knob.
    # Because the knob is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("knob is not left of the robot's gripper and knob is not forward aligned with the robot's gripper"):
        robot.grab("knob")
    # As long the gripper is still mostly around the knob and the knob isn't lined
    # up with the right, line up the knob with the right.
    if check("the robot's gripper is forward aligned with the knob and the knob is not horizontally aligned with right"):
        robot.align("knob with right")
    # If the knob is lined up with the right, we can turn the faucet closed.
    if check("knob is horizontally aligned with right"):
        robot.push("knob right")

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the knob
    #  2. Grab the knob with the gripper
    #  3. Line the knob up with the left
    #  4. Push the knob to the left
    # First, put the gripper above the knob.
    if check("the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    # If the knob becomes left of the gripper, go back to putting the gripper
    # above the knob.
    # Because the knob is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("knob is not left of the robot's gripper and knob is not forward aligned with the robot's gripper"):
        robot.grab("knob")
    # As