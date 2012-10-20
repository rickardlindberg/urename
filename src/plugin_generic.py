class GeneralPlugin(object):

    def use(self, src, dest):
        return True

    def tasks(self, src, dest):
        all_files = find(".") + [dest.path]
        src_base = os.path.splitext(os.path.basename(src.path))[0]
        dest_base = os.path.splitext(os.path.basename(dest.path))[0]
        return [
            SubstituteTask(all_files, src.path, dest.path),
            SubstituteTask(all_files, src_base, dest_base),
        ]


register_plugin(GeneralPlugin())
