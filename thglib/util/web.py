from __future__ import absolute_import
from __future__ import division
from thglib.util.misc import size
from thglib.network.buffer import Buffer
import os
import six
import tempfile

def downloadfile(url, save=None, timeout=5, **kwargs):
    r"""downloadfile(url, save=None, timeout=5) -> str
    Downloads a file via HTTP/HTTPS.
    Arguments:
      url (str): URL to download
      save (str or bool): Name to save as.  Any truthy value
            will auto-generate a name based on the URL.
      timeout (int): Timeout, in seconds
    Example:
      >>> url    = 'https://google.com/robots.txt'
      >>> result = downloadfile(url, timeout=60)
      >>> result
      b'User-agent: *\nDisallow: /deny\n'

      True
    """
    import requests

    response = requests.get(url, stream=True, timeout=timeout, **kwargs)

    if not response.ok:
        print("Got code %s" % response.status_code)
        return

    total_size = int(response.headers.get('content-length', 0))

    print('0 / %s' % size(total_size))

    chunk_size = 1
    while chunk_size < (total_size / 10):
        chunk_size *= 1000

    # Count chunks as they're received
    buf = Buffer()

    for chunk in response.iter_content(chunk_size=2 ** 10):
        buf.totalize(chunk)
        if total_size:
            print('%s / %s' % (size(buf.size,' bytes'), size(total_size)))
        else:
            print('%s' % size(buf.size,' bytes'))

    total_data = buf.get()

    if save:
        if not isinstance(save, (bytes, six.text_type)):
            save = os.path.basename(url)
            save = save or tempfile.NamedTemporaryFile(dir='.', delete=False).name
        with open(save, 'wb+') as f:
            f.write(total_data)
            print('Saved %r (%s)' % (f.name, size(total_data)))
    else:
        print('%s' % size(total_data))

    return total_data

url = 'https://google.com/robots.txt'
result = downloadfile(url, timeout=60)
print(result)
filename = tempfile.mktemp()
result2 = downloadfile(url, filename, timeout=60)
print(result == open(filename, 'rb').read())
