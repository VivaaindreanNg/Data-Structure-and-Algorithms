# Data-Structure-and-Algorithms
Contains list of algorithms/DS for pattern searching, graphs, trees, DP (dynamic programming).


The format for sub-directories are as follows:
```
.
├── algorithms/
│ ├── __init__.py
│ ├── p1_algo_naive.py
│ ├── p1_algo_rabin_karp.py
│ │
│ └── tests/
│     ├── __init__.py
│     └── test_p1_pattern_searching.py
```

In the above's case, *p1* represents a particular unique problem(pattern searching, could be graph or tree based algo) that is stored
in tests/ subdir.


While in algorithms/ subdir, it contains all the possible solutions to
that particular *p1* problem.


## Running test cases
To run a particular test module under subdirs (i.e.: To run a unittest in ./data_structures/tests/test_xxx.py), run the following command in root of this repo:
```
$ python -m unittest data_structures.tests.test_xxx
```
