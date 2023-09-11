import re

from typing import List, Dict


class Directory:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent: "Directory" | None = parent
        self.dirs: List["Directory"] = []
        self.files: List[Dict[str, int]] = []
        self.size: int = 0

    def depth_first_traversal(self, n: int = 0):
        tabs = "|" * n
        n += 1
        print(tabs + self.name)
        for d in self.dirs:
            d.depth_first_traversal(n)

    def sum_files(self):
        sum = 0
        for f in self.files:
            sum += list(f.values())[0]
        return sum

    def get_sum(self) -> int:
        sum = self.sum_files()
        for d in self.dirs:
            sum += d.get_sum()
        return sum

    def sum_folder_sizes(self):
        max = 100000
        total = 0
        folder_size = self.get_sum()
        if folder_size <= max:
            total += folder_size
            print(self.name + ' : ' + str(folder_size))
        for d in self.dirs:
            total += d.sum_folder_sizes()
        return total


def main():
    root = create_tree("input")
    total = root.sum_folder_sizes()
    print(f'total is {total}')


def create_tree(file: str) -> Directory:
    with open(file) as f:
        counter = 0
        root = Directory("/", None)
        current_dir = root
        for line in f:
            line = line.rstrip()
            EXIT_DIR = re.match(r"^\$ cd \.\.$", line)
            GO_TO_ROOT = re.match(r"^\$ cd \/$", line)
            GO_TO_DIR = re.match(r"^\$ cd \w+$", line)
            LIST_DIR = re.match(r"^\$ ls$", line)
            DIR = re.match(r"^dir \w+", line)
            FILE = re.match(r"^\d+ \w+", line)
            if EXIT_DIR:
                current_dir = current_dir.parent
            elif GO_TO_DIR:
                dir_name = line.split()[2]
                temp = current_dir
                for d in current_dir.dirs:
                    if d.name == dir_name:
                        current_dir = d
                        break
                if temp == current_dir:
                    raise Exception("Failed to find child folder")
            elif LIST_DIR:
                pass
            elif DIR:
                dir_name = line.split()[1]
                d = Directory(dir_name, current_dir)
                current_dir.dirs.append(d)
                counter += 1
            elif FILE:
                size = int(line.split()[0])
                file_name = line.split()[1]
                current_dir.files.append({file_name: size})
            elif GO_TO_ROOT:
                continue
            else:
                raise Exception("Invalid input")

        print(f" conter : = {counter}")
        return root


if __name__ == "__main__":
    main()
