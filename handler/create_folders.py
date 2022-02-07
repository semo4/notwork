import os

class CreateFolder:
    def create_browser(self):
        if all([os.path.exists('browser'),
        os.path.exists('browser/downloads'), os.path.exists('browser/fingerprint'),
        os.path.exists('browser/history'), os.path.exists('browser/login_data')]) :
            pass
        else:
            os.makedirs('browser')
            os.makedirs('browser/downloads')
            os.makedirs('browser/fingerprint')
            os.makedirs('browser/history')
            os.makedirs('browser/login_data')
