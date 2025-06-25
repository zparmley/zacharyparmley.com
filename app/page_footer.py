import datetime

from fasthtml.common import A  # type: ignore
from fasthtml.common import Div
from fasthtml.common import Footer
from fasthtml.common import P

def PageFooter():
    return Footer(
        Div(cls='flex')(
            P(cls='col grow')(f'Copyright {datetime.datetime.now().year}.  All rights reserved'),
            P(cls='col contact')(
                A(href='mailto:zachary.parmley@gmail.com')('Contact'),
            ),
        ),
    )

    # <footer>
    #    <div class=flex>
    #       <p class="col grow">Copyright 2025. All rights
    #          reserved.
    #       </p>
    #       <p class="col contact"><a href=mailto:zachary.parmley@gmail.com>Contact</a></p>
    #    </div>
    #    <noscript><img src=https://sitestats.parmley.cloud/ingress/150c1a71-afda-4ad6-bb75-a69bf1e893bd/pixel.gif></noscript>
    #    <script defer src=https://sitestats.parmley.cloud/ingress/150c1a71-afda-4ad6-bb75-a69bf1e893bd/script.js></script>
    # </footer>
