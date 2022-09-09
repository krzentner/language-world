# assembly: put the wrench around the peg
def assembly(robot):
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.move_gripper("right of the wrench", close_gripper=True)
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with the peg")
    if check("wrench is horizontally aligned with peg"):
        robot.move_gripper("horizontally aligned with the peg")


# basketball: put the ball into into the hoop
def basketball(robot):
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    if check("ball is not left of the robot's gripper and ball is not forward aligned with the robot's gripper"):
        robot.move_gripper("near the ball", close_gripper=True)
    if check("the robot's gripper is forward aligned with the ball and the ball is not horizontally aligned with hoop"):
        robot.move_gripper("vertically aligned with the hoop")


# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    if check("the robot's gripper is not vertically aligned with the bin"):
        robot.move_gripper("vertically aligned with the cube")
    if check("the robot's gripper is almost vertically aligned with the bin and the robot's gripper is open"):
        robot.move_gripper("above the cube", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the bin"):
        robot.move_gripper("above the cube", close_gripper=True)


# box-close: pick up the box lid and place it on the box
def box_close(robot):
    if check("the robot's gripper is not around the box lid"):
        robot.move_gripper("vertically aligned with the lid", close_gripper=True)


# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")


# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("in front of the button")


# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("below the button", close_gripper=True)


# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("mostly below wall", open_gripper=True)


# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.move_gripper("vertically aligned with the button")
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.move_gripper("below the button", close_gripper=True)


# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not almost vertically aligned with the mug"):
        robot.move_gripper("almost vertically aligned with the mug")
    if check("the robot's gripper is almost vertically aligned with the mug and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the mug", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the target location", close_gripper=True)


# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug")
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around mug"):
        robot.move_gripper("left of the mug", close_gripper=True)


# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("left of the dial", close_gripper=True)


# disassemble: pull the wrench off the peg
def disassemble(robot):
    if check("wrench is left of the robot's gripper"):
        robot.move_gripper("left of the peg")
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")


# door-close: push the door closed to the target location
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the target location", close_gripper=True)


# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the door's lock")
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.move_gripper("mostly below the door's lock")


# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")


# door-unlock: turn the dial on the door
def door_unlock(robot):
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.move_gripper("in front of the door's lock", close_gripper=True)
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.move_gripper("vertically aligned with the door's lock")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door's lock")


# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    if check("the robot's gripper is almost vertically aligned with the puck and the robot's gripper is open"):
        robot.move_gripper("above the puck", close_gripper=True)
    if check("the puck is horizontally aligned with the target"):
        robot.move_gripper("near the puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")


# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")


# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("forward aligned with the drawer handle")


# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not almost vertically aligned with faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet")
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.move_gripper("left of the faucet")


# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the faucet handle is right of the robot's gripper and the robot's gripper is not near the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet")
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("right of the faucet")


# hammer: hit the nail with the hammer
def hammer(robot):
    if check("hammer is not left of the robot's gripper and hammer is not forward aligned with the robot's gripper"):
        robot.move_gripper("right of the hammer")
    if check("hammer is vertically aligned with nail"):
        robot.move_gripper("right of the hammer", close_gripper=True)
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move_gripper("vertically aligned with the hammer")


# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.move_gripper("near the handle", close_gripper=True)


# handle-press: push down the handle
def handle_press(robot):
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle")


# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle")
    if check("handle is vertically aligned with the robot"):
        robot.move_gripper("above the handle", close_gripper=True)


# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle", close_gripper=True)


# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.move_gripper("vertically aligned with the lever")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.move_gripper("right of the lever")


# peg-insert-side: insert the peg into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")


# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not around puck"):
        robot.move_gripper("above the puck", close_gripper=True)


# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the puck")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the puck")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with target location"):
        robot.move_gripper("horizontally aligned with the target location")
    if check("peg is horizontally aligned with target location"):
        robot.move_gripper("below the target location")


# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not at the target location"):
        robot.move_gripper("near the reach target")


# push-back: slide the puck backwards to the target location
def push_back(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")


# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("horizontally aligned with the puck")


# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is almost vertically aligned with puck and the robot's gripper is open"):
        robot.move_gripper("above the puck", close_gripper=True)
    if check("the robot's gripper is vertically aligned with puck"):
        robot.move_gripper("above the puck", close_gripper=True)


# plate-slide: slide the plate into the target location
def plate_slide(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the target location")
    if check("plate is horizontally aligned with target"):
        robot.move_gripper("vertically aligned with the target location")


# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("left of the plate", close_gripper=True)


# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    if check("the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate")
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("in front of the plate")


# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the plate", close_gripper=True)


# peg-unplug-side: pull the peg out from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("right of the peg")
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with the peg")


# soccer: push the soccer ball into the target location
def soccer(robot):
    if check("soccer ball is not left of the robot's gripper and soccer ball is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the ball")
    if check("the robot's gripper is forward aligned with the soccer ball and the soccer ball is not horizontally aligned with target location"):
        robot.move_gripper("almost vertically aligned with the goal")
    if check("the robot's gripper is not vertically aligned with the soccer ball"):
        robot.move_gripper("vertically aligned with the ball")
    if check("soccer ball is horizontally aligned with target location"):
        robot.move_gripper("forward aligned with the ball")


# stick-push: use the stick to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    if check("stick is not left of the robot's gripper"):
        robot.move_gripper("vertically aligned with the stick", close_gripper=True)
    if check("stick is horizontally aligned with thermos"):
        robot.move_gripper("horizontally aligned with the target location")


# stick-pull: use the stick to pull the thermos to the target location
def stick_pull(robot):
    if check("the robot's gripper is not vertically aligned with the thermos"):
        robot.move_gripper("vertically aligned with the thermos")
    if check("the robot's gripper is vertically aligned with the thermos and the robot's gripper is not around the thermos"):
        robot.move_gripper("vertically aligned with the target location")


# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    if check("the puck is not at the target location"):
        robot.move_gripper("above the puck", close_gripper=True)
    if check("the puck is not left of the wall"):
        robot.move_gripper("above the puck", close_gripper=True)


# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    if check("the robot's gripper is not at the target location"):
        robot.move_gripper("near the target location")


# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    if check("the robot's gripper is at target location"):
        robot.move_gripper("vertically aligned with the shelf", close_gripper=True)


# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is almost vertically aligned with cube and the robot's gripper is open"):
        robot.move_gripper("above the cube", close_gripper=True)
    if check("the robot's gripper is vertically aligned with cube"):
        robot.move_gripper("above the cube", close_gripper=True)


# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    if check("the robot's gripper is almost vertically aligned with the cube and the robot's gripper is open"):
        robot.move_gripper("above the cube", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.move_gripper("above the target location")


# window-open: slide the window open to the left
def window_open(robot):
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")


# window-close: slide the window closed to the right
def window_close(robot):
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
