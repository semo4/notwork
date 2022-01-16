from subprocess import PIPE, run
import subprocess
import os
from io import StringIO

def main():
    word = input("put word to search??")
    run_commend = f'python -m searchbin -t {word} memory/memdump.raw > word.txt'
    result = run(run_commend, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    # subprocess.call(run_commend, stderr=noError)
    with open("word_search.txt", 'w') as file:
        file.write(result.stdout)
    read_data(word)


def read_data(word):
    noError = open(os.devnull, 'w')
    offset_list = list()
    file = open('word_search.txt', 'r')
    for i in file:
        content = i.split(' ')
        while '' in content:
            content.remove('')
        offset_list.append(content[3])
    for offset in offset_list[0:10]:
        offset_count = int(offset) - 20
        word_count = len(word) + 20
        dd_commend = f'dd.exe if=memory/memdump.raw of=memory/{offset_count}.txt bs=1 skip={offset_count} count={word_count}'
        # dd_commend = f'dd.exe if=memory/memdump.raw of=memory/offset_count.txt bs=1 skip=639294170 count=20'
        subprocess.call(dd_commend, stderr=noError)


if __name__ == "__main__":
    main()
