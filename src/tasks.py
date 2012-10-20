import os.path
import re
import subprocess
import sys


class MoveTask(object):

    def __init__(self, src_path, dest_path):
        self.src_path = src_path
        self.dest_path = dest_path

    def perform(self):
        if self._can_be_done() and ask(self._question()):
            if not self._create_dest_dir():
                return False
            if not self._move_file():
                return False
        return True

    def _can_be_done(self):
        return os.path.exists(self.src_path)

    def _question(self):
        return "mv %s %s" % (self.src_path, self.dest_path)

    def _create_dest_dir(self):
        src_dir = os.path.dirname(self.src_path)
        dest_dir = os.path.dirname(self.dest_path)
        if src_dir == dest_dir:
            return True
        else:
            create_cmd = ["mkdir", "-p", dest_dir]
            return subprocess.call(create_cmd) != 0

    def _move_file(self):
        move_cmd = ["mv", self.src_path, self.dest_path]
        return subprocess.call(move_cmd) == 0


class SubstituteTask(object):

    def __init__(self, files, a, b):
        self.files = files
        self.a = a
        self.b = b
        self.find_pattern = re.compile(r"\b%s\b" % a.replace(".", r"\."))

    def perform(self):
        try:
            for filename in self.files:
                if os.path.exists(filename):
                    self._sub_file(filename)
            return True
        except Exception, e:
            print e
            return False

    def _sub_file(self, filename):
        lines = read_lines(filename)
        new_lines = [self._sub_line(filename, line) for line in lines]
        write_lines(filename, new_lines)

    def _sub_line(self, filename, line):
        match = self.find_pattern.search(line)
        if match and ask(self._question(filename, line)):
            return self.find_pattern.sub(self.b, line)
        else:
            return line

    def _question(self, filename, line):
        return "substitute: %s -> %s\n\t%s: %s" % (
            self.a, self.b, filename, line)


def read_lines(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def write_lines(filename, lines):
    f = open(filename, "w")
    f.writelines(lines)
    f.close()
