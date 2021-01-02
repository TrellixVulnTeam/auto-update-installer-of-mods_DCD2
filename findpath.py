import os


def find_dir(name, path):
    result = ""
    for root, dirs, files in os.walk(path):
        if name in dirs:
            result = os.path.join(root, name)
            break
    return result


def find_file(name, path):
    result = ""
    for root, dirs, files in os.walk(path):
        if name in files:
            result = os.path.join(root, name)
            break
    return result


def return_file(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files.__str__():
            result.append(files.__str__())

    return result


