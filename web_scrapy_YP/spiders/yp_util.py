__author__ = 'rui'
import re
import urllib, urlparse
def custom_strip(lst):
    try:
        assert type(lst)==type([])
        lst=lst
    except AssertionError as e:
        try:
            assert type(lst)==type(())
            lst=list(lst)
        except AssertionError as e1:
            assert type(lst)==type(u'') or type(lst)==type("")
            lst=[lst]
    pats = re.compile('([\w\s]+)')
    res = []
    for x in lst:
        x=x.strip()
        found = re.findall(pats,x)
        if len(found)>0:
            res.append(' '.join(found))
    return res

def addParamToUrl(url, params):
    #print 'params', params

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urllib.urlencode(query)

    return  urlparse.urlunparse(url_parts)

