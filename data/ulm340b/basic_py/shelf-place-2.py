
    if check("the robot's gripper is not near the block and the robot's gripper is not above the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is not above the block"):
        robot.grab("block")
    if check("the robot's gripper is near block and the robot's gripper is closed"):
        robot.move("block over goal")
    if check("the robot's gripper is above goal"):
        robot.drop("block on goal")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    if check("the robot's gripper is not above the puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("puck to goal")

# drawer-close-with-camera: push the drawer closed
def drawer_close_with_camera(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not forward aligned with drawer handle"):
        robot.move("gripper into drawer handle")
    if check("the robot's gripper is near drawer handle"):
        robot.move("gripper back towards drawer")

# drawer-open-with-camera: pull the drawer open
def drawer_open_with_camera(robot):
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with drawer handle and the robot's gripper is not open"):
        robot.open("gripper")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is open"):
        robot.move("gripper into drawer handle")