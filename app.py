from handler.intro import Banner
from handler.clear_console import ClearConsole
from handler.choices import Choices
from handler.history import BrowserHistory
from handler.memory import Memory
from videos.video import VideoCache
from handler.helper import DomainHelper
import os
import sys
import time
import subprocess


def main():
    no_error = open(os.devnull, 'w')
    clear_console: ClearConsole = ClearConsole()
    banner: Banner = Banner()
    choices: Choices = Choices()
    memory: Memory = Memory()
    video: VideoCache = VideoCache()
    browser: BrowserHistory = BrowserHistory()
    helper: DomainHelper = DomainHelper()
    sys.stdout.flush()
    os.system('color 0A')
    display_once = False
    while True:
        clear_console.clearConsole()
        os.system('color 0A')
        banner.banner()
        if not display_once:
            if clear_console.yesno():
                memory.mem_scrape()
                display_once = True
        choice = choices.choices()
        if choice == 'Browser Artifacts':
            print("here you can choice one of browser process")
            sub_choice = choices.browser_choices()
            if sub_choice == 'Browser History View':
                print("here we show you the browsing history ")
                browser.get_browser_history()
            # if sub_choice == 'passwords':
            #     print("here we show you the results of the passwords")
            #     time.sleep(5)
            #     browser.password()
            #     clear_console.yesno()
            # if sub_choice == 'emails':
            #     print("here we show you the Emails ")
            #     time.sleep(5)
            if sub_choice == 'Back':
                print("bye bye ")
                continue
            continue

        if choice == 'Memory Artifacts':
            print("here you can choice one of Memory process")
            memory_sub_choice = choices.memory_choices()
            if memory_sub_choice == 'Memory Acquisition':
                print("here we show you the cached images ")
                time.sleep(5)
            if memory_sub_choice == 'Memory Key Finds':
                print("here we show you the results of the keyFinds")
                time.sleep(5)
            if memory_sub_choice == 'Back':
                print("bye bye ")
                continue
            continue

        if choice == 'Extra History':
            print("here you can choice one of browser process")
            sub_choice = choices.extra_browser_choices()
            # if sub_choice == 'profiles':
            #     print("here we show you the browsing profiles ")
            #     subprocess.call('python infornito.py profiles', stderr=no_error)
            if sub_choice == 'history':
                domain = choices.social_media_domain()
                if domain == 'facebook':
                    filter_domain = helper.get_filter_domain('facebook.com')
                    print("here we show you the results of the facebook")
                    subprocess.call(filter_domain, stderr=no_error)
                if domain == 'twitter':
                    filter_domain = helper.get_filter_domain('twitter.com')
                    print("here we show you the twitter ")
                    subprocess.call(filter_domain, stderr=no_error)
                if domain == 'tiktok':
                    filter_domain = helper.get_filter_domain('tiktok.com')
                    print("here we show you the tiktok ")
                    subprocess.call(filter_domain, stderr=no_error)
                if domain == 'all':
                    filter_domain = helper.get_filter_domain('all')
                    print("here we show you the all domains ")
                    subprocess.call(filter_domain, stderr=no_error)
                if sub_choice == 'Back':
                    print("bye bye ")
                    continue
            # if sub_choice == 'history':
            #     print("here we show you the results of the history")
            #     subprocess.call('python infornito.py history --profile 2', stderr=no_error)
            if sub_choice == 'fingerprint':
                print("here we show you the fingerprint ")
                subprocess.call('python infornito.py fingerprint --profile 2', stderr=no_error)
            if sub_choice == 'downloads':
                print("here we show you the downloads ")
                subprocess.call('python infornito.py downloads --profile 2', stderr=no_error)
            if sub_choice == 'export':
                print("here we show you the export ")
                subprocess.call('python infornito.py export --profile 2', stderr=no_error)

            if sub_choice == 'Back':
                print("bye bye ")
                continue
            continue

        # if choice == 'Video':
        #     # call browsing history function
        #     print('this will show you all video in the browse')
        #     video.get_video()
        #     continue

        if choice == 'Exit':
            # call browsing history function
            print("bye bye ")
            sys.exit(0)


if __name__ == '__main__':
    main()
