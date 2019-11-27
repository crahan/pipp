#!/usr/bin/env python3

import subprocess
import sys
import argparse
from YamJam import yamjam, YAMLError


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '--profile',
    '-p',
    type=str
)

args, unknown = parser.parse_known_args()
pipargs = [sys.executable, '-m', 'pip']
pargs = []

if args.profile:
    try:
        p = yamjam()['pypi-profiles'][args.profile]['index']
    except (YAMLError, KeyError):
        sys.exit("Could not load {0}. Exiting.".format(args.profile))
    pargs = ['-i', p]

pipargs.extend(unknown)
pipargs.extend(pargs)
subprocess.call(pipargs)
