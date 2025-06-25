import re
import pathlib

import cyclopts
from fasthtml.common import serve  # type: ignore
from fasthtml.common import Div
from fasthtml.common import FastHTML
from fasthtml.common import NotFoundError, FileResponse
# from fasthtml.common import FastHTMLWithLiveReload

from app.page import Page
from app.pages.index import Index
from app.pages.resume import Resume
from app.listing import Listing
from app.markdown_content import MarkdownContent


STATIC_PATH_PATTERN = re.compile(r'^(?:css|js)/[a-zA-Z0-9_]+$')
PHOTOS_PATH_PATTERN = re.compile(r'^(?:[a-zA-Z0-9_-]+/)?[a-zA-Z0-9_-]+$')
MD_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')

app = FastHTML()

@app.route(r'/favicon.ico')
def favicon():
    return FileResponse(pathlib.Path(__file__).parent / 'static/favicon.ico')

@app.route(r'/static/{path:path}.{ext:static}')
async def static(request, path: str, ext: str):
    if not STATIC_PATH_PATTERN.match(path):
        raise NotFoundError()
    if ext not in ('css', 'js', ):
        raise NotFoundError()
    file_path = pathlib.Path(__file__).parent / 'static' / f'{path}.{ext}'
    return FileResponse(file_path)

@app.route(r'/photos/{path:path}.{ext:static}')
def photos(request, path: str, ext:str):
    print(request)
    print(photos.to(path='hammer', ext='webp'))
    if ext not in ('webp', 'jpg', 'png', 'gif', ):
        raise NotFoundError()
    file_path = pathlib.Path(__file__).parent / 'photos' / f'{path}.{ext}'
    return FileResponse(file_path)


@app.route
def index():
    return Page(
        Index(),
        current='Home',
    )

@app.route
def resume():
    return Page(
        Resume(),
        current='Resume',
    )

@app.route('/snippets/{key:str}')
def snippets(key: str):
    current = 'Snippets'
    if not key:
        return Page(
            Listing(current, pathlib.Path(__file__).parent / 'content/snippets'),
            current=current,
        )
    if not MD_PATTERN.match(key):
        raise NotFoundError()
    snippet_path = pathlib.Path(__file__).parent / 'content/snippets' / f'{key}.md'
    if not snippet_path.exists():
        raise NotFoundError()
    return Page(
        MarkdownContent(snippet_path),
        current='',
    )


@app.route('/cameras/{key:str}')
def cameras(key: str):
    current = 'Cameras'
    if not key:
        return Page(
            Listing(current, pathlib.Path(__file__).parent / 'content/cameras'),
            current=current,
        )
    if not MD_PATTERN.match(key):
        raise NotFoundError()
    snippet_path = pathlib.Path(__file__).parent / 'content/cameras' / f'{key}.md'
    if not snippet_path.exists():
        raise NotFoundError()
    return Page(
        MarkdownContent(snippet_path),
        current='',
    )

def main(port: int = 5002):
    serve(port=port)

cyclopts.run(main)
