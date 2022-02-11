import os
import inquirer


class ClearConsole:
    def clearConsole(self):
        """[it clear the console after each choices user entered]
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def yesno(self):
        """[summary]

        Returns:
            [String]: [the choice that user selected Yes/No]
        """
        os.system('color 0A')
        confirm = {
            inquirer.Confirm('confirmed',
                             message="Do you want to acquire the memory ?",
                             default=True),
        }
        confirmation = inquirer.prompt(confirm)
        return confirmation["confirmed"]
