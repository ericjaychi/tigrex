# tigrex

Tigrex is a Python CLI Tool for searching and pricing Magic the Gathering cards using Scryfall's API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install tigrex
```

## Usage

```bash
python -m tigrex search [card-name]
python -m tigrex price [card-name]
```

## Output
```bash
$~ python -m tigrex search black lotus
Black Lotus		{0}

Artifact

{T}, Sacrifice Black Lotus: Add three mana of any one color.



$~ python -m tigrex price black lotus
Black Lotus		{0}

	Vintage Championship (OVNT)
		$N/A / $N/A
	Magic Online Promos (PRM)
		$N/A / $N/A
	Vintage Masters (VMA)
		$N/A / $N/A
	Intl. Collectors’ Edition (CEI)
		$544.95 / $N/A
	Collectors’ Edition (CED)
		$2000.47 / $N/A
	Unlimited Edition (2ED)
		$3999.00 / $N/A
	Limited Edition Beta (LEB)
		$4650.00 / $N/A
	Limited Edition Alpha (LEA)
		$N/A / $N/A
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)