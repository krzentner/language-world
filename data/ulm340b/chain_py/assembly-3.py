
    # Steps:
    #  1. Put gripper above the wrench handle
    #  2. Grab the wrench handle
    #  3. Drop wrench around the peg
    #  4. Slide the wrench around the peg
    # First, put the gripper above the wrench handle.
    if check("the robot's gripper is not vertically aligned with wrench handle"):
        robot.put("gripper above wrench handle")
    # If the wrench isn't forward aligned with the gripper as seen from above,
    # we can try to grab the wrench handle.
    if check("the robot's gripper is vertically aligned with wrench handle and the wrench handle is not forward aligned with the robot's gripper"):
        robot.grab("wrench handle")
    # If the gripper is around the wrench handle, try to put the wrench around
    # the peg.
    if check("the robot's gripper is around wrench handle and the wrench handle is not around peg"):
        robot.put("wrench around peg")
    # If the wrench handle is around the peg, try to slide the wrench around the
    # peg.
    if check("the wrench handle is around peg and the wrench handle is not wrapped around peg"):
        robot.slide("wrench around peg")

# peg-unstack: grab the peg on top and lift it off the stack
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above the top of the peg stack
    #  2. Grab the top of the peg
    #  3. Lift the peg up
    # First, put the gripper above the peg stack.
    if check("the robot's gripper is not vertically aligned with peg stack and the robot's gripper is not around peg"):
        robot.put("gripper above peg stack")
    # If the gripper is above the top of the peg stack and not around the top of
    # the peg, grab it.
    if check("the robot's gripper is vertically aligned with peg stack and the robot's gripper is not around peg and the robot's gripper is open"):
        robot.grab("top of peg stack")
    # If the gripper is around the top of the peg stack and the gripper is
    # mostly above the rest of the peg stack, we can lift it.
  