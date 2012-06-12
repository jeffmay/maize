def v(*args):
    return vector(args)

class vector(object):
    """An augmented tuple that behaves like a vector."""

    def __init__(self, iterable=tuple()):
        self._tuple = tuple(iterable)

    def __iter__(self):
        return iter(self._tuple)

    def __getitem__(self, index):
        return self._tuple[index]

    def __getslice__(self, start, end):
        return self._tuple[start, end]

    def __len__(self):
        return len(self._tuple)

    def __repr__(self):
        return "v(%s)" % (', '.join(map(str, self)) if len(self) > 0 else '')

    def __str__(self):
        return "<%s>" % (', '.join(map(str, self)) if len(self) > 0 else '')

    def __unicode__(self):
        return unicode(str(self))

    def __eq__(self, other):
        """Check another vector or tuple for equality"""
        if isinstance(other, vector):
            return self._tuple == other._tuple
        else:
            return self._tuple == other

    def __req__(self, other):
        """Check another vector or tuple for equality"""
        return vector(other) == self

    def __ne__(self, other):
        """Check another vector or tuple for non-equality"""
        return not self == other

    def __rne__(self, other):
        """Check another vector or tuple for non-equality"""
        return self != other  # transitive

    def __index__(self):
        """Return the value of this vector as an index"""
        return self._tuple.__index__()

    def __hash__(self):
        # does it make sense to hash this the same as a tuple?
        return hash(self._tuple)

    def __pos__(self):
        return self

    def __neg__(self):
        """Scale by -1"""
        return -1 * self

    def __add__(self, other):
        """Vector addition"""
        return vector(reduce(lambda cur, nxt: cur + nxt, dim) for dim in zip(self, other))

    def __radd__(self, other):
        """Right-side vector addition"""
        return vector(other) + self

    def __iadd__(self, other):
        """Inline addition and assignment"""
        return self + other

    def __sub__(self, other):
        """Vector subtraction"""
        return vector(reduce(lambda cur, nxt: cur - nxt, dim) for dim in zip(self, other))

    def __rsub__(self, other):
        """Right-side vector subtration"""
        return vector(other) - self

    def __isub__(self, other):
        """Inline subtraction and assignment"""
        return self - other

    def __mul__(self, other):
        """Multiply by a scalar or use the dot product on an iterable"""
        try:
            if len(self) != len(other):
                raise ValueError("Cannot multiply vectors of different dimensions")
            matrix = zip(self, other)
        except TypeError:
            # scalar multiplication
            return vector(map(lambda cur: cur * other, self))
        else:
            # dot product
            return sum(reduce(lambda cur, nxt: cur * nxt, dim) for dim in matrix)

    def __rmul__(self, other):
        try:
            value = tuple(self)
        except TypeError:
            # use scalar multiplication (transitive)
            return self * other
        else:
            return vector(value) * other

