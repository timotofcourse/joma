#!/usr/share/python

import argparse
import os
import sys
import shutil
import time
import threading

# Check if parallel downloads are enabled and if not enable 16 parallel downloads

def is_parallel_downloads_enabled():

    try:

        pacman_conf = open("/etc/pacman.conf", "r").read()

        if "ParallelDownloads" in pacman_conf:

            lines = pacman_conf.split("\n")

            for line in lines:

                if line.strip().startswith("ParallelDownloads") and "=" in line:

                    value = line.split("=")[1].strip()

                    if value.isdigit() and int(value) > 0:

                        return True
                    
        return False
    
    except FileNotFoundError:

        return False

# Enable parallel downloads
 
def enable_parallel_downloads():

    try:

        with open("/etc/pacman.conf", "a") as pacman_conf:

            if not is_parallel_downloads_enabled():

                pacman_conf.write("ParallelDownloads = 16\n")

        print("Parallel downloads enabled.")

    except FileNotFoundError:

        print("Error: pacman.conf not found.")
        sys.exit(1)

# Add repository for pacman

def add_repository(repo_name, repo_url):

    try:

        with open("/etc/pacman.conf", "a") as pacman_conf:

            pacman_conf.write(f"[{repo_name}]\n")

            pacman_conf.write(f"Server = {repo_url}\n")

        print(f"Repository '{repo_name}' added.")

    except FileNotFoundError:

        print("Error: pacman.conf not found.")
        sys.exit(1)

# Check if git is installed and install it

def check_and_install_git():

    result = os.system("which git > /dev/null 2>&1")

    if result != 0:

        print("Git is not installed. Installing git...")
        os.system("sudo pacman -S git")

# Install an AUR helper

def install_aur_helper(helper_name):

    print(f"Installing {helper_name} from AUR...")

    # Clone the AUR helper's Git repository

    os.system(f"git clone https://aur.archlinux.org/{helper_name}.git")
    os.chdir(helper_name)
    
    # Check for and install dependencies and make dependencies

    os.system("makepkg -sri --needed --noconfirm")
    
    print(f"{helper_name} installed.")


# Add AUR support

def add_aur_support():

    check_and_install_git()
    
    # Check if yay and/or paru are installed

    result = os.system("which yay > /dev/null 2>&1")

    if result == 0:

        print("Yay is installed.")

        return

    result = os.system("which paru > /dev/null 2>&1")

    if result == 0:

        print("Paru is installed.")

        return

    # If neither Yay nor Paru is installed, prompt the user to choose one

    while True:

        choice = input("Neither Yay nor Paru is installed. Do you want to install Yay or Paru? (yay/paru): ").strip().lower()

        if choice == "yay":

            install_aur_helper("yay")

            return
        
        elif choice == "paru":

            install_aur_helper("paru")

            return
        
        else:

            print("Invalid choice. Please enter 'yay' or 'paru'.")

# Install Packages

def install_packages(package_names, aur_helper):

    if package_names:

        if aur_helper:
            
            result = os.system(f"which {aur_helper} > /dev/null 2>&1")

            if result == 0:

                print(f"Installing packages: {', '.join(package_names)} from AUR using {aur_helper}...")
                os.system(f"{aur_helper} -S --needed --noconfirm {' '.join(package_names)}")

            else:

                print(f"{aur_helper} is not installed. Falling back to pacman for installation...")

                if not is_parallel_downloads_enabled():

                    enable_parallel_downloads()

                os.system(f"pacman -S {' '.join(package_names)}")

        else:

            print(f"Installing packages: {', '.join(package_names)} from official repositories...")

            if not is_parallel_downloads_enabled():

                enable_parallel_downloads()

            os.system(f"pacman -S {' '.join(package_names)}")

    else:

        print("Usage: joma install <package1> <package2> ...")
        sys.exit(1)

# Remove packages

def remove_packages(package_names):

    if package_names:

        print(f"Removing {package_names} from the system")
        os.system(f"pacman -Rcnss {' '.join(package_names)}")

    else:
        print("Usage: joma install <package1> <package2> ...")
        sys.exit(1)
    

# Update packages

def update_packages(aur_helper):
    
    os.system("pacman -Syyu --noconfirm")
    
    if aur_helper:

        result = os.system(f"witch {aur_helper} > /dev/null 2>&1")

        if result == 0:

            print(f"Updating packages from AUR using {aur_helper}...")
            os.system(f"{aur_helper} -Syyu --noconfirm")

        else:
            pass
    else:
        pass


# Fix pacman keys (usefull for old iso instalations of if the system was not updated in long time)

def fix_pacman_keys():
    
    keyring_folder = "/etc/pacman.d/gnupg/"

    if os.path.exists(keyring_folder):
        shutil.rmtree(keyring_folder)
        print("Removed old keys")
    else:
        print("No old keys found")

    print("Initializing pacman keyring")
    os.system("pacman-key --init")

    print("Populate Arch Linux Keys")
    os.system("pacman-key --populate archlinux")

    print("Updating Arch Linux Keys")
    os.system("pacman -Sy archlinux-keyring --noconfirm")

if __name__ == "__main__":

    # Set the arguments for the wrapper

    parser = argparse.ArgumentParser(description="Pacman wrapper with AUR support.")
    parser.add_argument("action", choices=["install", "add-aur-support", "remove", "uninstall", "update", "upgrade", "fix-keys"], help="Action to perform")
    parser.add_argument("packages", nargs="*", help="Package names to install")
    parser.add_argument("--aur", choices=["yay", "paru"], help="AUR helper to use for package installation (only use for instalation)")
    parser.epilog = "\nThis pacman wrapper has super cow powers."
    args = parser.parse_args()

    # Select the action to take based on the arguments user provided

    if args.action == "install":
        install_packages(args.packages, args.aur)
    elif args.action == "update" or "upgrade":
        update_packages()
    elif args.action == "remove" or "uninstall":
        remove_packages(args.packages)
    elif args.action == "fix-keys":
        fix_pacman_keys()
    elif args.action == "add-aur-support":
        add_aur_support()