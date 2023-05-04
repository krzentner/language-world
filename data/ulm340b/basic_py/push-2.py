
    if check("the robot's gripper is not almost vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is almost vertically aligned with puck and the puck is not almost horizontally aligned with goal"):
        robot.push("puck to goal")
    if check("the puck is not almost horizontally aligned with goal and the puck is not near goal"):
        robot.push("puck harder to goal")
    if check("the puck is near goal"):
        robot.push("puck really hard to goal")

# shelf-place: place the shelf at the target location
def shelf_place(robot):
    if check("the robot's gripper is not near the top-middle of the shelf"):
        robot.put("gripper above top-middle of shelf")
    if check("the robot's gripper is near the top-middle of the shelf and the robot's gripper is open"):
        robot.close("gripper around top-middle of shelf")
    if check("the robot's gripper is around the top-middle of the shelf"):
        robot.move("shelf to goal")
    if check("the shelf is not vertically aligned with goal"):
        robot.put("shelf above goal")
    if check("the shelf is vertically aligned with goal"):
        robot.drop("shelf at goal")

# door-close: pull the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.pull("door closed")

# valve-turn: turn the valve clockwise
def valve_turn(robot):
    if check("the robot's gripper is not near the valve handle"):
        robot.put("gripper near valve handle")
    if check("the robot's gripper is near the valve handle and the robot's gripper is open"):
        robot.close("gripper around valve handle")
    if check("the robot's gripper is around the valve handle and the robot's gripper is facing right"):
        robot.turn("valve clockwise")
    if check("the robot's gripper is around the valve handle and the robot's gripper is facing left"):
        robot.turn("valve harder clockwise")
    if check("the