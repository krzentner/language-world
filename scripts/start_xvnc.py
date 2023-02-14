#!/usr/bin/env python3
from subprocess import Popen, check_output
import os
import time
import re


def main(display=2):
    env = os.environ.copy()
    env["DISPLAY"] = f":{display}"
    ip_addr = check_output(["ip", "addr", "show", "wg0"]).decode("utf-8")
    WG_IPs = re.findall(r"inet ([^ /]*)/", ip_addr)
    assert len(WG_IPs) == 1
    wg_ip = WG_IPs[0]
    xvfb_proc = Popen(["Xvfb", env["DISPLAY"], "-screen", "0,", "1366x768x24"])
    time.sleep(3)
    xvnc_proc = Popen(
        [
            "x11vnc",
            "-display",
            env["DISPLAY"],
            "-noxdamage",
            "-rfbport",
            "4900",
            "-listen",
            "localhost",
        ]
    )
    time.sleep(3)
    home = env["HOME"]
    novnc_proc = Popen(
        [
            f"{home}/noVNC/utils/novnc_proxy",
            "--vnc",
            "localhost:4900",
            "--listen",
            f"{wg_ip}:6081",
        ]
    )
    time.sleep(3)
    fluxbox_proc = Popen(["lxsession"])
    novnc_proc.wait()


if __name__ == "__main__":
    main()
