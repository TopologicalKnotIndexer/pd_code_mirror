# pd-code-mirror

Construct the mirror image of a knot or link represented by a PD code.

## Installation

```bash
pip install pd-code-mirror
```

## Usage example

```python
from pd_code_mirror import mirror_pd_code

pd = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]
print(mirror_pd_code(pd))
```

## Algorithm

Mirroring reverses the cyclic crossing order while keeping the first slot fixed: `[a,b,c,d]` becomes `[a,d,c,b]`. This switches over/under crossing information without changing arc incidences. The input and output are structurally validated, and the caller's list is not mutated.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Run examples and package checks before release. Python packages require Python 3.10 or newer. Build PyPI artifacts with:

```bash
poetry check
poetry build
```

## License

MIT. See `LICENSE`.
