
    # Steps:
    #  1. Reach the wrench above the peg
    #  2. Push the wrench over the peg
    #  3. Line up the wrench with the peg
    #  4. Put the wrench around the peg
    # We need to reach the wrench with the gripper above the peg before we can put
    # it around.
    if check("the robot's gripper is not above the peg"):
        robot.reach("wrench to above the peg")
    # If the wrench is right of the peg and we can see it from the side, push it 
    # with the gripper over the peg.
    if check("the wrench is right of the peg and the robot's gripper is not forward aligned with the peg"):
        robot.push("wrench to the left")
    # We need to line the wrench up with the peg from the side, so that we can
    # slide it around.
    if check("the robot's gripper is forward aligned with the peg and the wrench is not horizontally aligned with the peg"):
        robot.align("wrench to peg")
    # Now that it's lined up, slide the wrench around the peg.
    if check("the robot's gripper is forward aligned with the peg and the wrench is horizontally aligned with the peg"):
        robot.place("wrench around peg")