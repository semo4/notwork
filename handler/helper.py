import subprocess
import re
import os
from subprocess import run, PIPE


class DomainHelper:
    def __init__(self):
        self.no_error = open(os.devnull, 'w')

    def get_filter_domain(self, domain, index, file_name=None):
        """[it got the filter domain from user choice and store it in path we provide in last of the comment line]

        Args:
            domain ([String]): [te domain name the user selected]
            index ([int]): [the index of the profile the user selected to got the data for]
            file_name ([String], optional): [the file name where we need to store the result in folders]. Defaults to None.

        Returns:
            [String]: [the result will be commend line that contains the comment that we can run]
        """
        if domain != 'all':
            return f'python infornito.py history --profile {index} --filter domain={domain} --export csv --to browser/history/{file_name}'

        else:
            return f'python infornito.py history --profile {index} --filter --export csv --to browser/history/{file_name}'

    def get_profiles(self):
        """[it will got the profiles for chrome that exists in our device]

        Returns:
            [list]: [the list that contains all profiles exists in our device ]
        """
        profiles = \
            subprocess.Popen('python infornito.py profiles', stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[
                0]
        profiles = re.findall(
            r"[\w\t ]+", str(profiles).split('[~]')[1].split('Usage')[0])
        while 'r' in profiles:
            profiles.remove('r')
        while 'n' in profiles:
            profiles.remove('n')
        profiles_list = list()
        for word in range(len(profiles)):
            words = list()
            if len(profiles[word]) == 3:
                words.append(profiles[word + 1])
                words.append(profiles[word + 2])
                profiles_list.append(''.join(words))

        return profiles_list

    def call_process(self, commend):
        """[it will run the commend we will pass to it]

        Args:
            commend ([String]): [the command line that we need to execute]
        """
        subprocess.call(commend, stderr=self.no_error)

    def call_download_process(self, commend, path):
        """[it take the commend we need to execute and run it then store thr result in file in specific path we privide]

        Args:
            commend ([String]): [the commend line we need to execute]
            path ([String]): [the path where we need to store the file in it]
        """
        subprocess.call(commend, stderr=self.no_error)
        result = run(commend, stdout=PIPE, stderr=PIPE,
                     universal_newlines=True)

        path = os.path.join(path, f"{path.split('/')[1]}.csv")
        with open(path, 'w') as file:
            file.write(result.stdout)
