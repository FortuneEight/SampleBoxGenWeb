from PIL import Image as img
from PIL import ImageDraw, ImageFont
import streamlit as st
import pandas as pd


COVER_FILE_PATH = None
TOP_FONT_TTF_PATH = None
BOTTOM_FONT_TTF_PATH = None
SAVE_FILE_NAME = None
TRANSPARENT_BACKGROUND = None


def sample_box_creator(cover_file_path, direction, top_font_ttf, top_font_size, bottom_font_ttf, bottom_font_size, top_texts, bottom_texts, transparent):
    rect_shape = [(320, 193), (759.9, 632.9)]

    # create new transparent image
    if transparent == True:
        main_img = img.new('RGBA', (1080,1080), (0,0,0,0))
    else:
        main_img = img.new('RGB', (1080,1080), (0,0,0))

    # open cover image and resize
    cover_img = img.open(cover_file_path)
    cover_img = cover_img.resize((415, 415))

    # initialize ImageDraw object and draw rectangle
    draw = ImageDraw.Draw(main_img)

    # calculate image
    if direction <= -90:
        draw.rectangle(rect_shape, fill = "#ffb4b4")
    elif direction <= -80:
        draw.rectangle(rect_shape, fill = "#ff8f9b")
    elif direction <= -70:
        draw.rectangle(rect_shape, fill = "#ff688d")
    elif direction <= -60:
        draw.rectangle(rect_shape, fill = "#f7438f")
    elif direction <= -50:
        draw.rectangle(rect_shape, fill = "#cb3095")
    elif direction <= -40:
        draw.rectangle(rect_shape, fill = "#9f1c9b")
    elif direction <= -30:
        draw.rectangle(rect_shape, fill = "#a339d1")
    elif direction <= -20:
        draw.rectangle(rect_shape, fill = "#a459ff")
    elif direction <= -10:
        draw.rectangle(rect_shape, fill = "#a481ff")
    elif direction <= -3:
        draw.rectangle(rect_shape, fill = "#b0a4ff")
    elif direction <= 2:
        draw.rectangle(rect_shape, fill = "#c4c2ff")
    elif direction <= 9:
        draw.rectangle(rect_shape, fill = "#99b0ff")
    elif direction <= 19:
        draw.rectangle(rect_shape, fill = "#50b1e5")
    elif direction <= 29:
        draw.rectangle(rect_shape, fill = "#1eb480")
    elif direction <= 39:
        draw.rectangle(rect_shape, fill = "#00c950")
    elif direction <= 49:
        draw.rectangle(rect_shape, fill = "#008a00")
    elif direction <= 59:
        draw.rectangle(rect_shape, fill = "#20a300")
    elif direction <= 69:
        draw.rectangle(rect_shape, fill = "#49b700")
    elif direction <= 79:
        draw.rectangle(rect_shape, fill = "#77c700")
    elif direction <= 89:
        draw.rectangle(rect_shape, fill = "#77c700")
    elif direction <= 100:
        draw.rectangle(rect_shape, fill = "#e4e400")
    elif direction == 101:
        draw.rectangle(rect_shape, fill = "#ffffff")

    # draw cover
    main_img.paste(cover_img, (333, 205))

    # import fonts
    top_font = ImageFont.truetype(top_font_ttf, top_font_size)
    bottom_font = ImageFont.truetype(bottom_font_ttf, bottom_font_size)

    top_font_px = top_font_size * (4/3)
    bottom_font_px = bottom_font_size * (4/3)

    y_val = 670.73
    top_texts = top_texts.split("\n")
    bottom_texts = bottom_texts.split("\n")
    # add top text(s) - title of song, semitone value
    for i in range(len(top_texts)):
        w = draw.textlength(top_texts[i], font=top_font)
        position = ((1080 - w) / 2, y_val)
        bbox = draw.textbbox(position, top_texts[i], font=top_font)
        if transparent == False:
            draw.rectangle(bbox, fill="black")
        draw.text(position, top_texts[i], font=top_font, fill=(255,255,255))
        if i == len(top_texts) - 1:
            y_val += (bottom_font_px)
        else:
            y_val += (top_font_px)

    # add bottom text(s) - creator, album, year
    for i in range(len(bottom_texts)):
        w = draw.textlength(bottom_texts[i], font=bottom_font)
        position = ((1080 - w) / 2, y_val)
        bbox = draw.textbbox(position, bottom_texts[i], font=bottom_font)
        if transparent == False:
            draw.rectangle(bbox, fill="black")
        draw.text(position, bottom_texts[i], font=bottom_font, fill=(255,255,255))
        y_val += (bottom_font_px)

    main_img.save(f"{top_texts[0]}.png")
    return main_img



def generate_sample_box():
    global COVER_FILE_PATH
    global TOP_FONT_TTF_PATH
    global BOTTOM_FONT_TTF_PATH
    global SAVE_FILE_NAME
    global TRANSPARENT_BACKGROUND


    direction = int(txt_01.get(1.0, "end-1c"))
    top_font_size = int(txt_02.get(1.0, "end-1c"))
    bottom_font_size = int(txt_03.get(1.0, "end-1c"))
    top_texts = txt_04.get(1.0, "end-1c").split("\n")
    bottom_texts = txt_05.get(1.0, "end-1c").split("\n")
    TRANSPARENT_BACKGROUND = True if var1.get() == 1 else False

    filetypes = [("PNG Files", "*.png")]
    SAVE_FILE_NAME = fd.asksaveasfilename(title="Save as PNG File", filetypes=filetypes)
    sample_box_creator(COVER_FILE_PATH, direction, TOP_FONT_TTF_PATH, top_font_size, BOTTOM_FONT_TTF_PATH, bottom_font_size, top_texts, bottom_texts, SAVE_FILE_NAME, TRANSPARENT_BACKGROUND)

st.title("F8's Sample Box Generator")

file = st.file_uploader("Open Cover File", accept_multiple_files=False, type=["png", "jpg", "jpeg"])
direc = st.number_input("Direction (can go from -100 as 100% left to 100 as 100% right, and 101 = white border)", min_value=-100, max_value=101, value=0, step=1)
tfttf = st.file_uploader("Open Top font TTF", accept_multiple_files=False, type=["ttf"])
bfttf = st.file_uploader("Open Bottom font TTF", accept_multiple_files=False, type=["ttf"])
tfs = st.number_input("Top font size", min_value=1, max_value=200, value=53, step=1)
bfs = st.number_input("Bottom font size", min_value=1, max_value=200, value=46, step=1)
tts = st.text_area("Top text input", key=6)
bts = st.text_area("Bottom text input", key=7)
tranback = st.checkbox("Transparent background?")

try:
    st.image(sample_box_creator(file, direc, tfttf, tfs, bfttf, bfs, tts, bts, tranback))
    save_image_Filename = "{}.png".format(tts.split("\n")[0])
    with open(save_image_Filename, "rb") as f:
        st.download_button(label="Download Image!", data=f, file_name=save_image_Filename, mime="image/png")
except:
    st.markdown("## Fill out ALL inputs, then check back here.")
