from django.test import TestCase

# Create your tests here.

from cryptography.fernet import Fernet


key = Fernet.generate_key()
print(key)