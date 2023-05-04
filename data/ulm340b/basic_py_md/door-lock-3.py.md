

Once you complete the program, I will be able to run the robot.

    """

    example_code = [
        # drawer-close: push the drawer close
        "def drawer_close(robot):\n" +
        "    if check('the robot''s gripper is not near the drawer handle'):\n" +
        "        robot.grab('drawer handle')\n" +
        "    if check('the robot''s gripper is forward aligned with drawer handle'):\n" +
        "        robot.push('drawer closed')",

        # reach: reach to the target location
        "def reach(robot):\n" +
        "    if check('the robot''s gripper is not near reach target'):\n" +
        "        robot.reach('to goal')",

        # peg-insert-side: grab the peg and insert it into the hole from the side
        "def peg_insert_side(robot):\n" +
        "    if check('the robot''s gripper is not vertically aligned with the peg'):\n" +
        "        robot.put('gripper above peg')\n" +
        "    if check('peg is not left of the robot''s gripper and peg is not forward aligned with the robot''s gripper'):\n" +
        "        robot.grab('peg')\n" +
        "    if check('the robot''s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole'):\n" +
        "        robot.align('peg to hole')\n" +
        "    if check('peg is horizontally aligned with hole'):\n" +
        "        robot.insert('peg into hole')",

        # push: slide the puck to the target location
        "def push(robot):\n" +
        "    if check('the robot''s gripper is not above puck and the robot''s gripper is not vertically aligned with the puck'):\n" +
        "        robot.put('the gripper above the puck')\n" +
        "    if check('the robot''s gripper is vertically aligned with the puck and the robot''s gripper is not near puck'):\n" +
        "        robot.push('the gripper into the puck')\n" +
        "    if check('the robot''s gripper is near the puck and the puck is below the robot''s gripper'):\n" +
        "        robot