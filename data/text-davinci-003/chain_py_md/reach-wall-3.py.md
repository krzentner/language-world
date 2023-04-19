

The robot should then reach the target location with a short wall in the way.

Steps: 
1. Put Gripper Left of the wall
2. Reach over wall towards target location
3. Push against wall to line up the robot's gripper with the wall
4. Reach towards target location

```
# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Put gripper left of the wall
    #  2. Reach over wall towards target location
    #  3. Push against wall to line up the robot's gripper with the wall
    #  4. Reach towards target location
    # Put the gripper left of the wall
    if check("the robot's gripper is not left of the wall"):
        robot.put("gripper left of wall")
    # Reach over the wall towards the target.
    if check("the robot's gripper is left of the wall"):
        robot.reach("over wall to target")
    # Push against the wall to line up the gripper with it. 
    if check("the robot's gripper is not aligned with the wall"):
        robot.push("against wall")
    # Once the gripper is aligned with the wall, we can reach towards the 
    # target again.
    if check("the robot's gripper is aligned with the wall"): 
        robot.reach("towards target")
``