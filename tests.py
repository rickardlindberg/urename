import os
import shutil
import subprocess
import unittest

subprocess.call(["make"])

shutil.copyfile("bin/urename", "src.py")
import src
os.remove("src.py")


class Tests(unittest.TestCase):

    def test_foo(self):
        self.fail("....")


if __name__ == "__main__":
    unittest.main()
