from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io
# import textwrap

app = Flask(__name__)

def wrap_text(text, font, max_width, draw):
    lines = []
    current_line = ""
    for char in text:  # 文字単位で処理
        test_line = current_line + char
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = char
    if current_line:
        lines.append(current_line)
    return lines



@app.route("/ogp")
def ogp():
    title = request.args.get("title", "Default Title")
    author = request.args.get("author", "Unknown")

    try:
        bg = Image.open("bg.png").convert("RGBA")
    except:
        bg = Image.new("RGBA", (1200, 633), color=(255, 255, 255, 255))

    draw = ImageDraw.Draw(bg)

    overlay = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle(
        [(0, 50), (bg.width, bg.height-50)],
        fill=(0,0,0,200)
    )
    bg = Image.alpha_composite(bg, overlay)

    try:
        font_title = ImageFont.truetype("fonts/Noto_Sans_JP/static/NotoSansJP-Regular.ttf", 60)
        font_author = ImageFont.truetype("fonts/Noto_Sans_JP/static/NotoSansJP-Regular.ttf", 30)
    except:
        font_title = ImageFont.load_default()
        font_author = ImageFont.load_default()

    draw = ImageDraw.Draw(bg)
    
    max_width = 1050
    lines = wrap_text(title, font_title, max_width, draw)
    line_height = font_title.getsize("あ")[1] + 10 
    text_height = line_height * len(lines) - 10

    y_start = (bg.height - text_height) / 2
    y_text = y_start
    for line in lines:
        draw.text((bg.width/2, y_text), line, font=font_title, fill=(255,255,255), anchor="mm")
        y_text += line_height
    
    draw.text((bg.width/2, bg.height/5*4), "wolfSSL Japan", font=font_author, fill=(255,255,255), anchor="mm")

    buf = io.BytesIO()
    bg.convert("RGB").save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
