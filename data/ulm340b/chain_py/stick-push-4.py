
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Push gripper into thermos
    #  4. Slide thermos to goal
    # First, put the gripper above stick, so that we don't bump it while trying
    # to grab it.
    if check("the robot's gripper is not above stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is around the stick and the stick is near the thermos, we
    # can probably push the thermos by moving the gripper.
    if check("the robot's gripper is around stick and the stick is near thermos"):
        robot.move("gripper into thermos")
    # If the gripper is near the thermos and the stick is forward of the
    # gripper, we've trapped the thermos between the gripper and the stick.
    # We can now slide the thermos to the goal.
    if check("the robot's gripper is near thermos and the stick is forward of robot's gripper"):
        robot.slide("thermos to goal")

# lever-push: grab the lever and push the box into the target location
def lever_push(robot):
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Rotate lever away from box
    #  4. Slide lever into box
    #  5. Rotate lever into box
    # First, put the gripper above lever, so that we don't bump it while trying
    # to grab it.
    if check("the robot's gripper is not above lever"):
        robot.place("gripper above lever")
    # If the gripper isn't around the lever, put it around the lever.
    if check("the robot's gripper is not around lever and the robot's gripper is open"):
        robot.drop("gripper around lever")
    # If the