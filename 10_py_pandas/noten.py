import os
import sys


def file_exists(path):
    if not os.path.exists(path):
        i = 2
        error = os.strerror(i)
        sys.stderr.write(f"Error code {i}: " + error)
        sys.exit(i)
    if os.path.isdir(path):
        i = 21
        error = os.strerror(21)
        sys.stderr.write(f"Error code {i}: " + error)
        sys.exit(i)
    return True


def main():
    file_exists("C:\\Users\\fabia\\Downloads\\10_py_pandas\\schueler.xm")

if __name__ == '__main__':
    main()
