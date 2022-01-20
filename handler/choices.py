import os
import inquirer


class Choices():
    def choices(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What artifacts do you need?",
                          choices=['Browser Artifacts', 'Memory Artifacts', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def browser_choices(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Browsing do You Need?",
                          choices=['Browser History View', 'Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def memory_choices(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Memory do You Need?",
                          choices=['Memory Acquisition', 'Memory Key Finds', 'Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def extra_browser_choices(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Browsing do You Need?",
                          choices=[ 'history', 'fingerprint', 'downloads', 'login data', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def social_media_domain(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Memory do You Need?",
                          choices=['facebook', 'twitter', 'tiktok', 'all', 'Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def choices_profiles(self, profiles):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What artifacts do you need?",
                          choices=profiles,
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]