
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is around the door handle"):
        robot.push("the gripper towards the goal")

# block-stack-side: grab the block from the side and stack it on the target block
def block_stack_side(robot):
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is vertically aligned with the block and the robot's gripper is not right of the block"):
        robot.place("gripper above the block")
    if check("the robot's gripper is near the block"):
        robot.close("gripper around the block")
    if check("the robot's gripper is around the block"):
        robot.slide("the block to the goal")

# drawer-open-side: pull the drawer open from the side
def drawer_open_side(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle and the robot's gripper is not right of the drawer"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.close("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.pull("drawer handle")

# window-open-side: open the window from the side
def window_open_side(robot):
    if check("the robot's gripper is not vertically aligned with window handle and the robot's gripper is not right of the window handle"):
        robot.put("gripper above window handle")
    if check("the robot's gripper is vertically aligned with the window handle"):
        robot.close("gripper around window handle")
    if check("the robot's gripper is vertically aligned with the window handle and the gripper is closed"):
        robot.slide("the window to the left")

# lever-pull-side: pull the lever down from the side
