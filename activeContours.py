import sys

from PyQt5.QtCore import *

from helperWindow import *

# Name of the application, organization that created the application and current version of the application
applicationName = 'Active Contours Helper Window'
organizationName = 'Addison Elliott'
version = '0.1.0'


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


def runHelper():
    # Set application, organization name and version
    # This is used for the QSettings (when an empty constructor is given)
    QCoreApplication.setApplicationName(applicationName)
    QCoreApplication.setOrganizationName(organizationName)
    QCoreApplication.setApplicationVersion(version)

    app = QApplication(sys.argv)

    form = HelperWindow()
    form.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    runHelper()