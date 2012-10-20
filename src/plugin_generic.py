class GeneralPlugin(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def tasks(self):
        all_files = find(".")
        return [SubstituteTask(all_files, self.src.path, self.dest.path)]
