If check("the robot's gripper is not above the puck and the wall is blocking direct access to the puck"):
        robot.move("gripper to side of puck, away from the wall")
    if check("the robot's gripper is not around the puck and the gripper is open"):
        robot.put("gripper around puck")
    if check("the gripper is around the puck and the puck is not high enough to clear the wall"):
        robot.lift("puck over wall")
    if check("the gripper is holding the puck clear of the wall and the gripper is open"):
        robot.close("gripper around puck")
    if check("the gripper is holding the puck and the gripper is above the target location"):
        robot.place("puck at goal")