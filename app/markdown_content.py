import pathlib

from fasthtml.common import H1  # type: ignore
from fasthtml.common import NotStr
from fasthtml.common import Time

from app.models.markdown import Markdown


def MarkdownContent(path: pathlib.Path):
    entry = Markdown.factory(path)
    return (
        H1(entry.title),
        Time(datetime=entry.date.isoformat())(entry.date.strftime('%B %e, %Y')),
        NotStr(entry.html),
    )

