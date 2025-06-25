import dataclasses
import datetime
import itertools
import pathlib
import typing

import markdown
import frontmatter  # type: ignore


BLURB_STOP = '<!--more-->'

@dataclasses.dataclass
class Markdown:
    path: pathlib.Path
    title: str
    date: datetime.datetime
    draft: bool
    content: str

    @property
    def url(self) -> str:
        return f'/{self.path.parent.name}/{self.path.stem}'

    @property
    def html(self) -> str:
        return markdown.markdown(self.content, extensions=['fenced_code', 'attr_list'])  # type: ignore

    @property
    def blurb(self) -> str:
        content = '\n'.join(
            itertools.takewhile(
                lambda line: line != BLURB_STOP,
                self.content.split('\n'),
            ),
        )
        return markdown.markdown(content, extensions=['fenced_code', 'attr_list'])  # type: ignore

    @classmethod
    def factory(cls, path: pathlib.Path) -> typing.Self:
        loaded = frontmatter.load(path)
        title = loaded['title']
        date = datetime.datetime.fromisoformat(loaded['date']).astimezone()
        draft = loaded['draft']
        content = loaded.content

        return cls(path, title, date, draft, content)
