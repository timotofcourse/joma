#!/usr/share/python

import argparse
import os
import threading

parser = argparse.ArgumentParser(description='Package manager for Arch based systems that can use aur if needed', epilog='Joma has super autistic powers')

subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')
parser_install = subparsers.add_parser('install', help='Install packages')
parser_install2 = subparsers.add_parser('-S', help='Install packages')
parser_install.add_argument('packages', nargs='+', help='Packages to install')
parser_install2.add_argument('packages', nargs='+', help='ackages to install')


subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')
parser_search = subparsers.add_parser('search', help='Install packages')
parser_search2 = subparsers.add_parser('-Ss', help='Install packages')
parser_search.add_argument('packages', nargs='+', help='Packages to install')
parser_search2.add_argument('packages', nargs='+', help='ackages to install')


parser_remove = subparsers.add_parser('remove', help='Remove packages')
parser_remove2 = subparsers.add_parser('-R', help='Remove packages')
parser_remove.add_argument('packages', nargs='+', help='Packages to remove')
parser_remove2.add_argument('packages', nargs='+', help='Packages to remove')

parser_remove_with_deps = subparsers.add_parser('remove_with_deps', help='Remove packages with dependencies')
parser_remove_with_deps2 = subparsers.add_parser('-Rncss', help='Remove packages with dependencies')
parser_remove_with_deps.add_argument('packages', nargs='+', help='Packages to remove with dependencies')
parser_remove_with_deps2.add_argument('packages', nargs='+', help='Packages to remove with dependencies')

parser_update_repos = subparsers.add_parser('update', help='Update repositories')
parser_update_repos2 = subparsers.add_parser('-Sy', help='Update repositories')

parser_upgrade = subparsers.add_parser('upgrade',help='Upgrade packages')
parser_upgrade = subparsers.add_parser('-Syyu',help='Upgrade packages')

args = parser.parse_args()

def install_packages(packages):

    if packages:

        package_list = ' '.join(packages)

        try:

            os.system(f'sudo pacman -S --needed --noconfirm {package_list}')

        except Exception as e:

            print(f'Error: Can\'t find the packages {package_list} {e} on Pacman repos, trying AUR...')

            try:

                os.system(f'yay -S --needed --noconfirm {package_list}')

            except Exception as e:

                print(f'Error: Can\'t find the packages {package_list} {e} on AUR... Trying flatpak')

                try:

                    os.system(f'flatpak install {package_list} -y')

                except Exception as e:

                    print(f'Error: Can\'t find {package_list} on any flatpak repo')
    else:

        print("No packages provided for installation")

def remove_packages(packages):

    if packages:

        package_list = ' '.join(packages)

        try:

            os.system(f'sudo pacman -R --needed --noconfirm{package_list}')

        except Exception as e:

            print(f'Error: Can\'t find the packages {package_list} {e} on Pacman repos, trying AUR...')

            try:

                os.system(f'yay -R --needed --noconfirm {package_list}')

            except Exception as e:

                print(f'Error: Can\'t find the packages {package_list} {e} on AUR... Trying flatpak')

                try:

                    os.system(f'flatpak remove {package_list} -y')

                except Exception as e:

                    print(f'Error: Can\'t find {package_list} on any flatpak repo')

    else:

        print("No packages provided for installation")

def remove_packages_with_deps(packages):

    if packages:

        package_list = ' '.join(packages)

        try:

            os.system(f'sudo pacman -Rcnss --needed --noconfirm{package_list}')

        except Exception as e:

            print(f'Error: Can\'t find the packages {package_list} {e} on Pacman repos, trying AUR...')

            try:

                os.system(f'yay -Rcnss --needed --noconfirm {package_list}')

            except Exception as e:

                print(f'Error: Can\'t find the packages {package_list} {e} on AUR... Trying flatpak')

                try:

                    os.system(f'flatpak remove {package_list} -y')
                    print(f'{package_list} Removed')

                except Exception as e:

                    print(f'Packages {package_list} not found')

def update_repos():

    os.system('sudo pacman -Sy')
    os.system('yay -Sy')

def native_pkgs_upgrade():

    os.system('sudo pacman -Syyu')
    os.system('yay -Syyu')

def flat_pkgs_upgrade():
    os.system('flatpak update')

def search(packages):

    package_list = ' '.join(packages)

    try:

        os.system(f'sudo pacman -Ss {package_list}')

    except Exception as e:

        print(f'Error: Can\'t find the packages {package_list} {e} on Pacman repos, trying AUR...')

        try:

            os.system(f'yay -Ss {package_list}')

        except Exception as e:

            print(f'Error: Can\'t find the packages {package_list} {e} on AUR... Trying flatpak')

            try:

                os.system(f'flatpak search {package_list} -y')

            except Exception as e:

                print(f'Error: Can\'t find {package_list} on any flatpak repo')
    else:

        print(f"No packagesavailable for {package_list}")


def upgrade_packages():

    nativepkgs = threading.Thread(target=native_pkgs_upgrade)
    flatpkgs = threading.Thread(targer=flat_pkgs_upgrade)

    try:

        nativepkgs.start()
        flatpkgs.start()

        nativepkgs.join()
        flatpkgs.join()

        print('Upgraded packages')

    except Exception as e:

        print(f'Cannot update: {e}')

