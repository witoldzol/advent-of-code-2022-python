def parse_input(filename: str):
    data = open(filename, "r").read().strip()
    lines = data.split("\n")
    for l in lines:
        print(l)


def main(input):
    parse_input(input)


if __name__ == "__main__":
    input = "sample_input"
    input = "input"
    main(input)
