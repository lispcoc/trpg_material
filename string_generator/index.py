from PIL import Image, ImageDraw, ImageFont


def create_image_with_text(text, output_path):
    # フォントとサイズを指定
    font_path = "NotoSansJP-VariableFont_wght.ttf"  # フォントファイルのパス
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)

    # 一時的な画像を作成して描画オブジェクトを生成
    temp_image = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(temp_image)

    # 文字のバウンディングボックスを取得
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 実際の画像を作成
    image = Image.new("RGB", (80, 64), "black")
    draw = ImageDraw.Draw(image)

    # 文字を描画
    draw.text((80 -16 - text_width, 0), text, font=font, fill="white")

    # 画像を保存
    image.save(output_path)
    print("画像を保存しました: output.png")

for i in range(1, 11):
    create_image_with_text(f"+{i}", f"output_{i}.png")
