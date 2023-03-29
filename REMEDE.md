This a vendor project template that it uses to create initial version vendor project,
You can use rename.py to replace some name according to vendor specify name.
The replace names are vendor_name, board_name, chip_name.

The script usage:
> python rename.py
usage: rename.py [-h] dir_path new_vendor_name new_board_name new_chip_name
rename.py: error: the following arguments are required: dir_path, new_vendor_name, new_board_name, new_chip_name

Usage step:
1. cp -r template ambiq
2. cd ambiq
3. python rename.py ambiq ama4b2kl_eb apollo3x
4. rm rename.py
   rm REMEDE.md
   rm .git
5. git add *
6. push to gerrit
7. ./build.sh vendor/ambiq/boards/apollo3x/ama4b2kl_eb/configs/nsh -j8
8. ./build.sh vendor/ambiq/boards/apollo3x/ama4b2kl_eb/configs/nsh distclean
8. ./build.sh vendor/ambiq/boards/apollo3x/ama4b2kl_eb/configs/nsh menuconfig
