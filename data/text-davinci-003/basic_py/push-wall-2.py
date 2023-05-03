
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and the wall is in contact with the puck"):
        robot.push("the puck and wall together")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and the wall is past the puck"):
        robot.slide("puck to the goal")
```