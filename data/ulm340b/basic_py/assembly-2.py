
    if check("the robot's gripper is not above wrench and wrench is not vertically aligned with the robot's gripper"):
        robot.put("gripper above wrench")
    if check("wrench is above robot's gripper and robot's gripper is open"):
        robot.put("gripper around wrench")
    if check("robot's gripper is around wrench and wrench is not below robot's gripper"):
        robot.pick("up wrench")
    if check("wrench is below robot's gripper and wrench is not vertically aligned with peg"):
        robot.place("gripper above peg")
    if check("wrench is vertically aligned with peg and wrench is not horizontally aligned with peg"):
        robot.rotate("wrench towards peg")
    if check("wrench is horizontally aligned with peg"):
        robot.insert("wrench around peg")

# drawer-close-topdown: push the drawer close from above
def drawer_close_topdown(robot):
    if check("the robot's gripper is not almost vertically aligned with drawer handle and the drawer handle is not above the robot's gripper"):
        robot.put("gripper above drawer handle")
    if check("drawer handle is above robot's gripper and robot's gripper is not close to drawer handle"):
        robot.place("gripper above drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

#drawer-open-topdown: pull the drawer open from above
def drawer_open_topdown(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle and the drawer handle is not above the robot's gripper"):
        robot.put("gripper above drawer handle")
    if check("drawer handle is above robot's gripper and robot's gripper is not close to drawer handle"):
        robot.place("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is forward aligned with drawer handle"):
        robot.pull("away from drawer")

#pick-place-topdown: grab the puck and hold it at the target location
def pick_place_topdown(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not vertically