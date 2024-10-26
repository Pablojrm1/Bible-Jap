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

1「はっきり言(い)っておく。	羊(ひつじ)の囲(かこ)いに入(はい)るのに、門(もん)を通(とお)らないでほかの所(ところ)を乗(の)り越(こ)えて来(く)る者(もの)は、盗人(ぬすびと)であり、強盗(ごうとう)である。 2門(もん)から入(はい)る者(もの)が羊飼(ひつじか)いである。 3門番(もんばん)は羊飼(ひつじか)いには門(もん)を開(ひら)き、羊(ひつじ)はその声(こえ)を聞(き)き分(わ)ける。羊飼(ひつじか)いは自分(じぶん)の羊(ひつじ)の名(な)を呼(よ)んで連(つ)れ出(だ)す。 4自分(じぶん)の羊(ひつじ)をすべて連(つ)れ出(だ)すと、先頭(せんとう)に立(た)って行(い)く。羊(ひつじ)はその声(こえ)を知(し)っているので、ついて行(い)く。 5しかし、ほかの者(もの)には決(けっ)してついて行(い)かず、逃(に)げ去(さ)る。ほかの者(もの)たちの声(こえ)を知(し)らないからである。」 6イエスは、このたとえをファリサイ派(は)の人々(ひとびと)に話(はな)されたが、彼(かれ)らはその話(はなし)が何(なに)のことか分(わ)からなかった。
7イエスはまた言(い)われた。「はっきり言(い)っておく。わたしは羊(ひつじ)の門(もん)である。 8わたしより前(まえ)に来(き)た者(もの)は皆(みな)、盗人(ぬすびと)であり、強盗(ごうとう)である。しかし、羊(ひつじ)は彼(かれ)らの言(い)うことを聞(き)かなかった。 9わたしは門(もん)である。わたしを通(とお)って入(はい)る者(もの)は救(すく)われる。その人(ひと)は、門(もん)を出入(でい)りして牧草(ぼくそう)を見(み)つける。 10盗人(ぬすびと)が来(く)るのは、盗(ぬす)んだり、屠(ほふ)ったり、滅(ほろ)ぼしたりするためにほかならない。わたしが来(き)たのは、羊(ひつじ)が命(いのち)を受(う)けるため、しかも豊(ゆた)かに受(う)けるためである。 11わたしは良(よ)い羊飼(ひつじか)いである。良(よ)い羊飼(ひつじか)いは羊(ひつじ)のために命(いのち)を捨(す)てる。 12羊飼(ひつじか)いでなく、自分(じぶん)の羊(ひつじ)を持(も)たない雇(やと)い人(にん)は、狼(おおかみ)が来(く)るのを見(み)ると、羊(ひつじ)を置(お)き去(ざ)りにして逃(に)げる。――狼(おおかみ)は羊(ひつじ)を奪(うば)い、また追(お)い散(ち)らす。―― 13彼(かれ)は雇(やと)い人(にん)で、羊(ひつじ)のことを心(こころ)にかけていないからである。 14わたしは良(よ)い羊飼(ひつじか)いである。わたしは自分(じぶん)の羊(ひつじ)を知(し)っており、羊(ひつじ)もわたしを知(し)っている。 15それは、父(ちち)がわたしを知(し)っておられ、わたしが父(ちち)を知(し)っているのと同(おな)じである。わたしは羊(ひつじ)のために命(いのち)を捨(す)てる。 16わたしには、この囲(かこ)いに入(はい)っていないほかの羊(ひつじ)もいる。その羊(ひつじ)をも導(みちび)かなければならない。その羊(ひつじ)もわたしの声(こえ)を聞(き)き分(わ)ける。こうして、羊(ひつじ)は一人(ひとり)の羊飼(ひつじか)いに導(みちび)かれ、一(ひと)つの群(む)れになる。 17わたしは命(いのち)を、再(ふたた)び受(う)けるために、捨(す)てる。それゆえ、父(ちち)はわたしを愛(あい)してくださる。 18だれもわたしから命(いのち)を奪(うば)い取(と)ることはできない。わたしは自分(じぶん)でそれを捨(す)てる。わたしは命(いのち)を捨(す)てることもでき、それを再(ふたた)び受(う)けることもできる。これは、わたしが父(ちち)から受(う)けた掟(おきて)である。」
19この話(はなし)をめぐって、ユダヤ(ゆだや)人(じん)たちの間(あいだ)にまた対立(たいりつ)が生(しょう)じた。 20多(おお)くのユダヤ(ゆだや)人(じん)は言(い)った。「彼(かれ)は悪霊(あくりょう)に取(と)りつかれて、気(き)が変(へん)になっている。なぜ、あなたたちは彼(かれ)の言(い)うことに耳(みみ)を貸(か)すのか。」 21ほかの者(もの)たちは言(い)った。「悪霊(あくりょう)に取(と)りつかれた者(もの)は、こういうことは言(い)えない。悪霊(あくれい)に盲人(もうじん)の目(め)が開(あ)けられようか。」
22そのころ、エルサレムで神殿(しんでん)奉献(ほうけん)記念(きねん)祭(さい)が行(おこな)われた。冬(ふゆ)であった。 23イエスは、神殿(しんでん)の境内(けいだい)でソロモンの回廊(かいろう)を歩(ある)いておられた。 24すると、ユダヤ(ゆだや)人(じん)たちがイエスを取(と)り囲(かこ)んで言(い)った。「いつまで、わたしたちに気(き)をもませるのか。もしメシアなら、はっきりそう言(い)いなさい。」 25イエスは答(こた)えられた。「わたしは言(い)ったが、あなたたちは信(しん)じない。わたしが父(ちち)の名(な)によって行(おこな)う業(わざ)が、わたしについて証(あか)しをしている。 26しかし、あなたたちは信(しん)じない。わたしの羊(ひつじ)ではないからである。 27わたしの羊(ひつじ)はわたしの声(こえ)を聞(き)き分(わ)ける。わたしは彼(かれ)らを知(し)っており、彼(かれ)らはわたしに従(したが)う。 28わたしは彼(かれ)らに永遠(えいえん)の命(いのち)を与(あた)える。彼(かれ)らは決(けっ)して滅(ほろ)びず、だれも彼(かれ)らをわたしの手(て)から奪(うば)うことはできない。 29わたしの父(ちち)がわたしにくださったものは、すべてのものより偉大(いだい)であり、だれも父(ちち)の手(て)から奪(うば)うことはできない。 30わたしと父(ちち)とは一(ひと)つである。」
31ユダヤ人たちは、イエスを石(いし)で打(う)ち殺(ころ)そうとして、また石(いし)を取(と)り上(あ)げた。 32すると、イエスは言(い)われた。「わたしは、父(ちち)が与(あた)えてくださった多(おお)くの善業(ぜんごう)をあなたたちに示(しめ)した。その中(なか)のどの業(わざ)のために、石(いし)で打(う)ち殺(ころ)そうとするのか。」 33ユダヤ人たちは答(こた)えた。「善業(ぜんごう)のことで、石(いし)で打(う)ち殺(ころ)すのではない。神(かみ)を冒瀆(ぼうとく)したからだ。あなたは、人間(にんげん)なのに、自分(じぶん)を神(かみ)としているからだ。」 34そこで、イエスは言(い)われた。「あなたたちの律法(りっぽう)に、『わたしは言(い)う。あなたたちは神々(かみがみ)である』と書(か)いてあるではないか。 35神(かみ)の言葉(ことば)を受(う)けた人たちが、『神々(かみがみ)』と言(い)われている。そして、聖書(せいしょ)が廃(すた)れることはありえない。 36それなら、父(ちち)から聖(きよ)なる者(もの)とされて世(よ)に遣(つか)わされたわたしが、『わたしは神(かみ)の子(こ)である』と言(い)ったからとて、どうして『神(かみ)を冒瀆(ぼうとく)している』と言(い)うのか。 37もし、わたしが父(ちち)の業(わざ)を行(おこな)っていないのであれば、わたしを信(しん)じなくてもよい。 38しかし、行(おこな)っているのであれば、わたしを信(しん)じなくても、その業(わざ)を信(しん)じなさい。そうすれば、父(ちち)がわたしの内(うち)におられ、わたしが父(ちち)の内(うち)にいることを、あなたたちは知(し)り、また悟(さと)るだろう。」 39そこで、ユダヤ人たちはまたイエスを捕(とら)らえようとしたが、イエスは彼(かれ)らの手(て)を逃(に)げれて、去(さ)って行(い)かれた。 40イエスは、再(ふたた)びヨルダンの向(む)こう側(がわ)、ヨハネが最初(さいしょ)に洗礼(バプテスマ)を授(さず)けていた所(ところ)に行(い)って、そこに滞在(たいざい)された。 41多(おお)くの人(ひと)がイエスのもとに来(き)て言(い)った。「ヨハネは何(なに)のしるしも行(おこな)わなかったが、彼(かれ)がこの方(ほう)について話(はな)したことは、すべて本当(ほんとう)だった。」 42そこでは、多(おお)くの人(ひと)がイエスを信(しん)じた。

