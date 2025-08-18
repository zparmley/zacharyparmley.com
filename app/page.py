import typing

from fasthtml.common import Body  # type: ignore
from fasthtml.common import Head
from fasthtml.common import Html
from fasthtml.common import Link
from fasthtml.common import Main
from fasthtml.common import Meta
from fasthtml.common import Script
from fasthtml.common import Title

from app.page_header import PageHeader
from app.page_footer import PageFooter


def Page(
    *content: typing.Any,
    current: str = '',
    head_content: typing.Any = (),
    title: str | None = None,
):
    title = f'{title} | zacharyparmley.com' if title else 'zacharyparmley.com'

    return Html(
        Head(
            Meta(charset='utf-8'),
            Meta(name='viewport', content='width=device-width'),
            Title(title),
            Link(rel='preconnect', href='https://fonts.googleapis.com'),
            Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=True),
            Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Cousine:ital,wght@0,400;0,700;1,400;1,700&display=swap'),
            # Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11/styles/github.min.css'),
            # Link(rel='stylesheet', href='https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/styles/default.min.css'),
            Link(rel='stylesheet', href='/static/css/main.css'),
            Link(rel='stylesheet', href='/static/css/hljs.css'),
            Script(src='https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/highlight.min.js'),
            head_content,
        ),
        Body(
            PageHeader(current),
            Main(content),
            PageFooter(),
            Script('hljs.highlightAll();'),
        ),
        lang='en-us',
        dir='ltr',
    )
