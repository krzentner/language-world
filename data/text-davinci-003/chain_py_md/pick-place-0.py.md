

Then, write the code to perform the task:

```
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Reach down to grab the puck
    #  3. Move the puck to the target location
    #  4. Hold the puck at the goal
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # Then, reach down to grab the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck"):
        robot.grab("puck")
    # Now that the gripper is around the puck, move to the target location.
    if check("the robot's gripper is around the puck"):
        robot.move("puck to goal")
    # Once at the target location, open the gripper and hold the puck in place.
    if check("the robot's gripper is at goal"):
        robot.hold("puck in place")
```