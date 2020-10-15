from os import listdir
from os.path import join as pjoin
from os.path import splitext, abspath
from subprocess import TimeoutExpired, run
from sys import argv

path_py = abspath(argv[1])
path_data = abspath(argv[2])
if len(argv) < 4:
    timeout = 1
else:
    timeout = int(argv[3])

cases = sorted({splitext(i)[0] for i in listdir(path_data)})

pass_counter = 0
for case in cases:
    path_case = pjoin(path_data, case)
    print("testing case {}: ".format(case), end="")
    try:
        subp = run(["python", path_py],
                   stdin=open(path_case + ".in"),
                   timeout=timeout,
                   capture_output=True)

        with open(path_case + ".ans", "r", encoding="utf-8", newline="") as f:
            answers = f.read().splitlines()
        if answers != subp.stdout.decode().splitlines():
            print("WRONG ANSWER")
            continue

        pass_counter += 1
        print("ACCEPTED")
    except TimeoutExpired:
        print("TIME EXPIRED")

print()
print("passed {} of {} cases ({:.2f}%).".format(
    pass_counter, len(cases), pass_counter / len(cases) * 100))
