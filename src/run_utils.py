import clize


@clize.parser.value_converter
def float_list(arg):
    return [float(f) for f in arg.split(",")]


@clize.parser.value_converter
def str_list(arg):
    return [str(s) for s in arg.split(",")]
