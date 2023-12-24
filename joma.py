#!/usr/share/python

import argparse
import os
import threading



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
                except Exception as e:
                    print(f'Error: Can\'t find {package_list} on any flatpak repo')
    else:
        print("No packages provided for installation")

def update_repos():

    os.system('sudo pacman -Sy')
    os.system('yay -Sy')

def native_pkgs_upgrade():

    os.system('sudo pacman -Syyu')
    os.system('yay -Syyu')

def flat_pkgs_upgrade():
    os.system('flatpak update')

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

        print('Cannot update: {e}')

