def main(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line.rstrip())
    return 31

if __name__ == "__main__":
    main('sample_input')
