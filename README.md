### Django Encrypted Fields

This is a Python 3 fork of https://github.com/defrex/django-encrypted-fields that swaps the keyczar dependency for the cryptography module.

It uses [StackStorm's keyczar-compatible cryptography adapter](https://github.com/StackStorm/st2/blob/ddd3aba57d8cccaaaef64babd07dd48e0b68c42a/st2common/st2common/util/crypto.py), as referenced by the Google devs on the keyczar repo's issue tracker as an option for [migrating from keyczar to the cryptography module](https://github.com/google/keyczar/issues/213).

As such, this library *should* be a drop-in replacement for the original Python 2 django-encrypted-fields using your existing keyczar settings.

The changes were only intended to assist converting older Django projects on Python 2 to Python 3, before replacing this implementation with [django-fernet-fields](https://github.com/orcasgit/django-fernet-fields).