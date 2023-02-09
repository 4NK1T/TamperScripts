#!/usr/bin/env python
import urllib.parse

def tamper(payload, **kwargs):
    encoded_payload = urllib.parse.quote_plus(payload)
    encoded_payload = urllib.parse.quote_plus(encoded_payload)
    return encoded_payload
