# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Put the gripper above the thermos
    #  4. Push the thermos to the goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the gripper is not holding the stick, grab it.
    if check("the robot's gripper is not holding the stick"):
        robot.grab("stick")
    # Put the gripper above the thermos.
    if check("the robot's gripper is not above the thermos"):
        robot.put("gripper above thermos")
    # Push the thermos to the goal with the stick.
    if check("the robot's gripper is above the thermos"):
        robot.push("the thermos towards the goal with the stick")