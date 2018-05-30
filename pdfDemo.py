###################################################
#                                                 #
#    Class for generating demo PDF file           #
#                                                 #
###################################################
import os

class PDFDemo:
    """
    Class for generating PDF file with additional graphical data
    """
    def __init__(self, pdfFileName):
        self.pdfFile = pdfFileName
