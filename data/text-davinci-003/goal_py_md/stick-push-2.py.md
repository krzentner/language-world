

Steps:
1. Put the gripper right of the stick.
2. Drop the gripper around the stick.
3. Close the gripper around the stick.
4. Push the stick forward so it pushes the thermos.

```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper right of the stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Push the stick forward so it pushes the thermos
    # First, put the gripper right of the stick
    if check("the robot's gripper is not right of the stick"):
        robot.move_gripper("right of the stick")
    # If the gripper is right of the stick but not near it, move the gripper near
    # the stick.
    # We don't need to be careful about the direction, since the stick is thin and
    # we can just grab it.
    if check("the robot's gripper is not near the stick"):
        robot.move_gripper("near the stick")
    # Once the gripper is near the stick, close the gripper around the stick.
    if check("the robot's gripper is not around the stick"): 
        robot.move_gripper("around the stick", close_gripper=True)
    # If the stick is trapped by the gripper, push it forward so it pushes the
    # thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("near the target location")