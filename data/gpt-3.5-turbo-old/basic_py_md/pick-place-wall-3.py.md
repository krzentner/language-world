# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the puck is behind the wall and the robot's gripper is vertically aligned with the puck"):
        robot.move("gripper to the side of the wall")
    if check("the robot's gripper is next to the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")