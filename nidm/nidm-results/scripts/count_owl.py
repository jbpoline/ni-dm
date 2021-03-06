"""
Get number of classes/attributes and internal/external namespace
@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2016
"""

import os
import sys

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
NIDMPATH = os.path.join(NIDMRESULTSPATH, os.pardir)

# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from nidmresults.owl.owl_reader import *
from nidmresults.objects.constants_rdflib import *

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)


def main(owl=None):
    if owl is None:
        owl = os.path.join(NIDMRESULTSPATH, "terms",
                           "nidm-results.owl")

    owl_reader = OwlReader(owl)
    num_terms, num_classes, num_attributes, num_reused, all_terms = \
        owl_reader.count_by_namespaces()

    print "---"
    print str(num_terms) + " terms."
    print str(num_attributes) + " attributes and " + str(num_classes) + \
        " classes."
    print str(num_reused) + " re-used terms."
    print "---"

    for term_nsp, len_terms in all_terms.iteritems():
        length, term_list = len_terms
        print "\n" + str(length) + " terms in " + term_nsp + " namespace."
        print "\t\t" + ", ".join(map(owl_reader.get_label, term_list))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        owl = sys.argv[1]
    else:
        owl = None

    main(owl)