1 “Most assuredly, I say to you, he who does not enter the sheepfold by the door, but climbs up some other way, the same is a thief and a robber. 2 But he who enters by the door is the shepherd of the sheep. 3 To him the doorkeeper opens, and the sheep hear his voice; and he calls his own sheep by name and leads them out. 4 And when he brings out his own sheep, he goes before them; and the sheep follow him, for they know his voice. 5 Yet they will by no means follow a stranger, but will flee from him, for they do not know the voice of strangers.” 6 Jesus used this illustration, but they did not understand the things which He spoke to them.


7 Then Jesus said to them again, “Most assuredly, I say to you, I am the door of the sheep. 8 All who ever came [a]before Me are thieves and robbers, but the sheep did not hear them. 9 I am the door. If anyone enters by Me, he will be saved, and will go in and out and find pasture. 10 The thief does not come except to steal, and to kill, and to destroy. I have come that they may have life, and that they may have it more abundantly.

11 “I am the good shepherd. The good shepherd gives His life for the sheep. 12 But a [b]hireling, he who is not the shepherd, one who does not own the sheep, sees the wolf coming and leaves the sheep and flees; and the wolf catches the sheep and scatters them. 13 The hireling flees because he is a hireling and does not care about the sheep. 14 I am the good shepherd; and I know My sheep, and am known by My own. 15 As the Father knows Me, even so I know the Father; and I lay down My life for the sheep. 16 And other sheep I have which are not of this fold; them also I must bring, and they will hear My voice; and there will be one flock and one shepherd.

