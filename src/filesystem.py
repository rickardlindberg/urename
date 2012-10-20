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
