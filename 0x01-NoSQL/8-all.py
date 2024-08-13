#!/usr/bin/env python3
"""checking the number of document in a collection"""


def list_all(mongo_collection):
    """getting the numbers of document in a collection"""
    document = mongo_collection.find()
    
    if document.count == 0:
        return []
    return document
