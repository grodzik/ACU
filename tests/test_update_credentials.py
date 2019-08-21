import tests.mocked_credentials
from importlib_resources import read_text

from watcher.watcher import update_credentials


def test_updating_existing_credentials(tmp_path):
    credentials_file = tmp_path / "credentials"

    mocked_credentials = read_text(tests.mocked_credentials, "mocked_credentials")
    with open(credentials_file, "w") as tf:
        tf.write(mocked_credentials)

    new_credentials = (
        "[162485277353_DevOpsAccess]\n"
        "aws_access_key_id = ASIAWU6GL2STPQ27YRF7\n"
        "aws_secret_access_key = MnUgq2OXnko5Q6jRRW6iCcX03aSIFNGWac3PpLEy\n"
        "aws_session_token = AgoJb3JpZ2luX2VjECEaCXVzLWVhc3QtMSJIMEYCIQCRWt6l4szJoKPun8RMAFDBKYv8kqYxCrNKCGzi1aAXGAIhAOmry4fKlV5Zaza7BMfBQqA6m5HRRTT6tc7RxZsOxeLIKvQCCLr//////////wEQABoMNDU3MjkzMTU3NTQyIgx81kG8Nh75PbjaUI0qyAJkwR1r5G/BGr9bOZuxUDdL6pCNYnx0dfLXEhGUsUCf7X/BAshu6mTuNtAyKASXaTXbkoYZJnW+p2OIjMaG1VAlQr0rAvQn8kVWQZJB8g6K03KTyGG7gMc8Szqw+C8P8KaseROEivpNXMCa66xZ2MT16//M+fdOM0uJLmN46+fgqMmq3K8N4VRGod7J03eRdtXzQGk+oATVVVn2WMTWNDq6/KgzxhsdCM/IZlfGZ2pH9q9yKmS1zYKl1kKzMkJBzDAmfuBbzOO7jB+7QbO6OjpYWm4+ATMCnk/35WEayU54048LKKXVg6wR0p6TeuD2PL02PKg2fS7ztUwiSWPa+nx8vSNATn+b99P895dYaCs3037byXQyiEQb3d7xzlZ+ssj39HDV5xReNnCVyDvcBVoP1OrdLJwnBQzALg+vO6yT8B7M8VCS7UZjMNaO9OoFOrMBrZ+vbUqLHDn1MD0bQIHQZYd4gokqA5DIdP+6PQcgN0uWd4J82Q8GfES3rCcC8UJP3wongg1puSV/kGbdbc1Wgv2BVos+jhNLwLKXSeW17yY7jZP5PfEV6P0hU6sy+xqTPru/yRDEw3JW5qmeeXiQO+neQquIgdtIzqpFEvpl8EOFyjpfAGS/UmMZFvdkHPogEbZY6fZexgOLbLSMFJ33Wd7DOvoIbclf19zsP/chj3Yy/t0="  # noqa: E501
    )

    update_credentials(credentials_file, new_credentials)

    updated_credentials = read_text(
        tests.mocked_credentials, "expected_result_after_updating"
    )
    with open(credentials_file) as tf:
        assert tf.read() == updated_credentials


def test_adding_new_credentials(tmp_path):
    credentials_file = tmp_path / "credentials"

    mocked_credentials = read_text(tests.mocked_credentials, "mocked_credentials")
    with open(credentials_file, "w") as tf:
        tf.write(mocked_credentials)

    new_credentials = (
        "[201324774287_CodeCommitUser]\n"
        "aws_access_key_id = ASIA5UVDRZRERZ35U3JC\n"
        "aws_secret_access_key = K5kvwJxVCg9nRlMkm6OUv1WSXT7ImzKK13far9Vv\n"
        "aws_session_token = AgoJb3JpZ2luX2VjECAaCXVzLWVhc3QtMSJHMEUCIBiRynFjoN2z4/eORMpLarrseLiPjaLzX2V9uYqxHcdtAiEA9cq+2cYgtfb1xGwjsTZkfWo1xuNGqSKdJOUzGgZm1Dwq9AIIuf//////////ARAAGgw5Mzc3MTk2MTQ1MzciDDeUvebJk+ZrDIUffirIAj4WE9FcmA4cL9LEEng3CHO7tp1zxCkWv4TDeF2vvgG9l/tGsBriY69pVHJu1iciUsSiFPhsMwzc13ob5GX+Hvm/25UYi2fb8xgQtABoQMv4i+CbavWFEBMl89DmmptK9+A+paesZDTkjOhrOStnuL+5dfoTN7E2USkcKVSB2fKonR22QsMTfwCUgB88DoORDRA7X4/lH0/Q8jyiCZGphlRz+MSZZsAT3M+CyVuqONTes+GAU0y1rjrox5Kgi0CTm3qKr9swrfvYWl7ufN+9eS1y4KaLOekZMeS2VXekSj81t/HDsaf6ovjGSd0Lib4/+QyI0WbuB5kuq26KqM+DxjzTbg9im64uGXD8u0UJ8pzuHiGGTNkfKkGP50T46qAwondfgxwN484ooZQhulAHkRY1st2hbPC8uX8TI+8Jk3Yia91gW4Il6swwyuzz6gU6tAFHDkQAkq4T/R8emDKjY6LQ3bOyrk/r6xDeowE6sI3pw4OXEjin9IUnj5o6Oy1R+AsaOFYez8I/FdS4JVFGyYuiJJXM5cqNgMySaxEC6Ezh9PkVBABTj2DYtY6GQulP3DUrVHsXE+oX5xEQbPurJNFLqNY6DnqvErt1ri3LV9yxhj/0Dor9OP2H3mmov+xC+LorezS1iEpHz0Z86m0damYuktlYk5sxy2QqNhWyxG0vLn5tmoM="  # noqa: E501
    )

    update_credentials(credentials_file, new_credentials)

    updated_credentials = read_text(
        tests.mocked_credentials, "expected_result_after_appending"
    )
    with open(credentials_file) as tf:
        assert tf.read() == updated_credentials
