# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Move gripper above hammer
    #  2. Grab hammer handle
    #  3. Move gripper above nail
    #  4. Lower gripper onto nail
    #  5. Lift gripper back up
    #  6. Place hammer down
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.place("gripper above hammer")
    # Next, grab the hammer handle.
    if check("the robot's gripper is not around hammer handle and the robot's gripper is above the hammer"):
        robot.grab("hammer handle")
    # Move the gripper above the nail.
    if check("the robot's gripper is not above the nail and the robot's gripper is around hammer handle"):
        robot.place("gripper above nail")
    # Lower the gripper onto the nail and hit the nail.
    if check("the robot's gripper is above the nail and the robot's gripper is around hammer handle"):
        robot.lower("gripper")
        robot.hit("nail")
        robot.raise("gripper")
    # Lastly, place the hammer down.
    if check("the robot's gripper is above the hammer and the robot's gripper is around hammer handle"):
        robot.drop("hammer")