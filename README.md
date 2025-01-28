# LLM-benchmark-suite

LLM are assessed based on benchmarks, but could this create a risk of overfitting?

We propose to use tasks, which are not yet available directly on the internet with old computer code starting by classic 8-bit computers (Amstrad). These games of strategy are kept on tapes or disc and need to be converted to text first, prior to being used as test cases. This limits the risk that the LLM have already been trained on them.

## Project Overview

This project evaluates LLMs' capabilities in:
- Understanding business logic using code on which the LLM have not been trained, thus avoiding overfitting.
- Translating undocumented BASIC programs to modern Python an thus demonstrating an understanding of the underlying business logic.


## Benchmark Structure

Each test case (a game of strategy) in the suite contains:
1. Original source code in text format
2. Expected documentation outputs:
   - Program purpose and functionality
   - Key algorithms and data structures
   - Business logic description
   - Technical limitations and assumptions
3. Reference Python implementation
4. Evaluation metrics for assessing LLM performance

## Getting Started

### Prerequisites
- Python 3.8+
- Your preferred LLM API access


## Test Cases

The benchmark includes strategy games in Basic.

The first program is football manager a game from 1984 for the Amstrad CPC.
The second program is called Don Juan, a strategic game of seduction :).
Both of these games can be played using online emulators.


Each test case is organized in the following structure:
```
└── program_name/
    ├── source code/
    │   └── program.txt (original program converted to readable text)
    ├── reference/
    │   └── program.py
    ├── evaluation/
    │  ├── expected_documentation.md
    │  └── test_cases.json
    ├──  LLM1
    │   └── python code/
    │         ├── program.py
    │         ├── log of the LLM instructions given to product the code
    │         └── Evaluation of the code performed by individuals.
```

## Evaluation Metrics

The benchmark evaluates LLMs on:
1. Code Understanding
   - Accuracy of program documentation
   - Identification of key algorithms
   - Whether name given to variables follow a business logic
   - Business logic comprehension

2. Code Translation
   - Functional equivalence with original
   - Python best practices adoption
   - Code readability and maintainability

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:
- Adding new test cases
- Improving evaluation metrics
- Enhancing documentation
- Reporting issues

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original BASIC program authors
- Classic computer platform communities
- Contributors and maintainers

## Project Status

🚧 Currently under active development. Contributions and feedback welcome!

---

*Note: This benchmark is designed for research and educational purposes. Original BASIC programs are included with appropriate attribution to their authors where available.*

