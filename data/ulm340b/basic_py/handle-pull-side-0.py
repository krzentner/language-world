
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with the handle"):
        robot.pull("handle up")

# peg-unstack-side: unstack the peg by pulling to the side
def peg_unstack_side(robot):
    if check("the robot's gripper is not forward aligned with the peg"):
        robot.align("gripper to peg")
    if check("the robot's gripper is near peg and the peg is not below the robot's gripper"):
        robot.put("gripper around peg")
    if check("the robot's gripper is below the peg"):
        robot.pull("the peg right")

# pick-place-side: grab the puck from the side and hold it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not below the puck and the robot's gripper is not horizontally aligned with the puck"):
        robot.put("gripper to left of puck")
    if check("the robot's gripper is below the puck and the robot's gripper is left of the puck"):
        robot.grab("puck")
    if check("the robot's gripper is around puck"):
        robot.place("gripper at goal")

# pick-place-with-camera: find the puck and hold it at the target location
def pick_place_with_camera(robot):
    if check("the robot's gripper is not near puck"):
        robot.find("puck")
    if check("the robot's gripper is near puck"):
        pick_place(robot)

# pick-place-with-camera-side: find the puck and hold it at the target location
def pick_place_with_camera_side(robot):
    if check("the robot's gripper is not horizontally aligned with puck"):
        robot.find("puck")
    if check("the robot's gripper is horizontally aligned with puck"):
        pick_place_side(robot)

# push-with-camera: find the puck and push it to the target location
def push_with_camera(robot):
 