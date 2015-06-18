
from docutils import nodes
from sphinx.util.compat import Directive

class IconLink(Directive):

    required_arguments = 1
    has_content = True
    icon_class = 'fa-book'

    def run(self):
        """
        Called when parsing the document.
        """
        url = " ".join(self.arguments)
        html = '<a href="%s"><i class="fa %s fa-fw"></i></a>' % (url, self.icon_class)
        node = nodes.raw('', html, format='html')
        return [node]


def setup(app):

    def create_directive(fa_icon):
        return type(fa_icon, (IconLink, ), {'icon_class': fa_icon})

    app.add_directive("github",    create_directive('fa-github'))
    app.add_directive("bitbucket", create_directive('fa-bitbucket'))
    app.add_directive("rtfm",      create_directive('fa-book'))
