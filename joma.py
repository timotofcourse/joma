import time
import sys
import os
import subprocess

# Locations of package managers

home = os.path.expanduser("~")
wget = home + '/AppData/Local/Microsoft/WindowsApps/winget.exe'
scoop = home  + '/scoop/apps/scoop/current/'
pml = [wget, 'C:\\ProgramData\\chocolatey\\bin\\choco.exe', scoop]
scooplist = home + '/scoop-packages.txt'
chocolist = home + '/choco-packages.txt'
wingetlist = home + '/winget-packages.txt'
listnames = [scooplist, chocolist, wingetlist]
enablecmd1 = False
enablecmd2 = False
enablecmd3 = False

# Basic Functions


def jomainstall(package_list, enablecmd1=True, enablecmd2=True, enablecmd3=True):
    command1 = ['scoop', 'install'] + package_list + ['-y']
    command2 = ['choco', 'install'] + package_list + ['--yes']
    command3 = ['winget', 'install', '-e'] + package_list + ['-y']
    if enablecmd1:
        cmd = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if enablecmd2:
        cmd = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    if enablecmd3:
        cmd = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    
def jomaremove():
    command1 = ['scoop', 'uninstall', package_list, '-y']
    command2 = ['choco', 'uninstall', package_list, '--yes']
    command3 = ['winget', 'uninstall', package_list, '-y']
    if enablecmd1 == True:
        cmd = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd2 == True:
        cmd = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd3 == True:
        cmd = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
        
def jomaupdate():
    command1 = ['scoop', 'update', package_list, '-y']
    command2 = ['choco', 'upgrade', package_list, '--yes']
    command3 = ['winget', 'upgrade', package_list, '-y']
    if enablecmd1 == True:
        cmd = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd2 == True:
        cmd = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd3 == True:
        cmd = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    
def jomasearch():
    command1 = ['scoop', 'search', package_list]
    command2 = ['choco', 'search', package_list]
    command3 = ['winget', 'search', package_list]
    if enablecmd1 == True:
        cmd = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd2 == True:
        cmd = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd3 == True:
        cmd = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    
def jomaexport():
    command1 = ['scoop', 'export', '>', listnames[0]]
    command2 = ['choco', 'export', listnames[1]]
    command3 = ['winget', 'export', '-o', listnames[2]]
    if enablecmd1 == True:
        cmd = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd2 == True:
        cmd = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd3 == True:
        cmd = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    
def jomaimport():
    command1 = ['scoop', 'install', listnames[0]]
    command2 = ['choco', 'install', listnames[1]]
    command3 = ['winget', 'import', '-i', listnames[2]]
    if enablecmd1 == True:
        cmd = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd2 == True:
        cmd = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd3 == True:
        cmd = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)

def jomaupgrade():
    command1 = ['scoop', 'update', '*', '-y']
    command2 = ['choco', 'upgrade', 'all', '--yes']
    command3 = ['winget', 'upgrade', '--all', '-y']
    if enablecmd1 == True:
        cmd = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd2 == True:
        cmd = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    if enablecmd3 == True:
        cmd = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = cmd.communicate()
        if error:
            print(f"An error occurred: {error.decode('utf-8')}")
        else:
            print(f"Output: {output.decode('utf-8')}")
    else:
        time.sleep(0)
    
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
    if wait == True:
        runprocess.wait()
    

# Check if the package managers are installed

if os.path.exists(pml[2]):
    print('Scoop detected')
    enablecmd1 = True
    
    # Add all the buckets
    
    installgit = subprocess.Popen('scoop install git', shell=True)
    installgit.wait()
    mainbucket = subprocess.Popen('scoop bucket add main', shell=True)
    mainbucket.wait()
    gamesbucket = subprocess.Popen('scoop bucket add games', shell=True)
    gamesbucket.wait()
    extrasbucket = subprocess.Popen('scoop bucket add extras', shell=True)
    extrasbucket.wait()
    versionsbucket = subprocess.Popen('scoop bucket add versions', shell=True)
    versionsbucket.wait()
    javabucket = subprocess.Popen('scoop bucket add java', shell=True)
    javabucket.wait()
    nonportablebucket = subprocess.Popen('scoop bucket add nonportable', shell=True)
    nonportablebucket.wait()
    filmabembucket = subprocess.Popen('scoop bucket add filmabem https://github.com/FilmaBem2/applications.git', shell=True)
    filmabembucket.wait()
else:
    print('Scoop not detected')
    installscoopask = input('Do you want to install it? [Y/n]: ')
    if installscoopask == '' or 'y' or 'Y':
        
        # Install Scoop
        
        installscoop = subprocess.Popen('irm get.scoop.sh | iex', shell=True)
        installscoop.wait()
        enablecmd1 = True
        
        # Add all the buckets
        
        installgit = subprocess.Popen('scoop install git', shell=True)
        installgit.wait()
        mainbucket = subprocess.Popen('scoop bucket add main', shell=True)
        mainbucket.wait()
        gamesbucket = subprocess.Popen('scoop bucket add games', shell=True)
        gamesbucket.wait()
        extrasbucket = subprocess.Popen('scoop bucket add extras', shell=True)
        extrasbucket.wait()
        versionsbucket = subprocess.Popen('scoop', 'bucket', 'add', 'versions', shell=True)
        versionsbucket.wait()
        javabucket = subprocess.Popen('scoop bucket add java', shell=True)
        javabucket.wait()
        nonportablebucket = subprocess.Popen('scoop bucket add nonportable', shell=True)
        nonportablebucket.wait()
        filmabembucket = subprocess.Popen('scoop bucket add filmabem https://github.com/FilmaBem2/applications.git', shell=True)
        filmabembucket.wait()
    elif installscoopask == 'n' or 'N':
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
        
        # Install Chocolatey
        
        installchoco = subprocess.Popen("[System.Net.ServicePointManager]::SecurityProtocol", "=",  "[System.Net.ServicePointManager]::SecurityProtocol", "-bor", "3072;", "iex", "((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
        installchoco.wait()
        enablecmd2 = True
    elif installchocoask == 'n' or 'N':
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


