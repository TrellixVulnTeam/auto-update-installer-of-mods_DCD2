
import os

def download_forge(version):
    print("lk")


def find_dir(name, path):
    result = ""
    for root, dirs, files in os.walk(path):
        if name in dirs:
            result = os.path.join(root, name)
            break
    return result

def return_file(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files.__str__():
            result.append(files.__str__())

    return result


def forge(wanted_version):
    path = 'c:/Users'

    dir = find_dir('.minecraft', path)

    if dir:
        if find_dir('mods', dir):
            versions = find_dir('versions', dir)

            forge_versions = return_file('forge', versions)
            if forge_versions[0] != "":
                for string in forge_versions:
                    print(string)
                    #nu nog checken welke versie het is kan je doen met split en of het een jar of json file is
        else:
            download_forge("1.16.2")
    else:
        return "failed: no minecraft detected"


if __name__ == '__main__':
    forge("1.16.2")
