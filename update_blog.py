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
