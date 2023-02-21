import argparse
import os
import sys
import shutil
import time

def printhelp():
    print("""
          Welcome to Joma Wrapper. This is a Package Manager Wrapper to help you manage your packages. \n
          This are the options you can use and it's descriptions: \n
          Install       - Installs a Package \n
          Remove        - Removes/Uninstalls a Package \n
          Uninstall     - Removes/Uninstalls a Package \n
          Search        - Searches for a Package \n
          Import        - Imports the Package Lists from a directory \n
          Export        - Exports the Package Lists to a directory \n
          Help          - Shows this help
          """)

# Define Arguments

parser = argparse.ArgumentParser(description = "Joma is a package manager wrapper to help you manage the packages on your Windows system with 3 diffrent package managers.")
parser.add_argument('action', type=str, help=printhelp)
parser.add_argument('package_list', type=list, help='Package Name(s)', nargs='?', default=['tmp'])
parser.add_argument('file_path', type=str, help='Folder where the lists are located', nargs='?', default='.')
args = parser.parse_args()

file_path = args.file_path
package_list_file = args.package_list
action = args.action

# Joma Functions

def jomainstall(package_list):
    time.sleep(0)

def jomaremove(package_list):
    time.sleep(0)
    
def jomasearch(package_list):
    time.sleep(0)

def jomaupdate(package_list):
    time.sleep(0)

def jomaupgrade():
    time.sleep(0)

def jomaimport(package_list):
    time.sleep(0)
    
def jomaexport(package_list):
    time.sleep(0)
    
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
