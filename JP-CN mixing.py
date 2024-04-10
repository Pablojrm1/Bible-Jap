import re
from collections import defaultdict

def group_verses(text):
    # Use regular expression to find all matches of verse numbers and their texts
    pattern = re.compile(r'(\d+)([^\d]+)')
    matches = pattern.findall(text)
    
    # Create a dictionary to hold verses grouped by their number
    grouped_verses = defaultdict(list)
    
    # Iterate over the matches and group verses by number
    for number, verse in matches:
        grouped_verses[number].append(verse.strip())
    
    # Sort the dictionary by verse number
    sorted_verses = dict(sorted(grouped_verses.items(), key=lambda item: int(item[0])))
    
    # Combine grouped verses into a single string for each verse number
    combined_verses = []
    for number, verses in sorted_verses.items():
        # Add the first verse with its number
        combined_verses.append(f"{number}{verses[0]}")
        # Add the rest of the verses with a bullet
        combined_verses.extend([f"•{verse}" for verse in verses[1:]])
    
    return combined_verses

# Example text input
input_text = """1三日(にち)目(め)に、ガリラヤのカナで婚礼(こんれい)があって、イエスの母(はは)がそこにいた。 2イエスも、その弟子(でし)たちも婚礼(こんれい)に招(まね)かれた。 
3ぶどう酒(しゅ)が足(た)りなくなったので、母(はは)がイエスに、「ぶどう酒(しゅ)がなくなりました」と言(い)った。 1第三天，在加利利的迦拿有人舉辦婚宴，耶穌的母親在那裡。 2耶穌和門徒也被邀請去赴宴。 
3酒喝完了，耶穌的母親就對祂說：「他們沒有酒了。」"""

# Group the verses
grouped_verses = group_verses(input_text)

# Output the grouped verses
for verse in grouped_verses:
    print(verse)
