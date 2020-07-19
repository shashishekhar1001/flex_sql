# FLEX-SQL

FLEX-SQL is a Python library for getting the hard coded values and their associated columns from a complex SQL query.

## Dependencies
[Pandas](https://pypi.org/project/pandas/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sql_flex.

```bash
pip install sql_flex
```

## Usage

```python
from sql_flex import flex
query = "Some Complex SQL Query"
df = flex(query)
print(df)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPLv3+](https://choosealicense.com/licenses/gpl-3.0/)