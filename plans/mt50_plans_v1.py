# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")


# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    # Once the gripper is around the drawer handle, we can just pull the drawer
    # open.
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")


# assembly: put the wrench around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    #  5. Put gripper above the wrench
    #  6. Grab the wrench with the gripper
    #  7. Line the wrench up with the peg
    #  8. Slide the wrench sideways onto the peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")
    # Now that the peg is in the hole, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    # As long the gripper is still mostly around the wrench and the wrench isn't
    # lined up with the peg, line up the wrench with the peg.
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not horizontally aligned with peg"):
        robot.align("wrench to peg")
    # If the wrench is lined up with the peg to the side, insert it.
    if check("wrench is horizontally aligned with peg"):
        robot.insert("wrench onto peg")


# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball
    #  3. Align the ball with the hoop
    #  4. Drop the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.put("gripper above ball")
    # If the ball is left of the gripper, go back to putting the gripper above
    # the ball.
    if check("ball is not left of the robot's gripper and ball is not forward aligned with the robot's gripper"):
        robot.grab("ball")
    # As long the gripper is still mostly around the ball and the ball isn't
    # lined up with the hoop, line up the ball with the hoop.
    if check("the robot's gripper is forward aligned with the ball and the ball is not horizontally aligned with hoop"):
        robot.align("ball to hoop")
    # If the ball is lined up with the hoop to the side, drop it.
    if check("ball is horizontally aligned with hoop"):
        robot.drop("ball into hoop")


# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button from the front
    # Because this is "front", we just need to line up the gripper from the front.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper in front of button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")


# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "wall", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.put("gripper above coffee button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.push("down on coffee button")


# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around the mug
    #  3. Pull the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not almost vertically aligned with the mug"):
        robot.put("gripper above mug")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the mug and the robot's gripper is open"):
        robot.put("gripper around mug")
    # As long as the gripper is still vertically aligned with the mug,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the mug"):
        robot.pull("away from mug")


# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab mug
    #  3. Move gripper to target location
    #  4. Drop mug
    # If the gripper is not above the mug, move it there.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above mug")
    # If the gripper is above the mug, grab it.
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around mug"):
        robot.grab("mug")
    # If the gripper is around the mug, move it to the target location.
    if check("the robot's gripper is around mug"):
        robot.move("gripper to target location")
    # If the gripper is at the target location, drop the mug.
    if check("the robot's gripper is at target location"):
        robot.drop("mug")


# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Pick up the cube
    #  4. Put gripper above the bin
    #  5. Drop gripper around the bin
    #  6. Drop the cube into the bin
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    # As long as the gripper is still vertically aligned with the cube, it's being
    # opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.pull("cube up")
    # Now that the cube is picked up, put the gripper above the bin.
    if check("the robot's gripper is not vertically aligned with the bin"):
        robot.put("gripper above bin")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the bin and the robot's gripper is open"):
        robot.put("gripper around bin")
    # As long as the gripper is still vertically aligned with the bin, it's being
    # opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the bin"):
        robot.pull("cube down")


# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Turn the dial
    # If the gripper is not around the dial, put it around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.put("gripper around dial")
    # If the gripper is around the dial, turn the dial.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial")


# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench is left of the gripper, go back to putting the gripper
    # above the wrench.
    if check("wrench is left of the robot's gripper"):
        robot.grab("wrench")
    # If the gripper is around the wrench, pull it off the peg.
    if check("the robot's gripper is around the wrench"):
        robot.pull("wrench off peg")


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
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")


# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn faucet left
    # We need to put the gripper above the faucet handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not almost vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with faucet handle and the robot's gripper is open"):
        robot.put("gripper around faucet handle")
    # As long as the gripper is still vertically aligned with the faucet handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.turn("faucet left")


# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper left of the faucet handle
    #  2. Start turning the faucet handle right
    #  3. Turn the faucet handle right harder
    # If the faucet handle is right of the robot's gripper, we should move the
    # gripper near the faucet handle to start turning
    if check("the faucet handle is right of the robot's gripper and the robot's gripper is not near the faucet handle"):
        robot.move("gripper to left of faucet handle")
    # If the robot's gripper is near the faucet handle we can probably turn the
    # faucet handle now by moving the gripper right.
    if check("the robot's gripper is near the faucet handle"):
        robot.turn("faucet right")
    # If the robot's gripper is starting to be in front of the faucet handle,
    # turn harder.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.turn("faucet right harder")


# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Grab the hammer
    #  3. Align the hammer with the nail
    #  4. Hit the nail with the hammer
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.put("gripper above hammer")
    # If the hammer is not left of the gripper, go back to putting the gripper
    # above the hammer.
    # Because the hammer is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("hammer is not left of the robot's gripper and hammer is not forward aligned with the robot's gripper"):
        robot.grab("hammer")
    # As long the gripper is still mostly around the hammer and the hammer isn't
    # lined up with the nail, line up the hammer with the nail.
    if check("the robot's gripper is forward aligned with the hammer and hammer is not vertically aligned with nail"):
        robot.align("hammer to nail")
    # If the hammer is lined up with the nail, hit the nail with the hammer.
    if check("hammer is vertically aligned with nail"):
        robot.hit("hammer on nail")


# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Pick up the box lid
    #  2. Put the box lid on the box
    # Pick up the box lid.
    if check("the robot's gripper is not around the box lid"):
        robot.put("gripper around box lid")
    # Put the box lid on the box.
    if check("the robot's gripper is around the box lid"):
        robot.put("box lid on box")


# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle from the side
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.put("gripper above handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.push("down on handle")


# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")


# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle.
    # Because the handle is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    # As long the gripper is still mostly around the handle and the handle isn't
    # lined up with the robot, line up the handle with the robot.
    if check("the robot's gripper is forward aligned with the handle and the handle is not vertically aligned with the robot"):
        robot.align("handle to robot")
    # If the handle is lined up with the robot to the side, pull it up.
    if check("handle is vertically aligned with the robot"):
        robot.pull("handle up")


# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Pull up the handle
    # First, put the gripper mostly above the handle.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.put("gripper above handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    # As long as the gripper is still vertically aligned with the handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.pull("handle up")


# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above lever
    #  2. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    # Once the gripper is above the lever, rotate the lever up.
    if check("the robot's gripper is vertically aligned with lever"):
        robot.rotate("lever up")


# peg-insert-side: insert the peg into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")


# peg-unplug-side: pull the peg out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways out of the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")


# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Move the gripper to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the target location, line up the peg with the target location.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with target location"):
        robot.align("peg to target location")
    # If the peg is lined up with the target location, move the gripper to the
    # target location.
    if check("peg is horizontally aligned with target location"):
        robot.move("gripper to target location")


# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Pick up the puck
    #  4. Move the gripper to the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not almost vertically aligned with puck"):
        robot.put("gripper above puck")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with puck and the robot's gripper is open"):
        robot.put("gripper around puck")
    # As long as the gripper is still vertically aligned with the puck,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with puck"):
        robot.pull("puck")
    # As long as the gripper is still vertically aligned with the puck,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with puck"):
        robot.pull("puck")
    # As long as the gripper is still vertically aligned with the puck,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with puck"):
        robot.pull("puck")
    # As long as the gripper is still vertically aligned with the puck,
    # it's


# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Rotate the dial to the right
    #  3. Rotate the dial to the left
    #  4. Rotate the dial to the right
    #  5. Rotate the dial to the left
    #  6. Rotate the dial to the right
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # Rotate the dial to the right.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.rotate("dial right")
    # Rotate the dial to the left.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.rotate("dial left")


# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Pick up the puck
    #  4. Move the puck to the target location
    #  5. Drop the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    # As long as the gripper is still above the puck, move it down around the
    # puck.
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not around puck"):
        robot.put("gripper around puck")
    # As long as the gripper is still around the puck, pick up the puck.
    if check("the robot's gripper is around puck"):
        robot.pick("puck")
    # Move the puck to the target location.
    if check("the robot's gripper is holding puck"):
        robot.move("puck to target location")
    # Drop the puck.
    if check("the robot's gripper is holding puck"):
        robot.drop("puck")


# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target
    #  4. Slide the plate to the target
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    # As long the gripper is still mostly around the plate and the plate isn't
    # lined up with the target, line up the plate with the target.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with target"):
        robot.align("plate to target")
    # If the plate is lined up with the target to the side, insert it.
    if check("plate is horizontally aligned with target"):
        robot.slide("plate to target")


# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    # As long the gripper is still mostly around the plate and the plate isn't lined
    # up with the target location, line up the plate with the target location.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with target location"):
        robot.align("plate to target location")
    # If the plate is lined up with the target location to the side, insert it.
    if check("plate is horizontally aligned with target location"):
        robot.insert("plate into target location")


# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Start pushing against the plate to slide it back
    #  3. Push the plate back harder
    # If the plate is right of the robot's gripper, we should move the gripper
    # near the plate to start pushing
    if check("the plate is right of the robot's gripper and the robot's gripper is not near the plate"):
        robot.move("gripper to left of plate")
    # If the robot's gripper is near the plate we can probably slide the plate
    # back now by moving the gripper right.
    if check("the robot's gripper is near the plate"):
        robot.slide("plate back")
    # If the robot's gripper is starting to be in front of the plate, push
    # harder.
    if check("the robot's gripper is in front of the plate"):
        robot.push("plate back harder")


# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    # As long the gripper is still mostly around the plate and the plate isn't lined
    # up with the target location, line up the plate with the target location.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with target location"):
        robot.align("plate to target location")
    # If the plate is lined up with the target location to the side, insert it.
    if check("plate is horizontally aligned with target location"):
        robot.insert("plate into target location")


# push-back: slide the puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Push the puck back
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is not vertically aligned with the puck, go back to putting
    # the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is around the puck, push it back.
    if check("the robot's gripper is around the puck"):
        robot.push("puck back")


# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper right of the puck
    #  2. Push the puck to the target location
    # If the robot's gripper is not vertically lined up with the puck,
    # we should move the gripper near the puck to start pushing
    if check("the robot's gripper is not vertically aligned with the puck and the robot's gripper is below the puck"):
        robot.move("gripper to right of puck")
    # If the robot's gripper is near the puck we can probably slide the
    # puck to the target location now by moving the gripper left.
    if check("the robot's gripper is near the puck"):
        robot.slide("puck to target location")


# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Push the puck to the left of the wall
    #  2. Push the puck to the right of the wall
    #  3. Push the puck to the target location
    # First, push the puck to the left of the wall.
    if check("the puck is not left of the wall"):
        robot.push("puck to left of wall")
    # Then, push the puck to the right of the wall.
    if check("the puck is not right of the wall"):
        robot.push("puck to right of wall")
    # Finally, push the puck to the target location.
    if check("the puck is not at the target location"):
        robot.push("puck to target location")


# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Move the gripper to the target location
    if check("the robot's gripper is not at the target location"):
        robot.move("gripper to the target location")


# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Turn the door handle
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.turn("door handle")


# No useful completion for reach-wall:
# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move the gripper to the target location
    if check("the robot's gripper is not at the target location"):
        robot.move("gripper to the target location")


# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Pick up the block
    #  4. Move the gripper to the target location
    #  5. Drop the block
    # If the gripper is not above the block, put it above the block.
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    # If the gripper is above the block, drop the gripper around the block.
    if check("the robot's gripper is above the block"):
        robot.put("gripper around block")
    # If the gripper is around the block, pick up the block.
    if check("the robot's gripper is around the block"):
        robot.pick("block")
    # If the gripper is holding the block, move the gripper to the target location.
    if check("the robot's gripper is holding the block"):
        robot.move("gripper to target location")
    # If the gripper is at the target location, drop the block.
    if check("the robot's gripper is at target location"):
        robot.drop("block")


# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put gripper above the soccer ball
    #  2. Grab the soccer ball with the gripper
    #  3. Push the soccer ball into the target location
    # First, put the gripper above the soccer ball.
    if check("the robot's gripper is not vertically aligned with the soccer ball"):
        robot.put("gripper above soccer ball")
    # If the soccer ball becomes left of the gripper, go back to putting the
    # gripper above the soccer ball.
    if check("soccer ball is not left of the robot's gripper and soccer ball is not forward aligned with the robot's gripper"):
        robot.grab("soccer ball")
    # As long the gripper is still mostly around the soccer ball and the soccer
    # ball isn't lined up with the target location, line up the soccer ball
    # with the target location.
    if check("the robot's gripper is forward aligned with the soccer ball and the soccer ball is not horizontally aligned with target location"):
        robot.align("soccer ball to target location")
    # If the soccer ball is lined up with the target location, push it.
    if check("soccer ball is horizontally aligned with target location"):
        robot.push("soccer ball into target location")


# stick-push: use the stick to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos
    #  4. Push the thermos with the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the stick is left of the gripper, go back to putting the gripper
    # above the stick.
    if check("stick is not left of the robot's gripper"):
        robot.grab("stick")
    # As long the gripper is still mostly around the stick and the stick isn't
    # lined up with the thermos, line up the stick with the thermos.
    if check("the robot's gripper is forward aligned with the stick and the stick is not horizontally aligned with thermos"):
        robot.align("stick to thermos")
    # If the stick is lined up with the thermos to the side, push it.
    if check("stick is horizontally aligned with thermos"):
        robot.push("thermos with stick")


# stick-pull: use the stick to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the thermos
    #  2. Grab the thermos with the gripper
    #  3. Put the stick above the thermos
    #  4. Grab the stick with the gripper
    #  5. Pull the thermos to the target location
    # First, put the gripper above the thermos.
    if check("the robot's gripper is not vertically aligned with the thermos"):
        robot.put("gripper above thermos")
    # If the gripper is not around the thermos, grab the thermos.
    if check("the robot's gripper is vertically aligned with the thermos and the robot's gripper is not around the thermos"):
        robot.grab("thermos")
    # If the gripper is around the thermos, put the stick above the thermos.
    if check("the robot's gripper is around the thermos"):
        robot.put("stick above thermos")
    # If the stick is above the thermos, grab the stick.
    if check("the robot's gripper is around the thermos and the stick is above the thermos"):
        robot.grab("stick")
    # If the gripper is around the thermos and the gripper is around the stick,
    # pull the thermos to the target location.
    if check("the robot's gripper is around the thermos and the robot's gripper is around the stick"):
        robot.pull("thermos to target location")


# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Move gripper to target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    # As long as the gripper is still vertically aligned with the cube,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with cube"):
        robot.pull("cube")
    # As long as the gripper is still vertically aligned with the cube,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with cube"):
        robot.pull("cube")
    # As long as the gripper is still vertically aligned with the cube,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with cube"):
        robot.pull("cube")


# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Push cube to target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    # As long as the gripper is still vertically aligned with the cube,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.pull("cube to target location")


# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")


# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")


# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Pick up the puck
    #  4. Align the puck with the target
    #  5. Drop the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the puck and the robot's gripper is open"):
        robot.put("gripper around puck")
    # As long as the gripper is still vertically aligned with the puck,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.pull("puck")
    # If the puck is aligned with the target, drop it.
    if check("the puck is horizontally aligned with the target"):
        robot.drop("puck")


# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull closed the door
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can just pull the door
    # closed.
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")
