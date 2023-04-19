

Steps:
  1. Put gripper near the stick
  2. Grab the stick with the gripper
  3. Move the stick towards the thermos
  4. Push the thermos towards the target location

# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper near the stick
    #  2. Grab the stick with the gripper
    #  3. Move the stick towards the thermos
    #  4. Push the thermos towards the target location
    # First, put the gripper near the stick.
    if check("the robot's gripper is not near the stick"):
        robot.put("gripper near stick")
    # Once the gripper is near the stick, we should be able to grab it.
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.grab("stick")
    # After the gripper has the stick, move the stick towards the thermos.
    if check("the robot's gripper is holding the stick"):
        robot.move("stick towards thermos")
    # Once the stick is near the thermos, we can push the thermos towards the
    # target location.
    if check("the stick is near the thermos"):
        robot.push("thermos towards target location")