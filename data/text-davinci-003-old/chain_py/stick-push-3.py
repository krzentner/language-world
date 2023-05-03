
    # Steps:
    #  1. Put the stick in front of the thermos
    #  2. Put the robot's gripper above the stick
    #  3. Lower the robot's gripper onto the stick
    #  4. Push the stick so that it pushes the thermos to the target location
    # Put the stick in front of the thermos.
    if check("the stick is not in front of the thermos"):
        robot.move("stick in front of thermos")
    # Put the robot's gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move("gripper above stick")
    # Lower the robot's gripper onto the stick
    if check("the robot's gripper is not around the stick"):
        robot.slide("gripper onto stick")
    # Push the stick so that it pushes the thermos to the target location.
    if check("the robot's gripper is around the stick"):
        robot.push("stick towards target location")