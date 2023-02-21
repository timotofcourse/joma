import argparse
import os
import sys
import shutil
import time
import subprocess

def printhelp():
    print("""
          Welcome to Joma Wrapper. This is a Package Manager Wrapper to help you manage your packages. \n
          This are the options you can use and it's descriptions: \n
          Install       - Installs a Package \n
          Remove        - Removes/Uninstalls a Package \n
          Uninstall     - Removes/Uninstalls a Package \n
          Update        - Updates a Package \n
          Upgrade       - Updates all packages \n
          Search        - Searches for a Package \n
          Import        - Imports the Package Lists from a directory \n
          Export        - Exports the Package Lists to a directory \n
          Help          - Shows this help
          """)

# Define Arguments

parser = argparse.ArgumentParser(description = "Joma is a package manager wrapper to help you manage the packages on your Windows system with 3 diffrent package managers.")
parser.add_argument('action', type=str, help=printhelp)
parser.add_argument('package_list', type=list, help='Package Name(s)', nargs='?', default=['tmp'])
parser.add_argument('--file_path', '-f', type=str, help='Folder where the lists are located')
args = parser.parse_args()

file_path = args.file_path
package_list_file = args.package_list
action = args.action

# Check for installed package managers

if shutil.which('scoop') is not None:
    print('Scoop Found')
    runscoop = True
else:
    print('Scoop not Found')
    runscoop = False

if shutil.which('choco') is not None:
    print('Chocolatey Found')
    runchoco = True
else:
    print('Chocolatey not Found')
    runchoco = False

if shutil.which('winget') is not None:
    print('Winget Found')
    runwinget = True
else:
    print('Winget not Found')
    runwinget = False

if shutil.which('sudo') is not None:
    print('Sudo Found')
else:
    print('Sudo not Found')

# Joma Functions

def jomainstall(package_list):
    launchprocess(package_manager='scoop', action='install', args='-y')
    launchprocess(package_manager='choco', action='install', args='-y')
    launchprocess(package_manager='winget', action='install', args='-y')
    sys.exit(0)

def jomaremove(package_list):
    launchprocess(package_manager='scoop', action='uninstall', args='-y')
    launchprocess(package_manager='choco', action='uninstall', args='-y')
    launchprocess(package_manager='winget', action='uninstall', args='-y')
    sys.exit(0)
    
def jomasearch(package_list):
    launchprocess(package_manager='scoop', action='search', args='-y')
    launchprocess(package_manager='choco', action='search', args='-y')
    launchprocess(package_manager='winget', action='search', args='-y')
    sys.exit(0)

def jomaupdate(package_list):
    launchprocess(package_manager='scoop', action='update', args='-y')
    launchprocess(package_manager='choco', action='update', args='-y')
    launchprocess(package_manager='winget', action='update', args='-y')
    sys.exit(0)

def jomaupgrade():
    launchprocess(package_manager='scoop', action='upgrade', args='-y')
    launchprocess(package_manager='choco', action='upgrade', args='-y')
    launchprocess(package_manager='winget', action='upgrade', args='-y')
    sys.exit(0)

def jomaimport(package_list):
    launchprocess(package_manager='scoop', action='import', args=package_list)
    launchprocess(package_manager='choco', action='import', args=package_list)
    launchprocess(package_manager='winget', action='import', args=package_list)
    sys.exit(0)
    
def jomaexport(package_list):
    launchprocess(package_manager='scoop', action='export', args=package_list)
    launchprocess(package_manager='choco', action='export', args=package_list)
    launchprocess(package_manager='winget', action='export', args=package_list)
    sys.exit(0)
    
def launchprocess(package_manager, action, packages, args):
    command = package_manager, action, packages, args,
    runcommand = subprocess.Popen(command, shell=True)
    runcommand.communicate()
    runcommand.wait()
    

# Logic for the package manager arguments

if action == 'upgrade':
    jomaupgrade()
elif action == 'import':
    jomaimport(package_list=file_path)
elif action == 'export':
    jomaexport(package_list=file_path)
elif action == 'help':
    printhelp()
elif action == 'remove' or 'uninstall':
    jomaremove(package_list=package_list_file)
elif action == 'install':
    jomainstall(package_list=package_list_file)
elif action == 'update':
    jomaupdate(package_list=package_list_file)
elif action == 'search':
    jomasearch(package_list=package_list_file)
else:
    print('Action not supported')
