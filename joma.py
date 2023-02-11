import time
import argparse
import sys
import os
import platform
import subprocess

# Locations of package managers

home = os.path.expanduser("~")
wget = home + '/AppData/Local/Microsoft/WindowsApps/winget.exe'
scoop = home  + '/scoop/apps/scoop/current/'
pml = [wget, 'C:\\ProgramData\\chocolatey\\bin\\choco.exe', scoop]

# Basic functions

def jomainstall():
    print('code for this function')
    
def jomaremove():
    print('code for this function')
        
def jomaupdate():
    print('code for this function')
    
def jomasearch():
    print('code for this function')
    
def jomaexport():
    print('code for this function')
    
def jomaimport():
    print('code for this function')

def jomaupgrade():
    print('code for this function')
    
