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
1さて、ファリサイ派(は)に属(ぞく)する、ニコデモという人(ひと)がいた。ユダヤ人(じん)たちの議員(ぎいん)であった。 2ある夜(よる)、イエスのもとに来(き)て言(い)った。「ラビ、わたしどもは、あなたが神(かみ)のもとから来(こ)られた教師(きょうし)であることを知(し)っています。神(かみ)が共(とも)におられるのでなければ、あなたのなさるようなしるしを、だれも行(おこな)うことはできないからです。」 3イエスは答(こた)えて言(い)われた。「はっきり言(い)っておく。人(ひと)は、新(あら)たに生(う)まれなければ、神(かみ)の国(くに)を見(み)ることはできない。」 4ニコデモは言(い)った。「年(とし)をとった者(もの)が、どうして生(う)まれることができましょう。もう一度(いちど)母親(ははおや)の胎内(たいない)に入(はい)って生(う)まれることができるでしょうか。」 5イエスはお答(こた)えになった。「はっきり言(い)っておく。だれでも水(みず)と霊(れい)とによって生(う)まれなければ、神(かみ)の国(くに)に入(はい)ることはできない。 6肉(にく)から生(う)まれたものは肉(にく)である。霊(れい)から生(う)まれたものは霊(れい)である。 7『あなたがたは新(あら)たに生(う)まれねばならない』とあなたに言(い)ったことに、驚(おどろ)いてはならない。 8風(かぜ)は思(おも)いのままに吹(ふ)く。あなたはその音(おと)を聞(き)いても、それがどこから来(き)て、どこへ行(い)くかを知(し)らない。霊(れい)から生(う)まれた者(もの)も皆(みな)そのとおりである。」 9するとニコデモは、「どうして、そんなことがありえましょうか」と言(い)った。 10イエスは答(こた)えて言(い)われた。「あなたはイスラエルの教師(きょうし)でありながら、こんなことが分(わ)からないのか。 11はっきり言(い)っておく。わたしたちは知(し)っていることを語(かた)り、見(み)たことを証(あか)ししているのに、あなたがたはわたしたちの証(あか)しを受(う)け入(い)れない。 12わたしが地上(ちじょう)のことを話(はな)しても信(しん)じないとすれば、天上(てんじょう)のことを話(はな)したところで、どうして信(しん)じるだろう。 13天(てん)から降(くだ)って来(き)た者(もの)、すなわち人(ひと)の子(こ)のほかには、天(てん)に上(のぼ)った者(もの)はだれもいない。 14そして、モーセが荒(あ)れ野(の)で蛇(へび)を上(あ)げたように、人(ひと)の子(こ)も上(あ)げられねばならない。 15それは、信(しん)じる者(もの)が皆(みな)、人(ひと)の子(こ)によって永遠(えいえん)の命(いのち)を得(え)るためである。
16神(かみ)は、その独(ひと)り子(ご)をお与(あた)えになったほどに、世(よ)を愛(あい)された。独(ひと)り子(ご)を信(しん)じる者(もの)が一人(ひとり)も滅(ほろ)びないで、永遠(えいえん)の命(いのち)を得(え)るためである。 17神(かみ)が御子(みこ)を世(よ)に遣(つか)わされたのは、世(よ)を裁(さば)くためではなく、御子(みこ)によって世(よ)が救(すく)われるためである。 18御子(みこ)を信(しん)じる者(もの)は裁(さば)かれない。信(しん)じない者(もの)は既(すで)に裁(さば)かれている。神(かみ)の独(ひと)り子(ご)の名(な)を信(しん)じていないからである。 19光(ひかり)が世(よ)に来(き)たのに、人々(ひとびと)はその行(おこな)いが悪(わる)いので、光(ひかり)よりも闇(やみ)の方(ほう)を好(この)んだ。それが、もう裁(さば)きになっている。 20悪(あく)を行(おこな)う者(もの)は皆(みな)、光(ひかり)を憎(にく)み、その行(おこな)いが明(あか)るみに出(だ)されるのを恐(おそ)れて、光(ひかり)の方(ほう)に来(こ)ないからである。 21しかし、真理(しんり)を行(おこな)う者(もの)は光(ひかり)の方(ほう)に来(く)る。その行(おこな)いが神(かみ)に導(みちび)かれてなされたということが、明(あき)らかになるために。」
22その後(のち)、イエスは弟子(てし)たちとユダヤ地方(ちほう)に行(い)って、そこに一緒(いっしょ)に滞在(たいざい)し、洗礼(バプテスマ)を授(さず)けておられた。 23他方(たほう)、ヨハネは、サリムの近(ちか)くのアイノンで洗礼(バプテスマ)を授(さず)けていた。そこは水(みず)が豊(ゆた)かであったからである。人々(ひとびと)は来(き)て、洗礼(バプテスマ)を受(う)けていた。 24ヨハネはまだ投獄(とうごく)されていなかったのである。 25ところがヨハネの弟子(でし)たちと、あるユダヤ人(じん)との間(あいだ)で、清(きよ)めのことで論争(ろんそう)が起(お)こった。 26彼(かれ)らはヨハネのもとに来(き)て言(い)った。「ラビ、ヨルダン川(がわ)の向(む)こう側(がわ)であなたと一緒(いっしょ)にいた人(ひと)、あなたが証(あか)しされたあの人(ひと)が、洗礼(バプテスマ)を授(さず)けています。みんながあの人(ひと)の方(ほう)へ行(い)っています。」 27ヨハネは答(こた)えて言(い)った。「天(てん)から与(あた)えられなければ、人(ひと)は何(なに)も受(う)けることができない。 28わたしは、『自分(じぶん)はメシアではない』と言(い)い、『自分(じぶん)はあの方(ほう)の前(まえ)に遣(つか)わされた者(もの)だ』と言(い)ったが、そのことについては、あなたたち自身(じしん)が証(あか)ししてくれる。 29花嫁(はなよめ)を迎(むか)えるのは花婿(はなむこ)だ。花婿(はなむこ)の介添(かいぞ)え人(にん)はそばに立(た)って耳(みみ)を傾(かたむ)け、花婿(はなむこ)の声(こえ)が聞(き)こえると大(おお)いに喜(よろこ)ぶ。だから、わたしは喜(よろこ)びで満(み)たされている。 30あの方(かた)は栄(さか)え、わたしは衰(おとろ)えねばならない。」
31「上(うえ)から来(こ)られる方(かた)は、すべてのものの上(うえ)におられる。地(ち)から出(で)る者(もの)は地(ち)に属(ぞく)し、地(ち)に属(ぞく)する者(もの)として語(かた)る。天(てん)から来(こ)られる方(かた)は、すべてのものの上(うえ)におられる。 32この方(かた)は、見(み)たこと、聞(き)いたことを証(あか)しされるが、だれもその証(あか)しを受(う)け入(い)れない。 33その証(あか)しを受(う)け入(い)れる者(もの)は、神(かみ)が真実(しんじつ)であることを確認(かくにん)したことになる。 34神(かみ)がお遣(つか)わしになった方(かた)は、神(かみ)の言葉(ことば)を話(はな)される。神(かみ)が“霊(れい)”を限(かぎ)りなくお与(あた)えになるからである。 35御父(おんちち)は御子(みこ)を愛(あい)して、その手(て)にすべてをゆだねられた。 36御子(みこ)を信(しん)じる人(ひと)は永遠(えいえん)の命(いのち)を得(え)ているが、御子(みこ)に従(したが)わない者(もの)は、命(いのち)にあずかることがないばかりか、神(かみ)の怒(いか)りがその上(うえ)にとどまる。」

