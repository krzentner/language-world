# window-open: slide the window open to the left
# def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    
    # Check if the window is already open
    if check("the window is already open"):
        return
    
    # First, put gripper right of the window handle and above it
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.move("gripper to right of window handle")
        robot.put("gripper above window handle")
    
    # Push the window handle to slide the window open
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
        
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")