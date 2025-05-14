"""
Simple Passcode Mailer
----------------------

A simple Python library to send email confirmations via Gmail using App Passwords,
featuring a unique passcode and a timed confirmation link.
"""

from .PasscodeLinkMailer import PasscodeLinkMailer

__version__ = "0.1.0"
__author__ = "Jonatan Shaya"
__email__ = "your.email@example.com"

# You can list what gets imported with a wildcard import, e.g., from simple_passcode_mailer import *
# __all__ = ['PasscodeLinkMailer'] # Uncomment if you want to define __all__
