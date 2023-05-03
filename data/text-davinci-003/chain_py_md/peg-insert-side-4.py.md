

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Move gripper to side of peg
    #  2. Grab peg from the side 
    #  3. Insert peg into hole
    # To grab the peg, the gripper should be moved to the side of the peg.
    if check("the robot's gripper is not side aligned with peg"):
        robot.move("gripper to side of peg")
    # Once the gripper is roughly side-aligned with the peg, grasp the peg by 
    # lowering the gripper.
    if check("the robot's gripper is side aligned with peg and the robot's gripper is open"):
        robot.grab("peg from side")
    # Once the gripper has closed on the peg, insert the peg into the hole by 
    # pushing it with the gripper.
    if check("the robot's gripper is around peg"):
        robot.push("peg into hole")