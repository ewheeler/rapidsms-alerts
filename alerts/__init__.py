"""RapidSMS app for alerts & notifications."""

class Alert(object):
    """
    An alert, for display on the dashboard.
    """
    
    def __init__(self, text, url=None):
        self._text = text
        self._url = url
        
        
    @property
    def url(self):
        return self._url
    
    @property
    def text(self):
        return self._text


__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 0,
    'releaselevel': 'beta',
    'serial': 0
}


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0],
                              __version_info__['serial']))
    return ''.join(vers)

__version__ = get_version()
