if check("the robot's gripper is not above the puck and the wall is not blocking the path"):
        robot.place("gripper above puck")
    if check("the gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the gripper is above the puck and the robot's gripper is closed"):
        robot.lift("puck off surface")
    if check("the robot's gripper is not near the wall" and check("the gripper is above the goal")):
        robot.move("gripper to position")
    if check("the gripper is close to the wall"):
        robot.slide("gripper under wall")
    if check("the gripper is beyond the wall and the puck is over the goal"):
        robot.place("puck on the goal")
