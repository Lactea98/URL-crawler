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
