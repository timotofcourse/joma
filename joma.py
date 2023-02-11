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

# Check if the package managers are installed

if os.path.exists(pml[2]):
    print('Scoop detected')
else:
    print('Scoop not detected')
    installscoopask = input('Do you want to install it? [Y/n]: ')
    if installscoopask == '' or 'y' or 'Y':
        print('we will install it')
    elif installscoopask == 'n' or 'N':
        print('we will not install it')
    else:
        print('unsupported')

if os.path.exists(pml[1]):
    print('Chocolatey detected')
else:
    print('Chocolatey not detected')
    installchocoask = input('Do you want to install it? [Y/n]: ')
    if installchocoask == '' or 'y' or 'Y':
        print('we will install it')
    elif installchocoask == 'n' or 'N':
        print('we will not install it')
    else:
        print('unsupported')

if os.path.exists(pml[0]):
    print('Winget detected')
else:
    print('Winget not detected')
    print('Update your Windows and update your apps from microsoft store')

# Basic functions

def jomainstall():
    command1 = ['scoop', 'install', package_list, '-y']
    command2 = ['choco', 'install', package_list, '--yes']
    command3 = ['winget', 'install', '-e', package_list, '-y']
    
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
    
# Get arguments

if len(sys.argv) < 3:
    print("Usage: joma action package")
    sys.exit(1)
    
action = sys.argv[1].lower()
package_list = sys.argv[2:]

# Identify action and add a temporary code for the actions

for package_name in package_list:
    if action == "install":
        command = ["winget", "install", '-e', package_name]
    elif action == "remove":
        command = ["winget", "uninstall", package_name]
    elif action == "uninstall":
        command = ["winget", "uninstall", package_name]
    elif action == "update":
        command = ["winget", "update", package_name]
    elif action == "upgrade":
        command = ["winget", "update", '--all']
    elif action == "search":
        command = ["winget", "search", package_name]
    elif action == "export":
        command = ["winget", "export", "-o", "wget_pkgs.json"]
    elif action == "import":
        command = ["winget", "import", "-i", "wget_pkgs.json"]
    else:
        print(f"Error: Unknown action '{action}'")
        sys.exit(1)

    result = subprocess.run(command, stdout=subprocess.PIPE)