from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route("/ogp")
def ogp():
    title = request.args.get("title", "Default Title")
    author = request.args.get("author", "Unknown")

    # 背景（白）
    img = Image.new("RGB", (1200, 630), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # フォント（日本語対応フォントを用意するのが望ましい）
    # LinuxやMacなら /usr/share/fonts にあるフォントを指定できる
    try:
        font = ImageFont.truetype("NotoSansJP-Regular.otf", 60)
    except:
        font = ImageFont.load_default()

    # テキスト描画
    draw.text((100, 200), title, font=font, fill=(0, 0, 0))
    draw.text((100, 400), f"by {author}", font=font, fill=(100, 100, 100))

    # バイナリに変換して返す
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

