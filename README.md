# πTex

A Python-based utility for generating and compiling LaTeX documents
programmatically. Ideal for automating the creation of complex LaTeX documents.

## Requirements

- πTex assumes that the command `pdflatex` available in your path. Please see
  [this page](https://www.latex-project.org/get/) for instructions on how to
  install LaTeX on your system.

## Installation

```bash
pip install pitex
```

## Quick Start

- Minimal example:

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
