if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the gripper cannot move straight down to reach the puck"):
        robot.move("gripper to the side of the wall")
    if check("the gripper can move straight down to grasp the puck and the gripper is open"):
        robot.drop("gripper around puck")
    if check("the gripper has grasped the puck and can move it above the wall"):
        robot.lift("gripper and puck above the wall")
    if check("the gripper is above the target location and can drop the puck"):
        robot.place("puck at goal")