import glob
import os
import csv
from collections import defaultdict
from urllib.parse import unquote
import difflib

def diff(branch_a=None, branch_b=None, commit_a=None, commit_b=None, test_name=None, key=None):
    path = os.getenv('REPO_HOME', '.')
    home = os.path.join(path, ".onaji")

    print("Reading files.")
    filename_a = next(iter(glob.glob(os.path.join(home, "{}.{}.csv".format(branch_a or "*", commit_a or "*")))))
    filename_b = next(iter(glob.glob(os.path.join(home, "{}.{}.csv".format(branch_b or "*", commit_b or "*")))))
    file_a = open(filename_a, 'r')
    file_b = open(filename_b, 'r')
    csv_a = sorted(csv.reader(file_a))
    csv_b = sorted(csv.reader(file_b))

    a = defaultdict(lambda: defaultdict(list))
    b = defaultdict(lambda: defaultdict(list))
    print("Reading left file")
    for x, y, z in csv_a:
        if test_name and x != test_name:
            continue
        if key and y != key:
            continue
        a[x][unquote(y)].append(unquote(z))

    print("Reading right file")
    for x, y, z in csv_b:
        if test_name and x != test_name:
            continue
        if key and y != key:
            continue
        b[x][unquote(y)].append(unquote(z))

    print("Done. Comparing.")
    print("")
    print("=" * 80)
    found = False
    for x in sorted(a):
        for y in sorted(a[x]):
            deltas = list(difflib.unified_diff(
                a[x][y], b[x][y],
                fromfile=(branch_a or "*") + "." + (commit_a or "*"),
                tofile=(branch_b or "*") + "." + (commit_b or "*"), n=0))
            if len(deltas):
                print("{} differences. in {} :: {}".format(len(deltas)-3, x, y))
                print("-"*80)
                print("")
                found = True
            for delta in deltas:
                print(delta)
    if not found:
        print("No deltas! Regression test good!")
