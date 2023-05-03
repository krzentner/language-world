
    if check("the robot's gripper is not above the door lock dial"):
        robot.place("gripper above the door lock dial")
    if check("the robot's gripper is not laying flat against the door lock dial"):
        robot.align("gripper to door lock dial") 
    if check("the robot's gripper is laying flat against the door lock dial and pointing to the desired position on the dial"):
        robot.turn("dial to desired position")