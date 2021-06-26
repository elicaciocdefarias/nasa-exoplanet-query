def get_next_five_pages(current_page, last_page):
    five_pages = current_page + 5
    next_five_pages = five_pages if five_pages <= last_page else last_page + 1

    result = list(
        range(
            current_page,
            next_five_pages,
        )
    )
    return result
