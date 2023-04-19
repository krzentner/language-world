

if check("the robot's gripper is not horizontally aligned with the handle"):
    robot.put("gripper to the side of the handle")
if check("the robot's gripper is horizontally aligned with the handle and the robot's gripper is not near the handle"):
    robot.move("the gripper closer to the handle")
if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not above the handle"):
    robot.put("gripper above the handle")
if check("the robot's gripper is near the handle"):
    robot.push("down on the handle")