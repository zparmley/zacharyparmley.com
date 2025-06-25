from fasthtml.common import Header
from fasthtml.common import H1
from fasthtml.common import H2

from app.navigation import Navigation

def PageHeader(current: str):
    return Header(
        H1('Zachary C. Parmley'),
        H2('Hobbies & Hacks'),
        Navigation(current),
    )
