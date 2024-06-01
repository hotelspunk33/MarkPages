import os
import shutil

DEFAULT_PAGE = "pages/default_page.html"
PAGE_FOLDER = "pages/"

# wish i had macros :/
def page_name(page):
    return PAGE_FOLDER + page


def init_website(pages, default_page):
    if (os.path.exists(DEFAULT_PAGE)):
        return False # website is already initialized

    os.makedirs('pages', exist_ok=True)
    os.makedirs('content', exist_ok=True)

    # todo: check_default_page(default_page) -> Bool

    # copies default page to pages folder
    shutil.copyfile(default_page, DEFAULT_PAGE)

    # copy any pages passed in - should already be formatted
    for page in pages:
        shutil.copyfile(page, page_name(os.path.basename(page)))