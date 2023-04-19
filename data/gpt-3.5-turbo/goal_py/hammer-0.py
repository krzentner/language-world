# Steps:
#  1. Put the gripper above the hammer
#  2. Grab the handle of the hammer with the gripper
#  3. Put the gripper above the nail
#  4. Grab the nail with the gripper
#  5. Line up the hammer above the nail
#  6. Move the hammer down towards the nail
#  7. Move the hammer up to hit the nail
#  8. Repeat steps 6 and 7 until the nail is fully inserted
# First, put the gripper above the hammer.
if check("the robot's gripper is not vertically aligned with the hammer handle"):
    robot.move_gripper("vertically aligned with the hammer handle")
# If the gripper is above the hammer, close the gripper around the hammer handle.
if check("the robot's gripper is above the hammer handle and the gripper is open"):
    robot.move_gripper("around the hammer handle")
# If the hammer is being held, move the gripper above the nail.
if check("the hammer handle is held by the gripper"):
    robot.move_gripper("vertically aligned with the nail")
# If the gripper is above the nail, grab the nail.
if check("the robot's gripper is above the nail and the gripper is open"):
    robot.move_gripper("around the nail")
# If the gripper is holding the nail and the hammer handle, move the hammer above
# the nail.
if check("the hammer handle is held by the gripper and the nail is held by the gripper"):
    robot.move_gripper("vertically aligned with the nail")
# If the gripper is above the nail and the hammer is above the nail, move the
# hammer down towards the nail.
if check("the robot's gripper is vertically aligned with the nail and the robot's gripper is above the nail"):
    robot.move_gripper("near the nail") # move the hammer down towards the nail
# If the hammer is near the nail, move it up to hit the nail.
if check("the robot's gripper is above the nail and the nail is held by the gripper"):
    robot.move_gripper("almost vertically aligned with the hammer head") # move the hammer up to hit the nail
# If the hammer is in position, repeat steps 6 and 7 until the nail is fully
# inserted.
if check("the hammer is in position and hitting the nail and the nail is not fully inserted"):
    robot.move_gripper("near the nail") # move the hammer down towards the nail again
elif check("the nail is fully inserted"):
    robot.move_gripper("vertically aligned with the hammer handle") # move the hammer away from the nail and release the nail and hammer.