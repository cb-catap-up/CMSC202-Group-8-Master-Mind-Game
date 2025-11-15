from constants import COLOR_MAP
def mapColors(colors):
    mapped_valid_colors = []
    # assigned each color with the respective circle
    for color in colors:
        mapped_valid_colors.append(f"{color} {COLOR_MAP[color.lower()]}")
    return mapped_valid_colors
