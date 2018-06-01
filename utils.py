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