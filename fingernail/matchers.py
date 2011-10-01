from fingernail import matcher


class BeEmpty(object):

    name = 'be_empty'

    def __call__(self):
        return self

    def match(self, container):
        self._container = container
        return len(container) == 0

    def message_for_failed_should(self):
        return "expected %s to be empty" % repr(self._container)

    def message_for_failed_should_not(self):
        return "expected %s not to be empty" % repr(self._container)


matcher(BeEmpty)


class BeGreaterThanOrEqualTo(object):

    name = 'be_greater_than_or_equal_to'

    def __call__(self, expected):
        self.expected = expected

    def match(self, actual):
        self.actual = actual
        return self.actual >= self.expected

    def message_for_failed_should(self):
          return 'expected %r to be greater than or equal to %r' % (
              self.actual, self.expected)

    def message_for_failed_should_not(self):
          return 'expected %r to not be greater than or equal to %r' % (
              self.actual, self.expected)


matcher(BeGreaterThanOrEqualTo)


class BeGreaterThan(object):

    name = 'be_greater_than'

    def __call__(self, expected):
        self.expected = expected

    def match(self, actual):
        self.actual = actual
        return self.actual > self.expected

    def message_for_failed_should(self):
          return 'expected %r to be greater than %r' % (
              self.actual, self.expected)

    def message_for_failed_should_not(self):
          return 'expected %r to not be greater than %r' % (
              self.actual, self.expected)


matcher(BeGreaterThan)

