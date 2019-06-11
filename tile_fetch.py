#!/usr/bin/env python3
# coding: utf-8

import base64
import hmac
import re
import shutil
import tifffile
import imageio
import numpy
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image
import lxml.html

from lxml import etree

from decryption import decrypt

IV = bytes.fromhex("7b2b4e23de2cc5c5")


def compute_url(path, token, x, y, z):
    """
    >>> path = b'wGcDNN8L-2COcm9toX5BTp6HPxpMPPPuxrMU-ZL-W-nDHW8I_L4R5vlBJ6ITtlmONQ'
    >>> token = b'KwCgJ1QIfgprHn0a93x7Q-HhJ04'
    >>> compute_url(path, token, 0, 0, 7)
    'https://lh3.googleusercontent.com/wGcDNN8L-2COcm9toX5BTp6HPxpMPPPuxrMU-ZL-W-nDHW8I_L4R5vlBJ6ITtlmONQ=x0-y0-z7-tHeJ3xylnSyyHPGwMZimI4EV3JP8'
    """
    sign_path = b'%s=x%d-y%d-z%d-t%s' % (path, x, y, z, token)
    encoded = hmac.new(IV, sign_path, 'sha1').digest()
    signature = base64.b64encode(encoded, b'__')[:-1]
    url_bytes = b'https://lh3.googleusercontent.com/%s=x%d-y%d-z%d-t%s' % (path, x, y, z, signature)
    return url_bytes.decode('utf-8')


class ImageInfo(object):
    def __init__(self, url):
        page_source = urllib.request.urlopen(url).read()

        url_path = urllib.parse.unquote_plus(urllib.parse.urlparse(url).path)
        self.image_slug, image_id = url_path.split('/')[-2:]
        self.image_name = '%s - %s' % (self.image_slug, image_id)

        tree = lxml.html.fromstring(page_source)
        image_url = tree.xpath("//meta[@property='og:image']/@content")[0]
        meta_info_tree = etree.fromstring(urllib.request.urlopen(image_url + '=g').read())
        self.tile_width = int(meta_info_tree.attrib['tile_width'])
        self.tile_height = int(meta_info_tree.attrib['tile_height'])
        self.tile_info = [
            ZoomLevelInfo(self, i, attrs.attrib)
            for i, attrs in enumerate(meta_info_tree.xpath('//pyramid_level'))
        ]

        self.path = image_url.split('/')[3].encode('utf-8')

        part = image_url.split(':', 1)[1].encode('utf-8')
        token_regex = rb'"%s","([^"]+)"' % (part,)
        self.token = re.findall(token_regex, page_source)[0]

    def fetch_tile(self, x, y, z):
        image_url = compute_url(self.path, self.token, x, y, z)
        encrypted_bytes = urllib.request.urlopen(image_url).read()
        return decrypt(encrypted_bytes)

    def __repr__(self):
        return '{} - zoom levels:\n{}'.format(
            self.image_slug,
            '\n'.join(map(str, self.tile_info))
        )


class ZoomLevelInfo(object):
    def __init__(self, img_info, level_num, attrs):
        self.num = level_num
        self.num_tiles_x = int(attrs['num_tiles_x'])
        self.num_tiles_y = int(attrs['num_tiles_y'])
        self.empty_x = int(attrs['empty_pels_x'])
        self.empty_y = int(attrs['empty_pels_y'])
        self.img_info = img_info

    @property
    def size(self):
        return (
            self.num_tiles_x * self.img_info.tile_width - self.empty_x,
            self.num_tiles_y * self.img_info.tile_height - self.empty_y
        )

    @property
    def total_tiles(self):
        return self.num_tiles_x * self.num_tiles_y

    def __repr__(self):
        return 'level {level.num:2d}: {level.size[0]:6d} x {level.size[1]:6d} ({level.total_tiles:6d} tiles)'.format(
            level=self)


def load_tiles(url, z=-1, outfile=None):
    print("Downloading image meta-information...")
    info = ImageInfo(url)

    if z >= len(info.tile_info):
        print('Invalid zoom level %d. The maximum zoom level is %d' % (z, len(info.tile_info)))
        return quit(1)

    z %= len(info.tile_info)  # keep 0 <= z < len(tile_info)
    level = info.tile_info[z]

    img = Image.new(mode="RGB", size=level.size)

    tiles_dir = Path(info.image_name)
    tiles_dir.mkdir(exist_ok=True)

    for x in range(level.num_tiles_x):
        for y in range(level.num_tiles_y):
            percent_complete = 100 * (y + x * level.num_tiles_y) // level.total_tiles
            print("Downloading tiles: {:3d}%".format(percent_complete), end='\r')
            file_path = tiles_dir / ('%sx%sx%s.tiff' % (x, y, z))
            if not file_path.exists():
                tile_bytes = info.fetch_tile(x, y, z)
                file_path.write_bytes(tile_bytes)
            tile_img = Image.open(file_path)
            img.paste(tile_img, (x * info.tile_width, y * info.tile_height))
    print("Downloaded all tiles. Saving...")
    final_image_filename = outfile or (info.image_name + '.tiff')
    img_num = numpy.array(img)
    tifffile.imwrite(final_image_filename, img_num, bigtiff=True)
    shutil.rmtree(tiles_dir)
    print("Saved the result as " + final_image_filename)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Download all image tiles from Google Arts and Culture website')
    parser.add_argument('url', type=str, help='an artsandculture.google.com url')
    parser.add_argument('--zoom', type=int, nargs='?',
                        help='Zoom level to fetch, can be negative. Will print zoom levels if omitted')
    parser.add_argument('--outfile', type=str, nargs='?',
                        help='The name of the file to create.')

    args = parser.parse_args()

    if args.zoom is None:
        print(ImageInfo(args.url))
    else:
        load_tiles(args.url, args.zoom, args.outfile)


if __name__ == '__main__':
    main()
