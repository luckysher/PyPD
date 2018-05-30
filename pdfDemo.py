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

        self.siteIcon = os.path.join(os.getcwd(), "inputs/pd_icon/site_icon.png")
        self.siteIcon2 = os.path.join(os.getcwd(), "inputs/pd_icon/site-icon2.png")
