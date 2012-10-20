import os
import shutil
import subprocess
import unittest

subprocess.call(["make"])

shutil.copyfile("bin/urename", "urename_module.py")
from urename_module import *
os.remove("urename_module.py")


class HaskellPluginTests(unittest.TestCase):

    def test_extract_module_name(self):
        self.assertEquals(
            extract_module_name_parts(""), [])
        self.assertEquals(
            extract_module_name_parts("module Foo where"), ["Foo"])
        self.assertEquals(
            extract_module_name_parts("module Foo.Bar.Baz where"), ["Foo", "Bar", "Baz"])


if __name__ == "__main__":
    unittest.main()
