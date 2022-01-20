import subprocess
import re
import os
from subprocess import run, PIPE


class DomainHelper:
    def __init__(self):
        self.no_error = open(os.devnull, 'w')

    def get_filter_domain(self, domain, index, file_name=None):
        if domain != 'all':
            if os.path.exists(f'browser/history/{file_name}'):
                return f'python infornito.py history --profile {index} --filter domain={domain} --export csv --to browser/history/{file_name}'
            else:
                os.makedirs(f'browser/history/{file_name}')
                return f'python infornito.py history --profile {index} --filter domain={domain} --export csv --to browser/history/{file_name}'

        else:
            if os.path.exists(f'browser/history/{file_name}'):
                return f'python infornito.py history --profile {index} --filter --export csv --to browser/history/{file_name}'
            else:
                os.makedirs(f'browser/history/{file_name}')
                return f'python infornito.py history --profile {index} --filter --export csv --to browser/history/{file_name}'

    def get_profiles(self):
        profiles = \
        subprocess.Popen('python infornito.py profiles', stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[
            0]
        profiles = re.findall(r"[\w\t ]+", str(profiles).split('[~]')[1].split('Usage')[0])
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
        subprocess.call(commend, stderr=self.no_error)

    def call_download_process(self, commend, path):
        subprocess.call(commend, stderr=self.no_error)
        result = run(commend, stdout=PIPE, stderr=PIPE, universal_newlines=True)

        path = os.path.join(path, f"{path.split('/')[1]}.csv")
        with open(path, 'w') as file:
            file.write(result.stdout)
