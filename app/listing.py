import operator
import pathlib

from fasthtml.common import A  # type: ignore
from fasthtml.common import Div
from fasthtml.common import H1
from fasthtml.common import H2
from fasthtml.common import NotStr
from fasthtml.common import P

from app.models.markdown import Markdown


def Listing(current: str, path: pathlib.Path):
    entries = (Markdown.factory(entity) for entity in path.iterdir())
    entries = filter(lambda entry: not entry.draft, entries)
    entries = sorted(entries, key=operator.attrgetter('date'))

    return (
        H1(current),
        Div(cls='entries')(
            Div(
                H2(
                    A(href=entry.url)(entry.title),
                ),
                P(
                    NotStr(entry.blurb), '…'
                ),
            ) for entry in entries
        )
    )
