# door-open: pull the door open
 def door_open(robot):
    if check("door handle is not vertically aligned with the robot's gripper"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("door handle is vertically aligned with the robot's gripper and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")
    if check("door handle is vertically aligned with the robot's gripper and the robot's gripper is around door handle"):
        robot.pull("away from door")


# drawer-open: pull the drawer open
 def drawer_open(robot):
    if check("drawer handle is not vertically aligned with the robot's gripper"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("drawer handle is vertically aligned with the robot's gripper and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")
    if check("drawer handle is vertically aligned with the robot's gripper and the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")


# assembly: put the wrench around the peg
 def assembly(robot):
    if check("wrench is not vertically aligned with the robot's gripper"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    if check("wrench is vertically aligned with the robot's gripper"):
        robot.put("gripper around wrench")
    if check("the robot's gripper is vertically aligned with wrench"):
        robot.put("gripper around wrench")
    if check("wrench is notleft of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    if check("wrench is not left of the robot's gripper and the robot's gripper is not forward aligned with wrench"):
        robot.grab("wrench")
    if check("wrench is forward aligned with the robot's gripper"):
        robot.put("gripper around peg")
    if check("the robot's gripper is forward aligned with wrench"):
        robot.put("gripper around peg")

    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("wrench is not left of the robot's gripper and the robot's gripper is not forward aligned with wrench"):
        robot.grab("peg")
    if check("wrench is forward aligned with the robot's gripper"):
        robot.put("gripper around peg")
    if check("the robot's gripper is forward aligned with wrench"):


# basketball: put the ball into into the hoop
 def basketball(robot):
    if check("ball is not vertically aligned with the robot's gripper"):
        robot.put("gripper above ball")
    if check("the robot's gripper is not vertically aligned with ball"):
        robot.put("gripper above ball")
    if check("ball is vertically aligned with the robot's gripper"):
        robot.grab("ball")
    if check("the robot's gripper is vertically aligned with ball"):
        robot.grab("ball")
    if check("ball is forward aligned with the robot'sgripper"):
        robot.push("ball into hoop")
    if check("the robot's gripper is forward aligned with ball"):
        robot.push("ball into hoop")


# button-press-topdown: push the button down from above
 def button_press_topdown(robot):
    if check("button is not vertically aligned with the robot's gripper"):
        robot.put("gripper above button")
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("button is vertically aligned with the robot's gripper"):
        robot.push("down on button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


# button-press-topdown-wall: push the button down from above with a short wall in the way
 def button_press_topdown_wall(robot):
    if check("button is not vertically aligned with the robot's gripper"):
        robot.put("gripper above button")
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("button is vertically aligned with the robot's gripper"):
        robot.push("down on button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


# button-press: push the button from the front
 def button_press(robot):
    if check("button is not horizontally aligned with the robot's gripper"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper in front of button")
    if check("button is horizontally aligned with the robot's gripper"):
        robot.push("down on button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")


# button-press-wall: push the button from the front with a short wall in the way
 def button_press_wall(robot):
    if check("button is not vertically aligned with the robot's gripper"):
        robot.put("gripper above button")
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("button is vertically aligned with the robot's gripper and button is not forward aligned with the robot's gripper"):
        robot.grab("button")
    if check("button is vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with button"):
        robot.grab("button")
    if check("button is forward aligned with the robot's gripper"):
        robot.push("down on button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")


# coffee-button: push the button on the coffee machine
 def coffee_button(robot):
    if check("coffee button is not vertically aligned with the robot's gripper"):
        robot.put("gripper above coffee button")
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.put("gripper above coffee button")
    if check("coffee button is vertically aligned with the robot's gripper and coffee button is not forward aligned with the robot's gripper"):
        robot.grab("coffee button")
    if check("coffee button is vertically aligned with the robot's gripper and the robot'sgripper is not forward aligned with coffee button"):
        robot.grab("coffee button")
    if check("coffee button is forward aligned with the robot's gripper"):
        robot.push("coffee button")
    if check("the robot's gripper is forward aligned with coffee button"):
        robot.push("coffee button")


# coffee-pull: grab the mug and pull it to the target location
 def coffee_pull(robot):
    if check("coffee is not below the robot's gripper"):
        robot.put("gripper above coffee")
    if check("the robot's gripper is not above coffee"):
        robot.put("gripper above coffee")
    if check("coffee is below the robot's gripper and gripper is open"):
        robot.drop("gripper around coffee")
    if check("the robot's gripper is above coffee and gripper is open"):
        robot.drop("gripper around coffee")
    if check("coffee is nearthe robot's gripper and gripper is closed"):
        robot.place("coffee at target")
    if check("the robot's gripper is near coffee and gripper is closed"):
        robot.place("coffee at target")


# coffee-push: grab the mug and move it to the target location
 def coffee_push(robot):
    if check("mug is not below the robot's gripper"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    if check("mug is below the robot's gripper and gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is above mug and gripper is open"):
        robot.drop("gripper around mug")
    if check("mug is nearthe robot's gripper and gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and gripper is open"):
        robot.drop("gripper around mug")
    if check("mug is below the robot's gripper and gripper is closed"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is above mug and gripper is closed"):
        robot.drop("gripper around mug")
    if check("mug is near the robot's gripper and gripper is closed"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and gripper is closed"):
        robot.drop("gripper around mug")
    if check("mug is below the robot's gripper and gripper is around mug"):
        robot.move("mug to target location")
    if check("the robot's gripper is above mug and gripper is around mug"):
        robot.move("mug to target location")
    if check("mug is near the robot's gripper and gripper is around mug"):
        robot.move("mug to target location")
    if check("the robot's gripper is near mug and gripper is around mug"):
        robot.move("mug to target location")


# bin-picking: pick up the cube and place it in the target bin
 def bin_picking(robot):
    if check("cube is not below the robot's gripper"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not above cube"):
        robot.place("gripper above cube")
    if check("cube is below the robot's gripper and gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is above cube and gripper is open"):
        robot.drop("gripper around cube")
    if check("cube is nearthe robot's gripper and gripper is open"):
        robot.place("gripper around cube")
    if check("the robot's gripper is near cube and gripper is open"):
        robot.place("gripper around cube")
    if check("cube is near the robot's gripper and gripper is closed"):
        robot.place("gripper around cube")
    if check("the robot's gripper is near cube and gripper is closed"):
        robot.place("gripper around cube")
    if check("cube is below the robot'sgripper and gripper is closed"):
        robot.place("gripper around cube")
    if check("the robot's gripper is above cube and gripper is closed"):
        robot.place("gripper around cube")
    if check("cube is near the robot's gripper and gripper is closed"):
        robot.place("gripper around cube")
    if check("the robot's gripper is near cube and gripper is closed"):
        robot.place("gripper around cube")
    if check("cube is around the robot's gripper"):


# dial-turn: turn the dial
 def dial_turn(robot):
    if check("dial is not vertically aligned with the robot's gripper"):
        robot.put("gripper above dial")
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("dial is vertically aligned with the robot's gripper"):
        robot.turn("clockwise")
    if check("the robot's gripper is vertically aligned with dial"):
        robot.turn("clockwise")


# disassemble: pull the wrench off the peg
 def disassemble(robot):
    if check("wrench is not vertically aligned with the robot's gripper"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    if check("wrench is vertically aligned with the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    if check("wrench is vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with wrench"):
        robot.grab("wrench")
    if check("wrench is forward aligned with the robot's gripper"):
        robot.pull("wrench off peg")
    if check("the robot's gripper is forward aligned with wrench"):
        robot.pull("wrench off peg")


# drawer-close: push the drawer close
 def drawer_close(robot):
    if check("gripper is open"):
        robot.put("the gripper in front of the drawer")
    if check("drawer handle is vertically aligned with the robot's gripper and gripper is open"):
        robot.put("the gripper in front of the drawer")
    if check("drawer handle is below the robot's gripper"):
        robot.put("the gripper above the drawer handle")
    if check("the robot's gripper is above drawer handle"):
        robot.put("the gripper above the drawer handle")
    ifcheck("drawer handle is not vertically aligned with the robot's gripper and drawer handle is not forward aligned with the robot's gripper"):
        robot.grab("drawer handle")
    if check("drawer handle is not vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with drawer handle"):
        robot.grab("drawer handle")
    if check("drawer handle is forward aligned with the robot's gripper"):
        robot.push("drawer closed")
    if check("the robot's gripper is forward aligned with drawer handle"):

        robot.push("drawer closed")


# faucet-open: turn the faucet left
 def faucet_open(robot):
    if check("faucet handle is not vertically aligned with the robot's gripper"):
        robot.move("gripper to right of faucet handle")
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move("gripper to right of faucet handle")
    if check("faucet handle is right of the robot's gripper"):
        robot.turn("faucet left")
    if check("the robot's gripper is left of faucet handle"):
        robot.turn("faucet left")


# faucet-close: turn the faucet right
 def faucet_close(robot):
    if check("faucet handle is not vertically aligned with the robot's gripper"):
        robot.move("gripper to left of faucet handle")
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move("gripper to left of faucet handle")
    if check("faucet handle is right of the robot's gripper"):
        robot.turn("faucet right")
    if check("the robot's gripper is left of faucet handle"):
        robot.turn("faucet right")


# hammer: hit the nail with the hammer
 def hammer(robot):
    if check("hammer is not above the robot's gripper"):
        robot.put("gripper above hammer")
    if check("the robot's gripper is not above hammer"):
        robot.put("gripper above hammer")
    if check("hammer is above the robot's gripper"):
        robot.grab("hammer")
    if check("the robot's gripper is below hammer"):
        robot.grab("hammer")
    if check("hammer is forward aligned with the robot's gripper"):
        robot.push("hammer down")
    if check("the robot's gripper is forward aligned with hammer"):
        robot.push("hammer down")


# box-close: pick up the box lid and place it on the box
 def box_close(robot):
    if check("box lid is not below the robot's gripper"):
        robot.put("gripper above box lid")
    if check("the robot's gripper is not above box lid"):
        robot.put("gripper above box lid")
    if check("box lid is vertically aligned with the robot's gripper and box lid is not left of the robot's gripper"):
        robot.grab("box lid")
    if check("box lid is vertically aligned with the robot's gripper and the robot's gripper is not right ofbox lid"):
        robot.grab("box lid")
    if check("box lid is left of the robot's gripper"):
        robot.move("gripper to right of box lid")
    if check("the robot's gripper is left of box lid"):
        robot.move("gripper to right of box lid")
    if check("box lid is right of the robot's gripper"):
        robot.move("gripper to left of box lid")
    if check("the robot's gripper is right of box lid"):

        robot.move("gripper to left of box lid")
    if check("box lid is horizontally aligned with the robot's gripper and box lid is not forward aligned with the robot's gripper"):
        robot.align("box lid to box")
    if check("box lid is horizontally aligned with the robot's gripper and the robot's gripper is not forward aligned with box lid"):
        robot.align("box lid to box")
    if check("box lid is forward aligned with the robot's gripper and box lid is not vertically aligned with the robot's gripper"):
        robot.align("box lid to box")
    if check("box lid is forward aligned with the robot's gripper and the robot's gripper is not vertically aligned with box lid"):
        robot.align("box lid to box")
    if check("box lid is vertically aligned with the robot's gripper and box lid is not forward aligned with the robot's gripper"):
        robot.align("box lid to box")
    if check("box lid is vertically aligned with the robot's gripper and the robot's gripper is not forwardaligned with box lid"):
        robot.align("box lid to box")
    if check("box lid is forward aligned with the robot's gripper and box lid is vertically aligned with the robot's gripper"):
        robot.put("box lid on box")
    if check("box lid is forward aligned with the robot's gripper and box lid is almost vertically aligned with the robot's gripper"):
        robot.put("box lid on box")
    if check("box lid is forward aligned with the robot's gripper and the robot's gripper is almost verticallyaligned with box lid"):
        robot.put("box lid on box")
    if check("box lid is almost forward aligned with the robot's gripper and box lid is vertically aligned with the robot's gripper"):
        robot.put("box lid on box")
    if check("box lid is almost forward aligned with the robot's gripper and box lid is almost vertically aligned with the robot's gripper"):
        robot.put("box lid on box")
    if check("box lid is almost forward aligned with the robot's gripper and the robot's gripperis almost vertically aligned with box lid"):
        robot.put("box lid on box")


# handle-press-side: push down the handle from the side
 def handle_press_side(robot):
    if check("handle is not vertically aligned with the robot's gripper"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("handle is vertically aligned with the robot's gripper"):
        robot.push("down on handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")


# handle-press: push down the handle
 def handle_press(robot):
    if check("handle is not vertically aligned with the robot's gripper"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("handle is vertically aligned with the robot's gripper"):
        robot.push("down on handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")


# handle-pull-side: pull up the handle from the side
 def handle_pull_side(robot):
    if check("handle is not vertically aligned with the robot's gripper"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("handle is vertically aligned with the robot's gripper"):
        robot.pull("up on handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.pull("up on handle")


# handle-pull: pull up the handle
 def handle_pull(robot):
    if check("handle is not vertically aligned with the robot's gripper"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("handle is vertically aligned with the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("handle is vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with handle"):
        robot.grab("handle")
    if check("handle is forward aligned with the robot's gripper"):
        robot.pull("up on handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("up on handle")


# lever-pull: rotate the lever up
 def lever_pull(robot):
    if check("lever is not vertically aligned with the robot's gripper"):
        robot.put("gripper above lever")
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("lever is vertically aligned with the robot's gripper"):
        robot.rotate("lever up")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.rotate("lever up")


# peg-insert-side: insert the peg into the hole from the side
 def peg_insert_side(robot):
    if check("peg is left of the robot's gripper"):
        robot.put("gripper above peg")
    if check("the robot's gripper is right of peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("peg is not left of the robot's gripper and the robot's gripper is not forward aligned with peg"):
        robot.grab("peg")
    if check("peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is forward aligned with the robot's gripper and hole is not horizontally aligned with peg"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")
    if check("hole is horizontally aligned with peg"):
        robot.insert("peg into hole")


# peg-unplug-side: pull the peg out from the side
 def peg_unplug_side(robot):
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("peg is not left of the robot's gripper and the robot's gripper is not forward aligned with peg"):
        robot.grab("peg")
    if check("peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is forward aligned with the robot'sgripper and hole is not horizontally aligned with peg"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.pull("peg out of hole")
    if check("hole is horizontally aligned with peg"):
        robot.pull("peg out of hole")


# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
 def pick_out_of_hole(robot):
    if check("peg is not left of the robot's gripper"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not left of peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("peg is not left of the robot's gripper and the robot's gripper is not forward aligned with peg"):

        robot.grab("peg")
    if check("peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is forward aligned with the robot's gripper and hole is not horizontally aligned with peg"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")
    if check("hole is horizontally aligned with peg"):
        robot.insert("peg into hole")
    if check("peg is not left of the robot's gripper"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not left of peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("peg is not left of the robot's gripper and the robot's gripper is not forward aligned with peg"):


# pick-place: pick up the puck and hold it at the target location
 def pick_place(robot):
    if check("puck is not below the robot's gripper"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("puck is below the robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is nearthe robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is below the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is near the robot'sgripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is below the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is closed"):
        robot.place("gripper around puck")


# door-lock: turn the dial on the door
 def door_lock(robot):
    if check("dial is not almost vertically aligned with the robot's gripper"):
        robot.put("gripper above dial")
    if check("the robot's gripper is not almost vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("dial is vertically aligned with the robot's gripper and the robot's gripper is not around dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not around dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is around dial"):
        robot.turn("clockwise")
    if check("dial is vertically aligned with the robot's gripper and the robot's gripper is around dial"):
        robot.turn("clockwise")


# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
 def pick_place_wall(robot):
    if check("puck is not below the robot's gripper"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("puck is below the robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is nearthe robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is below the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is near the robot'sgripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is vertically aligned with the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is vertically aligned with puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is forward aligned with the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is forward aligned with puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is forward aligned with the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is forward aligned with puck and gripper is closed"):
        robot.place("gripper around puck")


# plate-slide: slide the plate into the target location
 def plate_slide(robot):
    if check("plate is not below the robot's gripper"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    if check("plate is below the robot's gripper"):
        robot.slide("plate to target location")
    if check("the robot's gripper is above plate"):
        robot.slide("plate to target location")


# plate-slide-side: slide the plate sideways into the target location
 def plate_slide_side(robot):
    if check("plate is left of the robot's gripper"):
        robot.put("gripper above plate")
    if check("the robot's gripper is right of plate"):
        robot.put("gripper above plate")
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    if check("plate is not left of the robot's gripper and the robot's gripper is not forward aligned with plate"):
        robot.grab("plate")
    if check("plate is forward aligned with the robot's gripper and plate is not horizontally aligned with target"):
        robot.align("plate to target")
    if check("plate is forward aligned with the robot's gripper and target is not horizontally aligned with plate"):
        robot.align("plate to target")
    if check("plate is horizontally aligned with target"):
        robot.slide("plate to target")
    if check("target is horizontally aligned with plate"):
        robot.slide("plate to target")


# plate-slide-back: slide the plate back into the target location
 def plate_slide_back(robot):
    if check("plate is left of the robot's gripper"):
        robot.move("gripper to right of plate")
    if check("the robot's gripper is left of plate"):
        robot.move("gripper to right of plate")
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    if check("plate is not left of the robot's gripper and the robot's gripper is not forward aligned with plate"):
        robot.grab("plate")
    if check("plate is forward aligned with the robot's gripper"):
        robot.slide("plate back")
    if check("the robot's gripper is forward aligned with plate"):
        robot.slide("plate back")


# plate-slide-back-side: slide the plate back sideways into the target location
 def plate_slide_back_side(robot):
    if check("plate is left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move("gripper to right of plate")
    if check("plate is left of the robot's gripper and the robot's gripper is not forward aligned with plate"):
        robot.move("gripper to right of plate")
    if check("plate is forward aligned with the robot's gripper"):
        robot.slide("plate back")
    if check("the robot's gripper is forward aligned with plate"):
        robot.slide("plate back")


# push-back: grab the puck and move it back to the target location
 def push_back(robot):
    if check("puck is not below the robot's gripper"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("puck is near the robot's gripper and gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is near puck and gripper is open"):
        robot.close("gripper around puck")
    if check("puck is belowthe robot's gripper and gripper is closed"):
        robot.move("gripper to goal")
    if check("the robot's gripper is above puck and gripper is closed"):
        robot.move("gripper to goal")
    if check("puck is near the robot's gripper and gripper is closed"):
        robot.place("puck at goal")
    if check("the robot's gripper is near puck and gripper is closed"):
        robot.place("puck at goal")


# push: grab the puck and move it to the target location
 def push(robot):
    if check("puck is not below the robot's gripper"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("puck is below the robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is nearthe robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is below the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is near the robot'sgripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is below the robot's gripper and gripper is around puck"):
        robot.push("puck to target")
    if check("the robot's gripper is above puck and gripper is around puck"):
        robot.push("puck to target")
    if check("puck is near the robot's gripper and gripper isaround puck"):
        robot.push("puck to target")
    if check("the robot's gripper is near puck and gripper is around puck"):
        robot.push("puck to target")
    if check("puck is below the robot's gripper and gripper is not around puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is not around puck"):
        robot.place("gripper around puck")
    if check("puck is near the robot's gripper and gripper isnot around puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and gripper is not around puck"):
        robot.place("gripper around puck")
    if check("puck is below the robot's gripper and gripper is not closed"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and gripper is not closed"):
        robot.drop("gripper around puck")
    if check("puck is near the robot's gripper andgripper is not closed"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and gripper is not closed"):
        robot.drop("gripper around puck")
    if check("puck is below the robot's gripper and gripper is not open"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is not open"):
        robot.place("gripper around puck")
    if check("puck is near the robot's gripper andgripper is not open"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and gripper is not open"):
        robot.place("gripper around puck")
    if check("puck is below the robot's gripper and gripper is not around puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is not around puck"):
        robot.place("gripper around puck")


# push-wall: grab the puck and move it to the target location with a small wall in the way
def push_wall(robot):
    if check("puck is not below the robot's gripper"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("puck is below the robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is nearthe robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is below the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is near the robot'sgripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is below the robot's gripper"):
        robot.push("puck to target")
    if check("the robot's gripper is above puck"):
        robot.push("puck to target")
    if check("puck is near the robot's gripper"):
        robot.push("puck to target")

    if check("the robot's gripper is near puck"):
        robot.push("puck to target")


# reach: reach to the target location
 def reach(robot):
    if check("the robot's gripper is not above target location"):
        robot.move("gripper above target location")
    if check("the robot's gripper is not below target location"):
        robot.move("gripper below target location")
    if check("the robot's gripper is not left of target location"):
        robot.move("gripper left of target location")
    if check("the robot's gripper is not right of target location"):
        robot.move("gripper right of target location")

    if check("the robot's gripper is not forward aligned with target location"):
        robot.move("gripper forward aligned with target location")
    if check("the robot's gripper is not backward aligned with target location"):
        robot.move("gripper backward aligned with target location")


# door-unlock: turn the dial on the door
 def door_unlock(robot):
     if check("door handle is not vertically aligned with the robot's gripper"):
         robot.put("gripper above door handle")
     if check("the robot's gripper is not vertically aligned with door handle"):
         robot.put("gripper above door handle")
     if check("door handle is vertically aligned with the robot's gripper and the robot's gripper is not around door handle"):
         robot.put("gripper around door handle")
     if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
         robot.put("gripper around door handle")
     if check("the robot's gripper is around door handle"):
         robot.turn("door handle")
     if check("door handle is vertically aligned with the robot's gripper and the robot's gripper is around door handle"):
         robot.turn("door handle")


# reach-wall: reach to the target location with a short wall in the way
 def reach_wall(robot):
    if check("the robot is not near the target location"):
        robot.move("to the target location")
    if check("the robot is not near the target location"):
        robot.move("to the target location")
    if check("the robot is not near the target location"):
        robot.move("to the target location")
    if check("the robot is not near the target location"):
        robot.move("to the target location")
    if check("the robot is not near the target location"):


# shelf-place: pick up the block and place it at the target location
 def shelf_place(robot):
    if check("block is not below the robot's gripper"):
        robot.place("gripper above block")
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    if check("block is below the robot's gripper and gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is above block and gripper is open"):
        robot.drop("gripper around block")
    if check("block is nearthe robot's gripper and gripper is open"):
        robot.place("gripper around block")
    if check("the robot's gripper is near block and gripper is open"):
        robot.place("gripper around block")
    if check("block is below the robot's gripper and gripper is closed"):
        robot.place("gripper around block")
    if check("the robot's gripper is above block and gripper is closed"):
        robot.place("gripper around block")
    if check("block is near the robot'sgripper and gripper is closed"):
        robot.place("gripper around block")
    if check("the robot's gripper is near block and gripper is closed"):
        robot.place("gripper around block")
    if check("block is below the robot's gripper and gripper is closed"):
        robot.place("gripper around block")
    if check("the robot's gripper is above block and gripper is closed"):
        robot.place("gripper around block")


# soccer: push the soccer ball into the target location
 def soccer(robot):
    if check("the robot's gripper is above soccer ball"):
        robot.place("gripper above soccer ball")
    if check("soccer ball is below the robot's gripper and gripper is open"):
        robot.drop("gripper around soccer ball")
    if check("the robot's gripper is above soccer ball and gripper is open"):
        robot.drop("gripper around soccer ball")
    if check("soccer ball is near the robot's gripper and gripper is open"):
        robot.close("gripper around soccer ball")
    if check("the robot's gripper is near soccer ball and gripper is open"):
        robot.close("gripper around soccer ball")
    if check("soccer ball is below the robot's gripper and gripper is closed"):
        robot.kick("soccer ball")
    if check("the robot's gripper is above soccer ball and gripper is closed"):
        robot.kick("soccer ball")
    if check("soccer ball is near the robot's gripper and gripper is closed"):
        robot.kick("soccer ball")
    ifcheck("the robot's gripper is near soccer ball and gripper is closed"):
        robot.kick("soccer ball")


# stick-push: use the stick to push the thermos to the target location
 def stick_push(robot):
    if check("thermos is not below the robot's gripper"):
        robot.put("gripper above thermos")
    if check("the robot's gripper is not above thermos"):
        robot.put("gripper above thermos")
    if check("thermos is below the robot's gripper and gripper is open"):
        robot.drop("gripper around thermos")
    if check("the robot's gripper is above thermos and gripper is open"):
        robot.drop("gripper around thermos")
    if check("thermos is forward aligned with the robot's gripper and gripper is open"):
        robot.drop("gripper around thermos")
    if check("the robot's gripper is forward aligned with thermos and gripper is open"):
        robot.drop("gripper around thermos")
    if check("thermos is forward aligned with the robot's gripper and thermos is not horizontally aligned with the robot's gripper"):
        robot.align("thermos to gripper")
    if check("thermos is forward aligned with the robot's gripper and the robot's gripper is not horizontallyaligned with thermos"):
        robot.align("thermos to gripper")
    if check("thermos is horizontally aligned with the robot's gripper and thermos is not forward aligned with the robot's gripper"):
        robot.align("thermos to gripper")
    if check("thermos is horizontally aligned with the robot's gripper and the robot's gripper is not forward aligned with thermos"):
        robot.align("thermos to gripper")
    if check("thermos is horizontally aligned with the robot's gripper and thermos is forward aligned with the robot's gripper"):
        robot.push("thermos to target")
    if check("thermos is horizontally aligned with the robot's gripper and the robot's gripper is forward aligned with thermos"):
        robot.push("thermos to target")


# stick-pull: use the stick to pull the thermos to the target location
 def stick_pull(robot):
    if check("thermos is not in front of the robot's gripper"):
        robot.put("gripper in front of thermos")
    if check("the robot's gripper is not in front of thermos"):
        robot.put("gripper in front of thermos")
    if check("thermos is in front of the robot's gripper"):
        robot.grab("thermos")
    if check("the robot's gripper is in front of thermos"):
        robot.grab("thermos")
    if check("thermos is not in front of the robot's gripper and thermos is not forward aligned with the robot's gripper"):
        robot.align("thermos to gripper")
    if check("thermos is not in front of the robot's gripper and the robot's gripper is not forward aligned with thermos"):
        robot.align("thermos to gripper")
    if check("thermos is forward aligned with the robot's gripper"):
        robot.pull("thermos to target location")


# sweep-into: grab the cube and move it to the target location
 def sweep_into(robot):
    if check("cube is not below the robot's gripper"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    if check("cube is below the robot's gripper and gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is above cube and gripper is open"):
        robot.drop("gripper around cube")
    if check("cube is nearthe robot's gripper and gripper is open"):
        robot.grab("cube")
    if check("the robot's gripper is near cube and gripper is open"):
        robot.grab("cube")
    if check("cube is below the robot's gripper and gripper is closed"):
        robot.move("cube to goal")
    if check("the robot's gripper is above cube and gripper is closed"):
        robot.move("cube to goal")
    if check("cube is near the robot's gripper and gripper is closed"):

        robot.drop("cube")
    if check("the robot's gripper is near cube and gripper is closed"):
        robot.drop("cube")


# sweep: grab the cube and move sideways it to the target location
 def sweep(robot):
    if check("cube is not below the robot's gripper"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not above cube"):
        robot.place("gripper above cube")
    if check("cube is below the robot's gripper and gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is above cube and gripper is open"):
        robot.drop("gripper around cube")
    if check("cube is nearthe robot's gripper and gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and gripper is open"):
        robot.drop("gripper around cube")
    if check("cube is below the robot's gripper and gripper is closed"):
        robot.pick("cube up")
    if check("the robot's gripper is above cube and gripper is closed"):
        robot.pick("cube up")
    if check("cube is near the robot's gripper and gripper isclosed"):
        robot.pick("cube up")
    if check("the robot's gripper is near cube and gripper is closed"):
        robot.pick("cube up")
    if check("cube is above the robot's gripper and gripper is closed"):
        robot.put("cube down")
    if check("the robot's gripper is below cube and gripper is closed"):
        robot.put("cube down")
    if check("cube is near the robot's gripper and gripper is closed"):
        robot.put("cube down")


# window-open: slide the window open
 def window_open(robot):
    if check("window handle is not vertically aligned with the robot's gripper and the robot's gripper is mostly below window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is mostly below window handle and window handle is not vertically aligned with the robot's gripper"):
        robot.move("gripper to right of window handle")
    if check("window handle is left of the robot's gripper and window handle is vertically aligned with the robot's gripper"):
        robot.slide("window left")
    if check("window handle is left of the robot's gripper and window handle is almost vertically aligned with the robot's gripper"):
        robot.slide("window left")
    if check("window handle is near the robot's gripper"):
        robot.push("window left harder")
    if check("window handle is behind the robot's gripper"):
        robot.push("window left harder")


# window-close: slide the window closed
 def window_close(robot):
    if check("window handle is not vertically aligned with the robot's gripper"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is not vertically aligned with window handle"):
        robot.move("gripper to left of window handle")
    if check("window handle is right of the robot's gripper"):
        robot.slide("window right")
    if check("the robot's gripper is left of window handle"):
        robot.slide("window right")
    if check("window handle is vertically aligned with the robot's gripper and window handle is not right of the robot's gripper"):
        robot.push("window right harder")
    if check("window handle is vertically aligned with the robot's gripper and the robot's gripper is not left of window handle"):
        robot.push("window right harder")


# hand-insert: pick up the puck and move it to the target location
 def hand_insert(robot):
    if check("puck is not below the robot's gripper"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("puck is below the robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is nearthe robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is below the robot's gripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is near the robot'sgripper and gripper is closed"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and gripper is closed"):
        robot.place("gripper around puck")
    if check("puck is below the robot's gripper and gripper is around puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is around puck"):
        robot.place("gripper around puck")
    if check("puck is near the robot's gripper andgripper is around puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and gripper is around puck"):
        robot.place("gripper around puck")
    if check("puck is below the robot's gripper and gripper is around puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and gripper is around puck"):
        robot.place("gripper around puck")


# door-close: push the door closed to the target location
 def door_close(robot):
    if check("door handle is not almost vertically aligned with the robot's gripper"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("door handle is left of the robot's gripper and gripper is closed"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is right of door handle and gripper is closed"):
        robot.put("gripper around door handle")
    if check("door handle is vertically aligned with the robot's gripper and door handle is not left of the robot's gripper"):
        robot.push("door closed")
    if check("door handle is vertically aligned with the robot's gripper and the robot's gripper is not right of door handle"):
        robot.push("door closed")
