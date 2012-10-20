import os.path
import re
import subprocess
import sys


class MoveTask(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def perform(self):
        if self.can_be_done() and ask(self.question()):
            if os.path.dirname(self.src) != os.path.dirname(self.dest) and subprocess.call(["mkdir", "-p", os.path.dirname(self.dest)]) != 0:
                return False
            if subprocess.call(["mv", self.src, self.dest]) != 0:
                return False
        return True

    def can_be_done(self):
        return os.path.exists(self.src)

    def question(self):
        return "mv %s %s" % (self.src, self.dest)


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
                    f = open(filename, "r")
                    lines = f.readlines()
                    f.close()

                    def foo(line):
                        match = self.find_pattern.search(line)
                        if match and ask(self.question(filename, line)):
                            return self.find_pattern.sub(self.b, line)
                        return line
                    lines = [foo(line) for line in lines]

                    f = open(filename, "w")
                    f.writelines(lines)
                    f.close()

            return True
        except Exception, e:
            print e
            return False

    def question(self, filename, line):
        return "substitute: %s -> %s\n\t%s: %s" % (
            self.a, self.b, filename, line)


def run_tasks(tasks):
    for task in tasks:
        if not task.perform():
            sys.exit(1)


def ask(question):
    print question, "[Y/n]",
    answer = raw_input()
    if answer == "":
        return True
    elif answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
    else:
        return ask(question)
