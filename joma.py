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
listnames = ['scoop-packages.txt', 'choco-packages.txt', 'winget-packages.txt']
enablecmd1 = False
enablecmd2 = False
enablecmd3 = False

# Get arguments

if len(sys.argv) < 3:
    print("Usage: joma action package")
    sys.exit(1)
    
action = sys.argv[1].lower()
package_list = sys.argv[2:]

# Check if the package managers are installed

if os.path.exists(pml[2]):
    print('Scoop detected')
    enablecmd1 = True
else:
    print('Scoop not detected')
    installscoopask = input('Do you want to install it? [Y/n]: ')
    if installscoopask == '' or 'y' or 'Y':
        print('we will install it')
        enablecmd1 = True
    elif installscoopask == 'n' or 'N':
        print('we will not install it')
        enablecmd1 = False
    else:
        print('unsupported')

if os.path.exists(pml[1]):
    print('Chocolatey detected')
    enablecmd2 = True
else:
    print('Chocolatey not detected')
    installchocoask = input('Do you want to install it? [Y/n]: ')
    if installchocoask == '' or 'y' or 'Y':
        print('we will install it')
        enablecmd2 = True
    elif installchocoask == 'n' or 'N':
        print('we will not install it')
        enablecmd2 = False
    else:
        print('unsupported')

if os.path.exists(pml[0]):
    print('Winget detected')
    enablecmd3 = True
else:
    print('Winget not detected')
    print('Update your Windows and update your apps from microsoft store')
    enablecmd3 = False


# Basic functions

def jomainstall():
    command1 = ['scoop', 'install', package_list, '-y']
    command2 = ['choco', 'install', package_list, '--yes']
    command3 = ['winget', 'install', '-e', package_list, '-y']
    
def jomaremove():
    command1 = ['scoop', 'uninstall', package_list, '-y']
    command2 = ['choco', 'uninstall', package_list, '--yes']
    command3 = ['winget', 'uninstall', package_list, '-y']
        
def jomaupdate():
    command1 = ['scoop', 'update', package_list, '-y']
    command2 = ['choco', 'upgrade', package_list, '--yes']
    command3 = ['winget', 'update', package_list, '-y']
    
def jomasearch():
    command1 = ['scoop', 'search', package_list]
    command2 = ['choco', 'search', package_list]
    command3 = ['winget', 'search', package_list]
    
def jomaexport():
    command1 = ['scoop', 'list', '>', listnames[0]]
    command2 = ['choco', 'list', '--local-only', '>', listnames[1]]
    command3 = ['winget', 'show', 'installed' '>', listnames[2]]
    
def jomaimport():
    print('code for this function')

def jomaupgrade():
    command1 = ['scoop', 'update', '-y']
    command2 = ['choco', 'upgrade', '--yes']
    command3 = ['winget', 'update', '-y']
    

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