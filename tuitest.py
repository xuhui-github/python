#!/usr/bin/python2
from tui import tui, formats

__version__ = "0.1.0"
if __name__ == "__main__":
    o = tui(main=__file__, progname="MooseCounter")
    o.makeoption("horn-points", formats.BoundedInt(lowerbound=1), "13")
    o.makeoption("weight", formats.Float, "450.0", "w")
    o.makeposarg("observation_data", formats.ReadableFile)
    o.makeposarg("result_file", formats.WritableFile)
    o.initprog()
