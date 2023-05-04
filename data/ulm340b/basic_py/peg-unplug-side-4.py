
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("peg is forward aligned with the robot's gripper and the peg is left of the robot's gripper"):
        robot.pull("peg out of hole")

# pick-place-side: pick the puck from the left and place it on the target location
def pick_place_side(robot):
    if check("the robot's gripper is not right of puck"):
        robot.move("gripper to right of puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to near puck")
    if check("the robot's gripper is right of puck and the robot's gripper is not near puck"):
        robot.move("gripper to