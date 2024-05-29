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
1その後(のち)、ユダヤ(ゆだや)人(じん)の祭(まつ)りがあったので、イエスはエルサレムに上(のぼ)られた。 2エルサレムには羊(ひつじ)の門(もん)の傍(かたわ)らに、ヘブライ(へぶらい)語(ご)で「ベトザタ」と呼(よ)ばれる池(いけ)があり、そこには五(いつ)つの回廊(かいろう)があった。 3この回廊(かいろう)には、病気(びょうき)の人(ひと)、目(め)の見(み)えない人(ひと)、足(あし)の不自由(ふじゆう)な人(ひと)、体(からだ)の麻痺(まひ)した人(ひと)などが、大勢(おおぜい)横(よこ)たわっていた。 4† 5さて、そこに三十八年(ねん)も病気(びょうき)で苦(くる)しんでいる人(ひと)がいた。 6イエスは、その人(ひと)が横(よこ)たわっているのを見(み)、また、もう長(なが)い間(あいだ)病気(びょうき)であるのを知(し)って、「良(よ)くなりたいか」と言(い)われた。 7病人(びょうにん)は答(こた)えた。「主(しゅ)よ、水(みず)が動(うご)くとき、わたしを池(いけ)の中(なか)に入(い)れてくれる人(ひと)がいないのです。わたしが行(い)くうちに、ほかの人(ひと)が先(さき)に降(お)りて行(い)くのです。」 8イエスは言(い)われた。「起(お)き上(あ)がりなさい。床(とこ)を担(かつ)いで歩(ある)きなさい。」 9すると、その人(ひと)はすぐに良(よ)くなって、床(とこ)を担(かつ)いで歩(ある)きだした。
その日(ひ)は安息(あんそく)日(び)であった。 10そこで、ユダヤ(ゆだや)人(じん)たちは病気(びょうき)をいやしていただいた人(ひと)に言(い)った。「今日(きょう)は安息(あんそく)日(び)だ。だから床(とこ)を担(かつ)ぐことは、律法(りっぽう)で許(ゆる)されていない。」 11しかし、その人(ひと)は、「わたしをいやしてくださった方(ほう)が、『床(とこ)を担(かつ)いで歩(ある)きなさい』と言(い)われたのです」と答(こた)えた。 12彼(かれ)らは、「お前(まえ)に『床(とこ)を担(かつ)いで歩(ある)きなさい』と言(い)ったのはだれだ」と尋(たず)ねた。 13しかし、病気(びょうき)をいやしていただいた人(ひと)は、それがだれであるか知(し)らなかった。イエスは、群衆(ぐんしゅう)がそこにいる間(あいだ)に、立(た)ち去(さ)られたからである。 14その後(のち)、イエスは、神殿(しんでん)の境内(けいだい)でこの人(ひと)に出会(であ)って言(い)われた。「あなたは良(よ)くなったのだ。もう、罪(つみ)を犯(おか)してはいけない。さもないと、もっと悪(わる)いことが起(お)こるかもしれない。」 15この人(ひと)は立(た)ち去(さ)って、自分(じぶん)をいやしたのはイエスだと、ユダヤ(ゆだや)人(じん)たちに知(し)らせた。 16そのために、ユダヤ(ゆだや)人(じん)たちはイエスを迫害(はくがい)し始(はじ)めた。イエスが、安息(あんそく)日(び)にこのようなことをしておられたからである。 17イエスはお答(こた)えになった。「わたしの父(ちち)は今(いま)もなお働(はたら)いておられる。だから、わたしも働(はたら)くのだ。」 18このために、ユダヤ(ゆだや)人(じん)たちは、ますますイエスを殺(ころ)そうとねらうようになった。イエスが安息(あんそく)日(び)を破(やぶ)るだけでなく、神(かみ)を御自分(ごじぶん)の父(ちち)と呼(よ)んで、御自身(ごじしん)を神(かみ)と等(ひと)しい者(もの)とされたからである。
19そこで、イエスは彼(かれ)らに言(い)われた。「はっきり言(い)っておく。子(こ)は、父(ちち)のなさることを見(み)なければ、自分(じぶん)からは何事(なにごと)もできない。父(ちち)がなさることはなんでも、子(こ)もそのとおりにする。 20父(ちち)は子(こ)を愛(あい)して、御自分(ごじぶん)のなさることをすべて子(こ)に示(しめ)されるからである。また、これらのことよりも大(おお)きな業(わざ)を子(こ)にお示(しめ)しになって、あなたたちが驚(おどろ)くことになる。 21すなわち、父(ちち)が死者(ししゃ)を復活(ふっかつ)させて命(いのち)をお与(あた)えになるように、子(こ)も、与(あた)えたいと思(おも)う者(もの)に命(いのち)を与(あた)える。 22また、父(ちち)はだれをも裁(さば)かず、裁(さば)きは一切(いっさい)子(こ)に任(まか)せておられる。 23すべての人(ひと)が、父(ちち)を敬(うやま)うように、子(こ)をも敬(うやま)うようになるためである。子(こ)を敬(うやま)わない者(もの)は、子(こ)をお遣(つか)わしになった父(ちち)をも敬(うやま)わない。 24はっきり言(い)っておく。わたしの言葉(ことば)を聞(き)いて、わたしをお遣(つか)わしになった方(ほう)を信(しん)じる者(もの)は、永遠(えいえん)の命(いのち)を得(え)、また、裁(さば)かれることなく、死(し)から命(いのち)へと移(うつ)っている。 25はっきり言(い)っておく。死(し)んだ者(もの)が神(かみ)の子(こ)の声(こえ)を聞(き)く時(とき)が来(く)る。今(いま)やその時(とき)である。その声(こえ)を聞(き)いた者(もの)は生(い)きる。 26父(ちち)は、御自身(ごじしん)の内(うち)に命(いのち)を持(も)っておられるように、子(こ)にも自分(じぶん)の内(うち)に命(いのち)を持(も)つようにしてくださったからである。 27また、裁(さば)きを行(おこな)う権能(けんのう)を子(こ)にお与(あた)えになった。子(こ)は人(ひと)の子(こ)だからである。 28驚(おどろ)いてはならない。時(とき)が来(く)ると、墓(はか)の中(なか)にいる者(もの)は皆(みな)、人(ひと)の子(こ)の声(こえ)を聞(き)き、 29善(ぜん)を行(おこな)った者(もの)は復活(ふっかつ)して命(いのち)を受(う)けるために、悪(あく)を行(おこな)った者(もの)は復活(ふっかつ)して裁(さば)きを受(う)けるために出(で)て来(く)るのだ。
30わたしは自分(じぶん)では何(なに)もできない。ただ、父(ちち)から聞(き)くままに裁(さば)く。わたしの裁(さば)きは正(ただ)しい。わたしは自分(じぶん)の意志(いし)ではなく、わたしをお遣(つか)わしになった方(かた)の御心(みこころ)を行(おこな)おうとするからである。」
31「もし、わたしが自分(じぶん)自身(じしん)について証(あか)しをするなら、その証(あか)しは真実(しんじつ)ではない。 32わたしについて証(あか)しをなさる方(かた)は別(べつ)におられる。そして、その方(かた)がわたしについてなさる証(あか)しは真実(しんじつ)であることを、わたしは知(し)っている。 33あなたたちはヨハネのもとへ人(ひと)を送(おく)ったが、彼(かれ)は真理(しんり)について証(あか)しをした。 34わたしは、人間(にんげん)による証(あか)しは受(う)けない。しかし、あなたたちが救(すく)われるために、これらのことを言(い)っておく。 35ヨハネは、燃(も)えて輝(かがや)くともし火(び)であった。あなたたちは、しばらくの間(あいだ)その光(ひかり)のもとで喜(よろこ)び楽(たの)しもうとした。 36しかし、わたしにはヨハネの証(あか)しにまさる証(あか)しがある。父(ちち)がわたしに成(な)し遂(と)げるようにお与(あた)えになった業(わざ)、つまり、わたしが行(おこな)っている業(わざ)そのものが、父(ちち)がわたしをお遣(つか)わしになったことを証(あか)ししている。 37また、わたしをお遣(つか)わしになった父(ちち)が、わたしについて証(あか)しをしてくださる。あなたたちは、まだ父(ちち)のお声(こえ)を聞(き)いたこともなければ、お姿(すがた)を見(み)たこともない。 38また、あなたたちは、自分(じぶん)の内(うち)に父(ちち)のお言葉(ことば)をとどめていない。父(ちち)がお遣(つか)わしになった者(もの)を、あなたたちは信(しん)じないからである。 39あなたたちは聖書(せいしょ)の中(なか)に永遠(えいえん)の命(いのち)があると考(かんが)えて、聖書(せいしょ)を研究(けんきゅう)している。ところが、聖書(せいしょ)はわたしについて証(あか)しをするものだ。 40それなのに、あなたたちは、命(いのち)を得(え)るためにわたしのところへ来(こ)ようとしない。
41わたしは、人(ひと)からの誉(ほま)れは受(う)けない。 42しかし、あなたたちの内(うち)には神(かみ)への愛(あい)がないことを、わたしは知(し)っている。 43わたしは父(ちち)の名(な)によって来(き)たのに、あなたたちはわたしを受(う)け入(い)れない。もし、ほかの人(ひと)が自分(じぶん)の名(な)によって来(く)れば、あなたたちは受(う)け入(い)れる。 44互(たが)いに相手(あいて)からの誉(ほま)れは受(う)けるのに、唯一(ゆいいつ)の神(かみ)からの誉(ほま)れは求(もと)めようとしないあなたたちには、どうして信(しん)じることができようか。 45わたしが父(ちち)にあなたたちを訴(うった)えるなどと、考(かんが)えてはならない。あなたたちを訴(うった)えるのは、あなたたちが頼(たよ)りにしているモーセなのだ。 46あなたたちは、モーセを信(しん)じたのであれば、わたしをも信(しん)じたはずだ。モーセは、わたしについて書(か)いているからである。 47しかし、モーセの書(か)いたことを信(しん)じないのであれば、どうしてわたしが語(かた)ることを信(しん)じることができようか。」

