# door-open: pull the door open
def door_open(robot):# Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Once Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")


# drawer-open: pull the drawer open
def drawer_open(robot):# Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # Once the gripper is around the drawer handle, we can just pull the drawer
    # open.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")


# assembly: put the wrench around the peg
def assembly(robot):# Steps:
    #  1. Put the gripper above the peg
    #  2. Put the gripper around the peg
    #  3. Put the gripper around the wrench
    #  4. Put the wrench around the peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", open_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly mostly around the peg and the peg isn't lined
    # up with the wrench, line up the peg with the wrench.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with wrench"):
        robot.move_gripper("horizontally aligned with wrench")
    # If the peg is lined up with the wrench to the side, put the wrench
    # around the peg.
    if check("peg is horizontally aligned with wrench"):
        robot.move_gripper("above the peg peg")


# basketball: put the ball into into the hoop
def basketball(robot):# Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball
    #  3. Line the ball up with the hoop
    #  4. Put the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball", open_gripper=True)
    # If the the ball becomes left of the gripper, go back to putting the gripper
    # above the ball.
    if check("ball is not left of the robot's gripper and ball is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the ball", close_gripper=True)
    # As long the gripper is still mostly around the ball and the ball isn't lined
    # up with the hoop, line up the ball with the hoop.
    if check("the robot's gripper is is forward aligned with the ball and the ball is not horizontally aligned with the hoop"):
        robot.move_gripper("horizontally aligned with the hoop")
    # If the ball is lined up with the hoop to the side, put it into the hoop.
    if check("ball is horizontally aligned with the hoop"):
        robot.move_gripper("above the ball")


# button-press-topdown: push the button down from above
def button_press_topdown(robot):# Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")


# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):# Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")


# button-press: push the button from the front
def button_press(robot):# Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button from the front
    # Because this is "front", we just need to line up the gripper from the front.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("near the button")


# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):# Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "wall", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")


# coffee-button: push the button on the coffee machine
def coffee_button(robot):# Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")


# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):# Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Pull the mug to the target location
    #  4. Put the mug down
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug", open_gripper=True)
    # If If the mug becomes left of the gripper, go back to putting the gripper
    # above the mug.
    # Because the mug is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("mug is not left of the robot's gripper and mug is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the mug", close_gripper=True)
    # As long the gripper is still mostly around the mug and the the mug isn't lined
    # up with the target location, line up the mug with the target location.
    if check("the robot's gripper is forward aligned with the mug and the mug is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the mug is lined up with the target location to the side, move the mug
    # to the target location.
    if check("mug is horizontally aligned with the target location"):
        robot.move_gripper("above the mug")


# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):# Steps:
    #  1. Put the gripper around the mug
    #  2. Push the mug to the target location
    # If the gripper is not around the mug, move it around the mug.
    if check("the robot's gripper is not around the mug"):
        robot.move_gripper("around the mug")
    # If the gripper is around the mug, push the mug to the target location.
    if check("the robot's gripper is around the mug"):
        robot.move_gripper("to the target location")


# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):# Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the target bin
    #  4. Put the cube down in the target bin
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube", open_gripper=True)
    # If the cube becomes left of the gripper, go back to putting the gripper
    # above the cube.
    # Because the cube is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("cube is not left of the robot's gripper and cube is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the cube", close_gripper=True)
    # As long the gripper is still mostly mostly around the cube and the cube isn't lined
    # up with the target bin, line up the cube with the target bin.
    if check("the robot's gripper is forward aligned with the cube and the cube is not horizontally aligned with the target bin"):
        robot.move_gripper("horizontally aligned with the target bin")
    # If the cube is lined up with the target bin to the side, put it down.
    if check("cube is horizontally aligned with the target bin"):
        robot.move_gripper("above the the cube")


# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Turn the dial
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.move_gripper("around the dial")


# disassemble: pull the wrench off the peg
def disassemble(robot):# Steps:
    #  1. Put gripper above the wrench
    #  2. Pull the wrench off the peg
    # We need to put the gripper above the wrench before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # Once the gripper is lined up above the wrench, we should be able to to
    # grab the wrench by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with wrench and the robot's gripper is not around wrench"):
        robot.move_gripper("around the wrench")
    # Once the gripper is around the wrench, we can just pull the wrench
    # off the peg.
    if check("the robot's gripper is around wrench"):
        robot.move_gripper("above the wrench")


# drawer-close: push the drawer close
def drawer_close(robot):# Steps:
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
def faucet_open(robot):# Steps:
    #  1. Put gripper right of the faucet handle
    #  2. Start turning the faucet left
    #  3. Turn the faucet left harder
    # If the faucet handle is left of the robot's gripper, we should move the
    # gripper near the faucet handle to start turning
    if check("the faucet handle is left of the robot's gripper and the robot's gripper is not near the faucet handle"):
        robot.move_gripper("right of of the faucet handle")
    # If the robot's gripper is near the faucet handle we can probably turn the
    # faucet open now by moving the gripper left.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("forward aligned with the faucet handle")
    # If the robot's gripper is starting to be in front of the faucet handle,
    # turn harder.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.move_gripper("left of the faucet handle")


# faucet-close: turn the faucet right
def faucet_close(robot):# Steps:
    #  1. Put gripper right of the faucet handle
    #  2. Turn the faucet handle right
    # If the robot's gripper is not vertically aligned with the faucet handle,
    # we should move the gripper near the faucet handle to start turning
    if check("the robot's gripper is not vertically aligned with the faucet handle and the robot's gripper is below the faucet handle"):
        robot.move_gripper("right of faucet handle")
    # If the robot robot's gripper is near the faucet handle we can probably turn the
    # faucet handle now by moving the gripper right.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("forward aligned with the faucet handle")


# hammer: hit the nail with the hammer
def hammer(robot):# Steps:
    #  1. Put gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Move the hammer forward
    #  4. Move the hammer back
    # If the gripper is not above the hammer, move it above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move_gripper("vertically aligned with the hammer", open_gripper=True)
    # If the gripper is above the hammer, grab the hammer.
    if check("the robot's gripper is vertically aligned with the hammer"):
        robot.move_gripper("around the hammer")
    # If the gripper is around the hammer, move the hammer forward.
    if check("the robot's gripper is around the hammer"):
        robot.move_gripper("horizontally aligned with the hammer")
    # If the gripper is horizontally aligned with the hammer, move the hammer
    # back. back.
    if check("the robot's gripper is horizontally aligned with the hammer"):
        robot.move_gripper("around the hammer")


# box-close: pick up the box lid and place it on the box
def box_close(robot):# Steps:
    #  1. Pick up the box lid
    #  2. Put the box lid on the box
    # Pick up the box lid.
    if check("the robot's gripper is not around the box lid"):
        robot.move_gripper("around the box lid")
    # If the gripper is around the box lid, pick it up.
    if check("the robot's gripper is around the box lid"):
        robot.move_gripper("above the the box lid")
    # Put the box lid on the box.
    if check("the robot's gripper is above the box lid"):
        robot.move_gripper("above the box")


# handle-press-side: push down the handle from the side
def handle_press_side(robot):# Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle from the side
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.move_gripper("horizontally aligned with the handle", close_gripper=True)
    # Now that the the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.move_gripper("near the handle")


# handle-press: push down the handle
def handle_press(robot):# Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Now that that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle")


# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):# Steps:
    #  1. Put gripper above the handle
    #  2. Pull up on the handle
    # Because this is "side", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Now that the gripper is lined up, up, just pull up on the handle.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("above the handle")


# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Pull up on the handle
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("around the handle")


# lever-pull: rotate the lever up
def lever_pull(robot):# Steps:
    #  1. Put gripper above the lever
    #  2. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever")
    # If the lever is right of the gripper, rotate the lever up.
    if check("the robot's gripper is vertically aligned with the lever and the lever is right of the the robot's gripper"):
        robot.move_gripper("around the lever")


# peg-insert-side: insert the peg into the hole from the side
def peg_insert_side(robot):# Steps:
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
    # As long the gripper is still mostly mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")


# peg-unplug-side: pull the peg out from the side
def peg_unplug_side(robot):# Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways out of the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", open_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")


# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):# Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg out of the hole
    #  4. Move the peg to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", open_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")
    # If the gripper gripper is above the peg, grab the peg and lift it out of the hole.
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("near the peg")
    # If the gripper is near the peg, lift it out of the hole.
    if check("the robot's gripper is near the peg"):
        robot.move_gripper("above the peg")
    # If the gripper is above the peg, move it to the target location.
    if check("the robot's robot's gripper is above the peg"):
        robot.move_gripper("to the target location")


# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):# Steps:
    #  1. Put gripper above the puck
    #  2. Pick up the puck
    #  3. Move the puck to the target location
    # If the gripper is not above the puck, move it above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck", open_gripper=True)
    # If the gripper is above the puck, pick it it up.
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("around the puck")
    # If the gripper is around the puck, move the puck to the target location.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("near the target location")


# door-lock: turn the dial on the door
def door_lock(robot):# Steps:
    #  1. Put gripper right of the door handle
    #  2. Start pushing against the door handle to open the door
    #  3. Push the door open harder
    # If the robot's gripper is not vertically lined up with the door handle,
    # we should move the gripper near the door handle to start pushing
    if check("the robot's gripper is not vertically aligned with the door handle and the robot's gripper is below the door handle"):
        robot.move_gripper("right of door handle")
    # If the robot's gripper is near the door handle we can probably slide the
    # door open now by moving the gripper left.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("forward aligned with the door handle")
    # If the robot's gripper is starting to be in front of the door handle,
    # push harder.
    if check("the robot's gripper is in front front of the door handle"):
        robot.move_gripper("vertically aligned with the door handle")


# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):# Steps:
    #  1. Pick up the puck
    #  2. Move the gripper to the target location
    #  3. Move the gripper to the target location
    #  4. Move the gripper to the target location
    #  5. Move the gripper to the target location
    #  6. Move the gripper to the target location
    #  7. Move the gripper to the target location
    #  8. Move the gripper gripper to the target location
    #  9. Move the gripper to the target location
    # 10. Move the gripper to the target location
    # 11. Move the gripper to the target location
    # 12. Move the gripper to the target location
    # 13. Move the gripper to the target location
    # 14. Move the gripper to the target location
    # 15. Move the gripper to the target location
    # 16. Move the


# plate-slide: slide the plate into the target location
def plate_slide(robot):# Steps:
    #  1. Move the plate to the left
    #  2. Move the plate to the right
    #  3. Move the plate to the left
    #  4. Move the plate to the right
    #  5. Move the plate to the left
    #  6. Move the plate to the right
    #  7. Move the plate to the left
    #  8. Move the plate to the right right
    #  9. Move the plate to the left
    # 10. Move the plate to the right
    # 11. Move the plate to the left
    # 12. Move the plate to the right
    # 13. Move the plate to the left
    # 14. Move the plate to the right
    # 15. Move the plate to the left
    # 16. Move the plate to the right
    # 1


# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate", open_gripper=True)
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long the gripper is still mostly mostly around the plate and the plate isn't lined
    # up with the target location, line up the plate with the target location.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with target location"):
        robot.move_gripper("horizontally aligned with target location")
    # If the plate is lined up with the target location to the side, insert it.
    if check("plate is horizontally aligned with target location"):
        robot.move_gripper("above the plate")


# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):# Steps:
    #  1. Put gripper near the plate
    #  2. Push the plate back into the target location
    # If the gripper is not near the plate, move the gripper near the plate.
    if check("the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate")
    # If the gripper is near the plate, push the plate back into the target
    # location.
    if check("the robot's robot's gripper is near the plate"):
        robot.move_gripper("forward aligned with the plate")


# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate", open_gripper=True)
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long the gripper is still mostly mostly around the plate and the plate isn't lined
    # up with the target location, line up the plate with the target location.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the plate is lined up with the target location to the side, insert it.
    if check("plate is horizontally aligned with the target location"):
        robot.move_gripper("above the plate plate")


# push-back: slide the puck backwards to the target location
def push_back(robot):# Steps:
    #  1. Put gripper right of the puck
    #  2. Start pushing against the puck to slide it backwards
    #  3. Push the puck backwards harder
    # If the robot's gripper is not vertically lined up with the puck,
    # we should move the gripper near the puck to start pushing
    if check("the robot's gripper is not vertically aligned with the puck and the robot's gripper is below the puck"):
        robot.move_gripper
        robot.move_gripper("right of the puck")
    # If the robot's gripper is near the puck we can probably slide the
    # puck backwards now by moving the gripper left.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("forward aligned with the puck")
    # If the robot's gripper is starting to be in front of the puck,
    # push harder.
    if check("the robot's gripper is in front of the puck"):
        robot.move_gripper("vertically aligned with the puck")


# push: slide the puck to the target location
def push(robot):# Steps:
    #  1. Put gripper behind the puck
    #  2. Push the puck to the target location
    # If the gripper is not behind the puck, put the gripper behind the puck.
    if check("the robot's gripper is not behind the puck"):
        robot.move_gripper("behind the puck")
    # If the gripper is behind the puck, push the puck to the target location.
    if check("the robot's gripper is behind the puck"):
        robot.move_gripper("forward aligned with the puck")


# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):# Steps:
    #  1. Put gripper above the puck
    #  2. Push the puck to the left
    #  3. Push the puck to the right
    #  4. Push the puck to the left
    #  5. Push the puck to the right
    #  6. Push the puck to the left
    #  7. Push the puck to the right
    #  8. Push the puck to the left left
    #  9. Push the puck to the right
    #  10. Push the puck to the left
    #  11. Push the puck to the right
    #  12. Push the puck to the left
    #  13. Push the puck to the right
    #  14. Push the puck to the left
    #  15. Push the puck to the right
    #  16. Push the puck to the left


# reach: reach to the target location
def reach(robot):# Steps:
    #  1. Move the gripper to the target location
    #  2. Move the gripper to the target location
    #  3. Move the gripper to the target location
    #  4. Move the gripper to the target location
    #  5. Move the gripper to the target location
    #  6. Move the gripper to the target location
    #  7. Move the gripper to the target location
    #  8.  8. Move the gripper to the target location
    #  9. Move the gripper to the target location
    # 10. Move the gripper to the target location
    # 11. Move the gripper to the target location
    # 12. Move the gripper to the target location
    # 13. Move the gripper to the target location
    # 14. Move the gripper to the target location
    # 15. Move the gripper to the target location
    #


# door-unlock: turn the dial on the door
def door_unlock(robot):# Steps:
    #  1. Put gripper above the dial
    #  2. Turn the dial to the right
    #  3. Turn the dial to the left
    #  4. Turn the dial to the right
    #  5. Turn the dial to the left
    #  6. Turn the dial to the right
    #  7. Turn the dial to the left
    #  8. Turn the dial to the right right
    #  9. Turn the dial to the left
    # 10. Turn the dial to the right
    # 11. Turn the dial to the left
    # 12. Turn the dial to the right
    # 13. Turn the dial to the left
    # 14. Turn the dial to the right
    # 15. Turn the dial to the left
    # 16. Turn the dial to the right
    # 1


# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):# Steps:
    #  1. Move the gripper to the left of the wall
    #  2. Move the gripper to the right of the wall
    #  3. Move the gripper to the target location
    # If the robot's gripper is not left of the wall, move the gripper to the left
    # of the wall.
    if check("the robot's gripper is not left of the wall"):
        robot.move_gripper("left of the wall")
    # If the robot's gripper is left of the wall, move the gripper to the right
    # of the wall.
    if check("the robot's gripper is left of the wall"):
        robot.move_gripper("right of the wall")
    # If the robot's gripper is right of the wall, move the gripper to the target
    # location.
    if check("the robot's gripper is right of the wall"):
        robot.move_gripper("to the target location")


# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):# Steps:
    #  1. Pick up the block
    #  2. Move the block to the target location
    #  3. Put the block down
    # First, pick up the block.
    if check("the robot's gripper is not around the block"):
        robot.move_gripper("around the block")
    # If the gripper is around the block, pick it up.
    if check("the robot's gripper is around the block"):
        robot.move_gripper("vertically aligned with the block")
    # Once the block is picked up, move the gripper to the target location.
    if check("the robot's gripper is vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the target location")
    # Once the gripper is at the target location, put the block down.
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.move_gripper("around the block")


# soccer: push the soccer ball into the target location
def soccer(robot):# Steps:
    #  1. Line up the ball with the target
    #  2. Push the ball into the target
    # If the ball is not lined up with the target, line it up.
    if check("the ball is not horizontally aligned with the target"):
        robot.move_gripper("horizontally aligned with the target")
    # If the ball is lined up with the target, push it into the target.
    if check("the ball is horizontally aligned with the target"):
        robot.move_gripper("near the ball")


# stick-push: use the stick to push the thermos to the target location
def stick_push(robot):# Steps:
    #  1. Move the stick to the thermos
    #  2. Push the thermos to the target location
    # If the stick is not near the thermos, move the stick to the thermos.
    if check("the stick is not near the thermos"):
        robot.move_stick("near the thermos")
    # If the thermos is not near the target location, push the thermos to the
    # target location.
    if check("the thermos is not near the target target location"):
        robot.move_stick("to the target location")


# stick-pull: use the stick to pull the thermos to the target location
def stick_pull(robot):# Steps:
    #  1. Put gripper above the thermos
    #  2. Grab the thermos with the gripper
    #  3. Move the gripper to the target location
    #  4. Drop the thermos
    # First, put the gripper above the thermos.
    if check("the robot's gripper is not vertically aligned with the thermos"):
        robot.move_gripper("vertically aligned with the thermos", open_gripper=True)
    # If the the thermos becomes left of the gripper, go back to putting the gripper
    # above the thermos.
    # Because the thermos is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("thermos is not left of the robot's gripper and thermos is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the thermos", close_gripper=True)
    # As long the gripper is still mostly around the thermos and the the thermos isn't
    # lined up with the target location, line up the thermos with the target
    # location.
    if check("the robot's gripper is forward aligned with the thermos and the thermos is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the thermos is lined up with the target location to the side, move the
    # gripper to the target location.
    if check("thermos is horizontally aligned with the target location"):
        robot.move_gripper("above the thermos")


# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):# Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Move the gripper to the target location
    # If the gripper is not above the cube, move it above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube", open_gripper=True)
    # If the gripper is not around the cube, cube, move it around the cube.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube")
    # If the gripper is around the cube, move the gripper to the target location.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("to the target location")


# sweep: grab the cube and move sideways it to the target location
def sweep(robot):# Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube sideways to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube", open_gripper=True)
    # If the cube becomes left of the gripper, go back to putting putting the gripper
    # above the cube.
    # Because the cube is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("cube is not left of the robot's gripper and cube is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the cube", close_gripper=True)
    # As long the gripper is still mostly around the cube and the cube isn't lined
    # up with with the target location, line up the cube with the target location.
    if check("the robot's gripper is forward aligned with the cube and the cube is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the cube is lined up with the target location to the side, move the cube
    # to the target location.
    if check("cube is horizontally aligned with the target location"):
        robot.move_gripper("vertically aligned with the cube")


# window-open: slide the window open to the left
def window_open(robot):# Steps:
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
    if check("the robot's gripper is in front front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")


# window-close: slide the window closed to the right
def window_close(robot):# Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")


# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):# Steps:
    #  1. Move the gripper to the puck
    #  2. Pick up the puck
    #  3. Move the gripper to the target location
    #  4. Drop the puck
    # Move the gripper to the puck.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # Pick up the puck.
    if check("the robot's gripper gripper is near the puck"):
        robot.move_gripper("around the puck")
    # Move the gripper to the target location.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("near the target location")
    # Drop the puck.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("around the target location")


# door-close: push the door closed to the target location
def door_close(robot):# Steps:
    #  1. Put gripper right of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # If the robot's gripper is not vertically lined up with the door handle,
    # we should move the gripper near the door handle to start pushing
    if check("the robot's gripper is not vertically aligned with the door handle and the robot's gripper is below the door handle"):
        robot.move_gripper("right of door handle")
    # If the robot's gripper is near the door handle we can probably slide the
    # door open now by moving the gripper left.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("forward aligned with the door handle")
    # If the robot's gripper is starting to be in front of the door handle,
    # push harder.
    if check("the robot's gripper is in front front of the door handle"):
        robot.move_gripper("vertically aligned with the door handle")
