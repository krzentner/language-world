# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    # 1. Put gripper above the stick
    # 2. Grab the stick with the gripper
    # 3. Position the stick against the thermos and push it
    # 4. Move the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # Once the gripper is above the stick, grab it.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.grab("stick")
    # Now that the stick is grabbed, move it to the thermos and push it.
    if check("the robot's gripper is around the stick"):
        #position the stick next to the thermos by moving the robot's arm
        robot.move("stick next to thermos")
        #push the thermos using the stick
        robot.push("stick into thermos")
    # Once the thermos has been pushed, move it to the target location.
    if check("the thermos has been pushed with the stick"):
        robot.push("thermos to goal")