1 After this there was a feast of the Jews, and Jesus went up to Jerusalem. 2 Now there is in Jerusalem by the Sheep Gate a pool, which is called in Hebrew, [a]Bethesda, having five porches. 3 In these lay a great multitude of sick people, blind, lame, [b]paralyzed, [c]waiting for the moving of the water. 4 For an angel went down at a certain time into the pool and stirred up the water; then whoever stepped in first, after the stirring of the water, was made well of whatever disease he had. 5 Now a certain man was there who had an infirmity thirty-eight years. 6 When Jesus saw him lying there, and knew that he already had been in that condition a long time, He said to him, “Do you want to be made well?”

7 The sick man answered Him, “Sir, I have no man to put me into the pool when the water is stirred up; but while I am coming, another steps down before me.”

8 Jesus said to him, “Rise, take up your bed and walk.” 9 And immediately the man was made well, took up his bed, and walked.

And that day was the Sabbath. 10 The Jews therefore said to him who was cured, “It is the Sabbath; it is not lawful for you to carry your bed.”

11 He answered them, “He who made me well said to me, ‘Take up your bed and walk.’ ”

12 Then they asked him, “Who is the Man who said to you, ‘Take up your bed and walk’?” 13 But the one who was healed did not know who it was, for Jesus had withdrawn, a multitude being in that place. 14 Afterward Jesus found him in the temple, and said to him, “See, you have been made well. Sin no more, lest a worse thing come upon you.”

