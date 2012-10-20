plugins = []


def register_plugin(plugin):
    plugins.append(plugin)


def get_plugin(src, dest):
    for plugin in plugins:
        if plugin.use(src, dest):
            return plugin
