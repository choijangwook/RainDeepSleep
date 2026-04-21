<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>빗소리가 수면에 좋은 이유</title>
<link rel="../style.css">
</head>

<body>

<nav>
<a href="../index.html">홈</a>
</nav>

<h1>빗소리가 수면에 좋은 이유</h1>

<p>
빗소리는 백색소음으로 작용하여 주변 소음을 차단하고
뇌를 안정시키는 역할을 합니다.
</p>

<h2>1. 백색소음 효과</h2>
<p>
일정한 소리는 뇌의 긴장을 낮추고 수면을 유도합니다.
</p>

<h2>2. 스트레스 감소</h2>
<p>
자연의 소리는 심리적 안정감을 제공합니다.
</p>

<h2>결론</h2>
<p>
빗소리는 자연스럽고 효과적인 수면 유도 방법입니다.
</p>

</body>
</html>


<h2>🎧 추천 영상</h2>

<div style="position:relative; padding-bottom:56.25%; height:0;">
  <iframe 
    src="https://www.youtube.com/embed/영상ID" 
    frameborder="0" 
    allowfullscreen
    style="position:absolute; top:0; left:0; width:100%; height:100%;">
  </iframe>
</div>


https://www.youtube.com/watch?v=ABC123XYZ


<h3>관련 글</h3>
<ul>
<li><a href="post2.html">ASMR 효과</a></li>
<li><a href="post3.html">불면증 해결 방법</a></li>
</ul>


<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>{KEYWORD}</title>
<link rel="stylesheet" href="../style.css">
</head>

<body>

<h1>{KEYWORD}</h1>

<p>
{KEYWORD}에 대해 궁금한 사람들이 많습니다. 이 글에서는 쉽게 이해할 수 있도록 핵심만 정리합니다.
</p>

<h2>🎧 추천 영상</h2>
<div style="position:relative; padding-bottom:56.25%; height:0;">
  <iframe src="https://www.youtube.com/embed/{VIDEO_ID}" 
  style="position:absolute; width:100%; height:100%;" frameborder="0"></iframe>
</div>

<h2>{KEYWORD} 효과</h2>
<p>
이 방법은 스트레스 감소와 수면 개선에 도움이 됩니다.
</p>

<h2>{KEYWORD} 활용 방법</h2>
<p>
꾸준히 적용하면 더 큰 효과를 얻을 수 있습니다.
</p>

<h2>결론</h2>
<p>
{KEYWORD}은 간단하지만 매우 효과적인 방법입니다.
</p>

<h3>관련 글</h3>
<ul>
<li><a href="post2.html">ASMR 효과</a></li>
<li><a href="post3.html">불면증 해결 방법</a></li>
</ul>

</body>
</html>

template = open("template.html").read()

keyword = "빗소리 수면 효과"
video = "ABC123"

result = template.replace("{KEYWORD}", keyword).replace("{VIDEO_ID}", video)

open("post1.html", "w").write(result)




import os
from github import Github

# 🔑 설정
TOKEN = "여기에_토큰"
REPO_NAME = "username/username.github.io"

g = Github(TOKEN)
repo = g.get_repo(REPO_NAME)

# 템플릿 불러오기
template = open("template.html", "r", encoding="utf-8").read()

# 키워드 리스트
keywords = [
    "빗소리 수면 효과",
    "불면증 해결 방법",
    "ASMR 효과",
]

for i, kw in enumerate(keywords):
    content = template.replace("{KEYWORD}", kw).replace("{VIDEO_ID}", "ABC123")

    file_path = f"posts/post{i+10}.html"

    repo.create_file(
        file_path,
        f"Add {kw}",
        content,
        branch="main"
    )

print("업로드 완료")


