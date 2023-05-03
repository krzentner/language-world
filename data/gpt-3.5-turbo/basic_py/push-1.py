if check("the puck is not between the robot's gripper and the goal"):
        robot.move("gripper to above the puck")
    if check("the gripper is not around the puck"):
        robot.grab("puck")
    if check("the gripper is around the puck and the gripper is not forward aligned with the goal"):
        robot.align("puck to goal")
    if check("the gripper is forward aligned with the goal and the gripper is not above the goal"):
        robot.move("gripper above the goal")
    if check("the gripper is above the goal and the puck is not at the goal"):
        robot.push("puck to goal")