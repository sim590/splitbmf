#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import splitbmf

import os
import sys
import re
import subprocess
import argparse

FFMPEG_TEMPLATE    = [ "ffmpeg", "-y", "-nostdin", "-i", "INPUTFILE", "-ss", "BEGIN", "-to", "END", "OUTFILE.TYPE" ]
TRACK_DESC_PATTERN = "(([0-9]{2}:?){3})(.*)"

DEBUG = False

def DEBUG_PRINT(*args, **kwargs):
    component = "["+kwargs["component"]+"]" if "component" in kwargs else ""
    print("[DEBUG]"+component, *args, file=sys.stderr)

def main():
    ap = argparse.ArgumentParser(prog=splitbmf.__name__)
    ap.add_argument( "-t", "--type", nargs=1, type=str,
            help="Media type. Possible values are those understood by ffmpeg such as mp3,ogg,... Default is mp3.")
    ap.add_argument( "-i", "--input-file", required=True, nargs=1, type=str, help="Input file path.")
    ap.add_argument("-v", "--version", action="version", version="%(prog)s "+str(splitbmf.__version__))
    pa = ap.parse_args()

    cmd = FFMPEG_TEMPLATE
    if not pa.type:
        cmd = cmd[:-1] + ["-codec", "copy"] + cmd[-1:]

    cmd[cmd.index("-i")+1] = pa.input_file[0]
    _,intype = os.path.splitext(pa.input_file[0])
    intype = intype[1:]
    for line1 in sys.stdin:
        line2 = sys.stdin.readline()

        l1re = re.search(TRACK_DESC_PATTERN, line1)
        l2re = re.search(TRACK_DESC_PATTERN, line2)

        begin = l1re.group(1) if l1re else None
        end   = l2re.group(1) if l2re else None
        track = l1re.group(3) if l1re else None

        if DEBUG:
            DEBUG_PRINT("begin: ", begin, "end: ", end, "track: ", track)

        cmd[cmd.index("-ss")+1] = begin
        cmd[cmd.index("-to")+1] = end
        cmd[-1] = track + "." + (pa.type[0] if pa.type else intype)
        if DEBUG:
            DEBUG_PRINT("cmd: ", cmd)
        subprocess.run(cmd)

#  vim: set sts=4 ts=4 sw=4 tw=120 et :

