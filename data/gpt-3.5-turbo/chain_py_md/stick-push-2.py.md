# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Move the stick towards the thermos
    #  4. Put the stick under the thermos
    #  5. Push the stick to move the thermos
    #  6. Move the stick back to the starting position
    #  7. Release the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # If the gripper is above the stick and open, grab the stick.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.grab("the stick")
    # If the gripper has the stick, move the stick to the thermos.
    if check("the robot's gripper is holding the stick and the stick is not near the thermos"):
        robot.move("the stick towards the thermos")
    # If the stick is near the thermos, put the stick under the thermos.
    if check("the stick is near the thermos and the robot's gripper is holding the stick"):
        robot.put("the stick under the thermos")
    # If the stick is under the thermos, push the stick to move the thermos.
    if check("the stick is under the thermos and the robot's gripper is holding the stick"):
        robot.push("the stick to move the thermos")
    # If the thermos has been moved to the goal, move the stick back to the starting position.
    if check("the thermos is at the goal and the stick is under the thermos and the robot's gripper is holding the stick"):
        robot.move("the stick to the starting position")
    # If the stick is back at the starting position, release the stick.
    if check("the stick is at the starting position and the robot's gripper is holding the stick"):
        robot.release("the stick")