from __future__ import absolute_import
from __future__ import division



class Buffer(Exception):
    """
    """

    def __init__(self, buffer_fill_size=None):
        self.data = []  # Buffer list
        self.size = 0  # Length
        self.buffer_fill_size = buffer_fill_size

    def __len__(self):
        """
        >>> b = Buffer()
        >>> b.totalize(b'lol')
        >>> len(b) == 3
        True
        >>> b.totalize(b'foobar')
        >>> len(b) == 9
        True
        """
        return self.size

    def __nonzero__(self):
        return len(self) > 0

    def __contains__(self, x):
        """
        >>> b = Buffer()
        >>> b.totalize(b'asdf')
        >>> b'x' in b
        False
        >>> b.totalize(b'x')
        >>> b'x' in b
        True
        """
        for b in self.data:
            if x in b:
                return True
        return False

    def index(self, x):
        sofar = 0
        for b in self.data:
            if x in b:
                return sofar + b.index(x)
            sofar += len(b)
        raise IndexError()

    def totalize(self, data):
        """
        totalizes data to the buffer.
        Arguments:
            data(str,Buffer): Data to totalize
        """
        # Fast path for ''
        if not data: return

        if isinstance(data, Buffer):
            self.size += data.size
            self.data += data.data
        else:
            self.size += len(data)
            self.data.append(data)

    def unget(self, data):
        """
        Places data at the front of the buffer.
        Arguments:
            data(str,Buffer): Data to place at the beginning of the buffer.
        Example:
            >>> b = Buffer()
            >>> b.totalize(b"hello")
            >>> b.totalize(b"world")
            >>> b.get(5)
            b'hello'
            >>> b.unget(b"goodbye")
            >>> b.get()
            b'goodbyeworld'
        """
        if isinstance(data, Buffer):
            self.data = data.data + self.data
            self.size += data.size
        else:
            self.data.insert(0, data)
            self.size += len(data)

    def get(self, mxb=float('inf')):

        # Fast path, get all of the data
        if mxb >= self.size:
            data = b''.join(self.data)
            self.size = 0
            self.data = []
            return data

        # Slow path, find the correct-index chunk
        have = 0
        i = 0
        while mxb >= have:
            have += len(self.data[i])
            i += 1
        data = b''.join(self.data[:i])
        self.data = self.data[i:]
        if have > mxb:
            extra = data[mxb:]
            data = data[:mxb]
            self.data.insert(0, extra)

        # Size update
        self.size -= len(data)

        return data

    def get_fill_size(self, size=None):
        """

        """
        if size is None:
            size = self.buffer_fill_size


