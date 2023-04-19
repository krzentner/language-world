if check("the robot's gripper is not near the wrench and the wrench is not horizontally aligned with the peg"):
        robot.move("gripper to wrench")
    if check("the robot's gripper is near the wrench and the wrench is not vertically aligned with the peg"):
        robot.lift("wrench")
    if check("the robot's gripper is vertically aligned with the peg and the wrench is not around the peg"):
        robot.place("wrench around peg")
    if check("the wrench is around the peg"):
        robot.tighten("wrench on peg")