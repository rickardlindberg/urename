from optparse import OptionParser

class Options(object):

    def __init__(self):
        usage = "usage: %prog [options] src dest"
        parser = OptionParser(usage)
        (options, args) = parser.parse_args()
        if len(args) == 2:
            self.src = File(args[0])
            self.dest = File(args[1])
        else:
            parser.error("requires src and dest")
