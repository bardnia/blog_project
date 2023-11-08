# blog_project

<h2>목표</h2>

<ul>
  <li>blog 만들기</li>
  <li>모놀로그식 구성</li>
  <li>CBV기반 개발</li>
</ul>


<h2>기능</h2>
<ul>
  <li>로그인</li>
  <li>CRUD</li>
  <li>댓글 작성 가능</li>
  <li>조회수 체크</li>
</ul>

# 1. 요구사항
<h3>단계별 요구사항(0~3단계)</h3>
<ul>
  <li>0단계: Django Admin을 이용한 게시글 읽기 및 메인페이지 구현하기</li>
  <li>1단계: 블로그 CRUD 기능 구현하기</li>
  <li>2단계: 로그인/회원가입 기능을 이용하여 블로그 구현하기(인증 기능 추가)</li>
  <li>3단계: 블로그 기능 외 추가 기능 작성 및 배포</li>
</ul>



# 2. 프로젝트 구조
<h2>2.1 마인드맵</h2>

![MindMeister](https://github.com/bardnia/blog_project/assets/69304793/2a32b1f6-d5ca-4611-91a0-48ec9ef107e3)


<br>


<h2>2.2 urls 구조</h2>

<br>

- main

|APP|URL|Views Func Name|HTML File Name|Note|
|------|---|---|---|---|
|main|'/'|index|index.html|홈화면|
<br>

- blog

|APP|URL|Views Func Name|HTML File Name|Note|
|------|---|---|---|---|
|blog|'/'|post_list|post_list.html|게시판 목록|
|blog|'write/'|post_edit|post_edit.html|게시글 작성|
|blog|'<int:pk>/'|post_detail|post_detail.html|게시글 내용|
|blog|'edit/<int:pk>/'|post_edit|post_edit.html|게시글 수정|
|blog|'delete/<int:pk>/'|post_delete|post_delete.html|게시글 삭제|
|blog|'comment_new/<int:pk>/'|comment_new|comment_new.html|게시글 댓글 작성|
<br>

- accounts

|APP|URL|Views Func Name|HTML File Name|Note|
|------|---|---|---|---|
|accounts|'register/'|register|register.html|회원가입
|accounts|'login/'|login|login.html|로그인
|accounts|'logout/'|logout|logout.html|로그아웃
|accounts|'profile/'|profile|profile.html|유저정보

<br>

<h2>2.3 TREE 구조</h2>

<pre>
  
back_up
 ┣ accounts
 ┃ ┣ migrations
 ┃ ┣ __pycache__
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ forms.py
 ┃ ┣ models.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ blog
 ┃ ┣ migrations
 ┃ ┣ __pycache__
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ forms.py
 ┃ ┣ models.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ main
 ┃ ┣ migrations
 ┃ ┣ __pycache__
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ media
 ┃ ┗ blog
 ┃ ┃ ┣ files
 ┃ ┃ ┗ images
 ┣ setdjango
 ┃ ┣ __pycache__
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ wsgi.py
 ┃ ┗ __init__.py
 ┣ static
 ┃ ┣ css
 ┃ ┗ images
 ┣ templates
 ┃ ┣ blog
 ┃ ┃ ┣ post_delete.html
 ┃ ┃ ┣ post_detail.html
 ┃ ┃ ┣ post_edit.html
 ┃ ┃ ┣ post_list.html
 ┃ ┃ ┣ post_top.html
 ┃ ┃ ┗ post_write.html
 ┃ ┣ main
 ┃ ┃ ┗ index.html
 ┃ ┗ base.html
</pre>


<h2>2.4 ERD 구조</h2>

![edr구조](https://github.com/bardnia/test/assets/69304793/436f217c-91f2-4bcb-86e6-d187f94594d3)

<br>


