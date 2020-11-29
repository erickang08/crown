import logging
from collections import namedtuple
OP_AND = 0
OP_OR = 1

OP_ADD = 10
OP_SUB = 11
OP_MUL = 12
OP_DIV = 13
OP_AND = 14
OP_OR = 15
OP_XOR = 16
OP_USER = 19

OP_EQ = 20
OP_LT = 21
OP_LTE = 22
OP_GT = 23
OP_GTE = 24
OP_NE = 25
OP_IN = 26
OP_IS = 27
OP_LIKE = 28
OP_ILIKE = 29

# JOIN_INNER = 1
# JOIN_LEFT_OUTER = 2
# JOIN_FULL = 3

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('crown')



Ordering = namedtuple('Ordering', ('param', 'asc'))
R = namedtuple('R', ('value',))
# Join = namedtuple('Join', ('model_class', 'join_type', 'on'))

def dict_update(orig, extra):
    new = {}
    new.update(orig)
    new.update(extra)
    return new

def returns_clone(func):
    def inner(self, *args, **kwargs):
        clone = self.clone()
        func(clone, *args, **kwargs)
        return clone
    inner.call_local = func
    return inner

def not_allowed(fn):
    def inner(self, *args, **kwargs):
        raise NotImplementedError('%s is not allowed on %s instances' % (
            fn, type(self).__name__,
        ))
    return inner

class DoesNotExist(Exception):
    pass

# doing an IN on empty set
class EmptyResultException(Exception):
    pass