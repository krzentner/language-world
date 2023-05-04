

The robot must begin the task with the handle of the faucet on its left.

After you finish writing your program, save it under `/files`.
Then, enter `run(faucet_open)` into the console. If all went well, the faucet will turn to the left and the tap will open!
""",
    "data": {
        "tasks": {
            "push": {
                "source": """
# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")
"""
            },
            "window-close": {
                "source": """
# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle