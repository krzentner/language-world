# Steps:
    #  1. Move the robot's gripper above the basketball
    #  2. Grab the basketball
    #  3. Move the basketball towards the hoop
    #  4. Release the basketball into the hoop
    # First, move the gripper above the basketball.
    if check("the robot's gripper is not above the basketball"):
        robot.put("gripper above basketball")
    # If the gripper is above the basketball, grab it.
    if check("the robot's gripper is above the basketball and the robot's gripper is open"):
        robot.close("gripper around basketball")
    # If the gripper has grabbed the basketball, move it towards the hoop.
    if check("the robot's gripper is around the basketball"):
        robot.move("basketball towards hoop")
    # If the basketball is near enough to the hoop, release it.
    if check("the basketball is near the hoop"):
        robot.release("basketball into hoop")