15 The man departed and told the Jews that it was Jesus who had made him well.

Honor the Father and the Son
16 For this reason the Jews persecuted Jesus, [d]and sought to kill Him, because He had done these things on the Sabbath. 17 But Jesus answered them, “My Father has been working until now, and I have been working.”

18 Therefore the Jews sought all the more to kill Him, because He not only broke the Sabbath, but also said that God was His Father, making Himself equal with God. 19 Then Jesus answered and said to them, “Most assuredly, I say to you, the Son can do nothing of Himself, but what He sees the Father do; for whatever He does, the Son also does in like manner. 20 For the Father loves the Son, and shows Him all things that He Himself does; and He will show Him greater works than these, that you may marvel. 21 For as the Father raises the dead and gives life to them, even so the Son gives life to whom He will. 22 For the Father judges no one, but has committed all judgment to the Son, 23 that all should honor the Son just as they honor the Father. He who does not honor the Son does not honor the Father who sent Him.

Life and Judgment Are Through the Son
24 “Most assuredly, I say to you, he who hears My word and believes in Him who sent Me has everlasting life, and shall not come into judgment, but has passed from death into life. 25 Most assuredly, I say to you, the hour is coming, and now is, when the dead will hear the voice of the Son of God; and those who hear will live. 26 For as the Father has life in Himself, so He has granted the Son to have life in Himself, 27 and has given Him authority to execute judgment also, because He is the Son of Man. 28 Do not marvel at this; for the hour is coming in which all who are in the graves will hear His voice 29 and come forth—those who have done good, to the resurrection of life, and those who have done evil, to the resurrection of condemnation. 30 I can of Myself do nothing. As I hear, I judge; and My judgment is righteous, because I do not seek My own will but the will of the Father who sent Me.

The Fourfold Witness
31 “If I bear witness of Myself, My witness is not [e]true. 32 There is another who bears witness of Me, and I know that the witness which He witnesses of Me is true. 33 You have sent to John, and he has borne witness to the truth. 34 Yet I do not receive testimony from man, but I say these things that you may be saved. 35 He was the burning and shining lamp, and you were willing for a time to rejoice in his light. 36 But I have a greater witness than John’s; for the works which the Father has given Me to finish—the very works that I do—bear witness of Me, that the Father has sent Me. 37 And the Father Himself, who sent Me, has testified of Me. You have neither heard His voice at any time, nor seen His form. 38 But you do not have His word abiding in you, because whom He sent, Him you do not believe. 39 You search the Scriptures, for in them you think you have eternal life; and these are they which testify of Me. 40 But you are not willing to come to Me that you may have life.

41 “I do not receive honor from men. 42 But I know you, that you do not have the love of God in you. 43 I have come in My Father’s name, and you do not receive Me; if another comes in his own name, him you will receive. 44 How can you believe, who receive honor from one another, and do not seek the honor that comes from the only God? 45 Do not think that I shall accuse you to the Father; there is one who accuses you—Moses, in whom you trust. 46 For if you believed Moses, you would believe Me; for he wrote about Me. 47 But if you do not believe his writings, how will you believe My words?”

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