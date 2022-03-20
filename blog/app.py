from typing import Dict

blogs: Dict = dict() # blog name -> blog object
MENU_PROMPT = "Enter 'c' to create a blog, 'l' top list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit."

def menu():
    # show the user available blog
    # let the user make choice
    # do something with the choice
    # eventually exit
    print_blogs()
    selection = input(MENU_PROMPT)
    

def print_blogs():
    # print the available blogs
    for key, blog in blogs.items():
        print("- {}".format(blog))



