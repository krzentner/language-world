

The objective of this task is to slide a puck to a target location with a small wall in the way.

Steps: 
1. Put the gripper above the puck
2. Lower the gripper over the puck
3. Close the gripper around the puck
4. Push the puck sideways so that it is around the wall
5. Move the puck to the goal

```
# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Lower gripper over puck
    #  3. Close gripper around puck
    #  4. Push the puck sideways so that it moves around the wall
    #  5. Move puck to target location
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper isn't around the puck, lower it over the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.lower("gripper over puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Now push the puck sideways so that it moves around the wall.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.push("puck sideways so it moves around the wall")
    # Finally, move the puck to the goal.
    if check("the puck is around the wall"):
        robot.move("puck to the goal")
```