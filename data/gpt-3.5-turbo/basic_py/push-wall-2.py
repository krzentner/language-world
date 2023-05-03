If check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("the gripper into the puck")
    if check("the gripper is near the wall and the puck is below the robot's gripper"):
        robot.align("the puck to the gap in the wall")
    if check("the puck is aligned with the gap in the wall"):
        robot.slide("the puck through the gap and towards the goal")
    if check("the puck has reached the goal"):
        robot.release("the puck at the goal")