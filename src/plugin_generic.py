class GeneralPlugin(object):

    def use(self, src, dest):
        return True

    def tasks(self, src, dest):
        all_files = find(".")
        return [SubstituteTask(all_files, src.path, dest.path)]


register_plugin(GeneralPlugin())
