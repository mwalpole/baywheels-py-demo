import os
import requests
import tempfile
from logging import DEBUG
from logging import Logger
from urllib.parse import urljoin
from urllib.request import urlopen

import shutil
import zipfile
from bs4 import BeautifulSoup

ARCHIVE_URL="https://s3.amazonaws.com/baywheels-data/index.html"

logger = Logger('Baywheels Archive')


def get_tripdata_filenames(pprint=False): # TODO: mw@12/6 add type hints
    '''Returns a list of file names from the archive'''
    bucket_url = urljoin(ARCHIVE_URL, '.')
    response = requests.get(bucket_url) # TODO: mw@12/6 consider boto3 in place of web api
    xml_as_string = response.text
    soup = BeautifulSoup(xml_as_string, 'xml')
    if pprint:
        print(soup.prettify())
    keys = soup.findAll('Key')
    return [k.text for k in keys if k.text.endswith('.zip')]


def get_latest_tripdata_filename():
    '''Returns the latest trip data file name from the archive'''
    filename = get_tripdata_filenames()[-1]
    logger.log(DEBUG, 'Found: ', filename)
    return filename


def save_url_to_local(prefix=None, uncompress=False):
    filename = get_latest_tripdata_filename()
    url = urljoin(ARCHIVE_URL, filename)
    prefix = tempfile.mkdtemp() if prefix is None else prefix
    filepath = os.path.join(prefix, filename)
    with urlopen(url) as response, open(filepath, 'wb') as outfile:
        shutil.copyfileobj(response, outfile, length=16*1024) # urllib-shutil will handle chunking, TODO: mw@12/6 use s3.client.download_fileobj
    logger.log(DEBUG, 'Created: ', filepath) # TODO: mw@12/6 add some metrics, e.g. # rows, filesize on disk, free space
    if uncompress:
        filepaths = uncompress_local(filepath)
    else:
        filepaths = [filepath]
    return filepaths


def uncompress_local(filepath):
    filepaths = []
    prefix = os.path.dirname(filepath)
    with zipfile.ZipFile(filepath, 'r') as zfile:
        for filename in zfile.namelist():
            if filename.startswith('__MACOSX'):
                continue
            else:
                newfilepath = zfile.extract(filename, path=prefix)
                filepaths.append(newfilepath)
    return filepaths