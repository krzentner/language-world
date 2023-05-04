
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is not around the door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around the door handle"):
        robot.pull("away from door")

# button-press-side: slide the button to the right
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not right of the button"):
        robot.grab("the button")
    if check("the robot's gripper is right of the button"):
        robot.slide("the button right")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# pick-place-wall: pick up the puck and place it at the goal, starting near a wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck and the robot's gripper is not in front of the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.put("the gripper around the puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("the gripper around the puck")
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.place("the puck at the goal")

# peg-unstack-side: unstack the peg on the top
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with the top peg and the robot's gripper is not above the top peg"):
        robot.put("the gripper above the top peg")
    if check("the robot's gripper is vertically aligned with the top