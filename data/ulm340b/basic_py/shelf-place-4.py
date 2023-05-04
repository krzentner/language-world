
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")


# pick-place-with-camera: pick up the block and place it at the target location
def pick_place_with_camera(robot):
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.place("block at goal")

# place-red-in-green: pick up the red block and place it in the green cup
def place_red_in_green(robot):
    if check("the robot's gripper is not around red block and the robot's gripper is open"):
        robot.drop("gripper around red block")
    if check("the robot's gripper is near red block and the robot's gripper is open"):
        robot.close("gripper around red block")
    if check("the robot's gripper is above red block and the robot's gripper is closed"):
        robot.place("red block in green cup")

# shelf-place-no-camera: pick up the block and place it at the target location
def shelf_place_no_camera(robot):
    if check("the robot's gripper is not near puck and the robot's gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-under-camera: pick up the block and place it at the target location
def pick_place_under_camera(robot):
    if check("the robot's gripper is not near block and the robot's gripper is open"):
        robot.grab("block")
