import argparse
import os
import sys
import shutil
import time
import subprocess

# Check for existence of the installed package list

if not os.path.exists('installed.jamo'):
    f = open("installed.jamo", "x")

