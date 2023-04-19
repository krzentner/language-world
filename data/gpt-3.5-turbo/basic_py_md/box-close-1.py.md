# box-close: pick up the box lid and place it on the box
# def box_close(robot):
def box_close(robot):
    if check("the robot's gripper is not above the box lid"):
        robot.reach("to the box lid")
        robot.place("gripper above the box lid")
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around the box lid")
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.close("gripper around the box lid")
    if check("the robot's gripper is above the box and the robot's gripper is closed"):
        robot.place("the box lid on the box") 

# Check function to provide context to the states
def check(state):
    print(f"Checking if {state}")
    return True    # Replace with actual code to check if the state is true