

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck over wall
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
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
    # To move the puck over the wall, move the gripper up and slightly over the 
    # wall, then move it downwards and to the goal in one motion.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("gripper up and over wall")
        robot.move("puck to goal")
```