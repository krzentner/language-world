# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck on one side of wall
    #  2. Push gripper into top of puck
    #  3. Slide puck to edge of wall
    #  4. Move gripper to other side of wall, above the puck
    #  5. Slide puck to goal
    # The robot needs to slide the puck to the target location but there is a wall in the way.
    # If the puck isn't on one side of the wall, move it there by putting the gripper above it.
    if check("the robot's gripper is not above the puck and the puck is not on one side of the wall"):
        robot.move("gripper to one side of wall")
        robot.put("gripper above puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the edge of the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and the puck is not at the edge of the wall"):
        robot.slide("the puck to the edge of the wall")
    # Then move the gripper to the other side of the wall on top of the puck.
    if check("the robot's gripper is on the same side of the wall as it started"):
        robot.move("gripper to other side of wall")
        robot.put("gripper above puck")
    # Slide the puck all the way to the goal.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and the puck is at the edge of the wall"):
        robot.slide("the puck to the goal")