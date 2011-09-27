import re


class expect(object):

    def __init__(self, actual):
        self.actual = actual

    def __getattr__(self, attrname):
        r = re.match(r'to_(.+)', attrname)
        return self._run_matcher(_matchers[r.group(1)])

    def _run_matcher(self, matcher):
        if not matcher.match(self.actual):
            raise BrokenExpectation(matcher.message_for_failed_should())


_matchers = {}

def matcher(matcher_object):
    _matchers[matcher_object.name] = matcher_object()


class BrokenExpectation(AssertionError):
      pass

