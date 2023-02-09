#!/usr/bin/env python
import re

def tamper(payload, **kwargs):
    return re.sub(r'\bAND\b', 'OR', payload)
