# Steps:
    #  1. Put gripper near the peg
    #  2. Grab the peg
    #  3. Move the peg to the hole from the side
    #  4. Release the peg into the hole
    
    # First, we need to move the gripper near the peg
    if check("the robot's gripper is not near the peg"):
        robot.move("gripper near the peg")
    
    # Once the gripper is near the peg, we can grab it.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.grab("peg")
    
    # Now we can move the gripper and peg to the hole from the side
    if check("the robot's gripper is holding the peg and the peg is not near the hole"):
        robot.move("gripper and peg near the hole from the side")
    
    # Finally, we can release the peg into the hole
    if check("the robot's gripper is holding the peg and the peg is near the hole"):
        robot.release("peg into the hole")