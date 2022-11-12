# Smsnator.py

Python wrapper to access [Smsnator](https://emailnator.com/) programmatically.

# What is [Smsnator](https://smsnator.online/) ?

SMSnator is a free service that allows getting instant temporary phone number for receiving SMS. It is also known as "temp phone number", "disposable phone number", "receive SMS online", "free SMS receive", "verification SMS", and "fake phone number". It is used to receive SMS online like Facebook, Gmail, Telegram, WhatsApp, WeChat, etc. SMSnator is the most advanced disposable phone number service on the web because it offers you different numbers all over the world, you can use unlimited SMS verification, registration, etc. and it's totally free.

# Warning

Never use temporary phone number for important information. It is a public phone number and can be accessed by anyone and your phone number is only temporary.

# Example

```python
from smsnator import Smsnator

smsnator = smsnator()
smsnator.generate_email()

print(smsnator.get_email())
print(smsnator.get_inbox(wait=True))
```
