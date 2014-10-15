#!/usr/bin/env python3

# Copyright 2014 Claude (longneck) <longneck@scratchbook.ch>

# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

import argparse



def main():
    args = get_args()
    if args.browser == 'chromium':
        import_chromium(args.bookmarks)

def get_args():
    """Get the argparse parser."""
    parser = argparse.ArgumentParser("usage: importer.py")
    parser.add_argument('browser', help="Which browser?", choices=['chromium'],
                        metavar='browser')
    parser.add_argument('bookmarks', help="Bookmarks file")
    args = parser.parse_args()
    return args

def import_chromium(bookmarks_file):
    import codecs
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(codecs.open(bookmarks_file, encoding='utf-8'))

    html_tags = soup.findAll('a')

    bookmarks = []
    for tag in html_tags:
        if tag['href'] not in bookmarks:
            bookmarks.append(str(tag.string) + ' ' + str(tag['href']))

    for bookmark in bookmarks:
        print(bookmark)

if __name__ == '__main__':
    main()

