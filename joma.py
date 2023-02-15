import time
import sys
import os
import subprocess
import shutil

# Locations of package managers

home = os.path.expanduser("~")
packagemanagers = ['winget', 'choco', 'scoop']
scooplist = home + '/scoop-packages.txt'
chocolist = home + '/choco-packages.txt'
wingetlist = home + '/winget-packages.txt'
listnames = [scooplist, chocolist, wingetlist]

#  Check for package managers

def checkpackagemanagers(pm):
    return shutil.which(pm) is not None

scoopfound = checkpackagemanagers('scoop')
chocofound = checkpackagemanagers('choco')
wingetfound = checkpackagemanagers('winget')

# Basic Functions


def jomainstall(package_list):
    scoopcommand = ['scoop', 'install'] + package_list + ['-y']
    chococommand = ['choco', 'install'] + package_list + ['--yes']
    wingetcommand = ['winget', 'install', '-e'] + package_list + ['-y']
    if scoopfound:
        cmd = subprocess.run(scoopcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if chocofound:
        cmd = subprocess.run(chococommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if wingetfound:
        cmd = subprocess.run(wingetcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    
def jomaremove(package_list):
    scoopcommand = ['scoop', 'uninstall', package_list, '-y']
    chococommand = ['choco', 'uninstall', package_list, '--yes']
    wingetcommand = ['winget', 'uninstall', package_list, '-y']
    if scoopfound:
        cmd = subprocess.run(scoopcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if chocofound:
        cmd = subprocess.run(chococommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if wingetfound:
        cmd = subprocess.run(wingetcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
        
def jomaupdate(package_list):
    scoopcommand = ['scoop', 'update', package_list, '-y']
    chococommand = ['choco', 'upgrade', package_list, '--yes']
    wingetcommand = ['winget', 'upgrade', package_list, '-y']
    if scoopfound:
        cmd = subprocess.run(scoopcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if chocofound:
        cmd = subprocess.run(chococommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if wingetfound:
        cmd = subprocess.run(wingetcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    
def joma_search(package_list):
    package_list = package_list.lower()
    managers = ['scoop', 'choco', 'winget']
    for manager in managers:
        if checkpackagemanagers(manager):
            command = [manager, 'search', package_list]
            cmd = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = cmd.communicate()
            if error:
                print(f"An error occurred: {error.decode('utf-8')}")
            else:
                print(f"Output from {manager}:")
                print(output.decode('utf-8'))
        else:
            print(f"{manager} not found on this system.")
    
def jomaexport():
    scoopcommand = ['scoop', 'export', '>', listnames[0]]
    chococommand = ['choco', 'export', listnames[1]]
    wingetcommand = ['winget', 'export', '-o', listnames[2]]
    if scoopfound:
        cmd = subprocess.run(scoopcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if chocofound:
        cmd = subprocess.run(chococommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if wingetfound:
        cmd = subprocess.run(wingetcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    
def jomaimport():
    scoopcommand = ['scoop', 'install', listnames[0]]
    chococommand = ['choco', 'install', listnames[1]]
    wingetcommand = ['winget', 'import', '-i', listnames[2]]
    if scoopfound:
        cmd = subprocess.run(scoopcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if chocofound:
        cmd = subprocess.run(chococommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if wingetfound:
        cmd = subprocess.run(wingetcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")

def jomaupgrade():
    scoopcommand = ['scoop', 'update', '*', '-y']
    chococommand = ['choco', 'upgrade', 'all', '--yes']
    wingetcommand = ['winget', 'upgrade', '--all', '-y']
    if scoopfound:
        cmd = subprocess.run(scoopcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if chocofound:
        cmd = subprocess.run(chococommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if wingetfound:
        cmd = subprocess.run(wingetcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    
def jomaerror():
    print('Action not supported')
    
def jomahelp():
    print('Here\'s a list of supported operations: ')
    print("""
          install - Installs a package \n
          remove - Removes a package \n
          uninstall - Removes a package\n
          update - Updates a package\n
          upgrade - Updates all packages\n
          search - Search for a package\n
          export - Exports the lists of installed packages through scoop, chocolatey and winget \n
          import - Imports the lists from previous installed packages from scoop, chocolatey and winget\n
          \n
          Note: The Exported lists will have the package manager name in the filename so if you want to import a list make sure the names are the sames as joma exported""")
    sys.exit(1)

# Check for Installed package managers

def runsubprocess(process, wait):
    runprocess = subprocess.Popen(process)
    if wait:
        runprocess.wait()
    return runprocess.returncode
    

# Function to add scoop buckets

def addbuckets():
     # Add all the buckets
    
    basebuckets = ['main', 'games', 'extras', 'versions', 'java', 'nonportable']
    for bucket in basebuckets:
        bucket = subprocess.Popen(bucket, shell=True)
        bucket.wait()
        
    # Add my bucket
    
    runsubprocess(process='scoop' 'bucket' 'add' 'filmabem' 'https://github.com/FilmaBem2/applications.git', wait=True)

# Get arguments

if len(sys.argv) < 2:
    print("Usage: joma action [package]")
    print("Note: When you import/export package lists they will be stored/imported from your home folder")
    print("For help use: \"joma help\"")
    sys.exit(1)

action = sys.argv[1].lower()

if action == "upgrade" or "import" or "export" or "help":
    if action == "upgrade":
        jomaupgrade()
    elif action == "export":
        jomaexport()
    elif action == "import":
        jomaimport()
    elif action == "help":
        jomahelp()
else:
    if len(sys.argv) < 3:
        print("Usage: joma action package")
        print("Note: When you import/export package lists they will be stored/imported from your home folder")
        print("For help use: \"joma help\"")
        sys.exit(1)

    package_list = sys.argv[2:]
    
    # Perform other actions with package argument
    
    print(f"Performing {action} action on packages: {', '.join(package_list)}")
    for package_name in package_list:
        if action == "install":
            jomainstall(package_list=package_list)
        elif action == "remove":
            jomaremove(package_list=package_list)
        elif action == "uninstall":
            jomaremove(package_list=package_list)
        elif action == "update":
            jomaupdate(package_list=package_list)
        elif action == "search":
            jomasearch(package_list=package_list)
        else:
            jomaerror()
            sys.exit(1)


