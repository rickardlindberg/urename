import os.path
import subprocess
import sys


class MoveTask(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def perform(self):
        if self.can_be_done() and ask(self.question()):
            if subprocess.call(["mkdir", "-p", os.path.dirname(self.dest)]) != 0:
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

    def perform(self):
        try:
            for filename in self.files:
                f = open(self.filename, "r")
                lines = f.readlines()
                f.close()
                return True
        except Exception, e:
            print e
            return False

    def question(self, filename, lineno):
        return "substitute %s:%i: s/%s/%s/" % (
            filename, lineno, self.a, self.b)


def run_tasks(tasks):
    for task in tasks:
        task.perform()


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
