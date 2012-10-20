class HaskellPlugin(object):

    def use(self, src, dest):
        return src.path.endswith(".hs")

    def tasks(self, src, dest):
        print self._find_module_name(src.path)
        all_files = find(".")
        py_files = [x for x in all_files if x.endswith(".py")]
        old = os.path.basename(src.path)[:-3]
        new = os.path.basename(dest.path)[:-3]
        return [
            SubstituteTask(py_files, "import %s" % old, "import %s" % new),
            SubstituteTask(all_files, src.path, dest.path)
        ]

    def _find_module_name(self, path):
        f = open(path)
        content = f.read()
        f.close()
        match = re.search(r"^module *([a-zA-Z0-9.]+) *", content)
        if match:
            return match.group(1).split(".")
        else:
            return []


register_plugin(HaskellPlugin())
