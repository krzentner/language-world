

```
# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put the robot's gripper above the puck
    #  2. If the wall is in the way:
    #        A. Close the robot's gripper around the wall
    #        B. Slide the wall out of the way
    #  3. Push the gripper into the puck
    #  4. Slide the puck to the goal

    # First, put the gripper above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")

    # If the wall is in the way, we should probably move it.
    # If the robot's gripper isn't near the wall, we have to move it to the wall.
    if check("wall is in the way and the robot's gripper is not near wall"):
        robot.move("gripper to wall")

    # If the robot's gripper is near the wall, we can grab it.
    if check("wall is in the way and the robot's gripper is near wall"):
        robot.close("gripper around wall")

    # If the robot's gripper is above the wall, and the robot's gripper is near the wall,
    # we can slide the wall to the side.
    if check("wall is in the way and the robot's gripper is above wall"):
        robot.slide("wall to the side")

    # If the robot's gripper is near the puck, but not above the puck,
    # we can push the gripper into the puck.
    # If the robot's gripper is near the puck, the robot's gripper is vertically aligned with the puck, and the robot's gripper is not above the puck:
    if check("the robot's gripper is near puck and the robot's gripper is vertically aligned with the puck and the robot's gripper is not above puck"):
        robot.push("the gripper into the puck")

    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the grip