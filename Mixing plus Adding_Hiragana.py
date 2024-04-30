import re


# Part 1: Mixing verses..............................

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

input_text = """
1三日(みっか)目(め)に、ガリラヤのカナで婚礼(こんれい)があって、イエスの母(はは)がそこにいた。 2イエスも、その弟子(でし)たちも婚礼(こんれい)に招(まね)かれた。 3ぶどう酒(しゅ)が足(た)りなくなったので、母(はは)がイエスに、「ぶどう酒(しゅ)がなくなりました」と言(い)った。 4イエスは母(はは)に言(い)われた。「婦人(ふじん)よ、わたしとどんなかかわりがあるのです。わたしの時(とき)はまだ来(き)ていません。」 5しかし、母(はは)は召(め)し使(つか)いたちに、「この人(ひと)が何(なに)か言(い)いつけたら、そのとおりにしてください」と言(い)った。 6そこには、ユダヤ(ゆだや)人(じん)が清(きよ)めに用(もち)いる石(いし)の水(みず)がめが六(むっ)つ置(お)いてあった。いずれも二ないし三メトレテス入(はい)りのものである。 7イエスが、「水(みず)がめに水(みず)をいっぱい入(い)れなさい」と言(い)われると、召(め)し使(つか)いたちは、かめの縁(ふち)まで水(みず)を満(み)たした。 8イエスは、「さあ、それをくんで宴会(えんかい)の世話(せわ)役(やく)のところへ持(も)って行(い)きなさい」と言(い)われた。召(め)し使(つか)いたちは運(はこ)んで行(い)った。 9世話(せわ)役(やく)はぶどう酒(しゅ)に変(か)わった水(みず)の味見(あじみ)をした。このぶどう酒(しゅ)がどこから来(き)たのか、水(みず)をくんだ召(め)し使(つか)いたちは知(し)っていたが、世話(せわ)役(やく)は知(し)らなかったので、花婿(はなむこ)を呼(よ)んで、 10言(い)った。「だれでも初(はじ)めに良(よ)いぶどう酒(しゅ)を出(だ)し、酔(よ)いがまわったころに劣(おと)ったものを出(だ)すものですが、あなたは良(よ)いぶどう酒(しゅ)を今(いま)まで取(と)って置(お)かれました。」 11イエスは、この最初(さいしょ)のしるしをガリラヤのカナで行(おこな)って、その栄光(えいこう)を現(あらわ)された。それで、弟子(でし)たちはイエスを信(しん)じた。
12この後(あと)、イエスは母(はは)、兄弟(きょうだい)、弟子(でし)たちとカファルナウムに下(くだ)って行(い)き、そこに幾日(いくにち)か滞在(たいざい)された。
13ユダヤ人(じん)の過越(すぎこし)祭(さい)が近(ちか)づいたので、イエスはエルサレムへ上(のぼ)って行(い)かれた。 14そして、神殿(しんでん)の境内(けいだい)で牛(うし)や羊(ひつじ)や鳩(はと)を売(う)っている者(もの)たちと、座(すわ)って両替(りょうがえ)をしている者(もの)たちを御覧(ごらん)になった。 15イエスは縄(なわ)で鞭(むち)を作(つく)り、羊(ひつじ)や牛(うし)をすべて境内(けいだい)から追(お)い出(だ)し、両替(りょうがえ)人(にん)の金(かね)をまき散(ち)らし、その台(だい)を倒(たお)し、 16鳩(ばと)を売(う)る者(もの)たちに言(い)われた。「このような物(もの)はここから運(はこ)び出(だ)せ。わたしの父(ちち)の家(いえ)を商売(しょうばい)の家(いえ)としてはならない。」 17弟子(でし)たちは、「あなたの家(いえ)を思(おも)う熱意(ねつい)がわたしを食(く)い尽(つ)くす」と書(か)いてあるのを思(おも)い出(だ)した。 18ユダヤ(ゆだや)人(じん)たちはイエスに、「あなたは、こんなことをするからには、どんなしるしをわたしたちに見(み)せるつもりか」と言(い)った。 19イエスは答(こた)えて言(い)われた。「この神殿(しんでん)を壊(こわ)してみよ。三日(みっか)で建(た)て直(なお)してみせる。」 20それでユダヤ(ゆだや)人(じん)たちは、「この神殿(しんでん)は建(た)てるのに四十六年(ねん)もかかったのに、あなたは三日(みっか)で建(た)て直(なお)すのか」と言(い)った。 21イエスの言(い)われる神殿(しんでん)とは、御自分(ごじぶん)の体(からだ)のことだったのである。 22イエスが死者(ししゃ)の中(なか)から復活(ふっかつ)されたとき、弟子(でし)たちは、イエスがこう言(い)われたのを思(おも)い出(だ)し、聖書(せいしょ)とイエスの語(かた)られた言葉(ことば)とを信(しん)じた。
23イエスは過越(すぎこし)祭(さい)の間(あいだ)エルサレムにおられたが、そのなさったしるしを見(み)て、多(おお)くの人(ひと)がイエスの名(な)を信(しん)じた。 24しかし、イエス御自身(ごじしん)は彼(かれ)らを信用(しんよう)されなかった。それは、すべての人(ひと)のことを知(し)っておられ、 25人間(にんげん)についてだれからも証(あか)ししてもらう必要(ひつよう)がなかったからである。イエスは、何(なに)が人間(にんげん)の心(こころ)の中(なか)にあるかをよく知(し)っておられたのである。
1 On the third day there was a wedding in Cana of Galilee, and the mother of Jesus was there. 2 Now both Jesus and His disciples were invited to the wedding. 3 And when they ran out of wine, the mother of Jesus said to Him, “They have no wine.”

4 Jesus said to her, “Woman, what does your concern have to do with Me? My hour has not yet come.”

5 His mother said to the servants, “Whatever He says to you, do it.”

6 Now there were set there six waterpots of stone, according to the manner of purification of the Jews, containing twenty or thirty gallons apiece. 7 Jesus said to them, “Fill the waterpots with water.” And they filled them up to the brim. 8 And He said to them, “Draw some out now, and take it to the master of the feast.” And they took it. 9 When the master of the feast had tasted the water that was made wine, and did not know where it came from (but the servants who had drawn the water knew), the master of the feast called the bridegroom. 10 And he said to him, “Every man at the beginning sets out the good wine, and when the guests have well drunk, then the inferior. You have kept the good wine until now!”

11 This beginning of signs Jesus did in Cana of Galilee, and [a]manifested His glory; and His disciples believed in Him.

12 After this He went down to Capernaum, He, His mother, His brothers, and His disciples; and they did not stay there many days.

13 Now the Passover of the Jews was at hand, and Jesus went up to Jerusalem. 14 And He found in the temple those who sold oxen and sheep and doves, and the money changers [b]doing business. 15 When He had made a whip of cords, He drove them all out of the temple, with the sheep and the oxen, and poured out the changers’ money and overturned the tables. 16 And He said to those who sold doves, “Take these things away! Do not make My Father’s house a house of merchandise!” 17 Then His disciples remembered that it was written, “Zeal for Your house [c]has eaten Me up.”

18 So the Jews answered and said to Him, “What sign do You show to us, since You do these things?”

19 Jesus answered and said to them, “Destroy this temple, and in three days I will raise it up.”

20 Then the Jews said, “It has taken forty-six years to build this temple, and will You raise it up in three days?”

21 But He was speaking of the temple of His body. 22 Therefore, when He had risen from the dead, His disciples remembered that He had said this [d]to them; and they believed the Scripture and the word which Jesus had said.

23 Now when He was in Jerusalem at the Passover, during the feast, many believed in His name when they saw the signs which He did. 24 But Jesus did not commit Himself to them, because He knew all men, 25 and had no need that anyone should testify of man, for He knew what was in man.
"""

grouped_verses = group_verses(input_text)



# Part 2: Adding Hiragana and font size function...................



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
input_text = ' '.join(grouped_verses)
output_text = transform_text(input_text)
print(f"Transformed text:\n{output_text}")

with open("C:/Users/pablo/OneDrive/Documentos/Bible/Bible Jap/Bible-Jap/MyFile.txt", "w", encoding='utf-8') as f:
    f.write(output_text)