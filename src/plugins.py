plugins = []


def register_plugin(self, plugin):
    plugins.append(plugin)


def get_plugin(self, src, dest):
    for plugin in plugins:
        if plugin.use(src, dest):
            return plugin
