###################################################
#                                                 #
#    Class for generating demo PDF file           #
#                                                 #
###################################################
import os
from utils import *

class PDFDemo:
    """
    Class for generating PDF file with additional graphical data
    """
    def __init__(self, pdfFileName):
        self.pdfFile = pdfFileName

        self.siteIcon = os.path.join(os.getcwd(), "inputs/pd_icon/site_icon.png")
        self.siteIcon2 = os.path.join(os.getcwd(), "inputs/pd_icon/site-icon2.png")
        self.cIcon = os.path.join(os.getcwd(), "inputs/pd_icon/check.jpg")
        self.crsIcon = os.path.join(os.getcwd(), "inputs/pd_icon/cross.jpg")
        self.rIcon = os.path.join(os.getcwd(), "inputs/pd_icon/rate_icon.png")

    def createPDF(self):
        """
        Method for creating PDF file
        :return:
        """
        generatePDF(self.pdfFile)

    def addIcons(self, logo=False, checkIcon=False, cross=False):
        """
        Add icons to the PDF file
        :return:
        """
        if logo:
            addIconToPdf('logo')











if __name__ == '__main__':
    pdfGen = PDFDemo()
