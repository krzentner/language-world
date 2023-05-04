
    if check("the robot's gripper is not above the coffee machine"):
        robot.put("gripper above coffee machine")
    if check("the robot's gripper is vertically aligned with coffee machine"):
        robot.push("down on coffee machine")

# pick-place-wall: pick up the puck and hold it at the target location on the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# plug-socket: plug the plug into the wall socket
def plug_socket(robot):
    if check("the robot's gripper is not vertically aligned with plug"):
        robot.put("gripper above plug")
    if check("the robot's gripper is vertically aligned with plug and the robot's gripper is not in the plug"):
        robot.insert("gripper into plug")
    if check("the robot's gripper is forward aligned with plug"):
        robot.align("plug with socket")
    if check("plug is forward aligned with socket"):
        robot.insert("plug into socket")

# peg-unstack-side: unstack the pegs from the side
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with the target peg and the robot's gripper is left of the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the target peg"):
        robot.insert("gripper around peg")
    if check("the robot's gripper is forward aligned with the peg"):
        robot.lift("peg up")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not above the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is