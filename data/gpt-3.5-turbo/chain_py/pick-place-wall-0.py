# Steps:
    #  1. Put gripper above the puck on the side without the wall
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move gripper around the wall to the other side of the puck
    #  5. Move the puck to the goal
    # First, put the gripper above the puck, but on the side without the wall,
    # so that we can grab it easily.
    if check("the robot's gripper is not above the puck and the puck is not on the side without the wall"):
        robot.move("gripper to side without wall")
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
    # Now we need to move the gripper to the other side of the wall.
    # We can use the slide function to move the gripper left and right.
    if check("the robot's gripper is closed around the puck and the wall is between the puck and the goal"):
        robot.slide("gripper left")
        robot.slide("gripper right")
    # Once the gripper is on the other side of the wall, we can move the puck to
    # the goal.
    if check("the wall is not between the puck and the goal and the robot's gripper is closed around the puck"):
        robot.place("puck at goal")