#!/usr/bin/env python

"""
this small example program loads the BUFR B- and D-tables
and reports any inconsistencies it finds in the table definitions
"""

import sys
from pybufr_ecmwf import bufr

if len(sys.argv)<3:
    print 'please give 2 BUFR TABLE files as argument'
    sys.exit(1)

btable_file = sys.argv[1]
dtable_file = sys.argv[2]

#BT = bufr.BufrTable(tables_dir="my_BUFR_TABLES")
#BT = bufr.BufrTable(tables_dir="../ecmwf_bufrtables")
BT = bufr.BufrTable()
BT.load(btable_file)
BT.load(dtable_file)
