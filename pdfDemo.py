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
        self.cIcon = os.path.join(os.getcwd(), "inputs/pd_icon/check.jpg")
        self.crsIcon = os.path.join(os.getcwd(), "inputs/pd_icon/cross.jpg")
        self.rIcon = os.path.join(os.getcwd(), "inputs/pd_icon/rate_icon.png")


    def addIcons(self):
        """
        Add icons to the PDF file
        :return:
        """











if __name__ == '__main__':
    pdfGen = PDFDemo()
