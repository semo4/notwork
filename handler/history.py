import os
import subprocess


class BrowserHistory:
    def __init__(self):
        self.noError = open(os.devnull, 'w')
        self.buv_run = '\BrowsingHistoryView.exe'

    def get_browser_history(self):
        """[Collect the browser history]
        """
        print("[+] Getting User Browsing History\n", flush=True)
        bhv_exe_path = os.path.realpath('.') + self.buv_run
        bhv_param = " /SaveDirect /sort 3 /VisitTimeFilterType 1 /cfg " + "BrowsingHistoryView.cfg /scomma " + os.path.realpath(
            '.') + "/memory/BrowsingHistoryView.csv  "
        bhv_command = bhv_exe_path + bhv_param
        bhv_run = bhv_command
        subprocess.call(bhv_run, stderr=self.noError)

    # def get_browser_history2(self):
    #     """Collect the browser history"""
    #     print("[+] Getting User Browsing History\n", flush=True)
    #     bhv_dir = os.path.realpath('.') + "\\BrowsingHistoryView\\"
    #     bhv_exe_path = bhv_dir + "BrowsingHistoryView.exe"
    #     bhv_param = " /SaveDirect /sort 3 /VisitTimeFilterType 1 /cfg " + "BrowsingHistoryView.cfg /scomma " + CASEFOLDER + "/LiveResponseData/BasicInfo/BrowsingHistoryView.csv  "
    #     bhv_command = bhv_exe_path + bhv_param
    #     bhv_run = bhv_command
    #     subprocess.call(bhv_run, stderr=self.noError)

    def password(self):
        """[Collect Passwords from saved chrome files]"""
        print("[+] Getting Passwords\n", flush=True)
        execute = "py.exe" + " .\password.py"
        subprocess.call(execute, stderr=self.noError)
