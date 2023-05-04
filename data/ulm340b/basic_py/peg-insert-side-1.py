
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.place("peg above hole")
    if check("the peg is above the hole and the robot's gripper is around peg"):
        robot.move("the peg down into the hole")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.place("peg above hole")
    if check("the peg is above the hole and the robot's gripper is around peg"):
        robot.move("the peg down into the hole")

# pick-out-of-hole: grab the peg and pull it out from the hole
def pick_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg and the peg is not pulled out"):
        robot.pull("peg out of the hole")

# door-lock: push the door closed and lock it
def door_lock(robot):
    if check("the robot's gripper is not vertically aligned with door"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door and the robot's gripper is not near door"):
        robot.push("door shut")
    if check("the door is not shut"):
        robot.close("door")
    if check("the door is shut and the robot's gripper is near door handle"):
        robot.close("door lock")
    if check("the door is shut and the robot's gripper is not vertically aligned with door"):
