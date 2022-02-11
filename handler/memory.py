import os
import subprocess


class Memory:
    def __init__(self):
        self.noError = open(os.devnull, 'w')

    def mem_scrape(self):
        """[Acquires a raw memory dump from the target system]
        """
        os.system('color 0A')
        print("[+] Memory acquisition\n", flush=True)
        # variable to point to the "memory" subdir of current directory
        mem_dir = os.path.realpath('.') + "\\memory\\"
        print(mem_dir)
        # setting up variables to run winpemem with different parameters
        mem_acq_get = "winpmem_mini_x64_rc2.exe " + mem_dir + "\\memdump.raw"
        # executing winpmem
        subprocess.call(mem_acq_get, stderr=self.noError)
