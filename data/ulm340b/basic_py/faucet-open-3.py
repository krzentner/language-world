
    if check("the faucet is left of the robot's gripper and the robot's gripper is not around faucet"):
        robot.put("gripper around faucet")
    if check("the robot's gripper is around faucet"):
        robot.twist("faucet to left")

# toggle-switch-off: flip the toggle switch to the off position
def toggle_switch_off(robot):
    if check("the toggle switch is right of the robot's gripper and the robot's gripper is not vertically aligned with the toggle switch"):
        robot.put("gripper above toggle switch")
    if check("the robot's gripper is above the toggle switch and the toggle switch is not vertically aligned with the robot's gripper"):
        robot.flip("toggle switch left")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not vertically aligned with the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# drawer-close-side: push the drawer close from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.move("gripper to side of drawer handle")
    if check("the robot's gripper is near the drawer handle"):
        robot.slide("drawer closed")
    if check("the robot's gripper is in front of the drawer handle"):
        robot.push("drawer closed harder")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above the puck and the robot's gripper is not around puck"):
        robot.close("gripper around puck")
    if check("the robot