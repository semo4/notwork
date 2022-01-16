import os
import inquirer


class ClearConsole:
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def yesno(self):
        os.system('color 0A')
        confirm = {
            inquirer.Confirm('confirmed',
                             message="Do you want to acquire the memory ?",
                             default=True),
        }
        confirmation = inquirer.prompt(confirm)
        return confirmation["confirmed"]

