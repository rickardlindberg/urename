import subprocess
import sys

def generate_the_script(out_file):
    out = open(out_file, "w")
    write_shebang(out)
    for filename in master_files():
        write_file(out, filename)
    out.close()
    make_executable(out_file)

def write_shebang(out):
    out.write("#!/usr/bin/env python\n")

def master_files():
    master = open("master.pyt", "r")
    files = [x.strip() for x in master.readlines()]
    master.close()
    return files

def write_file(out, filepath):
    f = open(filepath)
    out.write(f.read())
    f.close()

def make_executable(out_file):
    subprocess.call(["chmod", "+x", out_file])

if __name__ == "__main__":
    generate_the_script(sys.argv[1])
