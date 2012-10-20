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
    if filepath.endswith(".pyc"):
        return False
    if filepath.endswith(".class"):
        return False
    if os.path.basename(filepath) == "tags":
        return False
    if is_binary(filepath):
        return False
    return True


def is_binary(filename):
    """
    Return true if the given filename appears to be binary.
    File is considered to be binary if it contains a NULL byte.
    FIXME: This approach incorrectly reports UTF-16 as binary.
    """
    with open(filename, 'rb') as f:
        for block in f:
            if '\0' in block:
                return True
    return False
