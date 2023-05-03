# push: slide the puck to the target location
def push(robot):
    # Steps:
    # 1. Put gripper above the puck
    # 2. Drop gripper around the puck
    # 3. Push the puck toward the target location
    # 4. Release the puck
    # First, put the gripper roughly above the puck to avoid bumping it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't dropped around the puck, drop it.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is around the puck, push the puck toward the target location.
    if check("the robot's gripper is around puck"):
        robot.slide("puck toward target")
    # Once the puck has reached the target location, release it by opening the gripper.
    if check("the puck has reached target location"):
        robot.open("gripper")