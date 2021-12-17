from ..p1_algo_naive import solve

# GeeksForGeeks: https://www.geeksforgeeks.org/algorithms-gq/pattern-searching/
INPUT = """\
AABAACAADAABAABA
"""

pattern = "AABA"

output = [0, 9, 12]

def test1() -> None:
    assert solve(INPUT, pattern) == output