
# import os
# import time
# import socket
# import sys
# import ctypes
# import subprocess
# import shutil
# import zipfile
# import hashlib
# import argparse
# import getpass
# import re
# import inquirer
# import time
# import password


# def has_admin_access():
#     """Admin rights check and exit if they are not found """
#     try:
#         is_admin = os.getuid() == 0
#     except AttributeError:
#         is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
#     if not is_admin:
#         print("\n[+] Has Local Admin rights? [NO]\n")
#         open("DFIRTriage must be ran as Local ADMIN.txt", 'w')
#         sys.exit(0)
#     else:
#         print("\n[+] Has Local Admin rights? [YES]")




with open("memory/memdump.raw", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    with open('test.csv', 'w') as file:
        file.write(str(data))
    # Seek position and read N bytes
    binary_file.seek(0,0)  # Go to beginning
    couple_bytes = binary_file.read(2)
    # print(couple_bytes)


# Match at offset:      639294170     261ADADA in  memory/memdump.raw

# dd.exe if=memory/memdump.raw of=memory/test.txt bs=1 skip=639294116 count=100

#  python -m searchbin -t "chrome" memory/memdump.raw
