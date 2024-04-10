# ALPHA SOFTWARE

This is my first attempt to make a wrapper (kinda) for pacman with support for a configurable aur helper, i'm doing this for me.

## Usage

```bash

joma action --argument

```

actions can be install, update, upgrade, remove, uninstall, fix-keys, search, list-installed, add-aur-support

install action is used to install packages and can use the --aur argument to make is use the configuration for an aur helper (Can't be used as root if the --aur argument is specified)
update and upgrade actions do the exact same thing, they upgrade packages, they both exist for familiarity with a few package managers (Can only be used as root)
remove and uninstall actions also do the same thing and they also exist for familiarity, they are used to remove packages (Can only be used as root)
search action searches for packages (Can be run as a regular user or root)
list-installed action lists the installed packages and can use the --file to define the output file (Can be run as a regular user or root)
fix-keys action fix pacman keys, i added this in case i need to fix the keys i can do it with on command (Can only be used as root)
add-aur-support action adds support for aur by installing an aur helper in case it's not installed, this was added to install the aur helper in case it's not installed (Can't be used as root)
