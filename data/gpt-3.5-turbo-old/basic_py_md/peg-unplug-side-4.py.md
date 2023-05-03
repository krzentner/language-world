# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
   if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
   if check("the robot's gripper is not around peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
   if check("the peg is horizontally aligned with hole"):
        robot.grab("peg")
   if check("the robot's gripper is forward aligned with the peg and the peg is not aligned with the hole"):
        robot.move("gripper to left of peg")
   if check("the robot's gripper is around peg"):
        robot.pull("peg out of hole")