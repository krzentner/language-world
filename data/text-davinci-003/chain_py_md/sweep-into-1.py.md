

Steps: 
  1. Put the gripper just above the cube
  2. Put the gripper around the cube
  3. Close the gripper around the cube
  4. Move the cube to the target location
  

```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put the gripper just above the cube
    #  2. Put the gripper around the cube
    #  3. Close the gripper around the cube
    #  4. Move the cube to the target location
    # First, put the gripper just above the cube so that we don't bump it
    # while trying to grab it. 
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper is above the cube, then grab the cube by moving the
    # gripper around it.
    if check("the robot's gripper is above cube and the robot's gripper is not around cube"):
        robot.grab("cube")
    # If the gripper is around the cube and open, we should be able to grab it
    # by closing the gripper.
    if check("the robot's gripper is around cube and robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("cube at target")