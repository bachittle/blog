from markdown import markdown
import os

# each file in content is a blog post, provided it has .md extension
BLOG_POSTS = [
    "index",
    "welcome"
]
SRC_DIR = "content"
BUILD_DIR = "docs"

for post in BLOG_POSTS:
    in_post = "{}/{}.md".format(SRC_DIR, post)
    print(in_post)
    with open(in_post, 'r') as f:
        text = f.read()
        if not os.path.exists(BUILD_DIR):
            os.mkdir(BUILD_DIR)
        html = markdown(text)
        with open("{}/{}.html".format(BUILD_DIR, post), 'w') as out:
            out.write(html)