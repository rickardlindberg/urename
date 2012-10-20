class Task(object):

    def can_be_done(self):
        return True

    def question(self):
        return "dummy task"

    def perform(self):
        pass


def run_task(task):
    if task.can_be_done() and ask(task.question()):
        print "performing"
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
