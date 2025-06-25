import dataclasses

from fasthtml.common import A
from fasthtml.common import Div
from fasthtml.common import Nav


@dataclasses.dataclass
class NavigationElement:
    text: str
    href: str
    attributes: dict = dataclasses.field(default_factory=dict)


elements = (
    NavigationElement('Home', '/', ),
    NavigationElement('Snippets', '/snippets', ),
    NavigationElement('Cameras', '/cameras', ),
    NavigationElement('Resume', '/resume', ),
)


def Navigation(current: str):
    current_attrs = {'aria_current': 'page', 'cls': 'active'}
    extra_attrs = {e.text: current_attrs if e.text == current else {} for e in elements}
    blocks = (
        Div(cls='col')(
            A(e.text, href=e.href, **extra_attrs[e.text]),
        )
        for e in elements
    )
    return Nav(cls='flex')(blocks)
