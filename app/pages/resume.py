import itertools
import tomllib

from fasthtml.common import A  # type: ignore
from fasthtml.common import Br
from fasthtml.common import Div
from fasthtml.common import Em
from fasthtml.common import H1
from fasthtml.common import H2
from fasthtml.common import H3
from fasthtml.common import Li
from fasthtml.common import P
from fasthtml.common import Strong
from fasthtml.common import Table
from fasthtml.common import Th
from fasthtml.common import Tr
from fasthtml.common import Ul

from app.util import project_root


def Resume():
    data_path = project_root() / 'data/resume.toml'
    with data_path.open('rb') as handle:
        data = tomllib.load(handle)

    skills_table = (
        Div(cls='flex')(
            Div(cls='col grow')(pair[0]),
            Div(cls='col grow')(pair[1]),
        ) for pair in itertools.batched(data['skills'], 2)
    )

    experience_listings = (
        P(
            Strong(
                f'{experience['title']}, {experience['company']}'
            ),
            ' ',
            Em(
                f'{experience['start_date']} - {experience['end_date']}'
            ),
            Ul(
                (Li(detail) for detail in experience['details']),
            )
        ) for experience in data['experience']
    )


    return Div(cls='resume')(
        H1(cls='center')('Zachary C. Parmley'),
        P(cls='center')(data['headline']),
        Div(cls='flex')(
            Div(cls='col grow')(
                H2(cls='center')('About'),
                P(data['about'])
            ),
            Div(cls='col grow center')(
                H2('Contact'),
                P(A(href='mailto:zachary.parmley@gmail.com')('zachary.parmley@gmail.com')),
                H2('Select Skills'),
                *skills_table,
            ),
        ),
        Div(
            *experience_listings,
        )
    )

