# pdfcompressor
Python script for PDF compression consisting of scanned images.
This is wrapper for [poppler](https://github.com/freedesktop/poppler)

## Preparing
1. Create and use [virtual enviroment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
2. Install all reqired packages

   > python pip install -r req.txt

3. Download poppler for example from [Anaconda site](https://anaconda.org/conda-forge/poppler/files). In testing stage i was using version 21.03.0
4. Put the correct path for the bin folder of poppler in cnf.ini

## Using
In command line write:

> python main.py PATH_FOR_PDF_FILE


### Avaible attributes
-d : folder which consist pdf for compression. Not recursive.

-r : flag for recursive

-g : if used do convert into grayscale

-o : if used will overwrite existed pdf

-dpi : DPI for outputfile

-dpi_image : DPI for compression images

-q : Quality for compression images

-output : Dir for saving compressed files
   
### Example

Will compress pdf files recursive from "C:/NotCompressed/" into grayscale mod and save result in "D:/compressed/"

> python main.py "C:/NotCompressed/" -drg -output "D:/compressed/" 
