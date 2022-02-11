import os
import json
import base64
import win32crypt
from Cryptodome.Cipher import AES
from datetime import datetime, timedelta


class ChromePassword:
    def chrome_date_and_time(self, chrome_date):
        """[it calculate the data from chrome]

        Args:
            chrome_data ([date]): [the date from chrome]

        Returns:
            [datetime]: [the calculate datetime after add chrome date]
        """
        # Chrome_data format is 'year-month-date
        # hr:mins:seconds.milliseconds
        # This will return datetime.datetime Object
        return datetime(1601, 1, 1) + timedelta(microseconds=chrome_date)

    def fetching_encryption_key(self):
        """[fetch data from chrome files that exist in appData]

        Returns:
            [String]: [decrypted key that will help to decrypt password that exist in chrome]
        """
        # Local_computer_directory_path will look
        # like this below
        # C: => Users => <Your_Name> => AppData =>
        # Local => Google => Chrome => User Data =>
        # Local State
        local_computer_directory_path = os.path.join(
            os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome",
            "User Data", "Local State")

        with open(local_computer_directory_path, "r", encoding="utf-8") as f:
            local_state_data = f.read()
            local_state_data = json.loads(local_state_data)

        # decoding the encryption key using base64
        encryption_key = base64.b64decode(
            local_state_data["os_crypt"]["encrypted_key"])

        # remove Windows Data Protection API (DPAPI) str
        encryption_key = encryption_key[5:]

        # return decrypted key
        return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]

    def password_decryption(self, password, encryption_key):
        """[it will decrept the password the got from chrome]

        Args:
            password ([type]): [description]
            encryption_key ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            iv = password[3:15]
            password = password[15:]
            # generate cipher
            cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
            # decrypt login_data
            return cipher.decrypt(password)[:-16].decode()
        except Exception as e:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except Exception as e:
                return f"No Passwords {e}"