17 “Therefore My Father loves Me, because I lay down My life that I may take it again. 18 No one takes it from Me, but I lay it down of Myself. I have power to lay it down, and I have power to take it again. This command I have received from My Father.”

19 Therefore there was a division again among the Jews because of these sayings. 20 And many of them said, “He has a demon and is [c]mad. Why do you listen to Him?”

21 Others said, “These are not the words of one who has a demon. Can a demon open the eyes of the blind?”


22 Now it was the Feast of Dedication in Jerusalem, and it was winter. 23 And Jesus walked in the temple, in Solomon’s porch. 24 Then the Jews surrounded Him and said to Him, “How long do You keep us in [d]doubt? If You are the Christ, tell us plainly.”

25 Jesus answered them, “I told you, and you do not believe. The works that I do in My Father’s name, they bear witness of Me. 26 But you do not believe, because you are not of My sheep, [e]as I said to you. 27 My sheep hear My voice, and I know them, and they follow Me. 28 And I give them eternal life, and they shall never perish; neither shall anyone snatch them out of My hand. 29 My Father, who has given them to Me, is greater than all; and no one is able to snatch them out of My Father’s hand. 30 I and My Father are one.”


31 Then the Jews took up stones again to stone Him. 32 Jesus answered them, “Many good works I have shown you from My Father. For which of those works do you stone Me?”

33 The Jews answered Him, saying, “For a good work we do not stone You, but for blasphemy, and because You, being a Man, make Yourself God.”

34 Jesus answered them, “Is it not written in your law, ‘I said, “You are gods” ’? 35 If He called them gods, to whom the word of God came (and the Scripture cannot be broken), 36 do you say of Him whom the Father sanctified and sent into the world, ‘You are blaspheming,’ because I said, ‘I am the Son of God’? 37 If I do not do the works of My Father, do not believe Me; 38 but if I do, though you do not believe Me, believe the works, that you may know and [f]believe that the Father is in Me, and I in Him.” 39 Therefore they sought again to seize Him, but He escaped out of their hand.


40 And He went away again beyond the Jordan to the place where John was baptizing at first, and there He stayed. 41 Then many came to Him and said, “John performed no sign, but all the things that John spoke about this Man were true.” 42 And many believed in Him there.



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