from fasthtml.common import Div  # type: ignore
from fasthtml.common import Img
from fasthtml.common import P
from fasthtml.common import Header
from fasthtml.common import H1
from fasthtml.common import H2
from fasthtml.common import H3
# from fasthtml.common import A
from fasthtml.common import Main
# from fasthtml.common import Footer


def Index():
    return Div(cls='home')(
        H3('Coding, Cameras, Electronics, Woodworking, ...'),
        Div(cls='images')(
            Img(alt='Camera Lens', src='/photos/lens.webp'),
            Img(alt='Electronic Circuit', src='/photos/circuit.webp'),
            Img(alt='Wooden Hammer', src='/photos/hammer.webp'),
        ),
    )

