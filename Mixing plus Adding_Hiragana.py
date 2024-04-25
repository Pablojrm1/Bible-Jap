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

input_text = """1三日(みっか)目(め)に、ガリラヤのカナで婚礼(こんれい)があって、イエスの母(はは)がそこにいた。 2イエスも、その弟子(でし)たちも婚礼(こんれい)に招(まね)かれた。 3ぶどう酒(しゅ)が足(た)りなくなったので、母(はは)がイエスに、「ぶどう酒(しゅ)がなくなりました」と言(い)った。 4イエスは母(はは)に言(い)われた。「婦人(ふじん)よ、わたしとどんなかかわりがあるのです。わたしの時(とき)はまだ来(き)ていません。」 5しかし、母(はは)は召(め)し使(つか)いたちに、「この人(ひと)が何(なに)か言(い)いつけたら、そのとおりにしてください」と言(い)った。 6そこには、ユダヤ(ゆだや)人(じん)が清(きよ)めに用(もち)いる石(いし)の水(みず)がめが六(むっ)つ置(お)いてあった。いずれも二ないし三メトレテス入(はい)りのものである。 7イエスが、「水(みず)がめに水(みず)をいっぱい入(い)れなさい」と言(い)われると、召(め)し使(つか)いたちは、かめの縁(ふち)まで水(みず)を満(み)たした。 8イエスは、「さあ、それをくんで宴会(えんかい)の世話(せわ)役(やく)のところへ持(も)って行(い)きなさい」と言(い)われた。召(め)し使(つか)いたちは運(はこ)んで行(い)った。 9世話(せわ)役(やく)はぶどう酒(しゅ)に変(か)わった水(みず)の味見(あじみ)をした。このぶどう酒(しゅ)がどこから来(き)たのか、水(みず)をくんだ召(め)し使(つか)いたちは知(し)っていたが、世話(せわ)役(やく)は知(し)らなかったので、花婿(はなむこ)を呼(よ)んで、 10言(い)った。「だれでも初(はじ)めに良(よ)いぶどう酒(しゅ)を出(だ)し、酔(よ)いがまわったころに劣(おと)ったものを出(だ)すものですが、あなたは良(よ)いぶどう酒(しゅ)を今(いま)まで取(と)って置(お)かれました。」 11イエスは、この最初(さいしょ)のしるしをガリラヤのカナで行(おこな)って、その栄光(えいこう)を現(あらわ)された。それで、弟子(でし)たちはイエスを信(しん)じた。
12この後(あと)、イエスは母(はは)、兄弟(きょうだい)、弟子(でし)たちとカファルナウムに下(くだ)って行(い)き、そこに幾日(いくにち)か滞在(たいざい)された。
13ユダヤ人(じん)の過越(すぎこし)祭(さい)が近(ちか)づいたので、イエスはエルサレムへ上(のぼ)って行(い)かれた。 14そして、神殿(しんでん)の境内(けいだい)で牛(うし)や羊(ひつじ)や鳩(はと)を売(う)っている者(もの)たちと、座(すわ)って両替(りょうがえ)をしている者(もの)たちを御覧(ごらん)になった。 15イエスは縄(なわ)で鞭(むち)を作(つく)り、羊(ひつじ)や牛(うし)をすべて境内(けいだい)から追(お)い出(だ)し、両替(りょうがえ)人(にん)の金(かね)をまき散(ち)らし、その台(だい)を倒(たお)し、 16鳩(ばと)を売(う)る者(もの)たちに言(い)われた。「このような物(もの)はここから運(はこ)び出(だ)せ。わたしの父(ちち)の家(いえ)を商売(しょうばい)の家(いえ)としてはならない。」 17弟子(でし)たちは、「あなたの家(いえ)を思(おも)う熱意(ねつい)がわたしを食(く)い尽(つ)くす」と書(か)いてあるのを思(おも)い出(だ)した。 18ユダヤ(ゆだや)人(じん)たちはイエスに、「あなたは、こんなことをするからには、どんなしるしをわたしたちに見(み)せるつもりか」と言(い)った。 19イエスは答(こた)えて言(い)われた。「この神殿(しんでん)を壊(こわ)してみよ。三日(みっか)で建(た)て直(なお)してみせる。」 20それでユダヤ(ゆだや)人(じん)たちは、「この神殿(しんでん)は建(た)てるのに四十六年(ねん)もかかったのに、あなたは三日(みっか)で建(た)て直(なお)すのか」と言(い)った。 21イエスの言(い)われる神殿(しんでん)とは、御自分(ごじぶん)の体(からだ)のことだったのである。 22イエスが死者(ししゃ)の中(なか)から復活(ふっかつ)されたとき、弟子(でし)たちは、イエスがこう言(い)われたのを思(おも)い出(だ)し、聖書(せいしょ)とイエスの語(かた)られた言葉(ことば)とを信(しん)じた。
23イエスは過越(すぎこし)祭(さい)の間(あいだ)エルサレムにおられたが、そのなさったしるしを見(み)て、多(おお)くの人(ひと)がイエスの名(な)を信(しん)じた。 24しかし、イエス御自身(ごじしん)は彼(かれ)らを信用(しんよう)されなかった。それは、すべての人(ひと)のことを知(し)っておられ、 25人間(にんげん)についてだれからも証(あか)ししてもらう必要(ひつよう)がなかったからである。イエスは、何(なに)が人間(にんげん)の心(こころ)の中(なか)にあるかをよく知(し)っておられたのである。
1 第三天，在加利利的迦拿有人舉辦婚宴，耶穌的母親在那裡。 2 耶穌和門徒也被邀請去赴宴。 3 酒喝完了，耶穌的母親就對祂說：「他們沒有酒了。」 4 耶穌說：「婦人，這跟你我有什麼相干[a]？我的時候還沒有到。」 5 祂母親對僕人說：「祂叫你們做什麼，你們就做什麼。」 6 那裡有六口猶太人用來行潔淨禮儀的石缸，每口可以盛約一百升水。
7 耶穌對僕人說：「把缸倒滿水！」他們就往缸裡倒水，一直滿到缸口。 8 耶穌又說：「現在可以舀些出來，送給宴席總管。」他們就送了去。 9 那些僕人知道這酒是怎樣來的，宴席總管卻不知道。他嚐過那水變的酒後，便把新郎叫來， 10 對他說：「人們都是先拿好酒款待客人，等客人喝夠了，才把次等的拿出來，你卻把好酒留到現在！」 11 這是耶穌第一次行神蹟，是在加利利的迦拿行的，彰顯了祂的榮耀，門徒都信了祂。
12 這事以後，耶穌和祂的母親、弟弟並門徒一起去迦百農住了幾天。
13 猶太人的逾越節快到了，耶穌便上耶路撒冷去。 14 祂看見聖殿區有人在賣牛羊和鴿子，還有人在兌換銀幣， 15 就用繩索做成鞭子把牛羊趕出去，倒掉錢商的銀幣，推翻他們的桌子， 16 又對賣鴿子的說：「把這些東西拿出去！不要把我父的殿當作市場。」 17 祂的門徒想起聖經上說：「我對你的殿充滿炙熱的愛。」
18 當時，猶太人質問祂：「你給我們顯什麼神蹟來證明你有權這樣做？」
19 耶穌回答說：「你們拆毀這座殿，我三天之內會把它重建起來。」
20 他們說：「這座殿用了四十六年才建成，你三天之內就要把它重建起來嗎？」 21 其實耶穌說的殿是指自己的身體， 22 所以等到祂從死裡復活以後，祂的門徒想起這句話，就相信了聖經和耶穌所傳的道。
23 耶穌在耶路撒冷過逾越節期間，許多人看見祂行的神蹟，就信了祂。 24 耶穌卻不信任他們，因為祂洞悉萬人。 25 不用別人告訴祂，祂也深知人的內心。
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