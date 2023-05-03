

Steps: 
1. Put gripper above the wall of the immediate location
2. Move gripper forward to the target location
3. Put gripper above puck
4. Drop gripper around puck
5. Close gripper around puck
6. Move puck to the target location

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above the wall of the immediate location
    #  2. Move gripper forward to the target location
    #  3. Put gripper above puck
    #  4. Drop gripper around puck
    #  5. Close gripper around puck
    #  6. Move puck to the target location
    # First, move the gripper to the top of the wall next to the puck.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # Once the gripper is at the end of the wall, move it forward to the 
    # target location.
    if check("the robot's gripper is near the wall"):
        robot.move_gripper("forward to the target location")
    # To pick up the puck, put the gripper above it.
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck")
    # Once the gripper is roughly above the puck, drop it down around the puck
    # to grab it.
    if check("the robot's gripper is above the puck and the robot's gripper is not around puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the gripper is around the puck, close the gripper to secure it.
    if check("the robot's gripper is around the puck and the robot's gripper is open"):
        robot.move_gripper("near the target location", close_gripper=True)
    # Once the puck is securely grasped, move it to the target location.
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")