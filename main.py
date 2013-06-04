from PIL import Image, ImageFont, ImageDraw

dpi = 300.0

def inches_to_pixels(inches):
	return int(dpi * inches)

def cm_to_inches(cm):
	return cm * 0.393700787

def cm_to_pixels(cm):
	return inches_to_pixels(cm_to_inches(cm))

a4_size = (cm_to_pixels(21.0), cm_to_pixels(29.7))
(a4_width, a4_height) = a4_size
print "A4 pixel dimensions: " + str(a4_size)

poker_size = (cm_to_pixels(6.3), cm_to_pixels(8.8))
(poker_width, poker_height) = poker_size
print "Poker card pixel dimensions: " + str(poker_size)

margin = cm_to_pixels(1.0)

title_font_path = '/Library/Fonts/Times New Roman.ttf'
title_font = ImageFont.truetype(title_font_path, 24, encoding='unic')

def draw_text_on_card(card, raw_text):
	text = raw_text.decode('utf-8')
	#(width, height) = font.getsize(text)
	draw = ImageDraw.Draw(card)
	draw.text((5, 5), text, font=title_font, fill=(0, 0, 0))

def create_card(card_data):
	illustration = Image.open("illustrations/" + card_data['illustration'] + ".png")
	card = Image.new("RGB", poker_size, "yellow")
	card.paste(illustration, (0, 40))
	draw_text_on_card(card, card_data['name'])
	return card

def create_paper(cards_data_set):
	cards = [create_card(data) for data in cards_data_set]
	paper = Image.new("RGB", a4_size, "white")
	card_index = 0
	for y in xrange(0, a4_height, poker_height + margin):
		for x in xrange(0, a4_width, poker_width + margin):
			card = cards[card_index % len(cards)]
			card_index += 1
			paper.paste(card, (x, y))
	return paper

card_set_1 = [
	{'illustration': "bison", 'name': "The Death", 'body': "Give each player a warm cup of coffee and a hug."}, 
	{'illustration': "citrus", 'name': "Lemonade", 'body': "If you're the oldest player at the table, eat a flower."}
]

create_paper(card_set_1).show()

