import webbrowser

webbrowser.open("https://www.google.pl/")

query = input("Enter the Query: ")
webbrowser.open_new_tab('https://google.pl/?q=%s' % query)
