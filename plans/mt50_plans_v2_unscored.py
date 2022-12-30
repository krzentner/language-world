# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")


# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")


# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck", open_gripper=True)
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.move_gripper("around the puck", close_gripper=True)
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")


# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.move_gripper("around the door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")


# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # Once the gripper is around the drawer handle, we can just pull the drawer
    # open.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")


# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("around the drawer handle")


# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")


# peg-insert-side: insert the peg into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", open_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")


# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move_gripper("right of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")


# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")


# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Start pulling against the door handle to open the door
    #  3. Pull the door open harder
    # If the robot's gripper is not left of the door handle, we should move the
    # gripper near the door handle to start pulling
    if check("the robot's gripper is not left of the door handle and the robot's gripper is not near the door handle"):
        robot.move_gripper("left of the door handle")
    # If the robot's gripper is near the door handle we can probably pull the
    # door open now by moving the gripper right.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("forward aligned with the door handle")
    # If the robot's gripper is starting to be in front of the door handle,
    # pull harder.
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("right of the door handle")


# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper horizontally aligned with drawer handle
    #  2. Pull open the drawer
    # If the gripper is not aligned with the drawer handle, move it to the
    # drawer handle.
    if check("the robot's gripper is not horizontally aligned with drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")
    # If the gripper is aligned with the drawer handle, pull the drawer open.
    if check("the robot's gripper is horizontally aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")


# assembly: put the wrench around the peg
def assembly(robot):
    # Steps:
    #  1. Put the wrench above the peg
    #  2. Put the wrench around the peg
    #  3. Turn the wrench
    # First, put the wrench above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", open_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")


# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Hold the ball
    #  2. Move the ball to the hoop
    #  3. Put the ball in the hoop
    # First, make sure the robot is holding the ball.
    if check("the robot is not holding the ball"):
        robot.move_gripper("around the ball")
    # If the robot is holding the ball, move it to the hoop.
    if check("the robot is holding the ball"):
        robot.move_gripper("above the hoop")
    # If the robot is above the hoop, put the ball in the hoop.
    if check("the robot is above the hoop"):
        robot.move_gripper("around the hoop")


# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # If the button is left of the gripper, move the gripper to the left.
    if check("the robot's gripper is vertically aligned with button and the button is left of the robot's gripper"):
        robot.move_gripper("left of the button")
    # If the button is right of the gripper, move the gripper to the right.
    if check("the robot's gripper is vertically aligned with button and the button is right of the robot's gripper"):
        robot.move_gripper("right of the button")


# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Push the button
    # If the robot's gripper is not in front of the button, move it there.
    if check("the robot's gripper is not in front of the button"):
        robot.move_gripper("in front of the button")
    # If the gripper is in front of the button, push the button.
    if check("the robot's gripper is in front of the button"):
        robot.move_gripper("near the button")


# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Line up the gripper with the button
    #  2. Push down on the button from the front
    # First, line up the gripper with the button.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # If the button is left of the gripper, move the gripper left.
    if check("the robot's gripper is forward aligned with the button and the button is left of the robot's gripper"):
        robot.move_gripper("left of the button")
    # If the button is right of the gripper, move the gripper right.
    if check("the robot's gripper is forward aligned with the button and the button is right of the robot's gripper"):
        robot.move_gripper("right of the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")


# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button from the top
    # Because we're looking at the coffee machine from the front, we need to
    # line up the gripper from the front.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("forward aligned with the button")
    # If the gripper is lined up with the button, push down on the button.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")


# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around the mug
    #  3. Pull the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug", open_gripper=True)
    # If the mug becomes left of the gripper, go back to putting the gripper
    # above the mug.
    if check("mug is not left of the robot's gripper and mug is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the mug", close_gripper=True)
    # As long the gripper is still mostly around the mug and the mug isn't lined
    # up with the target location, line up the mug with the target location.
    if check("the robot's gripper is forward aligned with the mug and the mug is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the mug is lined up with the target location, pull it there.
    if check("the mug is horizontally aligned with the target location"):
        robot.move_gripper("above the mug")


# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Grab the mug
    #  2. Move the mug to the target location
    # If the robot's gripper is not around the mug, move the gripper around the
    # mug.
    if check("the robot's gripper is not around the mug"):
        robot.move_gripper("around the mug")
    # If the robot's gripper is around the mug, move the mug to the target
    # location.
    if check("the robot's gripper is around the mug"):
        robot.move_gripper("to the target location")


# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Move the gripper to the cube
    #  2. Pick up the cube
    #  3. Move the gripper to the target bin
    #  4. Drop the cube
    # If the gripper is not near the cube, move the gripper near the cube.
    if check("the robot's gripper is not near the cube"):
        robot.move_gripper("near the cube")
    # If the gripper is near the cube, pick up the cube.
    if check("the robot's gripper is near the cube"):
        robot.move_gripper("around the cube")
    # If the gripper is around the cube, move the gripper to the target bin.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("near the target bin")
    # If the gripper is near the target bin, drop the cube.
    if check("the robot's gripper is near the target bin"):
        robot.move_gripper("around the target bin")


# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial
    # If the robot's gripper is not around the dial, move it around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # If the robot's gripper is around the dial, turn the dial.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turn the dial")


# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", open_gripper=True)
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the wrench", close_gripper=True)
    # As long the gripper is still mostly around the wrench and the wrench isn't
    # lined up with the hole, line up the wrench with the hole.
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # If the wrench is lined up with the hole to the side, pull it off.
    if check("wrench is horizontally aligned with hole"):
        robot.move_gripper("above the wrench")


# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("around the drawer handle")


# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper right of faucet handle
    #  2. Start turning the faucet handle to the left
    #  3. Turn the faucet handle to the left harder
    # If the robot's gripper is not vertically aligned with the faucet handle,
    # we should move the gripper near the faucet handle to start turning
    if check("the robot's gripper is not vertically aligned with faucet handle and the robot's gripper is below the faucet handle"):
        robot.move_gripper("right of faucet handle")
    # If the robot's gripper is near the faucet handle we can probably turn the
    # faucet open now by moving the gripper left.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("forward aligned with the faucet handle")
    # If the robot's gripper is starting to be in front of the faucet handle,
    # turn harder.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")


# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper right of the faucet handle
    #  2. Start turning the faucet right
    #  3. Turn the faucet right harder
    # If the faucet handle is left of the robot's gripper, we should move the
    # gripper near the faucet handle to start turning
    if check("the faucet handle is left of the robot's gripper and the robot's gripper is not near the faucet handle"):
        robot.move_gripper("right of the faucet handle")
    # If the robot's gripper is near the faucet handle we can probably turn the
    # faucet right now by moving the gripper right.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("forward aligned with the faucet handle")
    # If the robot's gripper is starting to be in front of the faucet handle,
    # turn harder.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.move_gripper("right of the faucet handle")


# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put hammer above the nail
    #  2. Hit the nail with the hammer
    # Because the hammer is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is not forward aligned with the hammer"):
        robot.move_gripper("forward aligned with the hammer", close_gripper=True)
    # If the hammer is left of the gripper, go back to putting the gripper
    # above the hammer.
    # Because the hammer is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("hammer is not left of the robot's gripper and hammer is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the hammer", close_gripper=True)
    # As long the gripper is still mostly around the hammer and the hammer isn't
    # lined up with the nail, line up the hammer with the nail.
    if check("the robot's gripper is forward aligned with the hammer and hammer is not vertically aligned with nail"):
        robot.move_gripper("vertically aligned with the nail")
    # If the hammer is lined up with the nail to the side, hit the nail.
    if check("hammer is vertically aligned with nail"):
        robot.move_gripper("above the hammer")


# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Grab the box lid
    #  2. Move the box lid to the box
    #  3. Place the box lid on the box
    # If the gripper is not around the box lid, move the gripper around the box
    # lid.
    if check("the robot's gripper is not around the box lid"):
        robot.move_gripper("around the box lid")
    # If the gripper is around the box lid, pick it up.
    if check("the robot's gripper is around the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper is above the box lid, move the gripper to the box.
    if check("the robot's gripper is above the box lid"):
        robot.move_gripper("above the box")


# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper left of the handle
    #  2. Push down on the handle from the side
    # If the robot's gripper is not left of the handle, we should move the
    # gripper near the handle to start pushing
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # If the robot's gripper is near the handle we can probably push down on
    # the handle now by moving the gripper down.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("down")


# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # If the handle is left of the gripper, go back to putting the gripper above
    # the handle.
    if check("the handle is left of the robot's gripper"):
        robot.move_gripper("vertically aligned with the handle", open_gripper=True)
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("near the handle")


# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Pull up the handle
    # If the robot's gripper is not above the handle, move it above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the robot's gripper is above the handle, pull up the handle.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("above the handle")


# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Pull up on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", open_gripper=True)
    # If the handle is left of the gripper, go back to putting the gripper
    # above the handle.
    if check("the robot's gripper is vertically aligned with the handle and the handle is left of the robot's gripper"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # If the handle is aligned with the gripper from the front, pull up on the
    # handle.
    if check("the robot's gripper is vertically aligned with the handle and the handle is forward aligned with the robot's gripper"):
        robot.move_gripper("above the handle")


# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Rotate the lever up
    # If the robot's gripper is not above the lever, move the gripper above the
    # lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever")
    # If the robot's gripper is above the lever, rotate it up.
    if check("the robot's gripper is vertically aligned with the lever"):
        robot.move_gripper("above the lever")


# peg-unplug-side: pull the peg out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out of the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", open_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")


# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper in front of the peg
    #  2. Grab the peg
    #  3. Move the gripper above the peg
    #  4. Move the gripper to the target location
    # First, put the gripper in front of the peg.
    if check("the robot's gripper is not forward aligned with the peg"):
        robot.move_gripper("forward aligned with the peg")
    # If the peg is in front of the gripper, grab the peg.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("around the peg")
    # If the gripper is around the peg, move the gripper above the peg.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the peg")
    # If the gripper is above the peg, move the gripper to the target location.
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("to the target location")


# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck
    #  3. Move the gripper to the target location
    #  4. Drop the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck", open_gripper=True)
    # If the gripper is not around the puck, grab the puck.
    if check("the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck")
    # Move the gripper to the target location.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("forward aligned with the target")
    # Drop the puck.
    if check("the robot's gripper is forward aligned with the target"):
        robot.move_gripper("vertically aligned with the target", close_gripper=True)


# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Turn the dial to the right
    #  3. Turn the dial to the left
    #  4. Turn the dial to the right
    # If the robot's gripper is not vertically aligned with the dial, move it
    # above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the robot's gripper is vertically aligned with the dial, turn the dial
    # to the right.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.move_gripper("right of the dial")
    # If the robot's gripper is right of the dial, turn the dial to the left.
    if check("the robot's gripper is right of the dial"):
        robot.move_gripper("left of the dial")


# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Pick up the puck
    #  2. Move the puck in front of the wall
    #  3. Move the puck to the target location
    #  4. Put the puck down
    # First, pick up the puck.
    if check("the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # If the puck is not in front of the wall, move it in front of the wall.
    if check("the puck is not in front of the wall"):
        robot.move_gripper("in front of the wall")
    # If the puck is in front of the wall, move it to the target location.
    if check("the puck is in front of the wall"):
        robot.move_gripper("at the target location")
    # If the puck is at the target location, put it down.
    if check("the puck is at the target location"):
        robot.move_gripper("above the puck", open_gripper=True)


# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Push the plate sideways to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate", open_gripper=True)
    # If the plate is left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long the gripper is still mostly around the plate and the plate isn't
    # lined up with the target location, line up the plate with the target
    # location.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the plate is lined up with the target location to the side, insert it.
    if check("plate is horizontally aligned with the target location"):
        robot.move_gripper("above the plate")


# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate", open_gripper=True)
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long the gripper is still mostly around the plate and the plate isn't lined
    # up with the target location, line up the plate with the target location.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the plate is lined up with the target location to the side, insert it.
    if check("plate is horizontally aligned with the target location"):
        robot.move_gripper("above the plate")


# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper right of the plate
    #  2. Push the plate back
    # If the gripper is not near the plate, move it near the plate.
    if check("the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate")
    # If the gripper is near the plate, push it back.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("right of the plate")


# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Line up the gripper with the plate
    #  2. Slide the plate back
    # First, line up the gripper with the plate.
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # If the plate is in front of the gripper, slide the plate back.
    if check("the plate is in front of the robot's gripper"):
        robot.move_gripper("vertically aligned with the plate")


# push-back: slide the puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper behind the puck
    #  2. Push the puck back
    # If the gripper is not behind the puck, move it behind the puck.
    if check("the robot's gripper is not behind the puck"):
        robot.move_gripper("behind the puck")
    # If the gripper is behind the puck, push the puck back.
    if check("the robot's gripper is behind the puck"):
        robot.move_gripper("forward aligned with the puck")


# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Move the gripper to the puck
    #  2. Push the puck to the wall
    #  3. Move the gripper to the puck
    #  4. Push the puck to the target location
    # If the gripper is not near the puck, move it near the puck.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # If the gripper is near the puck, push the puck to the wall.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("forward aligned with the puck")
    # If the gripper is aligned with the puck, move the gripper back to the
    # puck.
    if check("the robot's gripper is forward aligned with the puck"):
        robot.move_gripper("near the puck")


# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Put gripper left of the target
    #  2. Move the gripper right
    #  3. Stop when the gripper is at the target
    # If the gripper is not to the left of the target, we should move it there.
    if check("the robot's gripper is not left of the target"):
        robot.move_gripper("left of the target")
    # If the gripper is left of the target, we can move it right .
    if check("the robot's gripper is left of the target"):
        robot.move_gripper("right of the target")
    # If the gripper is right of the target, we can stop.
    if check("the robot's gripper is right of the target"):
        robot.move_gripper("stop")


# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper right of the dial
    #  2. Start pushing against the dial to turn the dial
    #  3. Push the dial harder
    # If the robot's gripper is not vertically aligned with the dial, we should
    # move the gripper near the dial to start pushing
    if check("the robot's gripper is not vertically aligned with the dial and the robot's gripper is below the dial"):
        robot.move_gripper("right of the dial")
    # If the robot's gripper is near the dial we can probably turn the dial now
    # by moving the gripper left.
    if check("the robot's gripper is near the dial"):
        robot.move_gripper("forward aligned with the dial")
    # If the robot's gripper is starting to be in front of the dial, push harder.
    if check("the robot's gripper is in front of the dial"):
        robot.move_gripper("vertically aligned with the dial")


# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move the gripper right of the wall
    #  2. Move the gripper around the wall
    #  3. Move the gripper to the target location
    # If the robot's gripper is not right of the wall, move it there.
    if check("the robot's gripper is not right of the wall"):
        robot.move_gripper("right of the wall")
    # If the robot's gripper is right of the wall, move it around the wall.
    if check("the robot's gripper is right of the wall"):
        robot.move_gripper("around the wall")
    # If the robot's gripper is around the wall, move it to the target location.
    if check("the robot's gripper is around the wall"):
        robot.move_gripper("to the target location")


# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Grab block
    #  3. Move gripper to target location
    #  4. Drop block
    # If the gripper is not above the block, move the gripper above the block.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the block", open_gripper=True)
    # If the gripper is not around the block, grab the block.
    if check("the robot's gripper is vertically aligned with the block and the robot's gripper is not around the block"):
        robot.move_gripper("around the block")
    # If the gripper is around the block and the block is not at the target
    # location, move the gripper to the target location.
    if check("the robot's gripper is around the block and the block is not at the target location"):
        robot.move_gripper("at the target location")
    # If the gripper is around the block and the block is at the target location,
    # drop the block.
    if check("the robot's gripper is around the block and the block is at the target location"):
        robot.move_gripper("vertically aligned with the block", close_gripper=True)


# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put gripper behind the soccer ball
    #  2. Push the soccer ball into the target location
    # If the robot's gripper is not behind the soccer ball, move it behind the
    # soccer ball.
    if check("the robot's gripper is not behind the soccer ball"):
        robot.move_gripper("behind the soccer ball")
    # If the gripper is behind the soccer ball, push the soccer ball into the
    # target location.
    if check("the robot's gripper is behind the soccer ball"):
        robot.move_gripper("forward aligned with the soccer ball")


# stick-push: use the stick to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Move the gripper to the stick
    #  2. Pick up the stick
    #  3. Move the gripper to the thermos
    #  4. Push the thermos
    # First, move the gripper to the stick.
    if check("the robot's gripper is not near the stick"):
        robot.move_gripper("near the stick")
    # If the stick is now left of the gripper, pick it up.
    if check("the stick is left of the robot's gripper"):
        robot.move_gripper("around the stick")
    # If the gripper is around the stick, move the gripper to the thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("near the thermos")
    # If the thermos is now left of the gripper, push it.
    if check("the thermos is left of the robot's gripper"):
        robot.move_gripper("around the thermos")


# stick-pull: use the stick to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick
    #  3. Move the stick to the thermos
    #  4. Move the stick to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick", open_gripper=True)
    # If the stick becomes left of the gripper, go back to putting the gripper
    # above the stick.
    # Because the stick is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # As long the gripper is still mostly around the stick and the stick isn't
    # lined up with the thermos, line up the stick with the thermos.
    if check("the robot's gripper is forward aligned with the stick and the stick is not horizontally aligned with the thermos"):
        robot.move_gripper("horizontally aligned with the thermos")
    # If the stick is lined up with the thermos to the side, move the stick to
    # the target location.
    if check("stick is horizontally aligned with the thermos"):
        robot.move_gripper("above the stick")


# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the target location
    # If the gripper is not above the cube, move it there.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube", open_gripper=True)
    # If the gripper is above the cube and the gripper is not around the cube,
    # grab the cube.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube")
    # If the gripper is around the cube and the cube is not at the target
    # location, move the cube to the target location.
    if check("the robot's gripper is around the cube and the cube is not at the target location"):
        robot.move_gripper("at the target location")


# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Move the cube sideways to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube", open_gripper=True)
    # If the cube becomes left of the gripper, go back to putting the gripper
    # above the cube.
    if check("cube is not left of the robot's gripper and cube is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the cube", close_gripper=True)
    # As long the gripper is still mostly around the cube and the cube isn't
    # lined up with the target location, line up the cube with the target
    # location.
    if check("the robot's gripper is forward aligned with the cube and cube is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the cube is lined up with the target location, move it sideways.
    if check("cube is horizontally aligned with the target location"):
        robot.move_gripper("above the cube")


# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")


# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Pick up the puck
    #  2. Move the puck to the target location
    #  3. Drop the puck
    # If the robot's gripper is not around the puck, pick up the puck.
    if check("the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck")
    # If the robot's gripper is around the puck, move the puck to the target
    # location.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the robot's gripper is horizontally aligned with the target location,
    # drop the puck.
    if check("the robot's gripper is horizontally aligned with the target location"):
        robot.move_gripper("around the puck")


# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # If the the door handle is right of the robot's gripper, we should move the
    # gripper near the door handle to start pushing
    if check("the door handle is right of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move_gripper("right of the door handle")
    # If the robot's gripper is near the door handle we can probably slide the
    # door close now by moving the gripper left.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("forward aligned with the door handle")
    # If the robot's gripper is starting to be in front of the door handle,
    # push harder.
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("left of the door handle")
