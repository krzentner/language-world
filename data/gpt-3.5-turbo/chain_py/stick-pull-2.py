# Steps:
#  1. Grab the stick with the gripper
#  2. Position the gripper and stick over the thermos
#  3. Use the stick to hook onto the handle of the thermos
#  4. Pull the thermos towards the target
# First, put the gripper around the stick.
if check("the robot's gripper is not around stick"):
    robot.drop("gripper around stick")
# If the gripper is not over the thermos, move it there.
if check("the robot's gripper is not above the thermos"):
    robot.move("gripper to thermos")
# If the stick isn't aligned with the thermos handle, line it up.
if check("the stick is not aligned with the thermos handle"):
    robot.align("stick to thermos handle")
# Use the hook at the end of the stick to grab onto the thermos handle.
if check("the stick is aligned with the thermos handle"):
    robot.hook("stick onto thermos handle")
# Use the stick to pull the thermos towards the target.
if check("the stick is attached to the thermos and the thermos is not at the target"):
    robot.pull("thermos towards target")