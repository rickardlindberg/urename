import sys

class Task(object):

    def can_be_done(self):
        return True

    def question(self):
        return "dummy task"

    def perform(self):
        return True


def run_tasks(tasks):
    for task in tasks:
        if task.can_be_done() and ask(task.question()):
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
