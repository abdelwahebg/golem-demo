
description = 'Verify the user can import a page into the test'

pages = ['login',
         'index',
         'left_menu',
         'project_tests',
         'test_builder',
         'project_pages']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    store('page_name', 'page_import_' + random('ccc'))
    click(left_menu.pages_menu)
    project_pages.add_page(data.page_name)
    click(left_menu.tests_menu)

def test(data):
    project_tests.create_access_test('test_import_page_' + random('ccc'))
    test_builder.import_page(data.page_name)
    test_builder.verify_page_in_list(data.page_name)


def teardown(data):
    pass
