import sys
import re


class expect(object):

    def __init__(self, actual):
        self._actual = actual

    def __getattr__(self, attrname):
        r = re.match(r'to_(not_)?(.+)', attrname)
        if r:
            self._matcher = _matchers[r.group(2)]
            self._to_not = r.group(1) == 'not_'
            return self
        else:
            raise AttributeError('%s instance has no attribute %r' % (
                self.__class__.__name__, attrname))

    def _run_matcher(self):
        if not self._evaluate(self._matcher, self._to_not):
            raise BrokenExpectation(
              self._to_not and self._matcher.message_for_failed_should_not() \
                      or self._matcher.message_for_failed_should())

    def _evaluate(self, matcher, to_not):
        if to_not:
            return not matcher.match(self._actual)
        return matcher.match(self._actual)

    def __call__(self, *args, **kwargs):
          self._matcher(*args, **kwargs)
          return self._run_matcher()


_matchers = {}

def matcher(matcher_object):
    try:
        _matchers[matcher_object.name] = matcher_object()
    except TypeError, e:
        e = sys.exc_info()[1]
        if str(e).startswith('__init__() takes exactly'):
            raise TypeError('matcher class constructor cannot have arguments')
        else:
            raise


class BrokenExpectation(AssertionError):
      pass

