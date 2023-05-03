# Steps:
    #  1. Put gripper above puck on the side of the wall facing the robot
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to above wall
    #  5. Put gripper on other side of wall
    #  6. Drop gripper around puck
    #  7. Open gripper to release puck
    # First, put the gripper roughly above the puck on the side facing the robot.
    if check("the robot's gripper is not above the puck and the puck is on the other side of the wall"):
        robot.place("gripper above puck on the side facing the robot")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around the puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around the puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it. Try to move the puck above the wall.
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.move("puck above the wall")
    # Once the gripper is on the other side of the wall, we can drop the gripper
    # around the puck again.
    if check("the robot's gripper is on the other side of the wall"):
        robot.place("gripper around the puck")
    # Open the gripper to release the puck.
    if check("the robot's gripper is around the puck"):
        robot.open("gripper to release the puck")