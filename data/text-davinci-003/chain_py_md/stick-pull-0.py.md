

Steps:
1. Put gripper above the stick
2. Grab the stick with the gripper
3. Move the stick to the thermos
4. Put the end of the stick in the notch of the thermos
5. Pull the thermos to the target location

If check("the robot's gripper is not vertically aligned with the stick"):
    robot.put("gripper above stick")

If check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around stick"):
    robot.grab("stick")

If check("the robot's gripper is around stick and the end of the stick is not near the notch on the thermos"):
    robot.move("stick to near the notch of the thermos")

If check("the end of the stick is near the notch of the thermos and the end of the stick is not in the notch"):
    robot.place("end of the stick in the notch of the thermos")

If check("the end of the stick is in the notch of the thermos"):
    robot.pull("the thermos to the target location")