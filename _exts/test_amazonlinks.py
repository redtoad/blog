import docutils.core
import pytest
import amazonlinks

@pytest.mark.parametrize('url,out', [
    ('http://google.de', 'http://google.de'),
    ('http://amazon-fake.de', 'http://amazon-fake.de'),
])
def test_leave_non_amazon_urls_untouched(url, out):
    assert amazonlinks.inject_affiliate_tag(url, '???') == out

@pytest.mark.parametrize('url,out', [
    ('http://amazon.de', 'http://amazon.de?tag=redtoad-10'),
    ('http://amazon.de/', 'http://amazon.de/?tag=redtoad-10'),
    ('http://www.amazon.de/', 'http://www.amazon.de/?tag=redtoad-10'),
    ('http://www.amazon.de/?ref=some_thing', 'http://www.amazon.de/?ref=some_thing&tag=redtoad-10'),
])
def test_append_tag_to_amazon_url(url, out):
    assert amazonlinks.inject_affiliate_tag(url, 'redtoad-10') == out

@pytest.mark.parametrize('url,out', [
    ('http://www.amazon.de/?tag=some_thing', 'http://www.amazon.de/?tag=redtoad-10'),
    ('http://amazon.de/?tag=some_thing&ref=xxx', 'http://amazon.de/?tag=redtoad-10&ref=xxx'),
])
def test_replace_existing_tag_in_amazon_url(url, out):
    assert amazonlinks.inject_affiliate_tag(url, 'redtoad-10') == out

RST = """

Wishlist
========

These are some of my things from Amazon:

* `WD My Cloud 2TB <http://www.amazon.de/gp/product/B00FOKN7FG/ref=s9_simh_gw_p147_d0_i1?pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=desktop-1&pf_rd_r=0CGQAQDYM15EZJGCVQEZ&pf_rd_t=36701&pf_rd_p=585296347&pf_rd_i=desktop>`_
* `Moon over Soho`_

Some other link: http://google.de

.. _Moon over Soho: http://www.amazon.de/gp/product/0575097620/?tag=red


"""

@pytest.fixture
def doctree():
    return docutils.core.publish_doctree(RST)

def test_finds_all_amazon_links(doctree, monkeypatch):
    def count(*args):
        count._counter += 1
    count._counter = 0
    monkeypatch.setattr(amazonlinks, 'inject_affiliate_tag', count)
    amazonlinks.replace_links(None, doctree)
    assert count._counter == 3  # find 3 links