1 There was a man of the Pharisees named Nicodemus, a ruler of the Jews. 2 This man came to Jesus by night and said to Him, “Rabbi, we know that You are a teacher come from God; for no one can do these signs that You do unless God is with him.”

3 Jesus answered and said to him, “Most assuredly, I say to you, unless one is born [a]again, he cannot see the kingdom of God.”

4 Nicodemus said to Him, “How can a man be born when he is old? Can he enter a second time into his mother’s womb and be born?”

5 Jesus answered, “Most assuredly, I say to you, unless one is born of water and the Spirit, he cannot enter the kingdom of God. 6 That which is born of the flesh is flesh, and that which is born of the Spirit is spirit. 7 Do not marvel that I said to you, ‘You must be born again.’ 8 The wind blows where it wishes, and you hear the sound of it, but cannot tell where it comes from and where it goes. So is everyone who is born of the Spirit.”

9 Nicodemus answered and said to Him, “How can these things be?”

10 Jesus answered and said to him, “Are you the teacher of Israel, and do not know these things? 11 Most assuredly, I say to you, We speak what We know and testify what We have seen, and you do not receive Our witness. 12 If I have told you earthly things and you do not believe, how will you believe if I tell you heavenly things? 13 No one has ascended to heaven but He who came down from heaven, that is, the Son of Man [b]who is in heaven. 14 And as Moses lifted up the serpent in the wilderness, even so must the Son of Man be lifted up, 15 that whoever believes in Him should [c]not perish but have eternal life. 16 For God so loved the world that He gave His only begotten Son, that whoever believes in Him should not perish but have everlasting life. 17 For God did not send His Son into the world to condemn the world, but that the world through Him might be saved.

18 “He who believes in Him is not condemned; but he who does not believe is condemned already, because he has not believed in the name of the only begotten Son of God. 19 And this is the condemnation, that the light has come into the world, and men loved darkness rather than light, because their deeds were evil. 20 For everyone practicing evil hates the light and does not come to the light, lest his deeds should be exposed. 21 But he who does the truth comes to the light, that his deeds may be clearly seen, that they have been done in God.”

22 After these things Jesus and His disciples came into the land of Judea, and there He remained with them and baptized. 23 Now John also was baptizing in Aenon near Salim, because there was much water there. And they came and were baptized. 24 For John had not yet been thrown into prison.

25 Then there arose a dispute between some of John’s disciples and the Jews about purification. 26 And they came to John and said to him, “Rabbi, He who was with you beyond the Jordan, to whom you have testified—behold, He is baptizing, and all are coming to Him!”

27 John answered and said, “A man can receive nothing unless it has been given to him from heaven. 28 You yourselves bear me witness, that I said, ‘I am not the Christ,’ but, ‘I have been sent before Him.’ 29 He who has the bride is the bridegroom; but the friend of the bridegroom, who stands and hears him, rejoices greatly because of the bridegroom’s voice. Therefore this joy of mine is fulfilled. 30 He must increase, but I must decrease. 31 He who comes from above is above all; he who is of the earth is earthly and speaks of the earth. He who comes from heaven is above all. 32 And what He has seen and heard, that He testifies; and no one receives His testimony. 33 He who has received His testimony has certified that God is true. 34 For He whom God has sent speaks the words of God, for God does not give the Spirit by measure. 35 The Father loves the Son, and has given all things into His hand. 36 He who believes in the Son has everlasting life; and he who does not believe the Son shall not see life, but the wrath of God abides on him.”
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