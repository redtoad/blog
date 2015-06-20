from urllib import urlencode
import urlparse
import collections
import re
import docutils.nodes

_urlreg = re.compile(r'^https?://(www\.)?amazon\.(de|com)', re.I)

def inject_affiliate_tag(url, tag):
    """
    Append or replace affiliate tag to Amazon URL. Non-Amazon URLs are left untouched.

    :param url: URL to Amazon website
    :param tag: Amazon affiliate tag
    """
    if not _urlreg.match(url):
        return url
    parts = urlparse.urlsplit(url)
    params = collections.OrderedDict(urlparse.parse_qsl(parts.query))
    params['tag'] = tag
    query = urlencode(params, True)
    return urlparse.urlunsplit([
        parts.scheme,
        parts.netloc,
        parts.path,
        query,
        parts.fragment
    ])


def replace_links(app, doctree):
    nodes = doctree.traverse(docutils.nodes.reference)
    tag = app.config.amazon_affiliate_id

    # stop right here if there is no tag configured
    if not tag:
        return

    for node in nodes:
        url = node.get('refuri', None)
        app.debug('Found link %s.' % url, True)
        node['refuri'] = inject_affiliate_tag(url, tag)


def setup(app):
    app.add_config_value('amazon_affiliate_id', None, True)
    app.connect('doctree-read', replace_links)

