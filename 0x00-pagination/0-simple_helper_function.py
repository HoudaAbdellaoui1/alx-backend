#!/usr/bin/env python3
""" Module to get index range"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_page = (page - 1) * page_size
    end_page = start_page + page_size
    return start_page, end_page
