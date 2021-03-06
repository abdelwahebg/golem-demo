
description = 'Verify the user can add an element to a page and save it successfully'

pages = ['login',
         'index',
         'left_menu',
         'project_pages',
         'page_builder']


def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    click(left_menu.pages_menu)


def test(data):
    store('element_def', ['some_element', 'id', 'selector_value', 'display_name'])
    project_pages.create_access_page('test_add_element_' + random('ddd'))
    page_builder.add_element(data.element_def)
    wait(1)
    page_builder.save_page()
    refresh_page()
    page_builder.verify_element_exists(data.element_def)


def teardown(data):
    close()
