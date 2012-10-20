class PythonPlugin(object):

    def use(self, src, dest):
        return src.path.endswith(".py")

    def tasks(self, src, dest):
        all_files = find(".")
        py_files = [x for x in all_files if x.endswith(".py")]
        old = ""
        new = ""
        return [
            SubstituteTask(py_files, "import %s" % old, "import %s" % new),
            SubstituteTask(all_files, src.path, dest.path)
        ]


register_plugin(PythonPlugin())
