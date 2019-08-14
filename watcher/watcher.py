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

recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        match = re.fullmatch(
            re.compile(r"(?P<account>\[\d{12}_\w+\])\n%s" % schema), recent_value
        )
        if match:
            with open(credentials_file.as_posix(), "r") as f:
                file_content = f.read()
            old_credentials = re.search(
                re.compile(r"(%s)\n%s" % (re.escape(match["account"]), schema)),
                file_content,
            )
            if old_credentials:
                with open(credentials_file.as_posix(), "w") as f:
                    f.write(file_content.replace(old_credentials[0], recent_value))
            else:
                with open(credentials_file.as_posix(), "a") as f:
                    f.write(f"\n{recent_value}")

    time.sleep(0.5)
