from findpath import return_file, find_dir


def write_file(text, name, path=None):
    import os

    if path is not None:
        direction = os.getcwd() + r"\{}\{}.txt".format(path, name)
        f = open(direction, "w+")
    else:
        direction = os.getcwd() + r"\{}.txt".format(name)
        f = open(direction, "w+")

    f.write(text)
    f.close()

    return direction


def download_forge(version):
    print("lk")


def forge(wanted_version):
    from os import startfile
    path = 'c:/Users'

    direction = find_dir('.minecraft', path)

    if direction:
        if find_dir('mods', direction):
            versions = find_dir('versions', direction)

            forge_versions = return_file('forge', versions)
            if forge_versions[0] != "":
                for string in forge_versions:
                    if wanted_version in string:
                        return True
                else:
                    download_forge(wanted_version)
                    return False
        else:
            download_forge(wanted_version)
            return False
    else:
        dir2 = write_file("NO MINECRAFT DETECTED", "error-minecraft", 'ERROR')
        startfile(dir2)
        return False


if __name__ == '__main__':
    if not forge("1.16.3"):
        print("install forge lol")

    if forge("1.16.2"):
        print("nice")
