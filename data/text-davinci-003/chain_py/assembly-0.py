
    # Steps:
    #  1. Wrap the wrench around the peg
    #  2. Put the wrench over the fastener
    #  3. Put the wrench around the fastener
    #  4. Tighten the fastener with the wrench
    # First, wrap the wrench around the peg.
    if check("the wrench is not wrapped around the peg"):
        robot.wrap("wrench around peg")
    # if the wrench is still not lined up with the fastener, put the wrench over
    # the fastener
    if check("the wrench is not aligned with fastener and the wrench is wrapped around the peg"):
        robot.put("wrench over fastener")
    # Now, close the wrench around the fastener.
    if check("the wrench is aligned with fastener"):
        robot.close("wrench around fastener")
    # Now, tighten the fastener with the wrench.
    if check("the wrench is closed around the fastener"):
        robot.tighten("fastener with wrench")