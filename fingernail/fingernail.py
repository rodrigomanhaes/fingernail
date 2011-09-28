import re


class expect(object):

    def __init__(self, actual):
        self.actual = actual

    def __getattr__(self, attrname):
        r = re.match(r'to_(not_)?(.+)', attrname)
        return self._run_matcher(_matchers[r.group(2)], to_not=r.group(1))

    def _run_matcher(self, matcher, to_not):
        if not self._evaluate(matcher, to_not):
            raise BrokenExpectation(
              to_not and matcher.message_for_failed_should_not() \
                      or matcher.message_for_failed_should())

    def _evaluate(self, matcher, to_not):
        if to_not:
            return not matcher.match(self.actual)
        return matcher.match(self.actual)



_matchers = {}

def matcher(matcher_object):
    _matchers[matcher_object.name] = matcher_object()


class BrokenExpectation(AssertionError):
      pass

