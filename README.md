# my-codex-project

This project contains a simple calculator implemented in Python and a .NET version.
Two interfaces are provided for Python, and the .NET solution includes both a
console application and a Windows Forms GUI.

## Usage

### Python command-line

Run `python calculator.py <operation> <a> <b>` where `<operation>` is one of
`add`, `sub`, `mul`, or `div`.

Example:

```bash
python calculator.py add 2 3
```

which outputs `5`.

### Python graphical (Windows)

Run `python gui_calculator.py` to open a small window where you can enter numbers
and choose the operation. The result will be displayed in the window.

### .NET version

The `DotNetCalculator` directory contains a .NET 6 solution with:

- `CalculatorLib` \- a library with calculator logic
- `CalculatorConsole` \- command-line interface
- `CalculatorWinForms` \- a Windows Forms GUI
- `CalculatorTests` \- xUnit tests

Build the solution on Windows with:

```bash
dotnet build DotNetCalculator/DotNetCalculator.sln
```

Run the console app:

```bash
dotnet run --project DotNetCalculator/CalculatorConsole -- add 2 3
```

Launch the Windows Forms GUI:

```bash
dotnet run --project DotNetCalculator/CalculatorWinForms
```

Run the .NET tests with:

```bash
dotnet test DotNetCalculator/CalculatorTests
```

## Development

Python tests are written with `pytest`. Run them with:

```bash
pytest
```
