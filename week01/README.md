# week01: 개발환경 세팅 및 기초 학습

## Goals
- [Git 간편 안내서](https://rogerdudler.github.io/git-guide/index.ko.html)
- [Git 기초](https://git-scm.com/book/ko/v1/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EA%B8%B0%EC%B4%88)
- [파이썬이란 무엇인가](https://wikidocs.net/5)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Git, Python, Markdown의 기초적인 지식을 쌓는걸 목표로 합시다!

알고 있는 내용이 각자 다르기 때문에 공부량도 다를 것 같네요. 모르는 부분은 카카오톡 채팅방을 통해 공유하면 될 것 같아요~

## Git Example

Git을 처음 사용하는 분 들은 참고하세요

```bash

// Repository를 로컬에 복사합니다
git clone https://github.com/incleaf/PythonStudy2015.git

// 이동
cd PythonStudy2015

// 본인 이름으로 브랜치를 만듭니다.
git branch hyeonsu

// 브랜치를 전환합니다.
git checkout hyeonsu

// 주간 목표가 작성되어 있는 디렉토리로 들어갑니다.
cd week01

// 주간 목표 디렉터리 안에 본인의 디렉터리를 만듭니다.
mkdir hyeonsu

// 이동
cd hyeonsu

// README 파일 생성, 이 파일에 요점 정리를 하면 됩니다.
touch README.md

// 상위 폴더로 이동
cd ..

// 커밋할 파일 추가
git add hyeonsu

// 커밋
git commit -m "내 디렉터리 생성"

// 푸시
git push origin hyeonsu

````
