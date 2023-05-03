

Steps:
1. Put gripper above wrench handle
2. Grab wrench handle with the gripper
3. Pull wrench off the peg

```
# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above wrench handle
    #  2. Grab wrench handle with the gripper
    #  3. Pull wrench off the peg
    # First, put the gripper above the wrench handle.
    if check("the robot's gripper is not vertically aligned with wrench handle"):
        robot.move_gripper("vertically aligned with the wrench handle")
    # If the wrench handle isn't left of the gripper, go back to putting the
    # gripper over the wrench handle.
    # Because the wrench handle is a small object, check if the gripper is
    # lined up with it from the side instead of above it.
    if check("wrench handle is not left of the robot's gripper and wrench handle is not sideways aligned with the robot's gripper"):
        robot.move_gripper("sideways aligned with the wrench handle", close_gripper=True)
    # As long the gripper is still mostly around the wrench handle, start pulling
    # it off the peg.
    if check("the robot's gripper is sideways aligned with wrench handle"):
        robot.move_gripper("left of the peg")