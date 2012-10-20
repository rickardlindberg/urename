def analyze(src, dest):
    tasks = [MoveTask(src.path, dest.path)]
    if src.path.endswith(".py"):
        return tasks + PythonPlugin(src, dest).tasks()
    else:
        return tasks + GeneralPlugin(src, dest).tasks()
