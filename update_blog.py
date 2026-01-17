import os

# This is your "Template" - I've put your exact CSS here
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        :root { --bg-deep: #0a0a0b; --accent-neon: #00f2ff; --text-main: #ffffff; }
        body { background-color: var(--bg-deep); color: var(--text-main); font-family: 'Inter', sans-serif; padding: 20px; }
        .match-card { background: #161618; border-radius: 16px; margin-bottom: 50px; border: 1px solid #27272a; }
        /* ... (The rest of your CSS goes here) ... */
    </style>
</head>
<body>
    <div class="container">
        <header class="hub-header">
            <div class="hub-date">LIGUE 1 MATCHDAY UPDATED</div>
        </header>
        </div>
</body>
</html>
"""

def create_match_block(home, away, score, summary, arena_id):
    # This generates one of your "Cards" automatically
    return f"""
    <div class="match-card">
        <div class="match-status-bar">
            <h2>{home} {score} {away}</h2>
            <span class="badge-final">AI GENERATED REPORT</span>
        </div>
        <div class="summary-wrapper">
            <div class="ai-label">🤖 AI MATCH SUMMARY</div>
            <div class="summary-text"><p>{summary}</p></div>
            <div class="arena-liveblog" data-event="{arena_id}"></div>
        </div>
    </div>
    """

# LOGIC TO SEND TO BLOGGER
# You will use the 'google-api-python-client' library to 
# send this finished HTML to your blog ID.

import os
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

# --- CONFIGURATION ---
# These are the IDs we found in your Blogger URL
BLOG_ID = 'YOUR_BLOG_ID'
POST_ID = 'YOUR_POST_ID'

# --- 1. THE INJECTION MATERIAL (Your HTML Design) ---
def generate_html(match_name, score, summary, arena_id):
    return f"""
<div class="match-card">
    <div class="match-status-bar">
        <h2>{match_name} {score}</h2>
        <span class="badge-final">AI FINAL REPORT</span>
    </div>
    <div class="summary-wrapper">
        <div class="ai-label">🤖 AI MATCH SUMMARY</div>
        <div class="summary-text">
            <p>{summary}</p>
        </div>
        <div class="arena-label">REAL-TIME PLAY-BY-PLAY FEED</div>
        <div class="arena-liveblog" data-event="{arena_id}"></div>
        <script async src="https://go.arena.im/public/js/arenalib.js?p=the-ai-sports-pulse&e={arena_id}"></script>
    </div>
</div>
"""

# --- 2. THE INJECTION PROCESS ---
def inject_content():
    # Load your "Master Key" from the GitHub Secret
    info = json.loads(os.environ['SERVICE_ACCOUNT_JSON'])
    creds = service_account.Credentials.from_service_account_info(info)
    scoped_creds = creds.with_scopes(['https://www.googleapis.com/auth/blogger'])
    
    # Connect to Blogger
    service = build('blogger', 'v3', credentials=scoped_creds)
    
    # Generate the new content
    # (In a full setup, you'd fetch these variables from a sports API)
    new_match_html = generate_html(
        "OM vs LYON", 
        "2 - 1", 
        "Marseille secured a dramatic victory...", 
        "NEW_ARENA_ID"
    )
    
    # Perform the injection
    # This takes your NEW html and UPDATES the existing post
    body = {
        "content": new_match_html 
    }
    
    service.posts().patch(blogId=BLOG_ID, postId=POST_ID, body=body).execute()
    print("Injection Successful!")

if __name__ == "__main__":
    inject_content()
