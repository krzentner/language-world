
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# cap_twist_off: twist cap off of bottle
# def cap_twist_off(robot):
    if check("the robot's gripper is not near bottle cap"):
        robot.grab("bottle cap")
    if check("the robot's gripper is vertically aligned with bottle cap"):
        robot.twist("bottle cap counter-clockwise")
    if check("the bottle cap is nearly detached"):
        robot.pull("bottle cap away from bottle")