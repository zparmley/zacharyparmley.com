import dataclasses

from fasthtml.common import A  # type: ignore

@dataclasses.dataclass
class Stub:
    url: str

    def A(self, *content, **attributes):
        return A(href=self.url, **attributes)(content)

class FileStub(Stub):
    pass


