
    if check("the ball is not vertically aligned with the robot's gripper"):
        robot.grab("basketball")
    if check("the ball is vertically aligned with the robot's gripper"):
        robot.place("ball above hoop")
    if check("the ball is vertically aligned with the robot's gripper and the ball is above the hoop"):
        robot.put("ball into hoop")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not forward aligned with button"):
        robot.grab("button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("into button")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# pick-place-wall: pick up the puck and place it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not almost vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is almost vertically aligned with the puck and the robot's gripper is open"):
        robot.put("gripper around puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is closed"):
        robot.put("puck at goal")

# push-wall: push the puck against the wall until it reaches the target location
def push_wall(robot):
    if check("the robot's gripper is not almost vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is almost vertically aligned with the puck and the robot's gripper is open"):
        robot.put("gripper around puck")
  