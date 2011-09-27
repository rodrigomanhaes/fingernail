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

