import sys
from subprocess import check_output


def test_minimal_call():
    check_output(
        [sys.executable, "../TikiToMWiki.py", "https://fb1-7.bs.ptb.de/tiki/",
         "./test/math.tar"])


def test_stdout_call():
    expected = '<mediawiki xml:lang="en">\r\n<siteinfo>\r\n<base>https://fb1' \
               '-7.bs.ptb.de/tiki/</base>\r\n</siteinfo>\r\n<page>\r\n<title' \
               '>Math testpage</title>\r\n<revision>\r\n<id>1</id>\r\n' \
               '<timestamp>2018-03-12T12:38:31Z</timestamp>\r\n<contributor' \
               '><username>mustermann</username></contributor>\r\n<text ' \
               'xml:space="preserve">\r\n__TOC__\r\n\r\n&lt;math&gt;\r\n\r' \
               '\na(t) \\equal \\frac{1}{2}\\left[\r\n\r\na_1 sin(\\omega t) ' \
               '+ a_2 sin(\\omega t - ' \
               '\\phi_0)\r\n\r\n\\right]\r\n\r\n&lt;/math&gt;\r\n\r\n</text' \
               '>\r\n</revision>\r\n</page>\r\n</mediawiki>\r\n\r\nnumber of ' \
               'pages = 1 number of versions = 1\r\nwith contributions by [' \
               '\'mustermann\']\r\nand file uploads on these pages: ' \
               'dict_keys([])\r\n'.encode()
    result = check_output(
        [sys.executable, "./TikiToMWiki.py", "-o", "-",
         "https://fb1-7.bs.ptb.de/tiki/", "./test/math.tar"])
    assert result == expected