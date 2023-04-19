
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# cup-stacking: stack the cup on top of another cup
# def cup_stacking(robot):
    if check("robot gripper is not above the cup"):
        robot.place("gripper above cup")
    if check("the robot's gripper is above the cup and the cup is not next to other cup"):
        robot.move("cup to be next to other cup")
    if check("the cup is next to other cup and the robot's gripper is almost vertically aligned with the cup"):
        robot.adjust("align the gripper vertically with cup")
    if check("the robot's gripper is vertically aligned with the cup and the robot's gripper is open"):
        robot.drop("gripper around cup")
    if check("the robot's gripper is near the cup"):
        robot.put("cup on top of other cup")
    else:
        print("Task done.")