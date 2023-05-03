

Then add code

```
# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above door lock
    #  2. Drop gripper around door lock
    #  3. Turn door lock to the right
    # First put the gripper above the door lock so that we don't bump it while 
    # trying to grab it.
    if check("the robot's gripper is not above the door lock"):
        robot.place("gripper above door lock")
    # If the gripper isn't around the door lock, put it around the door lock.
    if check("the robot's gripper is not around door lock and the robot's gripper is open"):
        robot.drop("gripper around door lock")
    # If the gripper is near the door lock and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near door lock and the robot's gripper is open"):
        robot.close("gripper around door lock")
    # We closed the gripper, and the door lock is still near the gripper, so maybe
    # we grabbed it.
    # Try to turn the door lock to the right.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above door lock and the robot's gripper is closed"):
        robot.turn("door lock right")
``