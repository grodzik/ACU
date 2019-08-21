import re
import time
from pathlib import Path

import pyperclip

schema = (
    r"(aws_access_key_id = )[^\n]+\n"
    r"(aws_secret_access_key = )[^\n]+\n"
    r"(aws_session_token = )[^\n]+"
)
credentials_file = Path.home() / ".aws" / "credentials"


def main():
    recent_value = pyperclip.paste()
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            new_credentials_match = re.fullmatch(
                re.compile(r"(?P<account>\[\d{12}_\w+\])\n%s" % schema), recent_value
            )
            if new_credentials_match:
                try:
                    with open(credentials_file.as_posix(), "r") as f:
                        file_content = f.read()
                except FileNotFoundError:
                    append_to_file(recent_value)
                    continue
                old_credentials_match = re.search(
                    re.compile(
                        r"(%s)\n%s"
                        % (re.escape(new_credentials_match["account"]), schema)
                    ),
                    file_content,
                )
                if old_credentials_match:
                    write_to_file(recent_value, old_credentials_match[0], file_content)
                else:
                    append_to_file(recent_value)

        time.sleep(0.5)


def write_to_file(new_credentials: str, old_credentials: str, file_content: str):
    with open(credentials_file.as_posix(), "w") as f:
        f.write(file_content.replace(old_credentials, new_credentials))


def append_to_file(credentials: str):
    with open(credentials_file.as_posix(), "a") as f:
        f.write(f"\n{credentials}")
