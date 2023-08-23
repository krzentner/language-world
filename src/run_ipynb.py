#!/bin/env python
from typing import Optional
from shutil import copy2
from subprocess import check_call
from os.path import splitext
import clize


def run_ipynb(notebook: str, in_config_file: str, *, out_config_file: str = ""):
    if not out_config_file:
        base_filename, _ = splitext(notebook)
        out_config_file = f"{base_filename}.yaml"
    copy2(in_config_file, out_config_file)
    check_call(["jupyter", "execute", notebook])

if __name__ == '__main__':
    clize.run(run_ipynb)
