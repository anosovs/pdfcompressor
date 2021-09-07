import os
from settings import *
from convert import *
import glob


if DIR_REC:
    listFiles = glob.glob(os.path.join(args.INPUT+'/**/', '*.pdf'), recursive=True)
    for el in listFiles:
        tmp_el = el.replace(args.INPUT, '')
        OUTPUT_DIR = os.path.dirname(OUTPUT_DIR_DEFAULT + tmp_el)
        if os.path.exists(OUTPUT_DIR):
            pass
        else:
            os.mkdir(OUTPUT_DIR)
        convertAndCompressPdf(el, OUTPUT_DIR)
elif IT_DIR:
    listFiles = glob.glob(os.path.join(args.INPUT, '*.pdf'))
    for el in listFiles:
        convertAndCompressPdf(el, args.OUTPUT_DIR)
else:
    convertAndCompressPdf(args.INPUT)
















