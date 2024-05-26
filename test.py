
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# inch_heights = []
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)

player_heights = [heights * 7920 for heights in player_heights]
    
print(player_heights)