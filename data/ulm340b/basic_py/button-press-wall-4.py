
    if check("the robot's gripper is not horizontally aligned with the button and the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("button")

# button-press-topdown-wall: push the button from above with a tall wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")

# peg-unstack-side: unstack the peg from the hole from the side
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg and the robot's gripper is not around the peg"):
        robot.put("the gripper around the peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is around the peg"):
        robot.pull("the peg out of the hole")

# peg-insert-vertical: insert the peg into the hole from above
def peg_insert_vertical(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("the gripper above the peg")
    if check("the robot's gripper is vertically aligned with the peg"):
        robot.push("the peg into the hole")

# pick-place-wall: pick up the puck and hold it at the target location with a wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.drop("the gripper around the puck")
    if check("the robot's gripper is around the puck"):
        robot.close("the gripper around the puck")
    if check("the puck is around the robot's gripper and the robot's gripper is closed"):
        robot.lift("the puck")
    if check("the robot's gripper is above the goal and the robot's gripper is above the puck"):