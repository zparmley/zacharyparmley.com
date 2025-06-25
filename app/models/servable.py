import abc
import dataclasses
import pathlib

from fasthtml.common import FileResponse  # type: ignore


@dataclasses.dataclass
class Servable(abc.ABC):
    url: str

    @property
    @abc.abstractmethod
    def content(self):
        ...


@dataclasses.dataclass
class ServableFile(Servable):
    file_path: pathlib.Path

    @property
    def content(self):
        return FileResponse(self.file_path)


@dataclasses.dataclass
class ServablePage(Servable):
    title: str
