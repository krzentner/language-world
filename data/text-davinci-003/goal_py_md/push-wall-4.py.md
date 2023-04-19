

In order to push the puck to the goal location, the robot must first line up its gripper around the puck with a small wall in the way. To do this, we must first move the gripper to an area above the wall and the puck. Then, we move the gripper down to the puck, trapping it in-between the gripper and the wall. Once the gripper is tight against the wall and the puck, we can slide the puck to the goal location.

# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Put gripper above wall and puck
    #  2. Drop gripper around puck while pressing against wall
    #  3. Slide puck to goal
    # First, put the gripper above the small wall and the puck.
    if check("the robot's gripper is not above wall and puck"):
        robot.move_gripper("above wall and puck")
    # Then, drop the gripper around the puck while pressing against the wall.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Now that the gripper is around the puck and tethered to the wall, we can
    # slide the puck to the goal location.
    if check("the robot's gripper is around the puck and the wall"):
        robot.move_gripper("above the target location")