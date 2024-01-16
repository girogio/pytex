# πTex

A Python-based utility for generating and compiling LaTeX documents
programmatically. Ideal for automating the creation of complex LaTeX documents.

## Features

- **Dynamic LaTeX Document Creation**: Easily create and manipulate LaTeX documents in Python.
- **Package and Command Management**: Add LaTeX packages and commands seamlessly.
- **Custom Configuration**: Configure document settings like page size and package options.
- **Compile LaTeX to PDF**: Automatically compile LaTeX documents to PDF with a single command.

## Installation

```bash
pip install pytex
```

## Quick Start

1. **Create a LaTeX Document**

```python
from pytex import LatexDocument

# Create a new LaTeX document
doc = LatexDocument("my_document")

# Add content to the document
doc.content += r"""
\section{Introduction}
This is an automatically generated LaTeX document.
"""

# Compile the LaTeX document to PDF
doc.compile()
```

## Documentation

Detailed documentation will be available soon.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing

The code in this project is licensed under [MIT license](LICENSE.md). This is a permissive license that is short and to the point. It lets people do almost anything they want with your project, like making and distributing closed source versions.
