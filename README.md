# URL crawler


------------

### # Function

사용자가 입력한 URL에 요청을 보내어 URL 만 파싱하여 결과를 html로 출력합니다.

개발 목적은 취약한 URL 이 있는지 분석을 위해 개발 되었습니다.

### # Used module

사용된 모듈은 아래와 같습니다.
```
requests
bs4
argparse
fake_useragent
json
urlparse
```

### # How to use

실행 방법은 아래와 같이 명령어를 입력하면 Crawler 를 시작합니다.

```bash
python3 urlcrawler.py --url https://lactea.kr
```

만약 해당 사이트가 Bot을 감지 한다면 --agent 옵션을 사용하면 랜덤으로 agent를 생성하여 요청을 보냅니다.

```bash
python3 urlcrawler.py --url https://lactea.kr --agent
```

crawler 깊이(depth)를 설정하여 crawler 할 URL 값을 제한 합니다.

--depth [number] 옵션으로 설정 할 수 있으며, 최대 값은 10, 기본값은 3 입니다.
```bash
python3 urlcrawler.py --url https://lactea.kr --agent --depth 5
```

URL crawler 중에서 content url은 파싱에서 제외 하고 싶으면 --nocontent 옵션을 추가 하면 img, css, js 같은 URL은 파싱하지 않습니다.

```bash
python3 urlcrawler.py --url https://lactea.kr --nocontent
```

기타 다른 기능들을 개발 중입니다.

### # Result

모든 URL을 가져와 result.html 파일로 보기 쉽게 결과를 저장합니다.

아래 code 는 위 스크립트를 실행 후 일부 결과를 나타낸 것 입니다.

```html
<html><head><title>URL crawler result | Universe</title><meta charset='utf-8'><link rel='stylesheet' href='./style.css'></head><body><div class='list' style='margin: 5px 0px 5px 15px;'>https://universe-blog.tistory.com/manage/entry/post</div>
<div class='list' style='margin: 5px 0px 5px 15px;'>https://lactea.kr/archive/202004<div class='list' style='margin: 5px 0px 5px 30px;'>https://lactea.kr/archive/202005<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/archive/202006<div class='list' style='margin: 5px 0px 5px 60px;'>https://lactea.kr/archive/202007</div>
</div>
</div>
</div>
<div class='list' style='margin: 5px 0px 5px 15px;'>https://lactea.kr/category/IT%20news<div class='list' style='margin: 5px 0px 5px 30px;'>https://lactea.kr/entry/%EA%B5%AC%EA%B8%80-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%82%A8%EC%9A%A9-%EC%8B%A0%EA%B3%A0%ED%95%98%EB%A9%B4-%ED%81%B0-%EC%83%81%EA%B8%88-%EC%A4%80%EB%8B%A4?category=856599<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/entry/thehackernews-안드로이드-폰에-영향을-줄-새로운-제로데이-취약점?category=856599?category=856599</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/entry/TheHackernews-맥-OS용-Zoom-Video-회의에-치명적인-원격-코드-실행-취약점?category=856599?category=856599</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/entry/공격자가-암호화된-연결을-감시-할-수-있는-새로운-블루투스-취약점?category=856599?category=856599</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>https://www.boannews.com/media/view.asp?idx=82664</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/entry/TheHackerNews-ProFTPD에-발견된-Arbitrary-file-copy-CVE-2019-12815?category=856599?category=856599</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/comment/add/71</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/entry/TheHackerNews-리눅스-데스크탑에-새로운-스파이-백도어-Evil-Gnome?category=856599?category=856599</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/entry/보안뉴스-이번-블랙햇을-통해-공개될-무료-툴-8가지?category=856599?category=856599</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>http://www.boannews.com/media/view.asp?idx=82664</div>
<div class='list' style='margin: 5px 0px 5px 45px;'>https://lactea.kr/entry/%EA%B5%AC%EA%B8%80-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%82%A8%EC%9A%A9-%EC%8B%A0%EA%B3%A0%ED%95%98%EB%A9%B4-%ED%81%B0-%EC%83%81%EA%B8%88-%EC%A4%80%EB%8B%A4</div>
</div>
...
```