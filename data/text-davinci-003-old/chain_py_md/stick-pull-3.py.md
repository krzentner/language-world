

# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Move robot's gripper above the stick
    #  2. Trap the stick with the robot's gripper
    #  3. Move the robot's gripper towards the thermos
    #  4. Pull the stick towards the target location
    # We need to put the robot's gripper above the stick before we can grab it, 
    # so move the robot's gripper to the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move("gripper above stick")
    # If the gripper is in front of the stick, try to grab it.
    if check("the robot's gripper is front aligned with the stick and the robot's gripper is open"):
        robot.trap("stick with gripper")
    # Move the robot's gripper towards the thermos to pull it with the stick
    if check("the robot's gripper is close to the stick and the thermos is not close to robot's gripper"):
        robot.move("gripper towards thermos")
    # Finally, pull the stick towards the target location.
    if check("the thermos is close to robot's gripper and the stick is below robot's gripper"):
        robot.pull("stick towards goal")