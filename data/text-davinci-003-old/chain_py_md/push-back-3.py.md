

Solution:
```
# push-back: slide the puck backwards to the target location
# def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into the top of puck
    #  3. Slide the puck to the target location
    # First, put the gripper roughly above the puck, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal by sliding it backwards, rather than
    # pulling it forwards.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.slide("the puck to the goal in the opposite direction")
```