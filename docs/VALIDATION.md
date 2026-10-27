# Validation

Executed locally on 27 October 2026 with Python 3.12.14, using NumPy and pandas from the available runtime. These results validate the minimal example and static source checks only; full historical applications and predictive performance were not tested.

## python examples/demo.py

Exit code: 0

```text
Synthetic consecutive observations: 0 through 11
Feature shape: (7, 4) Target shape: (7, 2)
First: [0.0, 1.0, 2.0, 3.0] -> [4.0, 5.0]
Last:  [6.0, 7.0, 8.0, 9.0] -> [10.0, 11.0]
```

## python -m unittest discover -s tests -v

Exit code: 0

```text
test_alignment_and_final_available_window (test_core.WindowTests.test_alignment_and_final_available_window) ... ok
test_exact_and_insufficient_history (test_core.WindowTests.test_exact_and_insufficient_history) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.019s

OK
```

## python tools/check_sources.py

Exit code: 0

```text
69 Python files; 22 notebooks; 0 documented unfinished files; 0 unexpected issues
```

