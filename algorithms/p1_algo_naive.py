

def solve(input_str: str, pattern: str) -> list:
    """
    Using sliding window technique to slide across every single
    input char in input_str with size n. 
    The length of the window/pattern is m, assuming m <= n.

    Time complexity: O(n*m)
    """
    output = []

    window_length = len(pattern)
    input_str = input_str.rstrip().lstrip()

    for idx, v in enumerate(input_str):
        start = idx 
        end = idx+window_length

        tmp = ""

        if end <= len(input_str):
            for x in range(start, end):
                tmp += input_str[x]

        if tmp == pattern:
            output.append(start)

    return output 

if __name__ == '__main__':
    input = """\
    AABAACAADAABAABA
    """
    pattern = "AABA"

    print(solve(input, pattern))