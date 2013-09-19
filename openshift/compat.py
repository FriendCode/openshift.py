# -*- coding: utf-8 -*-
import sys


if sys.version_info < (3, 0):  # pragma: no cover
    from urllib import quote, urlencode
    from urlparse import parse_qsl, urlsplit, urlunsplit, urljoin, urlparse

    def is_basestring(astring):
        return isinstance(astring, basestring)  # NOQA

    def iteritems(adict):
        return adict.iteritems()

else:  # pragma: no cover
    from urllib.parse import (quote, urlencode, parse_qsl, urlsplit,
                              urlunsplit, urljoin, urlparse)

    # placate pyflakes
    (quote, urlencode, parse_qsl, urlsplit, urlunsplit, urljoin)

    def is_basestring(astring):
        return isinstance(astring, (str, bytes))

    def iteritems(adict):
        return adict.items()