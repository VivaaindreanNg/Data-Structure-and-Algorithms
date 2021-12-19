from ..p1_algo_naive import solve as solve1
from ..p1_algo_optimized_naive import solve as solve2

# GeeksForGeeks: https://www.geeksforgeeks.org/algorithms-gq/PATTERN_1-searching/
INPUT_1 = """\
AABAACAADAABAABA
"""
PATTERN_1 = "AABA"
OUTPUT_1 = [0, 9, 12]

INPUT_2 = "ABC ABCDAB ABCDABCDABDE"
PATTERN_2 = "ABCDABD"
OUTPUT_2 = [15]



def test_algo_naive_1() -> None:
    assert solve1(INPUT_1, PATTERN_1) == OUTPUT_1

def test_algo_naive_2() ->None:
    assert solve1(INPUT_2, PATTERN_2) == OUTPUT_2

# def test2() -> None:
#     assert solve2(INPUT_1, PATTERN_1) == OUTPUT_1

