from ..p1_algo_naive import solve as solve1
from ..p1_algo_optimized_naive import solve as solve2

# GeeksForGeeks: https://www.geeksforgeeks.org/algorithms-gq/pattern-searching/
INPUT = """\
AABAACAADAABAABA
"""

pattern = "AABA"

output = [0, 9, 12]

def test1() -> None:
    assert solve1(INPUT, pattern) == output

# def test2() -> None:
#     assert solve2(INPUT, pattern) == output

