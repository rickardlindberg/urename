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
