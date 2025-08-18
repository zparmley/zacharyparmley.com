import datetime
import pathlib
import sys

import questionary
import slugify


PROJECT_ROOT = pathlib.Path(__file__).parent.parent.absolute()
sys.path.append(PROJECT_ROOT.as_posix())


from app.models.markdown import Markdown

CONTENT_TYPES = ('snippets', 'cameras', )

def load_known_tags(content_type):
    path = pathlib.Path(__file__).parent.parent / 'content' / content_type
    entries = (Markdown.factory(entity) for entity in path.iterdir())
    known_tags = set()
    for entry in entries:
        known_tags |= set(entry.tags)
    return sorted(known_tags)

def create_content(content_type: str, title: str, tags: list[str], ):
    slug = slugify.slugify(title)
    filename = f'{slug}.md'
    output_path = pathlib.Path(__file__).parent.parent / 'content' / content_type / filename
    if output_path.exists():
        raise ValueError(f'{title} => {slug} => {filename} exists!')

    now = datetime.datetime.now().astimezone()
    date = now.isoformat()
    template_path = pathlib.Path(__file__).parent / 'content_template.md'
    template = template_path.read_text()
    tags_string = ', '.join(f"'{tag}'" for tag in tags)
    formatted = template.format(
        title=title,
        date=date,
        tags_string=tags_string,
    )
    output_path.write_text(formatted)


if __name__ == '__main__':
    content_type = questionary.select(
        'Content Type',
        choices=CONTENT_TYPES,
    ).ask()
    title = questionary.text('Title?').ask()
    known_tags = load_known_tags(content_type)
    tag_choices = ['*NEW*', '*DONE*', *known_tags]
    tags: list[str] = []
    selected_tag = questionary.select('tag:', choices=tag_choices).ask()
    while selected_tag != '*DONE*':
        if selected_tag == '*NEW*':
            selected_tag = questionary.text('tag: ').ask()
        tags.append(selected_tag)
        print('tags: ', ', '.join(tags))
        selected_tag = questionary.select('tag:', choices=tag_choices).ask()

    create_content(content_type, title, tags)
