def analyze(src, dest):
    return [MoveTask(src.path, dest.path)] + GeneralPlugin(src, dest).tasks()
