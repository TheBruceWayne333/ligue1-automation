# This is inside your update_blog.py on GitHub
new_post_body = {
    'title': 'Ligue 1 Matchday Update',
    'content': YOUR_HTML_CODE_HERE  # This is where your long HTML/CSS string goes
}

# The "Push" command to connect to Blogger
service.posts().patch(
    blogId='YOUR_BLOG_ID', 
    postId='YOUR_POST_ID', 
    body=new_post_body
).execute()
