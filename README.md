# wolfOGP

## Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python3 app.py
```

## Usage

```bash
curl -G --data-urlencode "title=記事タイトル" http://127.0.0.1:8080/ogp --output ogp.png

# If the title is already percent-encoded,
curl "http://127.0.0.1:8080/ogp?title=%E8%A8%98%E4%BA%8B%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB" --output ogp.png
```

To check operation, it is convenient to use `&& open ...` or `&& start ...`.

```bash
# for macOS
curl -G --data-urlencode "title=記事タイトル" http://127.0.0.1:8080/ogp --output ogp.png && open ogp.png

# for Windows
curl -G --data-urlencode "title=記事タイトル" http://127.0.0.1:8080/ogp --output ogp.png && start ogp.png
```