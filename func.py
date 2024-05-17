from PIL import Image, ImageDraw, ImageFont
import random
import string
import datetime


def draw_name(draw,name):
    name_text = name
    name_font = ImageFont.truetype("./src/arial_narrow.ttf", size=35)
    name_x = 48
    name_y = 280
    draw.text((name_x, name_y), name_text, fill="black", font=name_font)


def draw_birth(draw,birth):
    birth_text = birth
    birth_font = ImageFont.truetype("./src/arial_narrow.ttf", size=35)
    birth_x = 48
    birth_y = 345
    draw.text((birth_x, birth_y), birth_text, fill="black", font=birth_font)


def draw_date(draw):
    def generate_random_date():
        current_date = datetime.datetime.now()
        last_september = datetime.datetime(current_date.year - 1, 9, 1)
        next_september = datetime.datetime(current_date.year + 1, 9, 1)
        return f"{last_september.strftime('%m/%Y')}-{next_september.strftime('%m/%Y')}"

    date_text = generate_random_date()
    date_font = ImageFont.truetype("./src/arial_narrow.ttf", size=35)
    date_x = 48
    date_y = 465
    draw.text((date_x, date_y), date_text, fill="black", font=date_font)


def draw_student_code(draw,student_code):
    if student_code == '':
        def generate_random_string(length):
            return ''.join(random.choice(string.digits) for _ in range(length))

        random_8_digits = generate_random_string(8)
        random_6_digits = generate_random_string(6)
    else:
        random_8_digits = student_code[:8]
        random_6_digits = student_code[-6:]
    student_code_text = f"-{random_8_digits}-{random_6_digits}"
    student_code_font = ImageFont.truetype("./src/arial_narrow.ttf", size=35)
    student_code_x = 92
    student_code_y = 401
    draw.text((student_code_x, student_code_y), student_code_text, fill="black", font=student_code_font)


def draw_card_number(draw,card_number):
    if card_number == '':
        def generate_random_string(length):
            return ''.join(random.choice(string.digits) for _ in range(length))

        random_3_digits = [generate_random_string(3) for _ in range(4)]
        card_number_text = ' '.join(random_3_digits)
    else:
        card_number_text = f"{card_number[:3]} {card_number[3:6]} {card_number[6:9]} {card_number[-3:]}"
    card_number_font = ImageFont.truetype("./src/arial_narrow.ttf", size=36)
    card_number_x = 527
    card_number_y = 46
    draw.text((card_number_x, card_number_y), card_number_text, fill="black", font=card_number_font)


def draw_pic(image,pic):
    image.paste(pic,(579,85))


def add_text(name,birth,student_code,card_number,filename):
    image = Image.open("./src/" + "front.png")
    icon = Image.open("./uploads/" + filename)

    draw = ImageDraw.Draw(image)
    draw_name(draw,name)
    draw_birth(draw,birth)
    draw_date(draw)
    draw_student_code(draw,student_code)
    draw_card_number(draw,card_number)
    draw_pic(image,icon)

    image.save("./outputs/" + filename)

