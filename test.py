from os import system
import subprocess
import sys
while True:
    command = input("INTEK$ ")
    if command == "exit":
        break
    a = sys.stdin.readline()
    system(command)
    subprocess.run(["./hello.py"])
