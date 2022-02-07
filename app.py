from handler.intro import Banner
from handler.clear_console import ClearConsole
from handler.choices import Choices
from handler.memory import Memory
from handler.helper import DomainHelper
from handler.password import Password
from handler.search_word import SearchWord
from handler.date import DateHelper
from handler.create_folders import CreateFolder
import os
import sys
import keyboard
import time


def main():
    clear_console: ClearConsole = ClearConsole()
    banner: Banner = Banner()
    choices: Choices = Choices()
    memory: Memory = Memory()
    helper: DomainHelper = DomainHelper()
    password: Password = Password()
    search: SearchWord = SearchWord()
    consumed: DateHelper = DateHelper()
    create: CreateFolder = CreateFolder()
    sys.stdout.flush()
    os.system('color 0A')
    display_once = False
    create.create_browser()
    while True:
        clear_console.clearConsole()
        os.system('color 0A')

        if not display_once:
            banner.banner()
            display_once = True
        choice = choices.choices()
        if choice == 'Memory Artifacts':
            start_time = time.time()
            print("here you can choice one of Memory process")
            memory_sub_choice = choices.memory_choices()

            if memory_sub_choice == 'Memory Acquisition':
                print("here we show you the cached images ")
                memory.mem_scrape()
                consumed_time = consumed.consumed_time(start_time)
                print(
                    f"Memory Artifacts/Memory Acquisition finished Successfully, Total time execution {consumed_time}")
                print('press space to continue ...')
                keyboard.wait('space')

            if memory_sub_choice == 'Memory Key Finds':
                print("here we show you the results of the keyFinds")
                word = input("put word to search??")
                result = search.main(word)
                if result:
                    search.read_data(word)
                else:
                    print("there is No data Found for this KeyWord")
                consumed_time = consumed.consumed_time(start_time)
                print(
                    f"Memory Artifacts/Memory Key Finds :: finished Successfully, Total time execution {consumed_time}")
                print('press space to continue ...')
                keyboard.wait('space')
            if memory_sub_choice == 'Back':
                print("bye bye ")
                continue
            continue

        if choice == 'Browser Artifacts':
            print("here you can choice one of browser process")
            profiles = helper.get_profiles()
            profile_choice = choices.choices_profiles(profiles)
            profile_index = profiles.index(profile_choice)
            sub_choice = choices.extra_browser_choices()
            if sub_choice == 'history':
                start_time = time.time()
                domain = choices.social_media_domain()
                if domain == 'facebook':
                    filter_domain = helper.get_filter_domain(
                        'facebook.com', profile_index + 1, 'facebook')
                    print("here we show you the results of the facebook")
                    helper.call_process(filter_domain)
                    consumed_time = consumed.consumed_time(start_time)
                    print(
                        f"Browser Artifacts/history/facebook :: finished Successfully, Total time execution {consumed_time}")
                    print('press space to continue ...')
                    keyboard.wait('space')
                if domain == 'twitter':
                    filter_domain = helper.get_filter_domain(
                        'twitter.com', profile_index + 1, 'twitter')
                    print("here we show you the twitter ")
                    helper.call_process(filter_domain)
                    consumed_time = consumed.consumed_time(start_time)
                    print(
                        f"Browser Artifacts/history/twitter :: finished Successfully, Total time execution {consumed_time}")
                    print('press space to continue ...')
                    keyboard.wait('space')
                if domain == 'tiktok':
                    filter_domain = helper.get_filter_domain(
                        'tiktok.com', profile_index + 1, 'tiktok')
                    print("here we show you the tiktok ")
                    helper.call_process(filter_domain)
                    consumed_time = consumed.consumed_time(start_time)
                    print(
                        f"Browser Artifacts/history/tiktok :: finished Successfully, Total time execution {consumed_time}")
                    print('press space to continue ...')
                    keyboard.wait('space')
                if domain == 'all':
                    filter_domain = helper.get_filter_domain(
                        'all', profile_index + 1)
                    print("here we show you the all domains")
                    helper.call_process(filter_domain)
                    consumed_time = consumed.consumed_time(start_time)
                    print(

                        f"Browser Artifacts/history/all :: finished Successfully, Total time execution {consumed_time}")
                    print('press space to continue ...')
                    keyboard.wait('space')
                if sub_choice == 'Back':
                    print("bye bye ")
                    continue
            if sub_choice == 'downloads':
                start_time = time.time()
                print("here we show you the downloads ")
                commend = f'python infornito.py downloads --profile {profile_index + 1}'
                helper.call_download_process(commend, 'browser/downloads')
                consumed_time = consumed.consumed_time(start_time)
                print(
                    f"Browser Artifacts/downloads :: finished Successfully, Total time execution {consumed_time}")
                print('press space to continue ...')
                keyboard.wait('space')
            if sub_choice == 'fingerprint':
                start_time = time.time()
                print("here we show you the fingerprint ")
                commend = f'python infornito.py fingerprint --profile {profile_index + 1}'
                helper.call_download_process(commend, 'browser/fingerprint')
                consumed_time = consumed.consumed_time(start_time)
                print(
                    f"Browser Artifacts/fingerprint :: finished Successfully, Total time execution {consumed_time}")
                print('press space to continue ...')
                keyboard.wait('space')
            if sub_choice == 'login data':
                start_time = time.time()
                print("here we show you the results of the passwords")
                print(
                    f'profile_choice {profile_choice} :: profile_index {profile_index}')
                password.main(f'Profile {profile_choice}')
                consumed_time = consumed.consumed_time(start_time)
                print(
                    f"Browser Artifacts/Login Data :: finished Successfully, Total time execution {consumed_time}")
                print('press space to continue ...')
                keyboard.wait('space')
                clear_console.yesno()
            if sub_choice == 'Back':
                print("bye bye ")
                continue
            continue

        if choice == 'Exit':
            print("bye bye ")
            sys.exit(0)


if __name__ == '__main__':
    main()
