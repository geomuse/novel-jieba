from matplotlib.font_manager import FontManager

fonts = FontManager()
font_names = [font.name for font in fonts.ttflist]
print(font_names)

for _ in font_names :
    if _ in ('SimHei.ttf') :
        print(_)

