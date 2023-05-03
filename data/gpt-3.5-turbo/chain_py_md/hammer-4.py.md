# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put the gripper above the hammer
    #  2. Grab the handle of the hammer
    #  3. Turn the hammer to face the nail head
    #  4. Move the hammer down to hit the nail
    #  5. Release the handle
    
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.place("gripper above hammer")
    # If the gripper isn't around the handle of the hammer, put it around the handle.
    if check("the robot's gripper is not around hammer handle and the robot's gripper is open"):
        robot.drop("gripper around hammer handle")
    # Turn the hammer handle until the head faces the nail.
    if check("the hammer head is not facing the nail"):
        robot.align("hammer head to nail")
    # If the gripper is around the handle and the hammer is aligned with the nail, move it down to hit the nail.
    if check("the robot's gripper is around hammer handle and the hammer head is facing the nail"):
        robot.push("hammer down onto nail")
    # If the hammer is hitting the nail, release the handle.
    if check("the robot's gripper is holding the hammer and the hammer is hitting the nail"):
        robot.release("hammer handle")