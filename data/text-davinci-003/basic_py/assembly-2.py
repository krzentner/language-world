
    if check("wrench is above peg"):
        robot.put("wrench below peg")
    if check("wrench is not around peg"):
        robot.wrap("wrench around peg")