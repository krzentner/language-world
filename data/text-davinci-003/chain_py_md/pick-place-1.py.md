

Steps:
1. Put gripper above puck
2. Grab the puck with the gripper
3. Move the puck to the target location
4. Put the puck down at the target location

```
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location
    #  4. Put the puck down at the target location

    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # Once the gripper is above the puck, close it and grab the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is open"):
        robot.grab("puck")
    # Now that the puck is held by the gripper, move it to the target location.
    if check("the robot's gripper is above the puck and the puck is not at the target location"):
        robot.move("puck to target location")
    # Once the puck is at the target location, put it down.
    if check("the puck is at the target location"):
        robot.put("puck down at target location")