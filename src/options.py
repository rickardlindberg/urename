from optparse import OptionParser

class Options(object):

    def __init__(self):
        parser = OptionParser()
        (options, args) = parser.parse_args()
