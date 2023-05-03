# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not near the puck on the table"):
        robot.reach("to puck on table")
    if check("the robot's gripper is above and open near the puck on the table"):
        robot.close("gripper around puck")
    if check("the robot's gripper is holding the puck"):
        robot.move("gripper to the left of the wall")
    if check("the robot's gripper is not near the wall"):
        robot.reach("to goal")
    if check("the robot's gripper is above and closed near the goal"):
        robot.open("gripper at goal")