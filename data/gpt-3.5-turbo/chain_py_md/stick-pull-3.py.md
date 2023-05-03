# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos
    #  4. Use the stick to pull the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the stick isn't below the gripper as seen from above, move the gripper
    # above the stick.
    if check("the stick is not below the robot's gripper and the robot's gripper is not horizontally aligned with the stick"):
        robot.grab("stick")
    # Once the gripper is around the stick, we want to line the stick up with the
    # thermos to drag it to the goal.
    if check("the robot's gripper is around the stick and the stick is not horizontally aligned with the thermos"):
        robot.put("stick near thermos")
    # Now that the stick is near the thermos, we can use it to drag it to the goal.
    if check("the stick is horizontally aligned with the thermos"):
        robot.drag("thermos to goal using the stick")