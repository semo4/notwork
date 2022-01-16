import subprocess
import os


class VideoCache:
    def get_video(self):
        no_error = open(os.devnull, 'w')
        commend = 'VideoCacheView.exe/copyall VideoFiles.txt'
        subprocess.call(commend, stderr=no_error)
