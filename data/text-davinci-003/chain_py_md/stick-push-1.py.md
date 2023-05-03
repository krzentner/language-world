

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Put the stick down in front of the thermos
    #  4. Push the thermos with the stick towards the goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the stick becomes left of the gripper, go back to putting the gripper
    # above the stick.
    # Because the stick is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    # If the gripper can be seen forward aligned (as seen from in front) with
    # the stick, put the stick down in front of the thermos.
    if check("the robot's gripper is forward aligned with the stick"):
        robot.put("stick in front of thermos")
    # Once the stick is in front of the thermos, push towards the goal.
    if check("the stick is in front of the thermos"):
        robot.push("thermos towards goal with stick")