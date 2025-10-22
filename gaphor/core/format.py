"""Format() and parse() provide a simple interface to:

1. format a model element to text
2. Update model element contents based on text
"""

from functools import singledispatch

from gaphor.core.modeling import Base, Diagram, Element


@singledispatch
def format(el: Base, **kwargs) -> str:
    """Format an element."""
    raise TypeError(f"Format routine for type {type(el)} not implemented yet")


@singledispatch
def parse(el: Base, text: str) -> None:
    """Parse text and update `el` accordingly."""
    raise TypeError(f"Parsing routine for type {type(el)} not implemented yet")


@format.register(Element)
def format_namedelement(el: Element, **kwargs):
    return el.name or ""


@format.register(Diagram)
def format_diagram(el: Diagram, **kwargs) -> str:
    if el.diagramType:
        return f"[{el.diagramType}] {el.name}"
    return el.name or ""


@parse.register(Element)
def parse_namedelement(el: Element, text: str) -> None:
    """Parse element by simply assigning text to its name."""
    el.name = text


@parse.register(Diagram)
def parse_Diagram(el: Diagram, text: str) -> None:
    el.name = text
