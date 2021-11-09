import re

url_pattern = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",
                         re.MULTILINE)


def find_urls(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)

    return [x[0] for x in url]


def split_urls(string):
    #list of (is_url, text or url)
    ret = []
    # the string position
    pos = 0
    m = url_pattern.search(string, pos=pos)
    while m:
        span = m.span(0)
        url = m.group(0)
        s = string[pos:span[0]]
        if s:
            ret.append((False, s))
        ret.append((True, url))
        pos = span[1]
        m = url_pattern.search(string, pos=pos)

    if pos < len(string):
        ret.append((False, string[pos:]))

    return ret

