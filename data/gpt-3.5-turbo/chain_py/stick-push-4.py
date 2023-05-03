# Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Position gripper so that stick can reach thermos
    #  4. Grab thermos with stick
    #  5. Drag thermos to target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above the stick")
    # If the gripper is above the stick but not holding it, grab the stick.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper has the stick, move the gripper so that the stick can reach
    # the thermos.
    if check("the robot's gripper is holding the stick and the thermos is not near the end of the stick"):
        robot.move("gripper to position for thermos")
    # If the gripper is holding the stick and near the thermos, grab the thermos
    # with the stick.
    if check("the robot's gripper is holding the stick and the thermos is near the end of the stick"):
        robot.grab("thermos with stick")
    # If the gripper has the stick and the thermos, slide/move the thermos to the
    # target location.
    if check("the robot's gripper is holding the stick and the thermos is grabbed by the stick"):
        robot.slide("thermos to the target location")