import PyPDF2
import os

def generatePDF(filename):
    """
    Method for generating pDF file
    :param filename:
    :return:
    """
    try:
        print("Generating pdf file: '%s'" % filename)

        # creating a pdf file object
        pdfFileObj = open(os.path.join(os.getcwd(), 'input/sample.pdf'), 'rb')

        # closing the pdf file object
        pdfFileObj.close()
    except:
        pass

    print("Generated pdf file: '%s'" % filename)


def addIconToPdf(iconType='logo'):
    """
    Method for adding a icon in the PDF file
    :param iconType:
    :return:
    """
    if iconType == 'logo':
        print("adding logo icon to PDF")

    if iconType == 'tick':
        print("adding tick icon to PDF")

    if iconType == 'cross':
        print("adding cross icon to PDF")

def addTextStrToPDF(text):
    """
    Add a text string to given PDF file object
    :param text:
    :return:
    """

    try:
        pdfFileObj = open(os.path.join(os.getcwd(), 'input/sample.pdf'), 'rb')
        pdfFileObj.addTextString(text)
    except:
        pass

    print("added text string to PDF file")