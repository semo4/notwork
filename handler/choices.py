import os
import inquirer


class Choices():
    def choices(self):
        """ [it display the main list choices that user can select from it.]

        Returns:
            [String]: [the choice that user selected from list of choices]
        """
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What artifacts do you need?",
                          choices=['Browser Artifacts',
                                   'Memory Artifacts', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def browser_choices(self):
        """[it display the sub list choices for the browser that user can select from it after he select the main choices.]

        Returns:
            [String]: [the choice that user selected from list of choices]
        """
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
        """[it display the sub list choices for the memory that user can select from it after he select the main choices.]

        Returns:
            [String]: [the choice that user selected from list of choices]
        """
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Memory do You Need?",
                          choices=['Memory Acquisition',
                                   'Memory Key Finds', 'Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def extra_browser_choices(self):
        """[it display the sub list choices for the extra browser that user can select from it after he select the main choices.]

        Returns:
            [String]: [the choice that user selected from list of choices]
        """
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Browsing do You Need?",
                          choices=['history', 'fingerprint',
                                   'downloads', 'login data', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def social_media_domain(self):
        """[it display the sub list choices for the social media that user can select from it after he select the main choices.]

        Returns:
            [String]: [the choice that user selected from list of choices]
        """
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What Type of Memory do You Need?",
                          choices=['facebook', 'twitter',
                                   'tiktok', 'all', 'Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]

    def choices_profiles(self, profiles):
        """[it display the sub list choices for the profiles that user can select from it after he select the main choices.]

        Args:
            profiles ([list]): [it contains the profiles name that will display to user to select from]

        Returns:
            [String]: [the profile that user selected from list of choices]
        """
        os.system('color 0A')
        questions = [
            inquirer.List('answer',
                          message="What artifacts do you need?",
                          choices=profiles,
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers["answer"]
