
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("peg at goal")

# pull-out-of-hole: pull the peg out of the hole
def pull_out_of_hole(robot):
    if check("the robot's gripper is not near peg"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and peg is in hole"):
        robot.lift("peg out of hole")
    if check("the robot's gripper is above peg"):
        robot.place("peg at goal")

# lift-out-of-hole: push down on the peg, and lift it out of the hole
def lift_out_of_hole(robot):
    if check("the robot's gripper is not near peg"):
        robot.grab("peg")
    if check("the robot's gripper is not below peg"):
        robot.push("down on peg")
    if check("the robot's gripper is below peg"):
        robot.lift("peg out of hole")
    if check("the robot's gripper is above peg"):
        robot.place("peg at goal")

# toggle-switch-topdown: push the button down to toggle the switch down
def toggle_switch_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the switch handle"):
        robot.put("gripper above switch handle")
    if check("the robot's gripper is vertically aligned with the switch handle and the robot's gripper is open"):
        robot.put("gripper around switch handle")
    if check("the robot's gripper is vertically aligned with the switch handle and the robot's gripper is not near switch"):
        robot.push("gripper into switch handle")
    if check("the robot's gripper is near the switch handle"):
        robot.push("switch handle down