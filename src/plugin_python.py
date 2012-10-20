class PythonPlugin(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def tasks(self):
        all_files = find(".")
        py_files = [x for x in all_files if x.endswith(".py")]
        old = ""
        new = ""
        return [
            SubstituteTask(py_files, "import %s" % old, "import %s" % new),
            SubstituteTask(all_files, self.src.path, self.dest.path)
        ]


def find(path):
    all_files = []
    for (root, dirs, files) in os.walk(path):
        all_files += filter(include, [os.path.join(root, x) for x in files])
    return all_files


def include(filepath):
    if ".git/" in filepath:
        return False
    if ".swp" in filepath:
        return False
    if os.path.basename(filepath) == "tags":
        return False
    return True
