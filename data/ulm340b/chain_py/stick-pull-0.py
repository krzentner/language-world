
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the stick from the top
    #  3. Pull the thermos to the target location
    # We need to put the gripper above the stick before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.put("gripper above stick")
    # Once the gripper is lined up, just push down on the stick.
    if check("the robot's gripper is vertically aligned with stick"):
        robot.push("gripper down on stick")
    # Now that the stick is grasped, slide it to the goal.
    if check("the robot's gripper is around stick"):
        robot.slide("stick to the goal")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the stick from the top
    #  3. Push the thermos to the target location
    # We need to put the gripper above the stick before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.put("gripper above stick")
    # Once the gripper is lined up, just push down on the stick.
    if check("the robot's gripper is vertically aligned with stick"):
        robot.push("gripper down on stick")
    # Now that the stick is grasped, slide it to the goal.
    if check("the robot's gripper is around stick"):
        robot.slide("stick to the goal")

# stick-slide: grab the stick and use it to push the thermos to the target location
def stick_slide(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the stick from the top
    #  3. Slide the thermos to the target location
    # We need to put the gripper above the stick before we can grab it,
   