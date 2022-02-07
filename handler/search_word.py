from subprocess import PIPE, run
import subprocess
import os


class SearchWord:
    def main(self, word):
        run_commend = f'python -m searchbin -t "{word}" memory/memdump.raw'
        result = run(run_commend, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        # subprocess.call(run_commend, stderr=noError)
        if result:
            if os.path.exists('memory/keyfinds'):
                with open("memory/keyfinds/word_search.txt", 'w') as file:
                    file.write(result.stdout)
                return True
            else:
                os.makedirs('memory/keyfinds')
                with open("memory/keyfinds/word_search.txt", 'w') as file:
                    file.write(result.stdout)
                return True
        return False

    def read_data(self, word):
        noError = open(os.devnull, 'w')
        offset_list = list()
        file = open('../memory/keyfinds/word_search.txt', 'r')
        for i in file:
            content = i.split(' ')
            while '' in content:
                content.remove('')
            offset_list.append(content[3])
        for offset in offset_list:
            offset_count = int(offset) - 80
            word_count = len(word) + 100
            dd_commend = f'dd.exe if=memory/memdump.raw of=memory/keyfinds/{offset}.txt bs=1 skip={offset_count} count={word_count}'
            # dd_commend = f'dd.exe if=memory/memdump.raw of=memory/offset_count.txt bs=1 skip=639294170 count=20'
            subprocess.call(dd_commend, stderr=noError)
