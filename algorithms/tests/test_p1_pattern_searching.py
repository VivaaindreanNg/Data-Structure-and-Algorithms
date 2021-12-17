from ..p1_algo_naive import solve

# GeeksForGeeks: https://www.geeksforgeeks.org/algorithms-gq/pattern-searching/
INPUT = """\
AABAACAADAABAABA
"""

output = [0, 9, 12]

def test1() -> None:
    assert solve(INPUT) == output