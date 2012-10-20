import subprocess

OUT_FILE = "urename"

def generate_the_script():
    out = open(OUT_FILE, "w")
    write_shebang(out)
    for filename in master_files():
        write_file(out, filename)
    out.close()
    make_executable()

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

def make_executable():
    subprocess.call(["chmod", "+x", OUT_FILE])

if __name__ == "__main__":
    generate_the_script()
