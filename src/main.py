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


if __name__ == "__main__":
    o = Options()
    run_tasks(analyze(o.src, o.dest))
