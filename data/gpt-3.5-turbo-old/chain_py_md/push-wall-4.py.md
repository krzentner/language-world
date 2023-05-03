# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    # 1. Put gripper above puck
    # 2. Push gripper into top of puck
    # 3. Slide puck to wall
    # 4. Push puck over the wall
    # 5. Slide puck to goal
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper is not around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the wall.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.slide("the puck to the wall")
    # Now that the gripper is at the wall, push the puck up and over it.
    if check("the robot's gripper is near the wall and the gripper has the puck"):
        robot.push("puck over the wall")
    # Finally, slide the puck to the goal.
    if check("the puck has been pushed over the wall"):
        robot.slide("the puck to the goal")