import argparse
import os
import sys
import shutil
import time

printhelp = print("""
                  
                  """)

# Define Arguments

parser = argparse.ArgumentParser(description = "Joma is a package manager wrapper to help you manage the packages on your Windows system with 3 diffrent package managers.")
parser.add_argument('action', metavar='action', type=str, help=printhelp)
parser.add_argument('packages', metavar='package_list', type=list, help='Package Name(s)', required=False)
parser.add_argument('file_path', metavar='file_path', type=str, help='Folder where the lists are located', required=False)
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