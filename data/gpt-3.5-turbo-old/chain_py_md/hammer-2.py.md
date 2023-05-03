# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put the gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Position the hammer above the nail
    #  4. Lower the hammer onto the nail
    #  5. Raise the hammer back up
    #  6. Release the hammer
    
    # First, put the gripper above the hammer
    if check("the robot's gripper is not above the hammer"):
        robot.place("gripper above hammer")
    # Once the gripper is above the hammer, grab it
    if check("the robot's gripper is above the hammer and the gripper is open"):
        robot.grab("the hammer handle")
    # After the gripper is around the hammer handle, position the hammer above the nail
    if check("the robot's gripper is around the hammer handle and the hammer is not above the nail"):
        robot.position("hammer above the nail")
    # Lower the hammer onto the nail
    if check("the hammer is above the nail"):
        robot.push("hammer onto the nail")
    # Raise the hammer back up
    if check("the hammer is on the nail and the hammer is not high enough"):
        robot.move("the hammer up")
    # Finally, release the hammer
    if check("the hammer is high enough and the gripper is around the hammer handle"):
        robot.release("the hammer")