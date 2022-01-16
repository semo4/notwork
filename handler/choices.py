import os
import inquirer


class Choices:
    def choices(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What artifacts do you need?",
                          choices=['Browser', 'Memory', 'Extra Browser', 'Videos', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def browser_choices(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Browsing do You Need?",
                          choices=['browsing history', 'passwords', 'emails', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def memory_choices(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Memory do You Need?",
                          choices=['cached images', 'memory key finds', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def extra_browser_choices(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Browsing do You Need?",
                          choices=['profiles', 'history', 'fingerprint', 'downloads', 'export', 'filter', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def social_media_domain(self):
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Memory do You Need?",
                          choices=['facebook', 'twitter', 'tiktok', 'all', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]