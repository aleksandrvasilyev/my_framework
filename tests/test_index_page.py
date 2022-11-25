def test_check_welcome_text(open_index_page):
    index_page = open_index_page
    assert index_page.welcome_text() == 'Welcome to our store'




