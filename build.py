from markdown import markdown
import os

# each file in content is a blog post, provided it has .md extension
BLOG_POSTS = [
    "hello"
]

for post in BLOG_POSTS:
    in_post = "content/{}.md".format(post)
    print(in_post)
    with open(in_post, 'r') as f:
        text = f.read()
        os.mkdir("build")
        html = markdown(text)
        with open("build/{}.html".format(post), 'w') as out:
            out.write(html)