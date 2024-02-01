#!/usr/bin/python3
"""Defines a locked class."""

class LockedClass:
    """
    Class that prevents the user from dynamicalluy creating new instance attributes, except if new instance attribute is called first_name"""

    __slots__ = ["fist_name"]
