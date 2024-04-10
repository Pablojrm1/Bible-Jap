import re

# Define a function to transform text based on the specified rules
def transform_text(text):
    # Rule 1: Prepend "XXX" before any number
    text = re.sub(r'(\d+)', r'XXX\1', text)

    # Rule 3: Prepend "YYY" before any bullet symbol (•)
    text = text.replace('•', 'YYY•')

    # Rule 2: Replace Kanji expressions followed by content in parenthesis
    def replace_kanji(match):
        kanji_expression = match.group(1)
        content = match.group(2)
        return f'ZZZ{content}AAA{kanji_expression}BBB'

    # Apply Rule 2 within the content between a number and a bullet
    kanji_pattern = r'([\u4e00-\u9faf]+)\(([^)]+)\)'
    text = re.sub(kanji_pattern, replace_kanji, text)

    # Replace placeholders with the specified HTML content
    text = text.replace('XXX', '</div></div></div><div class="hierarchy-item"> <span class="toggle">➕</span>')
    text = text.replace('ZZZ', '<span class="hiragana" data-hiragana="')
    text = text.replace('AAA', '" onclick="showHiragana(this)">')
    text = text.replace('BBB', '</span>')
    text = text.replace('YYY', '<div class="sub-items"> <div class="hierarchy-item">')

    return text

# Example usage
input_text = (
    """34わたしはそれを見(み)た。だから、この方(かた)こそ神(かみ)の子(こ)であると証(あか)ししたのである。
• 我看見了，便做見證，祂就是上帝的兒子。」
"""
)
output_text = transform_text(input_text)
print(f"Transformed text:\n{output_text}")
