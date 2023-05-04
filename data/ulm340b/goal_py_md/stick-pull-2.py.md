

and then define the function that starts with the same words "stick-pull:".
*/
// Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.
// Here's some code that demonstrates how the robot can do a variety of tasks:
//
// ```
// # button-press-topdown: push the button down from above
// def button_press_topdown(robot):
//     # Steps:
//     #  1. Line up the gripper as viewed from above
//     #  2. Push down on the button from the top
//     # Because this is "topdown", we just need to line up the gripper from above.
//     # Line up the robot's gripper from above.
//     if check("the robot's gripper is not vertically aligned with button"):
//         robot.move_gripper("vertically aligned with the button", close_gripper=True)
//     # Now that the gripper is lined up, just push down on the button.
//     if check("the robot's gripper is vertically aligned with button"):
//         robot.move_gripper("near the button")
//
// # drawer-close: push the drawer close
// def drawer_close(robot):
//     # Steps:
//     #  1. Put gripper roughly around the drawer handle
//     #  2. Push the drawer closed
//     # If the gripper is not near the drawer handle, move it to the drawer
//     # handle.
//     # We don't need to be careful about the direction, since the drawer is large
//     # and we're just pushing it (unlike when opening the drawer).
//     if check("the robot's gripper is not near the drawer handle"):
//         robot.move_gripper("near the drawer handle")
//     # If the drawer is aligned with the gripper as seen from in front, we can
//     # push the drawer closed.
//     if check("the robot's gripper is forward aligned with drawer handle"):
//         robot.move_gripper("around the drawer handle")
//
// # drawer-open: pull the drawer open
// def drawer_open(robot):
//     # Steps:
//     #  1. Put gripper above drawer handle
//     #  2. Drop gripper around drawer handle
//     #  3. Pull open the drawer
//     # We need to put the gripper above the drawer handle before we can grab it,
//     # because of the angle of the robot