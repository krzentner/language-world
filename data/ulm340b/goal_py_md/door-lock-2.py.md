


Your program should end in a line beginning with ```robot.move_gripper()``` that makes the robot close the door.

Write your code below, starting with the line of text:
# door-lock: turn the dial on the door
def door_lock(robot):

"""

# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")

    if check("the robot's gripper is vertically aligned with the dial"):
        robot.move_gripper("left of the door handle")

if __name__ == '__main__':
    world = make_world()
    world.load_settings()
    world.populate_from_default()
    world.reset_scene()

    test_functions = [
        ("drawer-close", drawer_close),
        ("reach", reach),
        ("peg-insert-side", peg_insert_side),
        ("push", push),
        ("window-close", window_close),
        ("button-press-topdown", button_press_topdown),
        ("pick-place", pick_place),
        ("window-open", window_open),
        ("drawer-open", drawer_open),
        ("door-open", door_open),
        ("door-lock", door_lock)
    ]

    # Test functions one by one.
    for function_name, function in test_functions:
        print("Testing", function_name, "...")
        test_function(world, function)


# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the window