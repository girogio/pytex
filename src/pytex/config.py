from typing import Optional
from pytex.document import PageType
from pytex.package import Package


class LatexConfig:
    page_type: Optional[PageType]
    page_numbering: bool
    packages: list[Package]

    def __init__(
        self,
        page_type: PageType = PageType.A4,
        page_numbering: bool = False,
        packages: list[str] = [],
    ):
        self.page_type = page_type
        self.page_numbering = page_numbering
        self.packages = list(map(Package, packages))

    def add_package(self, name: str, options: list[str] = []):
        self.packages.append(Package(name, options))

        return self

    def add_packages(self, names: list[str]):
        self.packages.extend(list(map(Package, names, [[] for _ in names])))

        return self
