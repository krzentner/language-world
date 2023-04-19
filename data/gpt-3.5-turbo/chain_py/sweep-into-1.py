# Steps:
#  1. Sweep the gripper towards the cube
#  2. Grab the cube
#  3. Lift the cube up off the ground
#  4. Sweep the gripper towards the target
#  5. Place the cube at the target location
# First, sweep the gripper towards the cube.
# If the gripper isn't lined up with the cube from the front, move it forward.
# Also move it down if it's not close to the cube.
if check("the robot's gripper is not forward aligned with the cube or the robot's gripper is not near the cube"):
    robot.sweep("gripper towards the cube")
# If the gripper is aligned with the cube and open, we can probably grab it by
# closing the gripper.
if check("the robot's gripper is near the cube and the robot's gripper is open"):
    robot.close("gripper around the cube")
# Once we've grabbed the cube, we'll need to lift it up off of the ground.
if check("the robot's gripper is around the cube"):
    robot.lift("the cube off the ground")
# Now we need to sweep the gripper towards the target location.
# If the gripper isn't lined up with the target from the front, move it forward.
# Also move it down if it's not close to the target.
if check("the robot's gripper is not forward aligned with the target or the robot's gripper is not near the target"):
    robot.sweep("gripper towards the target")
# If the gripper is aligned with the target, we can place the cube.
if check("the robot's gripper is near the target"):
    robot.place("cube at target location")