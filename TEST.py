import argparse


class FileComparator:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def compare_files(self):
        try:
            with open(self.file1, 'r') as f1, open(self.file2, 'r') as f2:

                content1 = f1.read()
                content2 = f2.read()

                #Compare
                if content1 == content2:
                    return True
                else:
                    return False
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return False


def main():

    parser = argparse.ArgumentParser(description="compare between 2 texts")

    parser.add_argument("file1", help="first file")
    parser.add_argument("file2", help="second file")

    args = parser.parse_args()

    comparator = FileComparator(args.file1, args.file2)

    if comparator.compare_files():
        print("DIFF!")
    else:
        print("PERFECT")


if __name__ == "__main__":
    main()
