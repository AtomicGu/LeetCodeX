from subprocess import TimeoutExpired, run
from sys import argv

path_py = argv[1]
if len(argv) < 3:
    timeout = 1
else:
    timeout = int(argv[2])

case_num = 13
pass_counter = 0

for i in range(1, case_num):
    path_in = "materials/data/{}.in".format(i)
    path_ans = "materials/data/{}.py.ans".format(i)
    print("testing case {}: ".format(i), end="")
    try:
        subp = run(["python", path_py],
                   stdin=open(path_in),
                   timeout=timeout,
                   capture_output=True)

        with open(path_ans, "r", encoding="utf-8", newline="") as f:
            ans_lines = f.read().splitlines()
        if subp.stdout.decode().splitlines() != ans_lines:
            print("WRONG ANSWER")
            continue

        pass_counter += 1
        print("ACCEPTED")
    except TimeoutExpired:
        print("TIME EXPIRED")

print()
print("passed {} of {} cases ({:.2f}%).".format(pass_counter, case_num,
                                                pass_counter / case_num * 100))
