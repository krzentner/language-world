

Steps:

1. Put gripper left of the puck with enough space for the small wall
2. Put the gripper against the wall
3. Push the gripper against the wall to slide the puck to the target location

# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Put gripper left of the puck with enough space for the small wall
    #  2. Put the gripper against the wall
    #  3. Push the gripper against the wall to slide the puck to the target location
    # First, put the gripper left of the puck with enough space for the wall.
    if check("the robot's gripper is not left of puck and the robot's gripper is not far enough away to leave space for wall"):
        robot.put("gripper left of puck with enough space for wall")
    # Make sure the gripper is against the wall.
    if check("the robot's gripper is not against wall"):
        robot.put("gripper against wall")
    # Now, push against the wall with the gripper to slide the puck to the
    # target location.
    if check("the robot's gripper is against wall"):
        robot.push("against wall to slide puck to goal")