import configparser
import argparse

#  tmp setting
tmppdf = ''
tmpimagefolder = './tmp/'

# reading from ini file
config = configparser.ConfigParser()
config.read('./cnf.ini')

# DEFAULT settings for resolution
DPI = int(config['QUALITY_SETTINGS']['DPI'])
DPI_TMP_IMAGE = int(config['QUALITY_SETTINGS']['DPI_TMP_IMAGE'])
WIDTH_INCH = float(config['QUALITY_SETTINGS']['WIDTH_INCH'])
HEIGHT_INCH = float(config['QUALITY_SETTINGS']['HEIGHT_INCH'])
QUALITY = int(config['QUALITY_SETTINGS']['QUALITY'])
GRAYSCALE = config['QUALITY_SETTINGS']['GRAYSCALE']
if GRAYSCALE == 'False':
    GRAYSCALE = False
else:
    GRAYSCALE = True

IT_DIR = False
DIR_REC = False
GRAYSCALE = False
OVERWRITE = False
OUTPUT_DIR = None


# Other settings
pooper_path = config['POPPLER']['POPPLER_PATH']
tmpimagefolder = config['FOLDERS']['TMP_IMAGE_FOLDER']

# parsing command line for args
argsparse = argparse.ArgumentParser(description='Probably this program allow to compress pdf`s which consist only images')

argsparse.add_argument('INPUT', help='filename or dirname for compression. Use " - for safety', type=str)
argsparse.add_argument('-d', action='store_true', dest='IT_DIR', help='folder which consist pdf for '
                                                                                       'compression')
argsparse.add_argument('-r', action='store_true', dest='DIR_REC', help='flag for recursive')
argsparse.add_argument('-g', action='store_true', dest="GRAYSCALE", help='if used do convert in grayscale image')
argsparse.add_argument('-o', action='store_true', dest="OVERWRITE", help='if used will overwrite existed pdf')
argsparse.add_argument('-dpi', dest="DPI", help='DPI for outputfile')
argsparse.add_argument('-dpi_image', dest="DPI_TMP_IMAGE", help='DPI for compression images')
argsparse.add_argument('-q', dest="QUALITY", help='Quality for compression images')
argsparse.add_argument('-output', dest="OUTPUT_DIR", help='place for peace')

args = argsparse.parse_args()

if args.DPI:
    DPI = args.DPI

if args.DPI_TMP_IMAGE:
    DPI_TMP_IMAGE = args.DPI_TMP_IMAGE

if args.IT_DIR:
    IT_DIR = True

if args.DIR_REC:
    DIR_REC = True

if args.GRAYSCALE:
    GRAYSCALE = True

if args.OVERWRITE:
    OVERWRITE = True

if args.OUTPUT_DIR:
    OUTPUT_DIR = args.OUTPUT_DIR
    OUTPUT_DIR_DEFAULT = args.OUTPUT_DIR

if args.QUALITY:
    QUALITY = args.QUALITY




print(f'\n\nSETTINGS:\n--------\n DPI: {DPI}\n Quality: {(QUALITY)}\n Grayscale: {GRAYSCALE}\n Poppler_path: '
      f'{pooper_path}\n DPI FOR IMAGE: {DPI_TMP_IMAGE}\n IT DIR {IT_DIR}, DIR REC {DIR_REC}, OVERWRITE {OVERWRITE}\n'
      f'  OUTPUT DIR {OUTPUT_DIR}')



