# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    # 1. Put the gripper near the door knob
    # 2. Turn the gripper to grab the knob
    # 3. Push the door towards the target location
    # First, we need to move the gripper close to the door knob. 
    if check("the robot's gripper is not near the door knob"):
        robot.move("gripper to door knob")
    # Next, turn the gripper to grab the knob. 
    if check("the robot's gripper is near the door knob and the robot's gripper is not turning to grab the knob"):
        robot.turn("gripper to grab knob")
    # Finally, we can push the door towards the target location. 
    if check("the robot's gripper is grabbing the knob"):
        robot.push("door towards target location")