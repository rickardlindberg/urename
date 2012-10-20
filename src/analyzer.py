def analyze(src, dest):
    plugin_tasks = get_plugin(src, dest).tasks(src, dest)
    return [MoveTask(src.path, dest.path)] + plugin_tasks
