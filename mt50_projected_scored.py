scored = {
    "assembly": [
        (
            -84.3189,
            '\n    #  1. Grab the wrench\n    #  2. Put the wrench around the peg\n    # First, grab the wrench.\n    if check("the robot\'s gripper is not around wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench is not around the peg, move the wrench around the peg.\n    if check("the robot\'s gripper is around wrench and the wrench is not around peg"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -84.326706,
            '\n    #  1. Grab the wrench\n    #  2. Put the wrench around the peg\n    # First, grab the wrench.\n    if check("the robot\'s gripper is not around wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench is not around the peg, move the wrench around the peg.\n    if check("the robot\'s gripper is around wrench and the wrench is not around peg"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -84.356064,
            '\n    #  1. Grab the wrench\n    #  2. Put the wrench around the peg\n    # First, grab the wrench.\n    if check("the robot\'s gripper is not around wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench is not around the peg, move the wrench around the peg.\n    if check("the robot\'s gripper is around wrench and the wrench is not around peg"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -84.356125,
            '\n    #  1. Grab the wrench\n    #  2. Put the wrench around the peg\n    # First, grab the wrench.\n    if check("the robot\'s gripper is not around wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench is not around the peg, move the wrench around the peg.\n    if check("the robot\'s gripper is around wrench and the wrench is not around peg"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -84.38963,
            '\n    #  1. Grab the wrench\n    #  2. Put the wrench around the peg\n    # First, grab the wrench.\n    if check("the robot\'s gripper is not around wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench is not around the peg, move the wrench around the peg.\n    if check("the robot\'s gripper is around wrench and the wrench is not around peg"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -84.425804,
            '\n    #  1. Grab the wrench\n    #  2. Put the wrench around the peg\n    # First, grab the wrench.\n    if check("the robot\'s gripper is not around wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench is not around the peg, move the wrench around the peg.\n    if check("the robot\'s gripper is around wrench and the wrench is not around peg"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -93.83419,
            '\n    #  1. Put gripper above the peg\n    #  2. Drop gripper around peg\n    #  3. Put gripper above wrench\n    #  4. Drop gripper around wrench\n    #  5. Put gripper above peg\n    #  6. Drop gripper around peg\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with peg"):\n        robot.slide("the puck to the goal")\n    # If the peg is left of the gripper, go back to putting the gripper above\n    # the peg.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -112.51674,
            '\n    #  1. Put gripper above the peg\n    #  2. Drop gripper around the peg\n    #  3. Put gripper above the wrench\n    #  4. Drop gripper around the wrench\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the peg and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # Once the gripper is lined up, we can just drop it around the peg.\n    if check("the robot\'s gripper is vertically aligned with the peg"):\n        robot.put("gripper above door handle")\n    # Repeat the steps for the wrench.\n    if check("the robot\'s gripper is not vertically aligned with the wrench"):\n        robot.push("the gripper into the puck")\n    if check("the robot\'s gripper is almost vertically aligned with the wrench and the robot\'s gripper is open"):\n        robot.push("window right harder")\n    if check("the robot\'s gripper is vertically aligned with the wrench"):\n        robot.place("puck at goal")\n',
        ),
    ],
    "basketball": [
        (
            -98.6143,
            '\n    #  1. Put gripper above the ball\n    #  2. Grab the ball with the gripper\n    #  3. Line up the ball with the hoop\n    #  4. Shoot the ball into the hoop\n    # First, put the gripper above the ball.\n    if check("the robot\'s gripper is not vertically aligned with the ball"):\n        robot.slide("the puck to the goal")\n    # If the ball becomes left of the gripper, go back to putting the gripper\n    # above the ball.\n    if check("the ball is not left of the robot\'s gripper and the ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the ball and the ball isn\'t lined\n    # up with the hoop, line up the ball with the hoop.\n    if check("the robot\'s gripper is forward aligned with the ball and the ball is not horizontally aligned with the hoop"):\n        robot.push("the gripper into the puck")\n    # If the ball is lined up with the hoop to the side, insert it.\n    if check("the ball is horizontally aligned with the hoop"):\n        robot.reach("to goal")\n',
        ),
        (
            -98.68968,
            '\n    #  1. Put gripper above the ball\n    #  2. Grab the ball with the gripper\n    #  3. Line up the ball with the hoop\n    #  4. Shoot the ball into the hoop\n    # First, put the gripper above the ball.\n    if check("the robot\'s gripper is not vertically aligned with the ball"):\n        robot.slide("the puck to the goal")\n    # If the ball becomes left of the gripper, go back to putting the gripper\n    # above the ball.\n    if check("the ball is not left of the robot\'s gripper and the ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the ball and the ball isn\'t lined\n    # up with the hoop, line up the ball with the hoop.\n    if check("the robot\'s gripper is forward aligned with the ball and the ball is not horizontally aligned with the hoop"):\n        robot.push("the gripper into the puck")\n    # If the ball is lined up with the hoop to the side, insert it.\n    if check("the ball is horizontally aligned with the hoop"):\n        robot.reach("to goal")\n',
        ),
        (
            -98.7083,
            '\n    #  1. Put gripper above the ball\n    #  2. Grab the ball with the gripper\n    #  3. Line up the ball with the hoop\n    #  4. Shoot the ball into the hoop\n    # First, put the gripper above the ball.\n    if check("the robot\'s gripper is not vertically aligned with the ball"):\n        robot.slide("the puck to the goal")\n    # If the ball becomes left of the gripper, go back to putting the gripper\n    # above the ball.\n    if check("the ball is not left of the robot\'s gripper and the ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the ball and the ball isn\'t lined\n    # up with the hoop, line up the ball with the hoop.\n    if check("the robot\'s gripper is forward aligned with the ball and the ball is not horizontally aligned with the hoop"):\n        robot.push("the gripper into the puck")\n    # If the ball is lined up with the hoop to the side, insert it.\n    if check("the ball is horizontally aligned with the hoop"):\n        robot.reach("to goal")\n',
        ),
        (
            -98.73938,
            '\n    #  1. Put gripper above the ball\n    #  2. Grab the ball with the gripper\n    #  3. Line up the ball with the hoop\n    #  4. Shoot the ball into the hoop\n    # First, put the gripper above the ball.\n    if check("the robot\'s gripper is not vertically aligned with the ball"):\n        robot.slide("the puck to the goal")\n    # If the ball becomes left of the gripper, go back to putting the gripper\n    # above the ball.\n    if check("the ball is not left of the robot\'s gripper and the ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the ball and the ball isn\'t lined\n    # up with the hoop, line up the ball with the hoop.\n    if check("the robot\'s gripper is forward aligned with the ball and the ball is not horizontally aligned with the hoop"):\n        robot.push("the gripper into the puck")\n    # If the ball is lined up with the hoop to the side, insert it.\n    if check("the ball is horizontally aligned with the hoop"):\n        robot.reach("to goal")\n',
        ),
        (
            -98.83014,
            '\n    #  1. Put gripper above the ball\n    #  2. Grab the ball with the gripper\n    #  3. Line up the ball with the hoop\n    #  4. Shoot the ball into the hoop\n    # First, put the gripper above the ball.\n    if check("the robot\'s gripper is not vertically aligned with the ball"):\n        robot.slide("the puck to the goal")\n    # If the ball becomes left of the gripper, go back to putting the gripper\n    # above the ball.\n    if check("the ball is not left of the robot\'s gripper and the ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the ball and the ball isn\'t lined\n    # up with the hoop, line up the ball with the hoop.\n    if check("the robot\'s gripper is forward aligned with the ball and the ball is not horizontally aligned with the hoop"):\n        robot.push("the gripper into the puck")\n    # If the ball is lined up with the hoop to the side, insert it.\n    if check("the ball is horizontally aligned with the hoop"):\n        robot.reach("to goal")\n',
        ),
        (
            -98.84577,
            '\n    #  1. Put gripper above the ball\n    #  2. Grab the ball with the gripper\n    #  3. Line up the ball with the hoop\n    #  4. Shoot the ball into the hoop\n    # First, put the gripper above the ball.\n    if check("the robot\'s gripper is not vertically aligned with the ball"):\n        robot.slide("the puck to the goal")\n    # If the ball becomes left of the gripper, go back to putting the gripper\n    # above the ball.\n    if check("the ball is not left of the robot\'s gripper and the ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the ball and the ball isn\'t lined\n    # up with the hoop, line up the ball with the hoop.\n    if check("the robot\'s gripper is forward aligned with the ball and the ball is not horizontally aligned with the hoop"):\n        robot.push("the gripper into the puck")\n    # If the ball is lined up with the hoop to the side, insert it.\n    if check("the ball is horizontally aligned with the hoop"):\n        robot.reach("to goal")\n',
        ),
        (
            -107.95711,
            '\n    #  1. Put the gripper above the ball\n    #  2. Grab the ball\n    #  3. Line the ball up with the hoop\n    #  4. Drop the ball into the hoop\n    # First, put the gripper above the ball.\n    if check("the robot\'s gripper is not vertically aligned with the ball"):\n        robot.slide("the puck to the goal")\n    # If the ball becomes left of the gripper, go back to putting the gripper\n    # above the ball.\n    if check("ball is not left of the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the ball and the ball isn\'t lined\n    # up with the hoop, line up the ball with the hoop.\n    if check("the robot\'s gripper is forward aligned with the ball and the ball is not horizontally aligned with hoop"):\n        robot.push("the gripper into the puck")\n    # If the ball is lined up with the hoop to the side, drop it.\n    if check("ball is horizontally aligned with hoop"):\n        robot.reach("to goal")\n',
        ),
        (
            -112.94753,
            '\n    #  1. Put gripper above the ball\n    #  2. Grab the ball\n    #  3. Line the ball up with the hoop\n    #  4. Drop the ball into the hoop\n    # First, put the gripper above the ball.\n    if check("the robot\'s gripper is not vertically aligned with the ball"):\n        robot.slide("the puck to the goal")\n    # If the ball is left of the gripper, go back to putting the gripper above\n    # the ball.\n    if check("the ball is left of the robot\'s gripper and the robot\'s gripper is not around the ball"):\n        robot.push("window right harder")\n    # As long as the gripper is still mostly around the ball and the ball isn\'t\n    # lined up with the hoop, line up the ball with the hoop.\n    if check("the robot\'s gripper is around the ball and the ball is not horizontally aligned with the hoop"):\n        robot.push("the gripper into the puck")\n    # If the ball is lined up with the hoop to the side, drop it into the hoop.\n    if check("the ball is horizontally aligned with the hoop"):\n        robot.reach("to goal")\n',
        ),
    ],
    "bin-picking": [
        (
            -70.96402,
            '\n    #  1. Pick up the cube\n    #  2. Place the cube in the target bin\n    # First, pick up the cube.\n    if check("the robot\'s gripper is not around cube"):\n        robot.slide("the puck to the goal")\n    # Now, place the cube in the target bin.\n    if check("the robot\'s gripper is around cube"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -90.83957,
            '\n    #  1. Pick up the cube\n    #  2. Move the cube to the bin\n    #  3. Place the cube in the bin\n    # First, pick up the cube.\n    if check("the robot\'s gripper is not around the cube"):\n        robot.slide("the puck to the goal")\n    # Move the cube to the bin.\n    if check("the robot\'s gripper is around the cube"):\n        robot.push("the gripper into the puck")\n    # Place the cube in the bin.\n    if check("the robot\'s gripper is around the cube"):\n        robot.put("gripper above drawer handle")',
        ),
        (
            -111.39081,
            '\n    #  1. Put gripper above the cube\n    #  2. Drop gripper around the cube\n    #  3. Pick up the cube\n    #  4. Put gripper above the bin\n    #  5. Drop gripper around the bin\n    #  6. Place the cube in the bin\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up with the cube, drop the gripper around the cube.\n    if check("the robot\'s gripper is vertically aligned with cube and the robot\'s gripper is not around cube"):\n        robot.push("window right harder")\n    # If the gripper is around the cube, pick it up.\n    if check("the robot\'s gripper is around cube"):\n        robot.push("the gripper into the puck")\n    # Now, put the gripper above the bin.\n    if check("the robot\'s gripper is not vertically aligned with bin"):\n        robot.reach("to goal")\n    # If the gripper is lined up with the bin, drop the gripper around the bin.\n    if check("the robot\'s gripper is vertically aligned with bin and the robot\'s gripper is not around bin"):\n        robot.put("gripper above door handle")\n    # If the gripper is around the bin, place the cube in the bin.\n    if check("the robot\'s gripper is around bin"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -111.44254,
            '\n    #  1. Put gripper above the cube\n    #  2. Drop gripper around the cube\n    #  3. Pick up the cube\n    #  4. Put gripper above the bin\n    #  5. Drop gripper around the bin\n    #  6. Place the cube in the bin\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up with the cube, drop the gripper around the cube.\n    if check("the robot\'s gripper is vertically aligned with cube and the robot\'s gripper is not around cube"):\n        robot.push("window right harder")\n    # If the gripper is around the cube, pick it up.\n    if check("the robot\'s gripper is around cube"):\n        robot.push("the gripper into the puck")\n    # Now, put the gripper above the bin.\n    if check("the robot\'s gripper is not vertically aligned with bin"):\n        robot.reach("to goal")\n    # If the gripper is lined up with the bin, drop the gripper around the bin.\n    if check("the robot\'s gripper is vertically aligned with bin and the robot\'s gripper is not around bin"):\n        robot.put("gripper above door handle")\n    # If the gripper is around the bin, place the cube in the bin.\n    if check("the robot\'s gripper is around bin"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -111.44746,
            '\n    #  1. Put gripper above the cube\n    #  2. Drop gripper around the cube\n    #  3. Pick up the cube\n    #  4. Put gripper above the bin\n    #  5. Drop gripper around the bin\n    #  6. Place the cube in the bin\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up with the cube, drop the gripper around the cube.\n    if check("the robot\'s gripper is vertically aligned with cube and the robot\'s gripper is not around cube"):\n        robot.push("window right harder")\n    # If the gripper is around the cube, pick it up.\n    if check("the robot\'s gripper is around cube"):\n        robot.push("the gripper into the puck")\n    # Now, put the gripper above the bin.\n    if check("the robot\'s gripper is not vertically aligned with bin"):\n        robot.reach("to goal")\n    # If the gripper is lined up with the bin, drop the gripper around the bin.\n    if check("the robot\'s gripper is vertically aligned with bin and the robot\'s gripper is not around bin"):\n        robot.put("gripper above door handle")\n    # If the gripper is around the bin, place the cube in the bin.\n    if check("the robot\'s gripper is around bin"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -111.46778,
            '\n    #  1. Put gripper above the cube\n    #  2. Drop gripper around the cube\n    #  3. Pick up the cube\n    #  4. Put gripper above the bin\n    #  5. Drop gripper around the bin\n    #  6. Place the cube in the bin\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up with the cube, drop the gripper around the cube.\n    if check("the robot\'s gripper is vertically aligned with cube and the robot\'s gripper is not around cube"):\n        robot.push("window right harder")\n    # If the gripper is around the cube, pick it up.\n    if check("the robot\'s gripper is around cube"):\n        robot.push("the gripper into the puck")\n    # Now, put the gripper above the bin.\n    if check("the robot\'s gripper is not vertically aligned with bin"):\n        robot.reach("to goal")\n    # If the gripper is lined up with the bin, drop the gripper around the bin.\n    if check("the robot\'s gripper is vertically aligned with bin and the robot\'s gripper is not around bin"):\n        robot.put("gripper above door handle")\n    # If the gripper is around the bin, place the cube in the bin.\n    if check("the robot\'s gripper is around bin"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -111.60003,
            '\n    #  1. Put gripper above the cube\n    #  2. Drop gripper around the cube\n    #  3. Pick up the cube\n    #  4. Put gripper above the bin\n    #  5. Drop gripper around the bin\n    #  6. Place the cube in the bin\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up with the cube, drop the gripper around the cube.\n    if check("the robot\'s gripper is vertically aligned with cube and the robot\'s gripper is not around cube"):\n        robot.push("window right harder")\n    # If the gripper is around the cube, pick it up.\n    if check("the robot\'s gripper is around cube"):\n        robot.push("the gripper into the puck")\n    # Now, put the gripper above the bin.\n    if check("the robot\'s gripper is not vertically aligned with bin"):\n        robot.reach("to goal")\n    # If the gripper is lined up with the bin, drop the gripper around the bin.\n    if check("the robot\'s gripper is vertically aligned with bin and the robot\'s gripper is not around bin"):\n        robot.put("gripper above door handle")\n    # If the gripper is around the bin, place the cube in the bin.\n    if check("the robot\'s gripper is around bin"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -111.67738,
            '\n    #  1. Put gripper above the cube\n    #  2. Drop gripper around the cube\n    #  3. Pick up the cube\n    #  4. Put gripper above the bin\n    #  5. Drop gripper around the bin\n    #  6. Place the cube in the bin\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up with the cube, drop the gripper around the cube.\n    if check("the robot\'s gripper is vertically aligned with cube and the robot\'s gripper is not around cube"):\n        robot.push("window right harder")\n    # If the gripper is around the cube, pick it up.\n    if check("the robot\'s gripper is around cube"):\n        robot.push("the gripper into the puck")\n    # Now, put the gripper above the bin.\n    if check("the robot\'s gripper is not vertically aligned with bin"):\n        robot.reach("to goal")\n    # If the gripper is lined up with the bin, drop the gripper around the bin.\n    if check("the robot\'s gripper is vertically aligned with bin and the robot\'s gripper is not around bin"):\n        robot.put("gripper above door handle")\n    # If the gripper is around the bin, place the cube in the bin.\n    if check("the robot\'s gripper is around bin"):\n        robot.place("gripper above puck")\n',
        ),
    ],
    "box-close": [
        (
            -79.19406,
            '\n    #  1. Pick up the box lid\n    #  2. Put the box lid on the box\n    # First, pick up the box lid.\n    if check("the robot\'s gripper is not around the box lid"):\n        robot.slide("the puck to the goal")\n    # Now that the robot has the box lid, put it on the box.\n    if check("the robot\'s gripper is around the box lid"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -79.24704,
            '\n    #  1. Pick up the box lid\n    #  2. Put the box lid on the box\n    # First, pick up the box lid.\n    if check("the robot\'s gripper is not around the box lid"):\n        robot.slide("the puck to the goal")\n    # Now that the robot has the box lid, put it on the box.\n    if check("the robot\'s gripper is around the box lid"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -79.25777,
            '\n    #  1. Pick up the box lid\n    #  2. Put the box lid on the box\n    # First, pick up the box lid.\n    if check("the robot\'s gripper is not around the box lid"):\n        robot.slide("the puck to the goal")\n    # Now that the robot has the box lid, put it on the box.\n    if check("the robot\'s gripper is around the box lid"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -79.27851,
            '\n    #  1. Pick up the box lid\n    #  2. Put the box lid on the box\n    # First, pick up the box lid.\n    if check("the robot\'s gripper is not around the box lid"):\n        robot.slide("the puck to the goal")\n    # Now that the robot has the box lid, put it on the box.\n    if check("the robot\'s gripper is around the box lid"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -79.470856,
            '\n    #  1. Pick up the box lid\n    #  2. Put the box lid on the box\n    # First, pick up the box lid.\n    if check("the robot\'s gripper is not around the box lid"):\n        robot.slide("the puck to the goal")\n    # Now that the robot has the box lid, put it on the box.\n    if check("the robot\'s gripper is around the box lid"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -79.51633,
            '\n    #  1. Pick up the box lid\n    #  2. Put the box lid on the box\n    # First, pick up the box lid.\n    if check("the robot\'s gripper is not around the box lid"):\n        robot.slide("the puck to the goal")\n    # Now that the robot has the box lid, put it on the box.\n    if check("the robot\'s gripper is around the box lid"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -104.51176,
            '\n    #  1. Pick up the box lid\n    #  2. Put the box lid on the box\n    #  3. Push the box lid down\n    # First, pick up the box lid.\n    if check("the robot\'s gripper is not around the box lid"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is around the box lid, put it on the box.\n    if check("the robot\'s gripper is around the box lid"):\n        robot.close("gripper around puck")\n    # If the box lid is on the box, push it down.\n    if check("the robot\'s gripper is around the box lid and the box lid is on the box"):\n        robot.put("gripper above drawer handle")\n',
        ),
        (
            -114.42283,
            '\n    #  1. Put gripper above the box lid\n    #  2. Drop gripper around the box lid\n    #  3. Pick up the box lid\n    #  4. Put the box lid on the box\n    # First, put the gripper above the box lid.\n    if check("the robot\'s gripper is not vertically aligned with the box lid"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the box lid, we should be able to\n    # grab it by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with the box lid and the robot\'s gripper is not around box lid"):\n        robot.reach("to goal")\n    # Once the gripper is around the box lid, we can just pick it up.\n    if check("the robot\'s gripper is around box lid"):\n        robot.slide("window right")\n    # Once we\'ve picked up the box lid, we can put it on the box.\n    if check("the robot\'s gripper is holding box lid"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "button-press": [
        (
            -70.116394,
            '\n    #  1. Line up the gripper as viewed from the front\n    #  2. Push down on the button from the front\n    # Because this is "front", we just need to line up the gripper from the front.\n    # Line up the robot\'s gripper from the front.\n    if check("the robot\'s gripper is not horizontally aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is horizontally aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -70.14296,
            '\n    #  1. Line up the gripper as viewed from the front\n    #  2. Push down on the button from the front\n    # Because this is "front", we just need to line up the gripper from the front.\n    # Line up the robot\'s gripper from the front.\n    if check("the robot\'s gripper is not horizontally aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is horizontally aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -70.14973,
            '\n    #  1. Line up the gripper as viewed from the front\n    #  2. Push down on the button from the front\n    # Because this is "front", we just need to line up the gripper from the front.\n    # Line up the robot\'s gripper from the front.\n    if check("the robot\'s gripper is not horizontally aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is horizontally aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -70.164,
            '\n    #  1. Line up the gripper as viewed from the front\n    #  2. Push down on the button from the front\n    # Because this is "front", we just need to line up the gripper from the front.\n    # Line up the robot\'s gripper from the front.\n    if check("the robot\'s gripper is not horizontally aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is horizontally aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -70.167145,
            '\n    #  1. Line up the gripper as viewed from the front\n    #  2. Push down on the button from the front\n    # Because this is "front", we just need to line up the gripper from the front.\n    # Line up the robot\'s gripper from the front.\n    if check("the robot\'s gripper is not horizontally aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is horizontally aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -70.179565,
            '\n    #  1. Line up the gripper as viewed from the front\n    #  2. Push down on the button from the front\n    # Because this is "front", we just need to line up the gripper from the front.\n    # Line up the robot\'s gripper from the front.\n    if check("the robot\'s gripper is not horizontally aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is horizontally aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -70.19151,
            '\n    #  1. Line up the gripper as viewed from the front\n    #  2. Push down on the button from the front\n    # Because this is "front", we just need to line up the gripper from the front.\n    # Line up the robot\'s gripper from the front.\n    if check("the robot\'s gripper is not horizontally aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is horizontally aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -70.201965,
            '\n    #  1. Line up the gripper as viewed from the front\n    #  2. Push down on the button from the front\n    # Because this is "front", we just need to line up the gripper from the front.\n    # Line up the robot\'s gripper from the front.\n    if check("the robot\'s gripper is not horizontally aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is horizontally aligned with button"):\n        robot.reach("to goal")\n',
        ),
    ],
    "button-press-topdown": [
        (
            -61.262115,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -61.345524,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -61.355316,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -61.360867,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -61.3665,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -61.372517,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -61.37859,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -61.37965,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
    ],
    "button-press-topdown-wall": [
        (
            -62.84551,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -62.849297,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -62.90779,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -62.95024,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -62.9541,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -62.98284,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -62.989513,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -62.997322,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
    ],
    "button-press-wall": [
        (
            -65.58791,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "wall", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -65.64779,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Push down on the button from the top\n    # Because this is "wall", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -74.52567,
            '\n    #  1. Put gripper above the button\n    #  2. Push down on the button from the top\n    # Because this is "wall", we just need to line up the gripper from in front.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -74.57567,
            '\n    #  1. Put gripper above the button\n    #  2. Push down on the button from the top\n    # Because this is "wall", we just need to line up the gripper from in front.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -74.72528,
            '\n    #  1. Put gripper above the button\n    #  2. Push down on the button from the top\n    # Because this is "wall", we just need to line up the gripper from in front.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -74.72994,
            '\n    #  1. Put gripper above the button\n    #  2. Push down on the button from the top\n    # Because this is "wall", we just need to line up the gripper from in front.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -74.803185,
            '\n    #  1. Put gripper above the button\n    #  2. Push down on the button from the top\n    # Because this is "wall", we just need to line up the gripper from in front.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
        (
            -74.82634,
            '\n    #  1. Put gripper above the button\n    #  2. Push down on the button from the top\n    # Because this is "wall", we just need to line up the gripper from in front.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with button"):\n        robot.reach("to goal")\n',
        ),
    ],
    "coffee-button": [
        (
            -77.55113,
            '\n    #  1. Put gripper above the coffee button\n    #  2. Push down on the coffee button\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with coffee button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with coffee button"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.552216,
            '\n    #  1. Put gripper above the coffee button\n    #  2. Push down on the coffee button\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with coffee button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with coffee button"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.6073,
            '\n    #  1. Put gripper above the coffee button\n    #  2. Push down on the coffee button\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with coffee button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with coffee button"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.61822,
            '\n    #  1. Put gripper above the coffee button\n    #  2. Push down on the coffee button\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with coffee button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with coffee button"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.624146,
            '\n    #  1. Put gripper above the coffee button\n    #  2. Push down on the coffee button\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with coffee button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with coffee button"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.65121,
            '\n    #  1. Put gripper above the coffee button\n    #  2. Push down on the coffee button\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with coffee button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with coffee button"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.655594,
            '\n    #  1. Put gripper above the coffee button\n    #  2. Push down on the coffee button\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with coffee button"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the button.\n    if check("the robot\'s gripper is vertically aligned with coffee button"):\n        robot.reach("to goal")\n',
        ),
        (
            -79.09871,
            '\n    #  1. Put gripper above the coffee button\n    #  2. Push down on the coffee button\n    # Put the gripper above the coffee button.\n    if check("the robot\'s gripper is not vertically aligned with coffee button"):\n        robot.slide("the puck to the goal")\n    # Push down on the coffee button.\n    if check("the robot\'s gripper is vertically aligned with coffee button"):\n        robot.reach("to goal")\n',
        ),
    ],
    "coffee-pull": [
        (
            -95.2021,
            '\n    #  1. Put gripper above mug\n    #  2. Drop gripper around mug\n    #  3. Pull mug to target location\n    # First, put the gripper mostly above the mug.\n    if check("the robot\'s gripper is not almost vertically aligned with mug"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with mug and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the mug,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with mug"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.21745,
            '\n    #  1. Put gripper above mug\n    #  2. Drop gripper around mug\n    #  3. Pull mug to target location\n    # First, put the gripper mostly above the mug.\n    if check("the robot\'s gripper is not almost vertically aligned with mug"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with mug and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the mug,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with mug"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.2865,
            '\n    #  1. Put gripper above mug\n    #  2. Drop gripper around mug\n    #  3. Pull mug to target location\n    # First, put the gripper mostly above the mug.\n    if check("the robot\'s gripper is not almost vertically aligned with mug"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with mug and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the mug,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with mug"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.28676,
            '\n    #  1. Put gripper above mug\n    #  2. Drop gripper around mug\n    #  3. Pull mug to target location\n    # First, put the gripper mostly above the mug.\n    if check("the robot\'s gripper is not almost vertically aligned with mug"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with mug and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the mug,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with mug"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.28822,
            '\n    #  1. Put gripper above mug\n    #  2. Drop gripper around mug\n    #  3. Pull mug to target location\n    # First, put the gripper mostly above the mug.\n    if check("the robot\'s gripper is not almost vertically aligned with mug"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with mug and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the mug,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with mug"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.3068,
            '\n    #  1. Put gripper above mug\n    #  2. Drop gripper around mug\n    #  3. Pull mug to target location\n    # First, put the gripper mostly above the mug.\n    if check("the robot\'s gripper is not almost vertically aligned with mug"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with mug and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the mug,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with mug"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -96.09018,
            '\n    #  1. Put gripper above the mug\n    #  2. Drop gripper around the mug\n    #  3. Pull the mug to the target location\n    # First, put the gripper above the mug.\n    if check("the robot\'s gripper is not almost vertically aligned with the mug"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the mug and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the mug, it\'s being\n    # opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the mug"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -98.23988,
            '\n    #  1. Put gripper above mug\n    #  2. Drop gripper around mug\n    #  3. Pull mug to target location\n    # First, put the gripper above the mug.\n    if check("the robot\'s gripper is not vertically aligned with the mug"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the mug and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the mug,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the mug"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "coffee-push": [
        (
            -71.98401,
            '\n    #  1. Grab the mug\n    #  2. Move the mug to the target location\n    # Grab the mug.\n    if check("the robot\'s gripper is not around the mug"):\n        robot.slide("the puck to the goal")\n    # Move the mug to the target location.\n    if check("the robot\'s gripper is around the mug"):\n        robot.put("gripper around drawer handle")\n',
        ),
        (
            -74.651665,
            '\n    #  1. Grab the mug with the gripper\n    #  2. Move the gripper to the target location\n    # Grab the mug with the gripper.\n    if check("the robot\'s gripper is not around the mug"):\n        robot.slide("the puck to the goal")\n    # Move the gripper to the target location.\n    if check("the robot\'s gripper is around the mug"):\n        robot.put("gripper around drawer handle")\n',
        ),
        (
            -74.73792,
            '\n    #  1. Grab the mug with the gripper\n    #  2. Move the gripper to the target location\n    # Grab the mug with the gripper.\n    if check("the robot\'s gripper is not around the mug"):\n        robot.slide("the puck to the goal")\n    # Move the gripper to the target location.\n    if check("the robot\'s gripper is around the mug"):\n        robot.put("gripper around drawer handle")\n',
        ),
        (
            -74.765396,
            '\n    #  1. Grab the mug with the gripper\n    #  2. Move the gripper to the target location\n    # Grab the mug with the gripper.\n    if check("the robot\'s gripper is not around the mug"):\n        robot.slide("the puck to the goal")\n    # Move the gripper to the target location.\n    if check("the robot\'s gripper is around the mug"):\n        robot.put("gripper around drawer handle")\n',
        ),
        (
            -74.83392,
            '\n    #  1. Grab the mug with the gripper\n    #  2. Move the gripper to the target location\n    # Grab the mug with the gripper.\n    if check("the robot\'s gripper is not around the mug"):\n        robot.slide("the puck to the goal")\n    # Move the gripper to the target location.\n    if check("the robot\'s gripper is around the mug"):\n        robot.put("gripper around drawer handle")\n',
        ),
        (
            -74.88099,
            '\n    #  1. Grab the mug with the gripper\n    #  2. Move the gripper to the target location\n    # Grab the mug with the gripper.\n    if check("the robot\'s gripper is not around the mug"):\n        robot.slide("the puck to the goal")\n    # Move the gripper to the target location.\n    if check("the robot\'s gripper is around the mug"):\n        robot.put("gripper around drawer handle")\n',
        ),
        (
            -74.8935,
            '\n    #  1. Grab the mug with the gripper\n    #  2. Move the gripper to the target location\n    # Grab the mug with the gripper.\n    if check("the robot\'s gripper is not around the mug"):\n        robot.slide("the puck to the goal")\n    # Move the gripper to the target location.\n    if check("the robot\'s gripper is around the mug"):\n        robot.put("gripper around drawer handle")\n',
        ),
        (
            -112.04729,
            '\n    #  1. Put gripper above the mug\n    #  2. Grab the mug\n    #  3. Align the mug to the target location\n    #  4. Push the mug to the target location\n    # First, put the gripper above the mug.\n    if check("the robot\'s gripper is not vertically aligned with the mug"):\n        robot.slide("the puck to the goal")\n    # If the mug becomes left of the gripper, go back to putting the gripper\n    # above the mug.\n    if check("the mug is not left of the robot\'s gripper"):\n        robot.put("gripper around drawer handle")\n    # As long the gripper is still mostly around the mug and the mug isn\'t lined\n    # up with the hole, line up the mug with the hole.\n    if check("the robot\'s gripper is forward aligned with the mug and the mug is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the mug is lined up with the hole to the side, insert it.\n    if check("the mug is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
    ],
    "dial-turn": [
        (
            -82.39091,
            '\n    #  1. Put gripper above the dial\n    #  2. Turn the dial\n    # If the robot\'s gripper is not vertically aligned with the dial, put it\n    # above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # Turn the dial.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -82.40061,
            '\n    #  1. Put gripper above the dial\n    #  2. Turn the dial\n    # If the robot\'s gripper is not vertically aligned with the dial, put it\n    # above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # Turn the dial.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -82.44887,
            '\n    #  1. Put gripper above the dial\n    #  2. Turn the dial\n    # If the robot\'s gripper is not vertically aligned with the dial, put it\n    # above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # Turn the dial.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -82.48731,
            '\n    #  1. Put gripper above the dial\n    #  2. Turn the dial\n    # If the robot\'s gripper is not vertically aligned with the dial, put it\n    # above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # Turn the dial.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -82.50726,
            '\n    #  1. Put gripper above the dial\n    #  2. Turn the dial\n    # If the robot\'s gripper is not vertically aligned with the dial, put it\n    # above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # Turn the dial.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -82.60402,
            '\n    #  1. Put gripper above the dial\n    #  2. Turn the dial\n    # If the robot\'s gripper is not vertically aligned with the dial, put it\n    # above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # Turn the dial.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.698074,
            '\n    #  1. Put gripper above the dial\n    #  2. Drop gripper around the dial\n    #  3. Turn the dial\n    # First, put the gripper above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the dial and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the dial,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -102.74669,
            '\n    #  1. Put gripper right of the dial\n    #  2. Start pushing against the dial to turn it\n    #  3. Push the dial harder\n    # If the robot\'s gripper is not vertically lined up with the dial, we should\n    # move the gripper near the dial to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the dial and the robot\'s gripper is below the dial"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the dial we can probably turn the dial now\n    # by moving the gripper left.\n    if check("the robot\'s gripper is near the dial"):\n        robot.drop("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the dial, push\n    # harder.\n    if check("the robot\'s gripper is in front of the dial"):\n        robot.put("gripper around drawer handle")\n',
        ),
    ],
    "disassemble": [
        (
            -53.108807,
            '\n    #  1. Pull the wrench off the peg\n    # If the wrench is still on the peg, pull it off.\n    if check("the wrench is on the peg"):\n        robot.slide("the puck to the goal")\n',
        ),
        (
            -85.03196,
            '\n    #  1. Put gripper above the wrench\n    #  2. Grab the wrench with the gripper\n    #  3. Pull the wrench off the peg\n    # First, put the gripper above the wrench.\n    if check("the robot\'s gripper is not vertically aligned with the wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench becomes left of the gripper, go back to putting the gripper\n    # above the wrench.\n    # Because the wrench is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("wrench is not left of the robot\'s gripper and wrench is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the wrench and the wrench isn\'t\n    # lined up with the hole, line up the wrench with the hole.\n    if check("the robot\'s gripper is forward aligned with the wrench and the wrench is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the wrench is lined up with the hole to the side, insert it.\n    if check("wrench is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -85.06354,
            '\n    #  1. Put gripper above the wrench\n    #  2. Grab the wrench with the gripper\n    #  3. Pull the wrench off the peg\n    # First, put the gripper above the wrench.\n    if check("the robot\'s gripper is not vertically aligned with the wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench becomes left of the gripper, go back to putting the gripper\n    # above the wrench.\n    # Because the wrench is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("wrench is not left of the robot\'s gripper and wrench is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the wrench and the wrench isn\'t\n    # lined up with the hole, line up the wrench with the hole.\n    if check("the robot\'s gripper is forward aligned with the wrench and the wrench is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the wrench is lined up with the hole to the side, insert it.\n    if check("wrench is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -85.0776,
            '\n    #  1. Put gripper above the wrench\n    #  2. Grab the wrench with the gripper\n    #  3. Pull the wrench off the peg\n    # First, put the gripper above the wrench.\n    if check("the robot\'s gripper is not vertically aligned with the wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench becomes left of the gripper, go back to putting the gripper\n    # above the wrench.\n    # Because the wrench is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("wrench is not left of the robot\'s gripper and wrench is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the wrench and the wrench isn\'t\n    # lined up with the hole, line up the wrench with the hole.\n    if check("the robot\'s gripper is forward aligned with the wrench and the wrench is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the wrench is lined up with the hole to the side, insert it.\n    if check("wrench is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -85.08801,
            '\n    #  1. Put gripper above the wrench\n    #  2. Grab the wrench with the gripper\n    #  3. Pull the wrench off the peg\n    # First, put the gripper above the wrench.\n    if check("the robot\'s gripper is not vertically aligned with the wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench becomes left of the gripper, go back to putting the gripper\n    # above the wrench.\n    # Because the wrench is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("wrench is not left of the robot\'s gripper and wrench is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the wrench and the wrench isn\'t\n    # lined up with the hole, line up the wrench with the hole.\n    if check("the robot\'s gripper is forward aligned with the wrench and the wrench is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the wrench is lined up with the hole to the side, insert it.\n    if check("wrench is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -85.09715,
            '\n    #  1. Put gripper above the wrench\n    #  2. Grab the wrench with the gripper\n    #  3. Pull the wrench off the peg\n    # First, put the gripper above the wrench.\n    if check("the robot\'s gripper is not vertically aligned with the wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench becomes left of the gripper, go back to putting the gripper\n    # above the wrench.\n    # Because the wrench is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("wrench is not left of the robot\'s gripper and wrench is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the wrench and the wrench isn\'t\n    # lined up with the hole, line up the wrench with the hole.\n    if check("the robot\'s gripper is forward aligned with the wrench and the wrench is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the wrench is lined up with the hole to the side, insert it.\n    if check("wrench is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -85.15015,
            '\n    #  1. Put gripper above the wrench\n    #  2. Grab the wrench with the gripper\n    #  3. Pull the wrench off the peg\n    # First, put the gripper above the wrench.\n    if check("the robot\'s gripper is not vertically aligned with the wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench becomes left of the gripper, go back to putting the gripper\n    # above the wrench.\n    # Because the wrench is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("wrench is not left of the robot\'s gripper and wrench is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the wrench and the wrench isn\'t\n    # lined up with the hole, line up the wrench with the hole.\n    if check("the robot\'s gripper is forward aligned with the wrench and the wrench is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the wrench is lined up with the hole to the side, insert it.\n    if check("wrench is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -106.9815,
            '\n    #  1. Put gripper above the wrench\n    #  2. Grab the wrench with the gripper\n    #  3. Pull the wrench off the peg\n    # First, put the gripper above the wrench.\n    if check("the robot\'s gripper is not vertically aligned with the wrench"):\n        robot.slide("the puck to the goal")\n    # If the wrench becomes left of the gripper, go back to putting the gripper\n    # above the wrench.\n    if check("wrench is not left of the robot\'s gripper and wrench is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the wrench and the wrench isn\'t\n    # lined up with the hole, line up the wrench with the hole.\n    if check("the robot\'s gripper is forward aligned with the wrench and the wrench is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the wrench is lined up with the hole to the side, insert it.\n    if check("wrench is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
    ],
    "door-close": [
        (
            -89.60498,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Push door closed\n    # We need to put the gripper above the door handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the door handle, we should be able to\n    # grab the door handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with door handle and the robot\'s gripper is not around door handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the door handle, we can just push the door\n    # closed.\n    if check("the robot\'s gripper is around door handle"):\n        robot.put("gripper above peg")\n',
        ),
        (
            -89.72103,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Push door closed\n    # We need to put the gripper above the door handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the door handle, we should be able to\n    # grab the door handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with door handle and the robot\'s gripper is not around door handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the door handle, we can just push the door\n    # closed.\n    if check("the robot\'s gripper is around door handle"):\n        robot.put("gripper above peg")\n',
        ),
        (
            -89.74407,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Push door closed\n    # We need to put the gripper above the door handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the door handle, we should be able to\n    # grab the door handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with door handle and the robot\'s gripper is not around door handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the door handle, we can just push the door\n    # closed.\n    if check("the robot\'s gripper is around door handle"):\n        robot.put("gripper above peg")\n',
        ),
        (
            -89.7606,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Push door closed\n    # We need to put the gripper above the door handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the door handle, we should be able to\n    # grab the door handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with door handle and the robot\'s gripper is not around door handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the door handle, we can just push the door\n    # closed.\n    if check("the robot\'s gripper is around door handle"):\n        robot.put("gripper above peg")\n',
        ),
        (
            -89.77382,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Push door closed\n    # We need to put the gripper above the door handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the door handle, we should be able to\n    # grab the door handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with door handle and the robot\'s gripper is not around door handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the door handle, we can just push the door\n    # closed.\n    if check("the robot\'s gripper is around door handle"):\n        robot.put("gripper above peg")\n',
        ),
        (
            -89.80773,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Push door closed\n    # We need to put the gripper above the door handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the door handle, we should be able to\n    # grab the door handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with door handle and the robot\'s gripper is not around door handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the door handle, we can just push the door\n    # closed.\n    if check("the robot\'s gripper is around door handle"):\n        robot.put("gripper above peg")\n',
        ),
        (
            -90.80349,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull closed the door\n    # We need to put the gripper above the door handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the door handle, we should be able to\n    # grab the door handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with door handle and the robot\'s gripper is not around door handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the door handle, we can just pull the door\n    # closed.\n    if check("the robot\'s gripper is around door handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.50922,
            '\n    #  1. Put gripper right of the door handle\n    #  2. Start pushing against the door handle to close the door\n    #  3. Push the door closed harder\n    # If the robot\'s gripper is not vertically lined up with the door handle,\n    # we should move the gripper near the door handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the door handle and the robot\'s gripper is below the door handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the door handle we can probably slide the\n    # door open now by moving the gripper left.\n    if check("the robot\'s gripper is near the door handle"):\n        robot.drop("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the door handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the door handle"):\n        robot.reach("to goal")\n',
        ),
    ],
    "door-lock": [
        (
            -89.66214,
            '\n    #  1. Put gripper above door lock\n    #  2. Turn the dial on the door lock\n    # First, put the gripper above the door lock.\n    if check("the robot\'s gripper is not vertically aligned with the door lock"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the door lock, we can turn it.\n    if check("the robot\'s gripper is vertically aligned with the door lock"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -89.72988,
            '\n    #  1. Put gripper above door lock\n    #  2. Turn the dial on the door lock\n    # First, put the gripper above the door lock.\n    if check("the robot\'s gripper is not vertically aligned with the door lock"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the door lock, we can turn it.\n    if check("the robot\'s gripper is vertically aligned with the door lock"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -89.73424,
            '\n    #  1. Put gripper above door lock\n    #  2. Turn the dial on the door lock\n    # First, put the gripper above the door lock.\n    if check("the robot\'s gripper is not vertically aligned with the door lock"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the door lock, we can turn it.\n    if check("the robot\'s gripper is vertically aligned with the door lock"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -89.76291,
            '\n    #  1. Put gripper above door lock\n    #  2. Turn the dial on the door lock\n    # First, put the gripper above the door lock.\n    if check("the robot\'s gripper is not vertically aligned with the door lock"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the door lock, we can turn it.\n    if check("the robot\'s gripper is vertically aligned with the door lock"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -89.82926,
            '\n    #  1. Put gripper above door lock\n    #  2. Turn the dial on the door lock\n    # First, put the gripper above the door lock.\n    if check("the robot\'s gripper is not vertically aligned with the door lock"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the door lock, we can turn it.\n    if check("the robot\'s gripper is vertically aligned with the door lock"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -89.841484,
            '\n    #  1. Put gripper above door lock\n    #  2. Turn the dial on the door lock\n    # First, put the gripper above the door lock.\n    if check("the robot\'s gripper is not vertically aligned with the door lock"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the door lock, we can turn it.\n    if check("the robot\'s gripper is vertically aligned with the door lock"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -101.48152,
            '\n    #  1. Put gripper above the door handle\n    #  2. Drop gripper around door handle\n    #  3. Turn the door handle\n    # First, put the gripper above the door handle.\n    if check("the robot\'s gripper is not vertically aligned with the door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -107.39345,
            '\n    #  1. Put gripper above the dial\n    #  2. Rotate the dial counterclockwise\n    #  3. Rotate the dial clockwise\n    # First, put the gripper above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # Rotate the dial counterclockwise.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.close("gripper around puck")\n    # Rotate the dial clockwise.\n    if check("the robot\'s gripper is around the dial"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "door-open": [
        (
            -79.955765,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull open the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -80.08562,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull open the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -80.117226,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull open the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -80.123856,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull open the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -80.14827,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull open the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -80.18202,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull open the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -80.27696,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull open the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -80.328926,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Pull open the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.put("the gripper above the puck")\n',
        ),
    ],
    "door-unlock": [
        (
            -74.51241,
            '\n    #  1. Put gripper near the dial\n    #  2. Turn the dial\n    if check("the robot\'s gripper is not near the dial"):\n        robot.slide("the puck to the goal")\n    if check("the robot\'s gripper is near the dial"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -87.88745,
            '\n    #  1. Put gripper above the dial\n    #  2. Turn the dial to unlock the door\n    # First, put the gripper above the dial.\n    if check("the robot\'s gripper is not vertically aligned with the dial"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the dial, turn the dial to unlock the door.\n    if check("the robot\'s gripper is vertically aligned with the dial"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -101.08667,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Turn the dial on the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.108955,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Turn the dial on the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.21658,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Turn the dial on the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.22814,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Turn the dial on the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.302284,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Turn the dial on the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.37803,
            '\n    #  1. Put gripper above door handle\n    #  2. Drop gripper around door handle\n    #  3. Turn the dial on the door\n    # First, put the gripper mostly above the door handle.\n    if check("the robot\'s gripper is not almost vertically aligned with door handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):\n        robot.place("gripper above puck")\n    # As long as the gripper is still vertically aligned with the door handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the door handle"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "drawer-close": [
        (
            -70.182724,
            '\n    #  1. Put gripper roughly around the drawer handle\n    #  2. Push the drawer closed\n    # If the gripper is not near the drawer handle, move it to the drawer\n    # handle.\n    # We don\'t need to be careful about the direction, since the drawer is large\n    # and we\'re just pushing it (unlike when opening the drawer).\n    if check("the robot\'s gripper is not near the drawer handle"):\n        robot.slide("the puck to the goal")\n    # If the drawer is aligned with the gripper as seen from in front, we can\n    # push the drawer closed.\n    if check("the robot\'s gripper is forward aligned with drawer handle"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -70.235504,
            '\n    #  1. Put gripper roughly around the drawer handle\n    #  2. Push the drawer closed\n    # If the gripper is not near the drawer handle, move it to the drawer\n    # handle.\n    # We don\'t need to be careful about the direction, since the drawer is large\n    # and we\'re just pushing it (unlike when opening the drawer).\n    if check("the robot\'s gripper is not near the drawer handle"):\n        robot.slide("the puck to the goal")\n    # If the drawer is aligned with the gripper as seen from in front, we can\n    # push the drawer closed.\n    if check("the robot\'s gripper is forward aligned with drawer handle"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -70.26167,
            '\n    #  1. Put gripper roughly around the drawer handle\n    #  2. Push the drawer closed\n    # If the gripper is not near the drawer handle, move it to the drawer\n    # handle.\n    # We don\'t need to be careful about the direction, since the drawer is large\n    # and we\'re just pushing it (unlike when opening the drawer).\n    if check("the robot\'s gripper is not near the drawer handle"):\n        robot.slide("the puck to the goal")\n    # If the drawer is aligned with the gripper as seen from in front, we can\n    # push the drawer closed.\n    if check("the robot\'s gripper is forward aligned with drawer handle"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -70.27327,
            '\n    #  1. Put gripper roughly around the drawer handle\n    #  2. Push the drawer closed\n    # If the gripper is not near the drawer handle, move it to the drawer\n    # handle.\n    # We don\'t need to be careful about the direction, since the drawer is large\n    # and we\'re just pushing it (unlike when opening the drawer).\n    if check("the robot\'s gripper is not near the drawer handle"):\n        robot.slide("the puck to the goal")\n    # If the drawer is aligned with the gripper as seen from in front, we can\n    # push the drawer closed.\n    if check("the robot\'s gripper is forward aligned with drawer handle"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -70.273346,
            '\n    #  1. Put gripper roughly around the drawer handle\n    #  2. Push the drawer closed\n    # If the gripper is not near the drawer handle, move it to the drawer\n    # handle.\n    # We don\'t need to be careful about the direction, since the drawer is large\n    # and we\'re just pushing it (unlike when opening the drawer).\n    if check("the robot\'s gripper is not near the drawer handle"):\n        robot.slide("the puck to the goal")\n    # If the drawer is aligned with the gripper as seen from in front, we can\n    # push the drawer closed.\n    if check("the robot\'s gripper is forward aligned with drawer handle"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -70.28209,
            '\n    #  1. Put gripper roughly around the drawer handle\n    #  2. Push the drawer closed\n    # If the gripper is not near the drawer handle, move it to the drawer\n    # handle.\n    # We don\'t need to be careful about the direction, since the drawer is large\n    # and we\'re just pushing it (unlike when opening the drawer).\n    if check("the robot\'s gripper is not near the drawer handle"):\n        robot.slide("the puck to the goal")\n    # If the drawer is aligned with the gripper as seen from in front, we can\n    # push the drawer closed.\n    if check("the robot\'s gripper is forward aligned with drawer handle"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -70.28549,
            '\n    #  1. Put gripper roughly around the drawer handle\n    #  2. Push the drawer closed\n    # If the gripper is not near the drawer handle, move it to the drawer\n    # handle.\n    # We don\'t need to be careful about the direction, since the drawer is large\n    # and we\'re just pushing it (unlike when opening the drawer).\n    if check("the robot\'s gripper is not near the drawer handle"):\n        robot.slide("the puck to the goal")\n    # If the drawer is aligned with the gripper as seen from in front, we can\n    # push the drawer closed.\n    if check("the robot\'s gripper is forward aligned with drawer handle"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -70.29192,
            '\n    #  1. Put gripper roughly around the drawer handle\n    #  2. Push the drawer closed\n    # If the gripper is not near the drawer handle, move it to the drawer\n    # handle.\n    # We don\'t need to be careful about the direction, since the drawer is large\n    # and we\'re just pushing it (unlike when opening the drawer).\n    if check("the robot\'s gripper is not near the drawer handle"):\n        robot.slide("the puck to the goal")\n    # If the drawer is aligned with the gripper as seen from in front, we can\n    # push the drawer closed.\n    if check("the robot\'s gripper is forward aligned with drawer handle"):\n        robot.drop("gripper around puck")\n',
        ),
    ],
    "drawer-open": [
        (
            -79.410194,
            '\n    #  1. Put gripper above drawer handle\n    #  2. Drop gripper around drawer handle\n    #  3. Pull open the drawer\n    # We need to put the gripper above the drawer handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with drawer handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab the drawer handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -79.43098,
            '\n    #  1. Put gripper above drawer handle\n    #  2. Drop gripper around drawer handle\n    #  3. Pull open the drawer\n    # We need to put the gripper above the drawer handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with drawer handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab the drawer handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -79.43234,
            '\n    #  1. Put gripper above drawer handle\n    #  2. Drop gripper around drawer handle\n    #  3. Pull open the drawer\n    # We need to put the gripper above the drawer handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with drawer handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab the drawer handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -79.44438,
            '\n    #  1. Put gripper above drawer handle\n    #  2. Drop gripper around drawer handle\n    #  3. Pull open the drawer\n    # We need to put the gripper above the drawer handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with drawer handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab the drawer handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -79.48013,
            '\n    #  1. Put gripper above drawer handle\n    #  2. Drop gripper around drawer handle\n    #  3. Pull open the drawer\n    # We need to put the gripper above the drawer handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with drawer handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab the drawer handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -79.48299,
            '\n    #  1. Put gripper above drawer handle\n    #  2. Drop gripper around drawer handle\n    #  3. Pull open the drawer\n    # We need to put the gripper above the drawer handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with drawer handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab the drawer handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -79.48802,
            '\n    #  1. Put gripper above drawer handle\n    #  2. Drop gripper around drawer handle\n    #  3. Pull open the drawer\n    # We need to put the gripper above the drawer handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with drawer handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab the drawer handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -79.54201,
            '\n    #  1. Put gripper above drawer handle\n    #  2. Drop gripper around drawer handle\n    #  3. Pull open the drawer\n    # We need to put the gripper above the drawer handle before we can grab it,\n    # because of the angle of the robot\'s gripper.\n    if check("the robot\'s gripper is not vertically aligned with drawer handle"):\n        robot.slide("the puck to the goal")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab the drawer handle by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.close("gripper around puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.put("the gripper above the puck")\n',
        ),
    ],
    "faucet-close": [
        (
            -116.677986,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Start turning the faucet handle right\n    #  3. Turn the faucet handle right harder\n    # If the robot\'s gripper is not vertically aligned with the faucet handle,\n    # we should move the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not vertically aligned with the faucet handle and the robot\'s gripper is below the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet handle now by moving the gripper right.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -116.690834,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Turn the faucet right\n    # If the robot\'s gripper is not vertically aligned with the faucet handle,\n    # move the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not vertically aligned with the faucet handle and the robot\'s gripper is below the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet now by moving the gripper right.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -116.77614,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Turn the faucet right\n    # If the robot\'s gripper is not vertically aligned with the faucet handle,\n    # move the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not vertically aligned with the faucet handle and the robot\'s gripper is below the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet now by moving the gripper right.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -116.79464,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Turn the faucet right\n    # If the robot\'s gripper is not vertically aligned with the faucet handle,\n    # move the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not vertically aligned with the faucet handle and the robot\'s gripper is below the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet now by moving the gripper right.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -116.798416,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Turn the faucet right\n    # If the robot\'s gripper is not vertically aligned with the faucet handle,\n    # move the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not vertically aligned with the faucet handle and the robot\'s gripper is below the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet now by moving the gripper right.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -116.83222,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Turn the faucet right\n    # If the robot\'s gripper is not vertically aligned with the faucet handle,\n    # move the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not vertically aligned with the faucet handle and the robot\'s gripper is below the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet now by moving the gripper right.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -116.874626,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Turn the faucet right\n    # If the robot\'s gripper is not vertically aligned with the faucet handle,\n    # move the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not vertically aligned with the faucet handle and the robot\'s gripper is below the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet now by moving the gripper right.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -120.41926,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Start turning the faucet handle right\n    #  3. Turn the faucet handle right harder\n    # If the robot\'s gripper is not right of the faucet handle, we should move\n    # the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not right of the faucet handle and the robot\'s gripper is not near the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet handle now by moving the gripper right.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.put("the gripper above the puck")\n',
        ),
    ],
    "faucet-open": [
        (
            -101.312935,
            '\n    #  1. Put gripper above faucet handle\n    #  2. Turn faucet handle left\n    # If the robot\'s gripper is not above the faucet handle, move it there.\n    if check("the robot\'s gripper is not vertically aligned with faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is above the faucet handle, turn the faucet handle\n    # left.\n    if check("the robot\'s gripper is vertically aligned with faucet handle"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -101.33537,
            '\n    #  1. Put gripper above faucet handle\n    #  2. Turn faucet handle left\n    # If the robot\'s gripper is not above the faucet handle, move it there.\n    if check("the robot\'s gripper is not vertically aligned with faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is above the faucet handle, turn the faucet handle\n    # left.\n    if check("the robot\'s gripper is vertically aligned with faucet handle"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -101.34829,
            '\n    #  1. Put gripper above faucet handle\n    #  2. Turn faucet handle left\n    # If the robot\'s gripper is not above the faucet handle, move it there.\n    if check("the robot\'s gripper is not vertically aligned with faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is above the faucet handle, turn the faucet handle\n    # left.\n    if check("the robot\'s gripper is vertically aligned with faucet handle"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -101.360115,
            '\n    #  1. Put gripper above faucet handle\n    #  2. Turn faucet handle left\n    # If the robot\'s gripper is not above the faucet handle, move it there.\n    if check("the robot\'s gripper is not vertically aligned with faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is above the faucet handle, turn the faucet handle\n    # left.\n    if check("the robot\'s gripper is vertically aligned with faucet handle"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -101.41615,
            '\n    #  1. Put gripper above faucet handle\n    #  2. Turn faucet handle left\n    # If the robot\'s gripper is not above the faucet handle, move it there.\n    if check("the robot\'s gripper is not vertically aligned with faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is above the faucet handle, turn the faucet handle\n    # left.\n    if check("the robot\'s gripper is vertically aligned with faucet handle"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -101.42427,
            '\n    #  1. Put gripper above faucet handle\n    #  2. Turn faucet handle left\n    # If the robot\'s gripper is not above the faucet handle, move it there.\n    if check("the robot\'s gripper is not vertically aligned with faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is above the faucet handle, turn the faucet handle\n    # left.\n    if check("the robot\'s gripper is vertically aligned with faucet handle"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -115.70848,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Start turning the faucet handle left\n    #  3. Turn the faucet handle left harder\n    # If the robot\'s gripper is not vertically aligned with the faucet handle,\n    # we should move the gripper near the faucet handle to start turning\n    if check("the robot\'s gripper is not vertically aligned with the faucet handle and the robot\'s gripper is below the faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet open now by moving the gripper left.\n    if check("the robot\'s gripper is near the faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of the faucet handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -118.667496,
            '\n    #  1. Put gripper right of the faucet handle\n    #  2. Start turning against the faucet handle to open the faucet\n    #  3. Turn the faucet open harder\n    # If the robot\'s gripper is not vertically lined up with the faucet handle,\n    # we should move the gripper near the faucet handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with faucet handle and the robot\'s gripper is below faucet handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the faucet handle we can probably turn the\n    # faucet open now by moving the gripper left.\n    if check("the robot\'s gripper is near faucet handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the faucet handle,\n    # turn harder.\n    if check("the robot\'s gripper is in front of faucet handle"):\n        robot.put("the gripper above the puck")\n',
        ),
    ],
    "hammer": [
        (
            -107.47505,
            '\n    #  1. Put gripper above the nail\n    #  2. Drop gripper around nail\n    #  3. Hit the nail with the hammer\n    # First, put the gripper above the nail.\n    if check("the robot\'s gripper is not vertically aligned with the nail"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is vertically aligned with the nail, drop the\n    # gripper around the nail.\n    if check("the robot\'s gripper is vertically aligned with the nail and the robot\'s gripper is not around the nail"):\n        robot.push("window right harder")\n    # Once the gripper is around the nail, hit the nail with the hammer.\n    if check("the robot\'s gripper is around the nail"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -107.49298,
            '\n    #  1. Put gripper above the nail\n    #  2. Drop gripper around nail\n    #  3. Hit the nail with the hammer\n    # First, put the gripper above the nail.\n    if check("the robot\'s gripper is not vertically aligned with the nail"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is vertically aligned with the nail, drop the\n    # gripper around the nail.\n    if check("the robot\'s gripper is vertically aligned with the nail and the robot\'s gripper is not around the nail"):\n        robot.push("window right harder")\n    # Once the gripper is around the nail, hit the nail with the hammer.\n    if check("the robot\'s gripper is around the nail"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -107.5536,
            '\n    #  1. Put gripper above the nail\n    #  2. Drop gripper around nail\n    #  3. Hit the nail with the hammer\n    # First, put the gripper above the nail.\n    if check("the robot\'s gripper is not vertically aligned with the nail"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is vertically aligned with the nail, drop the\n    # gripper around the nail.\n    if check("the robot\'s gripper is vertically aligned with the nail and the robot\'s gripper is not around the nail"):\n        robot.push("window right harder")\n    # Once the gripper is around the nail, hit the nail with the hammer.\n    if check("the robot\'s gripper is around the nail"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -107.60995,
            '\n    #  1. Put gripper above the nail\n    #  2. Drop gripper around nail\n    #  3. Hit the nail with the hammer\n    # First, put the gripper above the nail.\n    if check("the robot\'s gripper is not vertically aligned with the nail"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is vertically aligned with the nail, drop the\n    # gripper around the nail.\n    if check("the robot\'s gripper is vertically aligned with the nail and the robot\'s gripper is not around the nail"):\n        robot.push("window right harder")\n    # Once the gripper is around the nail, hit the nail with the hammer.\n    if check("the robot\'s gripper is around the nail"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -107.629196,
            '\n    #  1. Put gripper above the nail\n    #  2. Drop gripper around nail\n    #  3. Hit the nail with the hammer\n    # First, put the gripper above the nail.\n    if check("the robot\'s gripper is not vertically aligned with the nail"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is vertically aligned with the nail, drop the\n    # gripper around the nail.\n    if check("the robot\'s gripper is vertically aligned with the nail and the robot\'s gripper is not around the nail"):\n        robot.push("window right harder")\n    # Once the gripper is around the nail, hit the nail with the hammer.\n    if check("the robot\'s gripper is around the nail"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -107.65896,
            '\n    #  1. Put gripper above the nail\n    #  2. Drop gripper around nail\n    #  3. Hit the nail with the hammer\n    # First, put the gripper above the nail.\n    if check("the robot\'s gripper is not vertically aligned with the nail"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is vertically aligned with the nail, drop the\n    # gripper around the nail.\n    if check("the robot\'s gripper is vertically aligned with the nail and the robot\'s gripper is not around the nail"):\n        robot.push("window right harder")\n    # Once the gripper is around the nail, hit the nail with the hammer.\n    if check("the robot\'s gripper is around the nail"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -109.35215,
            '\n    #  1. Put gripper above nail\n    #  2. Drop gripper around nail\n    #  3. Hit nail with hammer\n    # First, put the gripper above the nail.\n    if check("the robot\'s gripper is not vertically aligned with the nail"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the nail and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the nail,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the nail"):\n        robot.put("gripper above drawer handle")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab it by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.put("the gripper above the puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.push("window right harder")\n',
        ),
        (
            -109.37225,
            '\n    #  1. Put gripper above nail\n    #  2. Drop gripper around nail\n    #  3. Hit the nail with the hammer\n    # First, put the gripper above the nail.\n    if check("the robot\'s gripper is not vertically aligned with the nail"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the nail and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the nail,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the nail"):\n        robot.put("gripper above drawer handle")\n    # Once the gripper is lined up above the drawer handle, we should be able to\n    # grab it by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):\n        robot.put("the gripper above the puck")\n    # Once the gripper is around the drawer handle, we can just pull the drawer\n    # open.\n    if check("the robot\'s gripper is around drawer handle"):\n        robot.push("window right harder")\n',
        ),
    ],
    "hand-insert": [
        (
            -63.59139,
            '\n    #  1. Pick up the puck\n    #  2. Move the puck to the target location\n    # If the robot\'s gripper is not around the puck, pick up the puck.\n    if check("the robot\'s gripper is not around the puck"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is around the puck, move the puck to the goal.\n    if check("the robot\'s gripper is around the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -63.6199,
            '\n    #  1. Pick up the puck\n    #  2. Move the puck to the target location\n    # If the robot\'s gripper is not around the puck, pick up the puck.\n    if check("the robot\'s gripper is not around the puck"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is around the puck, move the puck to the goal.\n    if check("the robot\'s gripper is around the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -63.64622,
            '\n    #  1. Pick up the puck\n    #  2. Move the puck to the target location\n    # If the robot\'s gripper is not around the puck, pick up the puck.\n    if check("the robot\'s gripper is not around the puck"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is around the puck, move the puck to the goal.\n    if check("the robot\'s gripper is around the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -63.661507,
            '\n    #  1. Pick up the puck\n    #  2. Move the puck to the target location\n    # If the robot\'s gripper is not around the puck, pick up the puck.\n    if check("the robot\'s gripper is not around the puck"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is around the puck, move the puck to the goal.\n    if check("the robot\'s gripper is around the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -63.663834,
            '\n    #  1. Pick up the puck\n    #  2. Move the puck to the target location\n    # If the robot\'s gripper is not around the puck, pick up the puck.\n    if check("the robot\'s gripper is not around the puck"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is around the puck, move the puck to the goal.\n    if check("the robot\'s gripper is around the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -63.693333,
            '\n    #  1. Pick up the puck\n    #  2. Move the puck to the target location\n    # If the robot\'s gripper is not around the puck, pick up the puck.\n    if check("the robot\'s gripper is not around the puck"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is around the puck, move the puck to the goal.\n    if check("the robot\'s gripper is around the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -100.87898,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Move the gripper to the target location\n    #  5. Drop the puck\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not vertically aligned with the puck"):\n        robot.slide("the puck to the goal")\n    # If the gripper is still above the puck, drop the gripper around the puck.\n    if check("the robot\'s gripper is vertically aligned with the puck and the robot\'s gripper is not around the puck"):\n        robot.push("window right harder")\n    # If the gripper is around the puck, pick up the puck.\n    if check("the robot\'s gripper is around the puck"):\n        robot.put("gripper above drawer handle")\n    # If the gripper is holding the puck, move the gripper to the target location.\n    if check("the robot\'s gripper is holding the puck"):\n        robot.push("the gripper into the puck")\n    # If the gripper is at the target location, drop the puck.\n    if check("the robot\'s gripper is at the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -114.2514,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Put gripper above goal\n    #  5. Drop gripper around goal\n    #  6. Drop puck into goal\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with the puck"):\n        robot.slide("the puck to the goal")\n    # If the gripper is not around the puck, drop it around the puck.\n    if check("the robot\'s gripper is not around the puck"):\n        robot.push("window right harder")\n    # Pick up the puck.\n    if check("the robot\'s gripper is around the puck"):\n        robot.put("gripper above drawer handle")\n    # Put the gripper above the goal.\n    if check("the robot\'s gripper is not almost vertically aligned with the goal"):\n        robot.push("the gripper into the puck")\n    # Drop the puck into the goal.\n    if check("the robot\'s gripper is around the goal"):\n        robot.reach("to goal")\n',
        ),
    ],
    "handle-press": [
        (
            -70.661385,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -71.24578,
            '\n    #  1. Line up the gripper as seen from above\n    #  2. Push down on the handle from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -71.528946,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -71.56245,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -71.59562,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -71.60646,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -71.62906,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -71.65873,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.reach("to goal")\n',
        ),
    ],
    "handle-press-side": [
        (
            -72.158424,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle from the side\n    # Because this is "side", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -72.28842,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle from the side\n    # Because this is "side", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -72.321754,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle from the side\n    # Because this is "side", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -72.362076,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle from the side\n    # Because this is "side", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -72.37213,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle from the side\n    # Because this is "side", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -72.416374,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle from the side\n    # Because this is "side", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -74.116875,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle from the side\n    # Because this is "side", we just need to line up the gripper from the side.\n    # Line up the robot\'s gripper from the side.\n    if check("the robot\'s gripper is not horizontally aligned with handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is horizontally aligned with handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -74.22319,
            '\n    #  1. Put gripper above the handle\n    #  2. Push down on the handle from the side\n    # Because this is "side", we just need to line up the gripper from the side.\n    # Line up the robot\'s gripper from the side.\n    if check("the robot\'s gripper is not horizontally aligned with handle"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just push down on the handle.\n    if check("the robot\'s gripper is horizontally aligned with handle"):\n        robot.reach("to goal")\n',
        ),
    ],
    "handle-pull": [
        (
            -94.08643,
            '\n    #  1. Put gripper above the handle\n    #  2. Drop gripper around the handle\n    #  3. Pull up the handle\n    # First, put the gripper mostly above the handle.\n    if check("the robot\'s gripper is not almost vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -94.205086,
            '\n    #  1. Put gripper above the handle\n    #  2. Drop gripper around the handle\n    #  3. Pull up the handle\n    # First, put the gripper mostly above the handle.\n    if check("the robot\'s gripper is not almost vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -94.229744,
            '\n    #  1. Put gripper above the handle\n    #  2. Drop gripper around the handle\n    #  3. Pull up the handle\n    # First, put the gripper mostly above the handle.\n    if check("the robot\'s gripper is not almost vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -94.25058,
            '\n    #  1. Put gripper above the handle\n    #  2. Drop gripper around the handle\n    #  3. Pull up the handle\n    # First, put the gripper mostly above the handle.\n    if check("the robot\'s gripper is not almost vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -94.28088,
            '\n    #  1. Put gripper above the handle\n    #  2. Drop gripper around the handle\n    #  3. Pull up the handle\n    # First, put the gripper mostly above the handle.\n    if check("the robot\'s gripper is not almost vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -94.35504,
            '\n    #  1. Put gripper above the handle\n    #  2. Drop gripper around the handle\n    #  3. Pull up the handle\n    # First, put the gripper mostly above the handle.\n    if check("the robot\'s gripper is not almost vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -96.01909,
            '\n    #  1. Put gripper above handle\n    #  2. Drop gripper around handle\n    #  3. Pull up on handle\n    # First, put the gripper mostly above the handle.\n    if check("the robot\'s gripper is not almost vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -98.49306,
            '\n    #  1. Put gripper above the handle\n    #  2. Drop gripper around the handle\n    #  3. Pull up the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with handle"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "handle-pull-side": [
        (
            -86.70476,
            '\n    #  1. Put gripper above the handle\n    #  2. Grab the handle with the gripper\n    #  3. Pull up on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # If the handle is left of the gripper, go back to putting the gripper\n    # above the handle.\n    # Because the handle is a long object, check if the gripper is lined up with\n    # it from the front instead of around it.\n    if check("the handle is not left of the robot\'s gripper and the handle is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the handle and the handle isn\'t\n    # lined up with the goal, line up the handle with the goal.\n    if check("the robot\'s gripper is forward aligned with the handle and the handle is not horizontally aligned with goal"):\n        robot.put("gripper around drawer handle")\n    # If the handle is lined up with the goal to the side, pull it.\n    if check("the handle is horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -86.74781,
            '\n    #  1. Put gripper above the handle\n    #  2. Grab the handle with the gripper\n    #  3. Pull up on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # If the handle is left of the gripper, go back to putting the gripper\n    # above the handle.\n    # Because the handle is a long object, check if the gripper is lined up with\n    # it from the front instead of around it.\n    if check("the handle is not left of the robot\'s gripper and the handle is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the handle and the handle isn\'t\n    # lined up with the goal, line up the handle with the goal.\n    if check("the robot\'s gripper is forward aligned with the handle and the handle is not horizontally aligned with goal"):\n        robot.put("gripper around drawer handle")\n    # If the handle is lined up with the goal to the side, pull it.\n    if check("the handle is horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -86.79196,
            '\n    #  1. Put gripper above the handle\n    #  2. Grab the handle with the gripper\n    #  3. Pull up on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # If the handle is left of the gripper, go back to putting the gripper\n    # above the handle.\n    # Because the handle is a long object, check if the gripper is lined up with\n    # it from the front instead of around it.\n    if check("the handle is not left of the robot\'s gripper and the handle is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the handle and the handle isn\'t\n    # lined up with the goal, line up the handle with the goal.\n    if check("the robot\'s gripper is forward aligned with the handle and the handle is not horizontally aligned with goal"):\n        robot.put("gripper around drawer handle")\n    # If the handle is lined up with the goal to the side, pull it.\n    if check("the handle is horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -86.855576,
            '\n    #  1. Put gripper above the handle\n    #  2. Grab the handle with the gripper\n    #  3. Pull up on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # If the handle is left of the gripper, go back to putting the gripper\n    # above the handle.\n    # Because the handle is a long object, check if the gripper is lined up with\n    # it from the front instead of around it.\n    if check("the handle is not left of the robot\'s gripper and the handle is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the handle and the handle isn\'t\n    # lined up with the goal, line up the handle with the goal.\n    if check("the robot\'s gripper is forward aligned with the handle and the handle is not horizontally aligned with goal"):\n        robot.put("gripper around drawer handle")\n    # If the handle is lined up with the goal to the side, pull it.\n    if check("the handle is horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -86.9196,
            '\n    #  1. Put gripper above the handle\n    #  2. Grab the handle with the gripper\n    #  3. Pull up on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # If the handle is left of the gripper, go back to putting the gripper\n    # above the handle.\n    # Because the handle is a long object, check if the gripper is lined up with\n    # it from the front instead of around it.\n    if check("the handle is not left of the robot\'s gripper and the handle is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the handle and the handle isn\'t\n    # lined up with the goal, line up the handle with the goal.\n    if check("the robot\'s gripper is forward aligned with the handle and the handle is not horizontally aligned with goal"):\n        robot.put("gripper around drawer handle")\n    # If the handle is lined up with the goal to the side, pull it.\n    if check("the handle is horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -87.01337,
            '\n    #  1. Put gripper above the handle\n    #  2. Grab the handle with the gripper\n    #  3. Pull up on the handle\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # If the handle is left of the gripper, go back to putting the gripper\n    # above the handle.\n    # Because the handle is a long object, check if the gripper is lined up with\n    # it from the front instead of around it.\n    if check("the handle is not left of the robot\'s gripper and the handle is not forward aligned with the robot\'s gripper"):\n        robot.close("gripper around puck")\n    # As long the gripper is still mostly around the handle and the handle isn\'t\n    # lined up with the goal, line up the handle with the goal.\n    if check("the robot\'s gripper is forward aligned with the handle and the handle is not horizontally aligned with goal"):\n        robot.put("gripper around drawer handle")\n    # If the handle is lined up with the goal to the side, pull it.\n    if check("the handle is horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -98.37343,
            '\n    #  1. Put gripper above the handle\n    #  2. Grab the handle with the gripper\n    #  3. Pull the handle up\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the handle and the robot\'s gripper is open"):\n        robot.reach("to goal")\n    # As long as the gripper is still vertically aligned with the handle,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the handle"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -99.75957,
            '\n    #  1. Put gripper above the handle\n    #  2. Grab the handle with the gripper\n    #  3. Pull the handle up\n    # First, put the gripper above the handle.\n    if check("the robot\'s gripper is not vertically aligned with the handle"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up with the handle, grab it.\n    if check("the robot\'s gripper is vertically aligned with the handle and the robot\'s gripper is not around the handle"):\n        robot.push("the gripper into the puck")\n    # If the gripper is around the handle, pull it up.\n    if check("the robot\'s gripper is around the handle"):\n        robot.reach("to goal")\n',
        ),
    ],
    "lever-pull": [
        (
            -76.475624,
            '\n    #  1. Put gripper above the lever\n    #  2. Rotate the lever up\n    # First, put the gripper above the lever.\n    if check("the robot\'s gripper is not vertically aligned with the lever"):\n        robot.slide("the puck to the goal")\n    # Rotate the lever up.\n    if check("the robot\'s gripper is vertically aligned with the lever"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -76.48224,
            '\n    #  1. Put gripper above the lever\n    #  2. Rotate the lever up\n    # First, put the gripper above the lever.\n    if check("the robot\'s gripper is not vertically aligned with the lever"):\n        robot.slide("the puck to the goal")\n    # Rotate the lever up.\n    if check("the robot\'s gripper is vertically aligned with the lever"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -76.54191,
            '\n    #  1. Put gripper above the lever\n    #  2. Rotate the lever up\n    # First, put the gripper above the lever.\n    if check("the robot\'s gripper is not vertically aligned with the lever"):\n        robot.slide("the puck to the goal")\n    # Rotate the lever up.\n    if check("the robot\'s gripper is vertically aligned with the lever"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -76.5581,
            '\n    #  1. Put gripper above the lever\n    #  2. Rotate the lever up\n    # First, put the gripper above the lever.\n    if check("the robot\'s gripper is not vertically aligned with the lever"):\n        robot.slide("the puck to the goal")\n    # Rotate the lever up.\n    if check("the robot\'s gripper is vertically aligned with the lever"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -76.56634,
            '\n    #  1. Put gripper above the lever\n    #  2. Rotate the lever up\n    # First, put the gripper above the lever.\n    if check("the robot\'s gripper is not vertically aligned with the lever"):\n        robot.slide("the puck to the goal")\n    # Rotate the lever up.\n    if check("the robot\'s gripper is vertically aligned with the lever"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -76.628395,
            '\n    #  1. Put gripper above the lever\n    #  2. Rotate the lever up\n    # First, put the gripper above the lever.\n    if check("the robot\'s gripper is not vertically aligned with the lever"):\n        robot.slide("the puck to the goal")\n    # Rotate the lever up.\n    if check("the robot\'s gripper is vertically aligned with the lever"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -76.655464,
            '\n    #  1. Put gripper above the lever\n    #  2. Rotate the lever up\n    # First, put the gripper above the lever.\n    if check("the robot\'s gripper is not vertically aligned with the lever"):\n        robot.slide("the puck to the goal")\n    # Rotate the lever up.\n    if check("the robot\'s gripper is vertically aligned with the lever"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -77.53238,
            '\n    #  1. Put gripper near the lever\n    #  2. Rotate the lever up\n    # If the robot\'s gripper is not near the lever, move the gripper near the\n    # lever.\n    if check("the robot\'s gripper is not near the lever"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the lever, rotate the lever up.\n    if check("the robot\'s gripper is near the lever"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "peg-insert-side": [
        (
            -62.682503,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways into the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -62.71866,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways into the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -62.72374,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways into the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -62.742023,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways into the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -62.76467,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways into the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -62.796127,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways into the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -62.80809,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways into the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -62.850372,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways into the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
    ],
    "peg-unplug-side": [
        (
            -67.008286,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways out of the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -67.06045,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways out of the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -67.082886,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways out of the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -67.118904,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways out of the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -67.12315,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways out of the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -67.16284,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways out of the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -67.17984,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways out of the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -67.224106,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Line the peg up with the hole\n    #  4. Slide the peg sideways out of the hole\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("the gripper into the puck")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
    ],
    "pick-out-of-hole": [
        (
            -73.13922,
            '\n    #  1. Line up the gripper as viewed from above\n    #  2. Pull up on the peg from the top\n    # Because this is "topdown", we just need to line up the gripper from above.\n    # Line up the robot\'s gripper from above.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # Now that the gripper is lined up, just pull up on the peg.\n    if check("the robot\'s gripper is vertically aligned with the peg"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -75.390015,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Move the peg to the target location\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.put("gripper around drawer handle")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
        (
            -75.40458,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Move the peg to the target location\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.put("gripper around drawer handle")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
        (
            -75.406525,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Move the peg to the target location\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.put("gripper around drawer handle")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
        (
            -75.42373,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Move the peg to the target location\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.put("gripper around drawer handle")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
        (
            -75.48924,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Move the peg to the target location\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.put("gripper around drawer handle")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
        (
            -75.55567,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg with the gripper\n    #  3. Move the peg to the target location\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.put("gripper around drawer handle")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
        (
            -81.35143,
            '\n    #  1. Put gripper above the peg\n    #  2. Grab the peg\n    #  3. Align the peg with the target location\n    #  4. Drop the peg\n    # First, put the gripper above the peg.\n    if check("the robot\'s gripper is not vertically aligned with the peg"):\n        robot.slide("the puck to the goal")\n    # If the peg becomes left of the gripper, go back to putting the gripper\n    # above the peg.\n    # Because the peg is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the peg and the peg isn\'t lined\n    # up with the hole, line up the peg with the hole.\n    if check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the peg is lined up with the hole to the side, insert it.\n    if check("peg is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
    ],
    "pick-place": [
        (
            -97.26286,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Move gripper to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.push("the gripper into the puck")\n    # Once the gripper is around the puck, we can move it to the target location.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("window right harder")\n',
        ),
        (
            -97.35231,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Move gripper to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.push("the gripper into the puck")\n    # Once the gripper is around the puck, we can move it to the target location.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("window right harder")\n',
        ),
        (
            -97.38402,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Move gripper to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.push("the gripper into the puck")\n    # Once the gripper is around the puck, we can move it to the target location.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("window right harder")\n',
        ),
        (
            -97.42343,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Move gripper to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.push("the gripper into the puck")\n    # Once the gripper is around the puck, we can move it to the target location.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("window right harder")\n',
        ),
        (
            -97.427734,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Move gripper to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.push("the gripper into the puck")\n    # Once the gripper is around the puck, we can move it to the target location.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("window right harder")\n',
        ),
        (
            -97.49313,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Move gripper to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.push("the gripper into the puck")\n    # Once the gripper is around the puck, we can move it to the target location.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("window right harder")\n',
        ),
        (
            -100.28285,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Put gripper above goal\n    #  5. Drop gripper around goal\n    #  6. Put puck at goal\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.put("gripper above drawer handle")\n    # Once the gripper is lined up above the puck, we should be able to grab it.\n    if check("the robot\'s gripper is vertically aligned with puck and the robot\'s gripper is not around puck"):\n        robot.push("the gripper into the puck")\n    # Now that the puck is in the gripper, we can put the gripper above the goal.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("window right harder")\n    # Once the gripper is lined up above the goal, we should be able to drop\n    # the puck into the goal.\n    if check("the robot\'s gripper is vertically aligned with goal and the robot\'s gripper is not around goal"):\n        robot.reach("to goal")\n    # Once the gripper is around the goal, we can just drop the puck.\n    if check("the robot\'s gripper is around goal"):\n        robot.place("gripper above puck")\n    # If the puck is in the gripper, we can just drop it.\n    if check("the robot\'s gripper is around puck"):\n        robot.align("peg to hole")',
        ),
        (
            -102.64699,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Put gripper at target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.pull("away from drawer")\n    # If the gripper is still lined up, it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.push("the gripper into the puck")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.put("gripper around door handle")',
        ),
    ],
    "pick-place-wall": [
        (
            -95.65204,
            '\n    #  1. Pick up the puck\n    #  2. Move the gripper to the target location\n    #  3. Drop the puck\n    # First, pick up the puck.\n    if check("the robot\'s gripper is not around puck"):\n        robot.slide("the puck to the goal")\n    # Then, move the gripper to the target location.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is not at the goal"):\n        robot.push("down on button")\n    # Finally, drop the puck.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is at the goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.661934,
            '\n    #  1. Pick up the puck\n    #  2. Move the gripper to the target location\n    #  3. Drop the puck\n    # First, pick up the puck.\n    if check("the robot\'s gripper is not around puck"):\n        robot.slide("the puck to the goal")\n    # Then, move the gripper to the target location.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is not at the goal"):\n        robot.push("down on button")\n    # Finally, drop the puck.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is at the goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.73102,
            '\n    #  1. Pick up the puck\n    #  2. Move the gripper to the target location\n    #  3. Drop the puck\n    # First, pick up the puck.\n    if check("the robot\'s gripper is not around puck"):\n        robot.slide("the puck to the goal")\n    # Then, move the gripper to the target location.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is not at the goal"):\n        robot.push("down on button")\n    # Finally, drop the puck.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is at the goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.7323,
            '\n    #  1. Pick up the puck\n    #  2. Move the gripper to the target location\n    #  3. Drop the puck\n    # First, pick up the puck.\n    if check("the robot\'s gripper is not around puck"):\n        robot.slide("the puck to the goal")\n    # Then, move the gripper to the target location.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is not at the goal"):\n        robot.push("down on button")\n    # Finally, drop the puck.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is at the goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.73274,
            '\n    #  1. Pick up the puck\n    #  2. Move the gripper to the target location\n    #  3. Drop the puck\n    # First, pick up the puck.\n    if check("the robot\'s gripper is not around puck"):\n        robot.slide("the puck to the goal")\n    # Then, move the gripper to the target location.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is not at the goal"):\n        robot.push("down on button")\n    # Finally, drop the puck.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is at the goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.76251,
            '\n    #  1. Pick up the puck\n    #  2. Move the gripper to the target location\n    #  3. Drop the puck\n    # First, pick up the puck.\n    if check("the robot\'s gripper is not around puck"):\n        robot.slide("the puck to the goal")\n    # Then, move the gripper to the target location.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is not at the goal"):\n        robot.push("down on button")\n    # Finally, drop the puck.\n    if check("the robot\'s gripper is around puck and the robot\'s gripper is at the goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -105.03295,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up the puck\n    #  4. Move the puck to the target location\n    #  5. Drop the puck\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # Drop the gripper around the puck.\n    if check("the robot\'s gripper is vertically aligned with puck and the robot\'s gripper is not around puck"):\n        robot.reach("to goal")\n    # Pick up the puck.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("the gripper into the puck")\n    # Move the puck to the target location.\n    if check("the robot\'s gripper is around puck"):\n        robot.push("window right harder")',
        ),
        (
            -121.0101,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Pick up puck\n    #  4. Move gripper to target location\n    #  5. Drop puck\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # Drop the gripper around the puck.\n    if check("the robot\'s gripper is almost vertically aligned with puck and the robot\'s gripper is not around puck"):\n        robot.push("down on button")\n    # Pick up the puck.\n    if check("the robot\'s gripper is around puck"):\n        robot.put("gripper above drawer handle")\n    # Move the gripper to the target location.\n    if check("the robot\'s gripper is not at the target location"):\n        robot.push("the gripper into the puck")\n    # Drop the puck.\n    if check("the robot\'s gripper is at the target location"):\n        robot.reach("to goal")\n',
        ),
    ],
    "plate-slide": [
        (
            -67.81675,
            '\n    #  1. Align the plate with the target location\n    #  2. Slide the plate into the target location\n    if check("the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    if check("the plate is horizontally aligned with the target location"):\n        robot.put("gripper above drawer handle")\n',
        ),
        (
            -100.97589,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Align the plate with the target\n    #  4. Slide the plate into the target\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t\n    # lined up with the target, line up the plate with the target.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with target"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target to the side, insert it.\n    if check("the plate is horizontally aligned with target"):\n        robot.reach("to goal")\n',
        ),
        (
            -100.97985,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Align the plate with the target\n    #  4. Slide the plate into the target\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t\n    # lined up with the target, line up the plate with the target.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with target"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target to the side, insert it.\n    if check("the plate is horizontally aligned with target"):\n        robot.reach("to goal")\n',
        ),
        (
            -101.02405,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Align the plate with the target\n    #  4. Slide the plate into the target\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t\n    # lined up with the target, line up the plate with the target.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with target"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target to the side, insert it.\n    if check("the plate is horizontally aligned with target"):\n        robot.reach("to goal")\n',
        ),
        (
            -101.06767,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Align the plate with the target\n    #  4. Slide the plate into the target\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t\n    # lined up with the target, line up the plate with the target.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with target"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target to the side, insert it.\n    if check("the plate is horizontally aligned with target"):\n        robot.reach("to goal")\n',
        ),
        (
            -101.10135,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Align the plate with the target\n    #  4. Slide the plate into the target\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t\n    # lined up with the target, line up the plate with the target.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with target"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target to the side, insert it.\n    if check("the plate is horizontally aligned with target"):\n        robot.reach("to goal")\n',
        ),
        (
            -101.16326,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Align the plate with the target\n    #  4. Slide the plate into the target\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t\n    # lined up with the target, line up the plate with the target.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with target"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target to the side, insert it.\n    if check("the plate is horizontally aligned with target"):\n        robot.reach("to goal")\n',
        ),
        (
            -111.27167,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate\n    #  3. Line up the plate with the target location\n    #  4. Slide the plate into the target location\n    # If the gripper is not above the plate, move it above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the plate, grab it.\n    if check("the robot\'s gripper is vertically aligned with the plate and the robot\'s gripper is not around the plate"):\n        robot.push("window right harder")\n    # If the gripper is around the plate, line it up with the target location.\n    if check("the robot\'s gripper is around the plate"):\n        robot.push("the gripper into the puck")\n    # If the gripper is forward aligned with the target location, slide the\n    # plate into the target location.\n    if check("the robot\'s gripper is forward aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
    ],
    "plate-slide-back": [
        (
            -49.33724,
            '\n    #  1. Put gripper above plate\n    #  2. Grab plate\n    #  3. Slide plate back\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n',
        ),
        (
            -68.91114,
            '\n    #  1. Align the plate with the target location\n    #  2. Slide the plate back into the target location\n    if check("plate is not horizontally aligned with target location"):\n        robot.push("the gripper into the puck")\n    if check("plate is horizontally aligned with target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -68.99079,
            '\n    #  1. Align the plate with the target location\n    #  2. Slide the plate back into the target location\n    if check("plate is not horizontally aligned with target location"):\n        robot.push("the gripper into the puck")\n    if check("plate is horizontally aligned with target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -68.99675,
            '\n    #  1. Align the plate with the target location\n    #  2. Slide the plate back into the target location\n    if check("plate is not horizontally aligned with target location"):\n        robot.push("the gripper into the puck")\n    if check("plate is horizontally aligned with target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -69.02073,
            '\n    #  1. Align the plate with the target location\n    #  2. Slide the plate back into the target location\n    if check("plate is not horizontally aligned with target location"):\n        robot.push("the gripper into the puck")\n    if check("plate is horizontally aligned with target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -69.06717,
            '\n    #  1. Align the plate with the target location\n    #  2. Slide the plate back into the target location\n    if check("plate is not horizontally aligned with target location"):\n        robot.push("the gripper into the puck")\n    if check("plate is horizontally aligned with target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -69.11331,
            '\n    #  1. Align the plate with the target location\n    #  2. Slide the plate back into the target location\n    if check("plate is not horizontally aligned with target location"):\n        robot.push("the gripper into the puck")\n    if check("plate is horizontally aligned with target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -95.225426,
            '\n    #  1. Put gripper right of the plate\n    #  2. Start pushing against the plate to slide it back\n    #  3. Push the plate back harder\n    # If the robot\'s gripper is not vertically lined up with the plate, we should\n    # move the gripper near the plate to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the plate and the robot\'s gripper is below the plate"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the plate we can probably slide the plate\n    # back now by moving the gripper left.\n    if check("the robot\'s gripper is near the plate"):\n        robot.put("gripper around drawer handle")\n    # If the robot\'s gripper is starting to be in front of the plate, push\n    # harder.\n    if check("the robot\'s gripper is in front of the plate"):\n        robot.place("gripper above puck")\n',
        ),
    ],
    "plate-slide-back-side": [
        (
            -77.81887,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    # Because the plate is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the target location, line up the plate with the target location.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target location to the side, insert it.\n    if check("plate is horizontally aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -82.41243,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate back into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t\n    # lined up with the target location, line up the plate with the target\n    # location.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target location, slide the plate back\n    # into the target location.\n    if check("the plate is horizontally aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -92.84992,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the hole, line up the plate with the hole.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the plate is lined up with the hole to the side, insert it.\n    if check("plate is horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.877,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the hole, line up the plate with the hole.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the plate is lined up with the hole to the side, insert it.\n    if check("plate is horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.88919,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the hole, line up the plate with the hole.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the plate is lined up with the hole to the side, insert it.\n    if check("plate is horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.96255,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the hole, line up the plate with the hole.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the plate is lined up with the hole to the side, insert it.\n    if check("plate is horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.96404,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the hole, line up the plate with the hole.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the plate is lined up with the hole to the side, insert it.\n    if check("plate is horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.97838,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("the plate is not left of the robot\'s gripper and the plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the hole, line up the plate with the hole.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the plate is lined up with the hole to the side, insert it.\n    if check("plate is horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "plate-slide-side": [
        (
            -77.32102,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    # Because the plate is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the target location, line up the plate with the target location.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target location to the side, insert it.\n    if check("plate is horizontally aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.3723,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    # Because the plate is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the target location, line up the plate with the target location.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target location to the side, insert it.\n    if check("plate is horizontally aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.445206,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    # Because the plate is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the target location, line up the plate with the target location.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target location to the side, insert it.\n    if check("plate is horizontally aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.45021,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    # Because the plate is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the target location, line up the plate with the target location.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target location to the side, insert it.\n    if check("plate is horizontally aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.458046,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    # Because the plate is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the target location, line up the plate with the target location.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target location to the side, insert it.\n    if check("plate is horizontally aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -77.50317,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    # Because the plate is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the target location, line up the plate with the target location.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the target location to the side, insert it.\n    if check("plate is horizontally aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
        (
            -78.58279,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Line the plate up with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    # Because the plate is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the hole, line up the plate with the hole.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the plate is lined up with the hole to the side, insert it.\n    if check("plate is horizontally aligned with hole"):\n        robot.reach("to goal")\n',
        ),
        (
            -96.90607,
            '\n    #  1. Put gripper above the plate\n    #  2. Grab the plate with the gripper\n    #  3. Align the plate with the target location\n    #  4. Slide the plate sideways into the target location\n    # First, put the gripper above the plate.\n    if check("the robot\'s gripper is not vertically aligned with the plate"):\n        robot.slide("the puck to the goal")\n    # If the plate becomes left of the gripper, go back to putting the gripper\n    # above the plate.\n    if check("plate is not left of the robot\'s gripper and plate is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the plate and the plate isn\'t lined\n    # up with the hole, line up the plate with the hole.\n    if check("the robot\'s gripper is forward aligned with the plate and the plate is not horizontally aligned with hole"):\n        robot.reach("to goal")\n    # If the plate is lined up with the hole to the side, insert it.\n    if check("plate is horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "push": [
        (
            -72.479965,
            '\n    #  1. Put gripper above the puck\n    #  2. Grab the puck with the gripper\n    #  3. Slide the puck to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not vertically aligned with the puck"):\n        robot.push("down on button")\n    # If the puck becomes left of the gripper, go back to putting the gripper\n    # above the puck.\n    # Because the puck is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("puck is not left of the robot\'s gripper and puck is not forward aligned with the robot\'s gripper"):\n        robot.reach("to goal")\n    # As long the gripper is still mostly around the puck and the puck isn\'t lined\n    # up with the goal, line up the puck with the goal.\n    if check("the robot\'s gripper is forward aligned with the puck and the puck is not horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -75.07302,
            '\n    #  1. Put gripper above puck\n    #  2. Slide the puck to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with the puck"):\n        robot.reach("to goal")\n    # If the gripper is almost vertically aligned with the puck, slide the puck\n    # to the goal.\n    if check("the robot\'s gripper is almost vertically aligned with the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.79155,
            '\n    #  1. Put gripper above puck\n    #  2. Put gripper behind puck\n    #  3. Push puck to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not vertically aligned with the puck"):\n        robot.slide("the puck to the goal")\n    # If the gripper is not behind the puck, move it behind the puck.\n    if check("the robot\'s gripper is not behind the puck"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is behind the puck, push the puck to the target location.\n    if check("the robot\'s gripper is behind the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.821106,
            '\n    #  1. Put gripper above puck\n    #  2. Put gripper behind puck\n    #  3. Push puck to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not vertically aligned with the puck"):\n        robot.slide("the puck to the goal")\n    # If the gripper is not behind the puck, move it behind the puck.\n    if check("the robot\'s gripper is not behind the puck"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is behind the puck, push the puck to the target location.\n    if check("the robot\'s gripper is behind the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.87564,
            '\n    #  1. Put gripper above puck\n    #  2. Put gripper behind puck\n    #  3. Push puck to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not vertically aligned with the puck"):\n        robot.slide("the puck to the goal")\n    # If the gripper is not behind the puck, move it behind the puck.\n    if check("the robot\'s gripper is not behind the puck"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is behind the puck, push the puck to the target location.\n    if check("the robot\'s gripper is behind the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.889206,
            '\n    #  1. Put gripper above puck\n    #  2. Put gripper behind puck\n    #  3. Push puck to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not vertically aligned with the puck"):\n        robot.slide("the puck to the goal")\n    # If the gripper is not behind the puck, move it behind the puck.\n    if check("the robot\'s gripper is not behind the puck"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is behind the puck, push the puck to the target location.\n    if check("the robot\'s gripper is behind the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.92296,
            '\n    #  1. Put gripper above puck\n    #  2. Put gripper behind puck\n    #  3. Push puck to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not vertically aligned with the puck"):\n        robot.slide("the puck to the goal")\n    # If the gripper is not behind the puck, move it behind the puck.\n    if check("the robot\'s gripper is not behind the puck"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is behind the puck, push the puck to the target location.\n    if check("the robot\'s gripper is behind the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -95.958206,
            '\n    #  1. Put gripper above puck\n    #  2. Put gripper behind puck\n    #  3. Push puck to the target location\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not vertically aligned with the puck"):\n        robot.slide("the puck to the goal")\n    # If the gripper is not behind the puck, move it behind the puck.\n    if check("the robot\'s gripper is not behind the puck"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is behind the puck, push the puck to the target location.\n    if check("the robot\'s gripper is behind the puck"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "push-back": [
        (
            -66.66154,
            '\n    #  1. Put gripper above puck\n    #  2. Push back the puck\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.slide("window right")\n',
        ),
        (
            -72.99564,
            '\n    #  1. Push the puck back to the target location\n    # If the puck is in front of the robot\'s gripper, push it backwards.\n    if check("the puck is in front of the robot\'s gripper"):\n        robot.put("gripper around drawer handle")\n    # If the puck is in front of the robot\'s gripper, push it backwards.\n    if check("the puck is in front of the robot\'s gripper"):\n        robot.reach("to goal")',
        ),
        (
            -83.82197,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Push puck backwards\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.pull("away from drawer")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.reach("to goal")\n',
        ),
        (
            -83.82337,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Push puck backwards\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.pull("away from drawer")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.reach("to goal")\n',
        ),
        (
            -83.839935,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Push puck backwards\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.pull("away from drawer")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.reach("to goal")\n',
        ),
        (
            -83.89685,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Push puck backwards\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.pull("away from drawer")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.reach("to goal")\n',
        ),
        (
            -83.92343,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Push puck backwards\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.pull("away from drawer")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.reach("to goal")\n',
        ),
        (
            -83.93089,
            '\n    #  1. Put gripper above puck\n    #  2. Drop gripper around puck\n    #  3. Push puck backwards\n    # First, put the gripper above the puck.\n    if check("the robot\'s gripper is not almost vertically aligned with puck"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with puck"):\n        robot.pull("away from drawer")\n    # As long as the gripper is still vertically aligned with the puck,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with puck"):\n        robot.reach("to goal")\n',
        ),
    ],
    "push-wall": [
        (
            -85.1087,
            '\n    #  1. Move the gripper to the puck\n    #  2. Grab the puck\n    #  3. Push the puck to the target\n    if check("the robot\'s gripper is not near the puck"):\n        robot.reach("to goal")\n    if check("the robot\'s gripper is not around the puck"):\n        robot.push("the gripper into the puck")\n    if check("the robot\'s gripper is around the puck"):\n        robot.put("gripper above drawer handle")\n',
        ),
        (
            -85.11832,
            '\n    #  1. Move the gripper to the puck\n    #  2. Grab the puck\n    #  3. Push the puck to the target\n    if check("the robot\'s gripper is not near the puck"):\n        robot.reach("to goal")\n    if check("the robot\'s gripper is not around the puck"):\n        robot.push("the gripper into the puck")\n    if check("the robot\'s gripper is around the puck"):\n        robot.put("gripper above drawer handle")\n',
        ),
        (
            -85.12181,
            '\n    #  1. Move the gripper to the puck\n    #  2. Grab the puck\n    #  3. Push the puck to the target\n    if check("the robot\'s gripper is not near the puck"):\n        robot.reach("to goal")\n    if check("the robot\'s gripper is not around the puck"):\n        robot.push("the gripper into the puck")\n    if check("the robot\'s gripper is around the puck"):\n        robot.put("gripper above drawer handle")\n',
        ),
        (
            -85.15748,
            '\n    #  1. Move the gripper to the puck\n    #  2. Grab the puck\n    #  3. Push the puck to the target\n    if check("the robot\'s gripper is not near the puck"):\n        robot.reach("to goal")\n    if check("the robot\'s gripper is not around the puck"):\n        robot.push("the gripper into the puck")\n    if check("the robot\'s gripper is around the puck"):\n        robot.put("gripper above drawer handle")\n',
        ),
        (
            -85.16906,
            '\n    #  1. Move the gripper to the puck\n    #  2. Grab the puck\n    #  3. Push the puck to the target\n    if check("the robot\'s gripper is not near the puck"):\n        robot.reach("to goal")\n    if check("the robot\'s gripper is not around the puck"):\n        robot.push("the gripper into the puck")\n    if check("the robot\'s gripper is around the puck"):\n        robot.put("gripper above drawer handle")\n',
        ),
        (
            -85.24258,
            '\n    #  1. Move the gripper to the puck\n    #  2. Grab the puck\n    #  3. Push the puck to the target\n    if check("the robot\'s gripper is not near the puck"):\n        robot.reach("to goal")\n    if check("the robot\'s gripper is not around the puck"):\n        robot.push("the gripper into the puck")\n    if check("the robot\'s gripper is around the puck"):\n        robot.put("gripper above drawer handle")\n',
        ),
        (
            -96.772804,
            '\n    #  1. Move the puck to the left of the wall\n    #  2. Move the puck to the right of the wall\n    #  3. Move the puck to the target location\n    # If the puck is not left of the wall, move it to the left of the wall.\n    if check("the puck is not left of the wall"):\n        robot.push("the gripper into the puck")\n    # If the puck is left of the wall, move it to the right of the wall.\n    if check("the puck is left of the wall"):\n        robot.reach("to goal")\n    # If the puck is right of the wall, move it to the target location.\n    if check("the puck is right of the wall"):\n        robot.put("gripper around drawer handle")\n',
        ),
        (
            -101.22516,
            '\n    #  1. Push the puck to the wall\n    #  2. Push the puck into the wall\n    #  3. Push the puck to the target location\n    # First, push the puck to the wall.\n    if check("puck is not near wall"):\n        robot.push("the gripper into the puck")\n    # If the puck is near the wall, push it into the wall.\n    if check("puck is near wall"):\n        robot.reach("to goal")\n    # If the puck is in the wall, push it to the target location.\n    if check("puck is in wall"):\n        robot.put("gripper above drawer handle")\n',
        ),
    ],
    "reach": [
        (
            -72.20824,
            '\n    #  1. Move the gripper near the target location\n    #  2. Move the gripper to the target location\n    # If the robot\'s gripper is not near the target location, move it there.\n    if check("the robot\'s gripper is not near the target location"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the target location, move it to the target\n    # location.\n    if check("the robot\'s gripper is near the target location"):\n        robot.pull("away from drawer")\n',
        ),
        (
            -95.89662,
            '\n    #  1. Put gripper above the target location\n    #  2. Drop gripper around the target location\n    #  3. Pull open the gripper\n    # First, put the gripper mostly above the target location.\n    if check("the robot\'s gripper is not almost vertically aligned with the target location"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with the target location and the robot\'s gripper is open"):\n        robot.put("gripper above drawer handle")\n    # As long as the gripper is still vertically aligned with the target location,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with the target location"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.11537,
            '\n    #  1. Put gripper above the target\n    #  2. Drop gripper around the target\n    #  3. Grab the target\n    # First, put the gripper above the target.\n    if check("the robot\'s gripper is not vertically aligned with the target"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the target, drop it around the target.\n    if check("the robot\'s gripper is vertically aligned with the target and the robot\'s gripper is not around the target"):\n        robot.push("window right harder")\n    # If the gripper is around the target, grab it.\n    if check("the robot\'s gripper is around the target"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.164795,
            '\n    #  1. Put gripper above the target\n    #  2. Drop gripper around the target\n    #  3. Grab the target\n    # First, put the gripper above the target.\n    if check("the robot\'s gripper is not vertically aligned with the target"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the target, drop it around the target.\n    if check("the robot\'s gripper is vertically aligned with the target and the robot\'s gripper is not around the target"):\n        robot.push("window right harder")\n    # If the gripper is around the target, grab it.\n    if check("the robot\'s gripper is around the target"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.21587,
            '\n    #  1. Put gripper above the target\n    #  2. Drop gripper around the target\n    #  3. Grab the target\n    # First, put the gripper above the target.\n    if check("the robot\'s gripper is not vertically aligned with the target"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the target, drop it around the target.\n    if check("the robot\'s gripper is vertically aligned with the target and the robot\'s gripper is not around the target"):\n        robot.push("window right harder")\n    # If the gripper is around the target, grab it.\n    if check("the robot\'s gripper is around the target"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.23288,
            '\n    #  1. Put gripper above the target\n    #  2. Drop gripper around the target\n    #  3. Grab the target\n    # First, put the gripper above the target.\n    if check("the robot\'s gripper is not vertically aligned with the target"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the target, drop it around the target.\n    if check("the robot\'s gripper is vertically aligned with the target and the robot\'s gripper is not around the target"):\n        robot.push("window right harder")\n    # If the gripper is around the target, grab it.\n    if check("the robot\'s gripper is around the target"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.243286,
            '\n    #  1. Put gripper above the target\n    #  2. Drop gripper around the target\n    #  3. Grab the target\n    # First, put the gripper above the target.\n    if check("the robot\'s gripper is not vertically aligned with the target"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the target, drop it around the target.\n    if check("the robot\'s gripper is vertically aligned with the target and the robot\'s gripper is not around the target"):\n        robot.push("window right harder")\n    # If the gripper is around the target, grab it.\n    if check("the robot\'s gripper is around the target"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -101.3474,
            '\n    #  1. Put gripper above the target\n    #  2. Drop gripper around the target\n    #  3. Grab the target\n    # First, put the gripper above the target.\n    if check("the robot\'s gripper is not vertically aligned with the target"):\n        robot.slide("the puck to the goal")\n    # If the gripper is above the target, drop it around the target.\n    if check("the robot\'s gripper is vertically aligned with the target and the robot\'s gripper is not around the target"):\n        robot.push("window right harder")\n    # If the gripper is around the target, grab it.\n    if check("the robot\'s gripper is around the target"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "reach-wall": [
        (
            -103.90055,
            '\n    #  1. Move the gripper to the left of the wall\n    #  2. Move the gripper to the right of the wall\n    #  3. Move the gripper to the target location\n    # If the gripper is not near the wall, move it to the left of the wall.\n    if check("the robot\'s gripper is not near the wall"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the wall, move it to the right of the wall.\n    if check("the robot\'s gripper is left of the wall"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is right of the wall, move it to the target location.\n    if check("the robot\'s gripper is right of the wall"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -103.96636,
            '\n    #  1. Move the gripper to the left of the wall\n    #  2. Move the gripper to the right of the wall\n    #  3. Move the gripper to the target location\n    # If the gripper is not near the wall, move it to the left of the wall.\n    if check("the robot\'s gripper is not near the wall"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the wall, move it to the right of the wall.\n    if check("the robot\'s gripper is left of the wall"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is right of the wall, move it to the target location.\n    if check("the robot\'s gripper is right of the wall"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -103.97243,
            '\n    #  1. Move the gripper to the left of the wall\n    #  2. Move the gripper to the right of the wall\n    #  3. Move the gripper to the target location\n    # If the gripper is not near the wall, move it to the left of the wall.\n    if check("the robot\'s gripper is not near the wall"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the wall, move it to the right of the wall.\n    if check("the robot\'s gripper is left of the wall"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is right of the wall, move it to the target location.\n    if check("the robot\'s gripper is right of the wall"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -103.99503,
            '\n    #  1. Move the gripper to the left of the wall\n    #  2. Move the gripper to the right of the wall\n    #  3. Move the gripper to the target location\n    # If the gripper is not near the wall, move it to the left of the wall.\n    if check("the robot\'s gripper is not near the wall"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the wall, move it to the right of the wall.\n    if check("the robot\'s gripper is left of the wall"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is right of the wall, move it to the target location.\n    if check("the robot\'s gripper is right of the wall"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -104.01339,
            '\n    #  1. Move the gripper to the left of the wall\n    #  2. Move the gripper to the right of the wall\n    #  3. Move the gripper to the target location\n    # If the gripper is not near the wall, move it to the left of the wall.\n    if check("the robot\'s gripper is not near the wall"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the wall, move it to the right of the wall.\n    if check("the robot\'s gripper is left of the wall"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is right of the wall, move it to the target location.\n    if check("the robot\'s gripper is right of the wall"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -104.03469,
            '\n    #  1. Move the gripper to the left of the wall\n    #  2. Move the gripper to the right of the wall\n    #  3. Move the gripper to the target location\n    # If the gripper is not near the wall, move it to the left of the wall.\n    if check("the robot\'s gripper is not near the wall"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the wall, move it to the right of the wall.\n    if check("the robot\'s gripper is left of the wall"):\n        robot.put("gripper around drawer handle")\n    # If the gripper is right of the wall, move it to the target location.\n    if check("the robot\'s gripper is right of the wall"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -108.968445,
            '\n    #  1. Put gripper above the wall\n    #  2. Drop gripper around wall\n    #  3. Reach to goal\n    # First, put the gripper above the wall.\n    if check("the robot\'s gripper is not vertically aligned with the wall"):\n        robot.slide("the puck to the goal")\n    # Then, drop the gripper around the wall.\n    if check("the robot\'s gripper is vertically aligned with the wall and the robot\'s gripper is not around the wall"):\n        robot.pull("away from drawer")\n    # Finally, reach to the goal.\n    if check("the robot\'s gripper is around the wall"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -109.167145,
            '\n    #  1. Move the gripper to the right of the wall\n    #  2. Move the gripper above the wall\n    #  3. Move the gripper to the left of the wall\n    #  4. Move the gripper to the target location\n    # If the robot\'s gripper is not right of the wall, move it to the right of\n    # the wall.\n    if check("the robot\'s gripper is not right of the wall"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is right of the wall, move it above the wall.\n    if check("the robot\'s gripper is right of the wall"):\n        robot.put("gripper around drawer handle")\n    # If the robot\'s gripper is above the wall, move it to the left of the wall.\n    if check("the robot\'s gripper is above the wall"):\n        robot.push("the gripper into the puck")\n    # If the robot\'s gripper is left of the wall, move it to the target location.\n    if check("the robot\'s gripper is left of the wall"):\n        robot.place("gripper above puck")\n',
        ),
    ],
    "shelf-place": [
        (
            -90.48381,
            '\n    #  1. Pick up the block\n    #  2. Move the block to the target location\n    #  3. Put the block down\n    # First, pick up the block.\n    if check("the robot\'s gripper is not around the block"):\n        robot.slide("the puck to the goal")\n    # Move the block to the target location.\n    if check("the robot\'s gripper is around the block"):\n        robot.push("the gripper into the puck")\n    # Put the block down.\n    if check("the robot\'s gripper is around the block"):\n        robot.push("window right harder")',
        ),
        (
            -99.79748,
            '\n    #  1. Pick up the block\n    #  2. Align the block with the shelf\n    #  3. Place the block on the shelf\n    # First, pick up the block.\n    if check("the robot\'s gripper is not around block"):\n        robot.slide("the puck to the goal")\n    # If the block is in front of the gripper, align it with the shelf.\n    if check("the robot\'s gripper is forward aligned with block"):\n        robot.push("window right harder")\n    # If the block is aligned with the shelf, place it on the shelf.\n    if check("the robot\'s gripper is horizontally aligned with block"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -99.85563,
            '\n    #  1. Pick up the block\n    #  2. Align the block with the shelf\n    #  3. Place the block on the shelf\n    # First, pick up the block.\n    if check("the robot\'s gripper is not around block"):\n        robot.slide("the puck to the goal")\n    # If the block is in front of the gripper, align it with the shelf.\n    if check("the robot\'s gripper is forward aligned with block"):\n        robot.push("window right harder")\n    # If the block is aligned with the shelf, place it on the shelf.\n    if check("the robot\'s gripper is horizontally aligned with block"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -99.90645,
            '\n    #  1. Pick up the block\n    #  2. Align the block with the shelf\n    #  3. Place the block on the shelf\n    # First, pick up the block.\n    if check("the robot\'s gripper is not around block"):\n        robot.slide("the puck to the goal")\n    # If the block is in front of the gripper, align it with the shelf.\n    if check("the robot\'s gripper is forward aligned with block"):\n        robot.push("window right harder")\n    # If the block is aligned with the shelf, place it on the shelf.\n    if check("the robot\'s gripper is horizontally aligned with block"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -99.921165,
            '\n    #  1. Pick up the block\n    #  2. Align the block with the shelf\n    #  3. Place the block on the shelf\n    # First, pick up the block.\n    if check("the robot\'s gripper is not around block"):\n        robot.slide("the puck to the goal")\n    # If the block is in front of the gripper, align it with the shelf.\n    if check("the robot\'s gripper is forward aligned with block"):\n        robot.push("window right harder")\n    # If the block is aligned with the shelf, place it on the shelf.\n    if check("the robot\'s gripper is horizontally aligned with block"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -99.93699,
            '\n    #  1. Pick up the block\n    #  2. Align the block with the shelf\n    #  3. Place the block on the shelf\n    # First, pick up the block.\n    if check("the robot\'s gripper is not around block"):\n        robot.slide("the puck to the goal")\n    # If the block is in front of the gripper, align it with the shelf.\n    if check("the robot\'s gripper is forward aligned with block"):\n        robot.push("window right harder")\n    # If the block is aligned with the shelf, place it on the shelf.\n    if check("the robot\'s gripper is horizontally aligned with block"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -99.95288,
            '\n    #  1. Pick up the block\n    #  2. Align the block with the shelf\n    #  3. Place the block on the shelf\n    # First, pick up the block.\n    if check("the robot\'s gripper is not around block"):\n        robot.slide("the puck to the goal")\n    # If the block is in front of the gripper, align it with the shelf.\n    if check("the robot\'s gripper is forward aligned with block"):\n        robot.push("window right harder")\n    # If the block is aligned with the shelf, place it on the shelf.\n    if check("the robot\'s gripper is horizontally aligned with block"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -113.281876,
            '\n    #  1. Put gripper above the block\n    #  2. Drop gripper around the block\n    #  3. Pick up the block\n    #  4. Align the block with the target location\n    #  5. Drop the block at the target location\n    # First, put the gripper above the block.\n    if check("the robot\'s gripper is not vertically aligned with the block"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up above the block, drop the gripper around the\n    # block.\n    if check("the robot\'s gripper is vertically aligned with the block"):\n        robot.push("down on button")\n    # If the gripper is around the block, pick up the block.\n    if check("the robot\'s gripper is around the block"):\n        robot.push("the gripper into the puck")\n    # Align the block with the target location.\n    if check("the robot\'s gripper is forward aligned with the block"):\n        robot.reach("to goal")\n    # Drop the block at the target location.\n    if check("the robot\'s gripper is aligned with the goal"):\n        robot.put("gripper above door handle")\n',
        ),
    ],
    "soccer": [
        (
            -51.99027,
            '\n    #  1. Put gripper above soccer ball\n    #  2. Drop gripper around soccer ball\n    #  3. Push soccer ball into the target location\n    if check("the robot\'s gripper is not vertically aligned with the soccer ball"):\n        robot.slide("the puck to the goal")\n',
        ),
        (
            -102.92405,
            '\n    #  1. Put gripper above soccer ball\n    #  2. Grab the soccer ball\n    #  3. Push the soccer ball into the target location\n    # First, put the gripper above the soccer ball.\n    if check("the robot\'s gripper is not vertically aligned with soccer ball"):\n        robot.slide("the puck to the goal")\n    # If the soccer ball becomes left of the gripper, go back to putting the\n    # gripper above the soccer ball.\n    if check("soccer ball is not left of the robot\'s gripper and soccer ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the soccer ball and the soccer\n    # ball isn\'t lined up with the goal, line up the soccer ball with the goal.\n    if check("the robot\'s gripper is forward aligned with soccer ball and soccer ball is not horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n    # If the soccer ball is lined up with the goal to the side, insert it.\n    if check("soccer ball is horizontally aligned with goal"):\n        robot.reach("to goal")\n',
        ),
        (
            -102.97263,
            '\n    #  1. Put gripper above soccer ball\n    #  2. Grab the soccer ball\n    #  3. Push the soccer ball into the target location\n    # First, put the gripper above the soccer ball.\n    if check("the robot\'s gripper is not vertically aligned with soccer ball"):\n        robot.slide("the puck to the goal")\n    # If the soccer ball becomes left of the gripper, go back to putting the\n    # gripper above the soccer ball.\n    if check("soccer ball is not left of the robot\'s gripper and soccer ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the soccer ball and the soccer\n    # ball isn\'t lined up with the goal, line up the soccer ball with the goal.\n    if check("the robot\'s gripper is forward aligned with soccer ball and soccer ball is not horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n    # If the soccer ball is lined up with the goal to the side, insert it.\n    if check("soccer ball is horizontally aligned with goal"):\n        robot.reach("to goal")\n',
        ),
        (
            -102.9748,
            '\n    #  1. Put gripper above soccer ball\n    #  2. Grab the soccer ball\n    #  3. Push the soccer ball into the target location\n    # First, put the gripper above the soccer ball.\n    if check("the robot\'s gripper is not vertically aligned with soccer ball"):\n        robot.slide("the puck to the goal")\n    # If the soccer ball becomes left of the gripper, go back to putting the\n    # gripper above the soccer ball.\n    if check("soccer ball is not left of the robot\'s gripper and soccer ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the soccer ball and the soccer\n    # ball isn\'t lined up with the goal, line up the soccer ball with the goal.\n    if check("the robot\'s gripper is forward aligned with soccer ball and soccer ball is not horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n    # If the soccer ball is lined up with the goal to the side, insert it.\n    if check("soccer ball is horizontally aligned with goal"):\n        robot.reach("to goal")\n',
        ),
        (
            -103.00832,
            '\n    #  1. Put gripper above soccer ball\n    #  2. Grab the soccer ball\n    #  3. Push the soccer ball into the target location\n    # First, put the gripper above the soccer ball.\n    if check("the robot\'s gripper is not vertically aligned with soccer ball"):\n        robot.slide("the puck to the goal")\n    # If the soccer ball becomes left of the gripper, go back to putting the\n    # gripper above the soccer ball.\n    if check("soccer ball is not left of the robot\'s gripper and soccer ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the soccer ball and the soccer\n    # ball isn\'t lined up with the goal, line up the soccer ball with the goal.\n    if check("the robot\'s gripper is forward aligned with soccer ball and soccer ball is not horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n    # If the soccer ball is lined up with the goal to the side, insert it.\n    if check("soccer ball is horizontally aligned with goal"):\n        robot.reach("to goal")\n',
        ),
        (
            -103.05289,
            '\n    #  1. Put gripper above soccer ball\n    #  2. Grab the soccer ball\n    #  3. Push the soccer ball into the target location\n    # First, put the gripper above the soccer ball.\n    if check("the robot\'s gripper is not vertically aligned with soccer ball"):\n        robot.slide("the puck to the goal")\n    # If the soccer ball becomes left of the gripper, go back to putting the\n    # gripper above the soccer ball.\n    if check("soccer ball is not left of the robot\'s gripper and soccer ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the soccer ball and the soccer\n    # ball isn\'t lined up with the goal, line up the soccer ball with the goal.\n    if check("the robot\'s gripper is forward aligned with soccer ball and soccer ball is not horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n    # If the soccer ball is lined up with the goal to the side, insert it.\n    if check("soccer ball is horizontally aligned with goal"):\n        robot.reach("to goal")\n',
        ),
        (
            -103.0548,
            '\n    #  1. Put gripper above soccer ball\n    #  2. Grab the soccer ball\n    #  3. Push the soccer ball into the target location\n    # First, put the gripper above the soccer ball.\n    if check("the robot\'s gripper is not vertically aligned with soccer ball"):\n        robot.slide("the puck to the goal")\n    # If the soccer ball becomes left of the gripper, go back to putting the\n    # gripper above the soccer ball.\n    if check("soccer ball is not left of the robot\'s gripper and soccer ball is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the soccer ball and the soccer\n    # ball isn\'t lined up with the goal, line up the soccer ball with the goal.\n    if check("the robot\'s gripper is forward aligned with soccer ball and soccer ball is not horizontally aligned with goal"):\n        robot.push("the gripper into the puck")\n    # If the soccer ball is lined up with the goal to the side, insert it.\n    if check("soccer ball is horizontally aligned with goal"):\n        robot.reach("to goal")\n',
        ),
        (
            -109.54574,
            '\n    #  1. Put gripper above the soccer ball\n    #  2. Drop gripper around the soccer ball\n    #  3. Push the soccer ball toward the target location\n    # First, put the gripper above the soccer ball.\n    if check("the robot\'s gripper is not vertically aligned with the soccer ball"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up above the soccer ball, we should be able to grab\n    # the soccer ball by moving the gripper down around it.\n    if check("the robot\'s gripper is vertically aligned with the soccer ball and the robot\'s gripper is not around the soccer ball"):\n        robot.put("gripper above drawer handle")\n    # Once the gripper is around the soccer ball, we can just push the soccer\n    # ball toward the target location.\n    if check("the robot\'s gripper is around the soccer ball"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "stick-pull": [
        (
            -106.69002,
            '\n    #  1. Move the gripper to the left of the stick\n    #  2. Grab the stick\n    #  3. Move the gripper to the left of the thermos\n    #  4. Push the thermos to the target location\n    # First, move the gripper to the left of the stick.\n    if check("the robot\'s gripper is not left of the stick"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the stick, grab the stick.\n    if check("the robot\'s gripper is left of the stick"):\n        robot.put("gripper above drawer handle")\n    # If the gripper is left of the thermos, push the thermos to the target\n    # location.\n    if check("the robot\'s gripper is left of the thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -106.72651,
            '\n    #  1. Move the gripper to the left of the stick\n    #  2. Grab the stick\n    #  3. Move the gripper to the left of the thermos\n    #  4. Push the thermos to the target location\n    # First, move the gripper to the left of the stick.\n    if check("the robot\'s gripper is not left of the stick"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the stick, grab the stick.\n    if check("the robot\'s gripper is left of the stick"):\n        robot.put("gripper above drawer handle")\n    # If the gripper is left of the thermos, push the thermos to the target\n    # location.\n    if check("the robot\'s gripper is left of the thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -106.80148,
            '\n    #  1. Move the gripper to the left of the stick\n    #  2. Grab the stick\n    #  3. Move the gripper to the left of the thermos\n    #  4. Push the thermos to the target location\n    # First, move the gripper to the left of the stick.\n    if check("the robot\'s gripper is not left of the stick"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the stick, grab the stick.\n    if check("the robot\'s gripper is left of the stick"):\n        robot.put("gripper above drawer handle")\n    # If the gripper is left of the thermos, push the thermos to the target\n    # location.\n    if check("the robot\'s gripper is left of the thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -106.84114,
            '\n    #  1. Move the gripper to the left of the stick\n    #  2. Grab the stick\n    #  3. Move the gripper to the left of the thermos\n    #  4. Push the thermos to the target location\n    # First, move the gripper to the left of the stick.\n    if check("the robot\'s gripper is not left of the stick"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the stick, grab the stick.\n    if check("the robot\'s gripper is left of the stick"):\n        robot.put("gripper above drawer handle")\n    # If the gripper is left of the thermos, push the thermos to the target\n    # location.\n    if check("the robot\'s gripper is left of the thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -106.87339,
            '\n    #  1. Move the gripper to the left of the stick\n    #  2. Grab the stick\n    #  3. Move the gripper to the left of the thermos\n    #  4. Push the thermos to the target location\n    # First, move the gripper to the left of the stick.\n    if check("the robot\'s gripper is not left of the stick"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the stick, grab the stick.\n    if check("the robot\'s gripper is left of the stick"):\n        robot.put("gripper above drawer handle")\n    # If the gripper is left of the thermos, push the thermos to the target\n    # location.\n    if check("the robot\'s gripper is left of the thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -106.99702,
            '\n    #  1. Move the gripper to the left of the stick\n    #  2. Grab the stick\n    #  3. Move the gripper to the left of the thermos\n    #  4. Push the thermos to the target location\n    # First, move the gripper to the left of the stick.\n    if check("the robot\'s gripper is not left of the stick"):\n        robot.slide("the puck to the goal")\n    # If the gripper is left of the stick, grab the stick.\n    if check("the robot\'s gripper is left of the stick"):\n        robot.put("gripper above drawer handle")\n    # If the gripper is left of the thermos, push the thermos to the target\n    # location.\n    if check("the robot\'s gripper is left of the thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -123.311966,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick\n    #  3. Put gripper above the thermos\n    #  4. Push the thermos to the target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # Grab the stick.\n    if check("the robot\'s gripper is vertically aligned with the stick and the robot\'s gripper is not around the stick"):\n        robot.put("gripper above drawer handle")\n    # Put the gripper above the thermos.\n    if check("the robot\'s gripper is not vertically aligned with the thermos"):\n        robot.reach("to goal")\n    # Push the thermos to the target location.\n    if check("the robot\'s gripper is vertically aligned with the thermos"):\n        robot.close("gripper around puck")\n',
        ),
        (
            -125.515144,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick\n    #  3. Put gripper above the thermos\n    #  4. Drop gripper around thermos\n    #  5. Pull thermos to target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # If the gripper is not around the stick, grab it.\n    if check("the robot\'s gripper is not around the stick"):\n        robot.push("window right harder")\n    # Put the gripper above the thermos.\n    if check("the robot\'s gripper is not vertically aligned with the thermos"):\n        robot.reach("to goal")\n    # Drop the gripper around the thermos.\n    if check("the robot\'s gripper is vertically aligned with the thermos and the robot\'s gripper is not around the thermos"):\n        robot.put("gripper above door handle")\n    # Pull the thermos to the target location.\n    if check("the robot\'s gripper is around the thermos"):\n        robot.push("the gripper into the puck")\n',
        ),
    ],
    "stick-push": [
        (
            -88.055954,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick\n    #  3. Put gripper above the thermos\n    #  4. Push the thermos to the target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # If the stick becomes left of the gripper, go back to putting the gripper\n    # above the stick.\n    # Because the stick is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("stick is not left of the robot\'s gripper and stick is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the stick and the stick isn\'t lined\n    # up with the thermos, line up the stick with the thermos.\n    if check("the robot\'s gripper is forward aligned with the stick and the stick is not horizontally aligned with thermos"):\n        robot.reach("to goal")\n    # If the stick is lined up with the thermos to the side, push the thermos.\n    if check("stick is horizontally aligned with thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -88.12303,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick\n    #  3. Put gripper above the thermos\n    #  4. Push the thermos to the target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # If the stick becomes left of the gripper, go back to putting the gripper\n    # above the stick.\n    # Because the stick is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("stick is not left of the robot\'s gripper and stick is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the stick and the stick isn\'t lined\n    # up with the thermos, line up the stick with the thermos.\n    if check("the robot\'s gripper is forward aligned with the stick and the stick is not horizontally aligned with thermos"):\n        robot.reach("to goal")\n    # If the stick is lined up with the thermos to the side, push the thermos.\n    if check("stick is horizontally aligned with thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -88.1319,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick with the gripper\n    #  3. Put gripper above the thermos\n    #  4. Push the thermos to the target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # If the stick becomes left of the gripper, go back to putting the gripper\n    # above the stick.\n    # Because the stick is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("stick is not left of the robot\'s gripper and stick is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the stick and the stick isn\'t lined\n    # up with the thermos, line up the stick with the thermos.\n    if check("the robot\'s gripper is forward aligned with the stick and the stick is not horizontally aligned with the thermos"):\n        robot.reach("to goal")\n    # If the stick is lined up with the thermos to the side, push it.\n    if check("stick is horizontally aligned with the thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -88.20226,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick\n    #  3. Put gripper above the thermos\n    #  4. Push the thermos to the target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # If the stick becomes left of the gripper, go back to putting the gripper\n    # above the stick.\n    # Because the stick is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("stick is not left of the robot\'s gripper and stick is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the stick and the stick isn\'t lined\n    # up with the thermos, line up the stick with the thermos.\n    if check("the robot\'s gripper is forward aligned with the stick and the stick is not horizontally aligned with thermos"):\n        robot.reach("to goal")\n    # If the stick is lined up with the thermos to the side, push the thermos.\n    if check("stick is horizontally aligned with thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -88.2268,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick\n    #  3. Put gripper above the thermos\n    #  4. Push the thermos to the target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # If the stick becomes left of the gripper, go back to putting the gripper\n    # above the stick.\n    # Because the stick is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("stick is not left of the robot\'s gripper and stick is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the stick and the stick isn\'t lined\n    # up with the thermos, line up the stick with the thermos.\n    if check("the robot\'s gripper is forward aligned with the stick and the stick is not horizontally aligned with thermos"):\n        robot.reach("to goal")\n    # If the stick is lined up with the thermos to the side, push the thermos.\n    if check("stick is horizontally aligned with thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -88.26979,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick\n    #  3. Put gripper above the thermos\n    #  4. Push the thermos to the target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # If the stick becomes left of the gripper, go back to putting the gripper\n    # above the stick.\n    # Because the stick is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("stick is not left of the robot\'s gripper and stick is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the stick and the stick isn\'t lined\n    # up with the thermos, line up the stick with the thermos.\n    if check("the robot\'s gripper is forward aligned with the stick and the stick is not horizontally aligned with thermos"):\n        robot.reach("to goal")\n    # If the stick is lined up with the thermos to the side, push the thermos.\n    if check("stick is horizontally aligned with thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -88.297104,
            '\n    #  1. Put gripper above the stick\n    #  2. Grab the stick\n    #  3. Put gripper above the thermos\n    #  4. Push the thermos to the target location\n    # First, put the gripper above the stick.\n    if check("the robot\'s gripper is not vertically aligned with the stick"):\n        robot.slide("the puck to the goal")\n    # If the stick becomes left of the gripper, go back to putting the gripper\n    # above the stick.\n    # Because the stick is a long object, check if the gripper is lined up with it\n    # from the front instead of around it.\n    if check("stick is not left of the robot\'s gripper and stick is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the stick and the stick isn\'t lined\n    # up with the thermos, line up the stick with the thermos.\n    if check("the robot\'s gripper is forward aligned with the stick and the stick is not horizontally aligned with thermos"):\n        robot.reach("to goal")\n    # If the stick is lined up with the thermos to the side, push the thermos.\n    if check("stick is horizontally aligned with thermos"):\n        robot.drop("gripper around puck")\n',
        ),
        (
            -103.06495,
            '\n    #  1. Pick up the stick\n    #  2. Line up the stick with the thermos\n    #  3. Push the thermos to the target location\n    # First, pick up the stick.\n    if check("the robot\'s gripper is not around the stick"):\n        robot.slide("the puck to the goal")\n    # If the stick is not aligned with the thermos, align it.\n    if check("the stick is not aligned with the thermos"):\n        robot.reach("to goal")\n    # If the thermos is not at the target location, push it there.\n    if check("the thermos is not at the goal"):\n        robot.put("the gripper above the puck")\n',
        ),
    ],
    "sweep": [
        (
            -48.49518,
            '\n    #  1. Put gripper above the cube\n    #  2. Grab the cube\n    #  3. Move the cube sideways to the target location\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n',
        ),
        (
            -78.89187,
            '\n    #  1. Put gripper above cube\n    #  2. Grab cube\n    #  3. Move sideways to the target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # If the gripper is aligned with the cube, grab it.\n    if check("the robot\'s gripper is vertically aligned with cube"):\n        robot.push("window right harder")\n',
        ),
        (
            -100.684616,
            '\n    #  1. Put gripper above the cube\n    #  2. Grab the cube with the gripper\n    #  3. Align the cube with the target location\n    #  4. Push the cube to the target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n    # If the cube becomes left of the gripper, go back to putting the gripper\n    # above the cube.\n    if check("cube is not left of the robot\'s gripper and cube is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the cube and the cube isn\'t lined\n    # up with the hole, line up the cube with the hole.\n    if check("the robot\'s gripper is forward aligned with the cube and the cube is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the cube is lined up with the hole to the side, insert it.\n    if check("cube is horizontally aligned with hole"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -100.83573,
            '\n    #  1. Put gripper above the cube\n    #  2. Grab the cube with the gripper\n    #  3. Align the cube with the target location\n    #  4. Push the cube to the target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n    # If the cube becomes left of the gripper, go back to putting the gripper\n    # above the cube.\n    if check("cube is not left of the robot\'s gripper and cube is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the cube and the cube isn\'t lined\n    # up with the hole, line up the cube with the hole.\n    if check("the robot\'s gripper is forward aligned with the cube and the cube is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the cube is lined up with the hole to the side, insert it.\n    if check("cube is horizontally aligned with hole"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -100.83699,
            '\n    #  1. Put gripper above the cube\n    #  2. Grab the cube with the gripper\n    #  3. Align the cube with the target location\n    #  4. Push the cube to the target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n    # If the cube becomes left of the gripper, go back to putting the gripper\n    # above the cube.\n    if check("cube is not left of the robot\'s gripper and cube is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the cube and the cube isn\'t lined\n    # up with the hole, line up the cube with the hole.\n    if check("the robot\'s gripper is forward aligned with the cube and the cube is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the cube is lined up with the hole to the side, insert it.\n    if check("cube is horizontally aligned with hole"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -100.846146,
            '\n    #  1. Put gripper above the cube\n    #  2. Grab the cube with the gripper\n    #  3. Align the cube with the target location\n    #  4. Push the cube to the target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n    # If the cube becomes left of the gripper, go back to putting the gripper\n    # above the cube.\n    if check("cube is not left of the robot\'s gripper and cube is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the cube and the cube isn\'t lined\n    # up with the hole, line up the cube with the hole.\n    if check("the robot\'s gripper is forward aligned with the cube and the cube is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the cube is lined up with the hole to the side, insert it.\n    if check("cube is horizontally aligned with hole"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -100.8507,
            '\n    #  1. Put gripper above the cube\n    #  2. Grab the cube with the gripper\n    #  3. Align the cube with the target location\n    #  4. Push the cube to the target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n    # If the cube becomes left of the gripper, go back to putting the gripper\n    # above the cube.\n    if check("cube is not left of the robot\'s gripper and cube is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the cube and the cube isn\'t lined\n    # up with the hole, line up the cube with the hole.\n    if check("the robot\'s gripper is forward aligned with the cube and the cube is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the cube is lined up with the hole to the side, insert it.\n    if check("cube is horizontally aligned with hole"):\n        robot.place("gripper above puck")\n',
        ),
        (
            -100.976776,
            '\n    #  1. Put gripper above the cube\n    #  2. Grab the cube with the gripper\n    #  3. Align the cube with the target location\n    #  4. Push the cube to the target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n    # If the cube becomes left of the gripper, go back to putting the gripper\n    # above the cube.\n    if check("cube is not left of the robot\'s gripper and cube is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the cube and the cube isn\'t lined\n    # up with the hole, line up the cube with the hole.\n    if check("the robot\'s gripper is forward aligned with the cube and the cube is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the cube is lined up with the hole to the side, insert it.\n    if check("cube is horizontally aligned with hole"):\n        robot.place("gripper above puck")\n',
        ),
    ],
    "sweep-into": [
        (
            -91.21348,
            '\n    #  1. Put gripper above the cube\n    #  2. Grab the cube\n    #  3. Move the gripper to the target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n    # If the cube becomes left of the gripper, go back to putting the gripper\n    # above the cube.\n    # Because the cube is a small object, check if the gripper is around it\n    # instead of forward aligned with it.\n    if check("the cube is not left of the robot\'s gripper and the cube is not forward aligned with the robot\'s gripper"):\n        robot.push("window right harder")\n    # As long the gripper is still mostly around the cube and the cube isn\'t lined\n    # up with the hole, line up the cube with the hole.\n    if check("the robot\'s gripper is forward aligned with the cube and the cube is not horizontally aligned with hole"):\n        robot.push("the gripper into the puck")\n    # If the cube is lined up with the hole to the side, insert it.\n    if check("the cube is horizontally aligned with hole"):\n        robot.put("gripper above door handle")\n',
        ),
        (
            -92.87031,
            '\n    #  1. Put gripper above cube\n    #  2. Drop gripper around cube\n    #  3. Move cube to target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not almost vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with cube and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the cube,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with cube"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.88358,
            '\n    #  1. Put gripper above cube\n    #  2. Drop gripper around cube\n    #  3. Move cube to target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not almost vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with cube and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the cube,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with cube"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.91442,
            '\n    #  1. Put gripper above cube\n    #  2. Drop gripper around cube\n    #  3. Move cube to target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not almost vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with cube and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the cube,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with cube"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -92.996994,
            '\n    #  1. Put gripper above cube\n    #  2. Drop gripper around cube\n    #  3. Move cube to target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not almost vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with cube and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the cube,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with cube"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -93.08941,
            '\n    #  1. Put gripper above cube\n    #  2. Drop gripper around cube\n    #  3. Move cube to target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not almost vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with cube and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the cube,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with cube"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -93.092445,
            '\n    #  1. Put gripper above cube\n    #  2. Drop gripper around cube\n    #  3. Move cube to target location\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not almost vertically aligned with cube"):\n        robot.slide("the puck to the goal")\n    # As long as the gripper is almost lined up, closing it should line it up\n    # all the way.\n    if check("the robot\'s gripper is almost vertically aligned with cube and the robot\'s gripper is open"):\n        robot.slide("window right")\n    # As long as the gripper is still vertically aligned with the cube,\n    # it\'s being opened, so keep pulling.\n    if check("the robot\'s gripper is vertically aligned with cube"):\n        robot.push("the gripper into the puck")\n',
        ),
        (
            -110.6703,
            '\n    #  1. Put gripper above the cube\n    #  2. Drop gripper around the cube\n    #  3. Pick up the cube\n    #  4. Move the gripper to the target location\n    #  5. Drop the cube\n    # First, put the gripper above the cube.\n    if check("the robot\'s gripper is not vertically aligned with the cube"):\n        robot.slide("the puck to the goal")\n    # If the gripper is lined up above the cube, drop it around the cube.\n    if check("the robot\'s gripper is vertically aligned with the cube and the robot\'s gripper is not around the cube"):\n        robot.push("window right harder")\n    # If the gripper is around the cube, pick it up.\n    if check("the robot\'s gripper is around the cube"):\n        robot.put("gripper above drawer handle")\n    # Move the gripper to the target location.\n    if check("the robot\'s gripper is not aligned with the target location"):\n        robot.push("the gripper into the puck")\n    # Drop the cube.\n    if check("the robot\'s gripper is aligned with the target location"):\n        robot.reach("to goal")\n',
        ),
    ],
    "window-close": [
        (0.0, ""),
        (
            -77.03858,
            '\n    #  1. Put gripper left of the window handle\n    #  2. Start pushing against the window handle to close the window\n    #  3. Push the window closed harder\n    # If the the window handle is right of the robot\'s gripper, we should move the\n    # gripper near the window handle to start pushing\n    if check("the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window close now by moving the gripper right.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.reach("to goal")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -77.04861,
            '\n    #  1. Put gripper left of the window handle\n    #  2. Start pushing against the window handle to close the window\n    #  3. Push the window closed harder\n    # If the the window handle is right of the robot\'s gripper, we should move the\n    # gripper near the window handle to start pushing\n    if check("the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window close now by moving the gripper right.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.reach("to goal")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -77.10193,
            '\n    #  1. Put gripper left of the window handle\n    #  2. Start pushing against the window handle to close the window\n    #  3. Push the window closed harder\n    # If the the window handle is right of the robot\'s gripper, we should move the\n    # gripper near the window handle to start pushing\n    if check("the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window close now by moving the gripper right.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.reach("to goal")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -77.10633,
            '\n    #  1. Put gripper left of the window handle\n    #  2. Start pushing against the window handle to close the window\n    #  3. Push the window closed harder\n    # If the the window handle is right of the robot\'s gripper, we should move the\n    # gripper near the window handle to start pushing\n    if check("the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window close now by moving the gripper right.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.reach("to goal")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -77.11448,
            '\n    #  1. Put gripper left of the window handle\n    #  2. Start pushing against the window handle to close the window\n    #  3. Push the window closed harder\n    # If the the window handle is right of the robot\'s gripper, we should move the\n    # gripper near the window handle to start pushing\n    if check("the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window close now by moving the gripper right.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.reach("to goal")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -77.12572,
            '\n    #  1. Put gripper left of the window handle\n    #  2. Start pushing against the window handle to close the window\n    #  3. Push the window closed harder\n    # If the the window handle is right of the robot\'s gripper, we should move the\n    # gripper near the window handle to start pushing\n    if check("the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window close now by moving the gripper right.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.reach("to goal")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.put("the gripper above the puck")\n',
        ),
        (
            -77.1355,
            '\n    #  1. Put gripper left of the window handle\n    #  2. Start pushing against the window handle to close the window\n    #  3. Push the window closed harder\n    # If the the window handle is right of the robot\'s gripper, we should move the\n    # gripper near the window handle to start pushing\n    if check("the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window close now by moving the gripper right.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.reach("to goal")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.put("the gripper above the puck")\n',
        ),
    ],
    "window-open": [
        (
            -78.28747,
            '\n    #  1. Put gripper right of the window handle\n    #  2. Start pushing against the window handle to open the window\n    #  3. Push the window open harder\n    # If the robot\'s gripper is not vertically lined up with the window handle,\n    # we should move the gripper near the window handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window open now by moving the gripper left.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -78.33518,
            '\n    #  1. Put gripper right of the window handle\n    #  2. Start pushing against the window handle to open the window\n    #  3. Push the window open harder\n    # If the robot\'s gripper is not vertically lined up with the window handle,\n    # we should move the gripper near the window handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window open now by moving the gripper left.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -78.34565,
            '\n    #  1. Put gripper right of the window handle\n    #  2. Start pushing against the window handle to open the window\n    #  3. Push the window open harder\n    # If the robot\'s gripper is not vertically lined up with the window handle,\n    # we should move the gripper near the window handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window open now by moving the gripper left.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -78.37618,
            '\n    #  1. Put gripper right of the window handle\n    #  2. Start pushing against the window handle to open the window\n    #  3. Push the window open harder\n    # If the robot\'s gripper is not vertically lined up with the window handle,\n    # we should move the gripper near the window handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window open now by moving the gripper left.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -78.38904,
            '\n    #  1. Put gripper right of the window handle\n    #  2. Start pushing against the window handle to open the window\n    #  3. Push the window open harder\n    # If the robot\'s gripper is not vertically lined up with the window handle,\n    # we should move the gripper near the window handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window open now by moving the gripper left.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -78.41069,
            '\n    #  1. Put gripper right of the window handle\n    #  2. Start pushing against the window handle to open the window\n    #  3. Push the window open harder\n    # If the robot\'s gripper is not vertically lined up with the window handle,\n    # we should move the gripper near the window handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window open now by moving the gripper left.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -78.463135,
            '\n    #  1. Put gripper right of the window handle\n    #  2. Start pushing against the window handle to open the window\n    #  3. Push the window open harder\n    # If the robot\'s gripper is not vertically lined up with the window handle,\n    # we should move the gripper near the window handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window open now by moving the gripper left.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.reach("to goal")\n',
        ),
        (
            -78.492645,
            '\n    #  1. Put gripper right of the window handle\n    #  2. Start pushing against the window handle to open the window\n    #  3. Push the window open harder\n    # If the robot\'s gripper is not vertically lined up with the window handle,\n    # we should move the gripper near the window handle to start pushing\n    if check("the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle"):\n        robot.slide("the puck to the goal")\n    # If the robot\'s gripper is near the window handle we can probably slide the\n    # window open now by moving the gripper left.\n    if check("the robot\'s gripper is near the window handle"):\n        robot.close("gripper around puck")\n    # If the robot\'s gripper is starting to be in front of the window handle,\n    # push harder.\n    if check("the robot\'s gripper is in front of the window handle"):\n        robot.reach("to goal")\n',
        ),
    ],
}
