#!/usr/bin/python3

"""Defines a LockedClass."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attribute
    """

    __slots__ = ["first_name"]
