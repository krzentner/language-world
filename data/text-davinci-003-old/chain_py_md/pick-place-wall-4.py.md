

Steps:
1. Put gripper above puck
2. Move gripper to center of wall
3. Drop gripper along short wall
4. Close gripper around puck
5. Move puck to the goal

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper to center of wall
    #  3. Drop gripper along short wall
    #  4. Close gripper around puck
    #  5. Move puck to the goal
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not in line with wall"):
        robot.move("gripper to center of wall")
    if check("the robot's gripper is not along the wall and the robot's gripper is open"):
        robot.drop("gripper along short wall")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")
``