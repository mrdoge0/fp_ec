#!/usr/bin/env python3
# fp_ec main wrapper
import sys

# "--help"
try:
    if sys.argv[1] == "--help":
        print("Usage: [--help] [--verbose] [--version]")
        exit(1)
except: print("")

# Import other standard libs.
import os
import ctypes
import hashlib
import shutil
import subprocess
import random

# Declare version.
def Version():
    try:
        with open("version", "r") as vfile:
            return vfile.readline().strip()
    except:
        return "unknown"

# "--version"
try:
    if sys.argv[1] == "--version":
        print("v" + Version())
        exit(0)
except: print("")

# Toggle verbose mode.
try:
    if sys.argv[1] == "--verbose":
        is_verbose = True
        print("Debug: Running in verbose mode.")
    else:
        is_verbose = False
except:
    is_verbose = False

# Exit successfully if nothing is active.
exit(0)
