def solve(input_str: str, pattern: str) -> list:
    """
    Using sliding window technique to slide across every single
    input char in input_str with size n.
    The length of the window/pattern is m, assuming m <= n.

    Number of comparison needed to be done: O(n-m+1)

    Time Complexity = O(n-m+1)
    """
    output = []

    window_length = len(pattern)
    input_str = input_str.rstrip().lstrip()

    for idx, _ in enumerate(input_str):
        start = idx
        end = idx + window_length

        if end <= len(input_str):
            if pattern == input_str[start:end]:
                output.append(start)

    return output


if __name__ == "__main__":
    input = """\
    AABAACAADAABAABA
    """
    pattern = "AABA"

    print(solve(input, pattern))
