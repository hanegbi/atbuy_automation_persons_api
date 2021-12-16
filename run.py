import subprocess
import sys

import pytest


def run():
    subprocess.check_call([sys.executable, "-m", "pip", "install","--no-cache-dir", "-r", "requirements.txt"])
    pytest.main(["-s", "--junitxml=reports/result.xml"])


if __name__ == '__main__':
    run()
