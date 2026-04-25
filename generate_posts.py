import json
import os
from datetime import datetime

with open("videos.json", "r") as f:
    videos = json.load(f)

os.makedirs("_posts", exist_ok=True)

for v in videos:
    title = v["title"]
    youtube_id = v["youtube_id"]
    category = v["category"]

    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"_posts/{date}-{youtube_id}.md"

    content = f"""---
title: "{title}"
date: {date}
categories: [{category}]
youtube_id: "{youtube_id}"
---

<iframe width="100%" height="400"
src="https://www.youtube.com/embed/{youtube_id}"
frameborder="0" allowfullscreen></iframe>
"""

    with open(filename, "w") as f:
        f.write(content)

print("Posts generated")
