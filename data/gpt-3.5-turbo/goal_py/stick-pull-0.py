# Steps:
    #  1. Position the stick so that it can reach the thermos from the target location
    #  2. Use the hook at the end of the stick to grab onto the thermos
    #  3. Slowly pull the thermos towards the target location
    # First, position the stick so that it can reach the thermos from the target location
    if check("the stick is not in position to reach the thermos from the target location"):
        robot.move_stick("in position")
    # If the hook is not around the thermos, use the hook to grab onto it
    if check("the hook is not around the thermos"):
        robot.use_hook("to grab the thermos")
    # Once the hook is secure, slowly pull the thermos towards the target location
    if check("the thermos has not been pulled to the target location yet"):
        robot.move_thermos("towards the target location")