from jinja2 import Template
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class IncludePlugin(BasePlugin):

    config_scheme = (
        # !!! TODO support multiple source dirs/lingos
        ('src_path', config_options.Type(str, default=None)),
    )
    page = None

    def include(self, filename):
        # !!! TODO support git+, https and other uris
        # !!! TODO support BOF, EOF markers
        # !!! TODO support line range
        path = f'{self.config["src_path"]}/{filename}'
        with open(path, 'r') as f:
            return f.read()

    def on_page_markdown(self, markdown, page, config, **kwargs):
        self.page = page
        md_template = Template(markdown)
        return md_template.render(include=self.include)
