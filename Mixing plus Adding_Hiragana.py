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
1さて、イエスがヨハネよりも多(おお)くの弟子(でし)をつくり、洗礼(バプテスマ)を授(さず)けておられるということが、ファリサイ派(は)の人々(ひとびと)の耳(みみ)に入(はい)った。イエスはそれを知(し)ると、 2――洗礼(バプテスマ)を授(さず)けていたのは、イエス御自身(ごじしん)ではなく、弟子(でし)たちである―― 3ユダヤを去(さ)り、再(ふたた)びガリラヤへ行(い)かれた。 4しかし、サマリアを通(とお)らねばならなかった。 5それで、ヤコブがその子(こ)ヨセフに与(あた)えた土地(とち)の近(ちか)くにある、シカルというサマリアの町(まち)に来(こ)られた。 6そこにはヤコブの井戸(いど)があった。イエスは旅(たび)に疲(つか)れて、そのまま井戸(いど)のそばに座(すわ)っておられた。正午(しょうご)ごろのことである。
7サマリアの女(おんな)が水(みず)をくみに来(き)た。イエスは、「水(みず)を飲(の)ませてください」と言(い)われた。 8弟子(でし)たちは食(た)べ物(もの)を買(か)うために町(まち)に行(い)っていた。 9すると、サマリアの女(おんな)は、「ユダヤ(ゆだや)人(じん)のあなたがサマリアの女(おんな)のわたしに、どうして水(みず)を飲(の)ませてほしいと頼(たの)むのですか」と言(い)った。ユダヤ(ゆだや)人(じん)はサマリア人(じん)とは交際(こうさい)しないからである。 10イエスは答(こた)えて言(い)われた。「もしあなたが、神(かみ)の賜(たまもの)物(もの)を知(し)っており、また、『水(みず)を飲(の)ませてください』と言(い)ったのがだれであるか知(し)っていたならば、あなたの方(ほう)からその人(ひと)に頼(たの)み、その人(ひと)はあなたに生(い)きた水(みず)を与(あた)えたことであろう。」 11女(おんな)は言(い)った。「主(しゅ)よ、あなたはくむ物(もの)をお持(も)ちでないし、井戸(いど)は深(ふか)いのです。どこからその生(い)きた水(みず)を手(て)にお入(い)れになるのですか。 12あなたは、わたしたちの父(ちち)ヤコブよりも偉(えら)いのですか。ヤコブがこの井戸(いど)をわたしたちに与(あた)え、彼(かれ)自身(じしん)も、その子供(こども)や家畜(かちく)も、この井戸(いど)から水(みず)を飲(の)んだのです。」 13イエスは答(こた)えて言(い)われた。「この水(みず)を飲(の)む者(もの)はだれでもまた渇(かわ)く。 14しかし、わたしが与(あた)える水(みず)を飲(の)む者(もの)は決(けっ)して渇(かわ)かない。わたしが与(あた)える水(みず)はその人(ひと)の内(うち)で泉(いずみ)となり、永遠(えいえん)の命(いのち)に至(いた)る水(みず)がわき出(で)る。」 15女(おんな)は言(い)った。「主(しゅ)よ、渇(かわ)くことがないように、また、ここにくみに来(こ)なくてもいいように、その水(みず)をください。」
16イエスが、「行(い)って、あなたの夫(おっと)をここに呼(よ)んで来(き)なさい」と言(い)われると、 17女(おんな)は答(こた)えて、「わたしには夫(おっと)はいません」と言(い)った。イエスは言(い)われた。「『夫(おっと)はいません』とは、まさにそのとおりだ。 18あなたには五人(ごにん)の夫(おっと)がいたが、今(いま)連(つ)れ添(そ)っているのは夫(おっと)ではない。あなたは、ありのままを言(い)ったわけだ。」 19女(おんな)は言(い)った。「主(しゅ)よ、あなたは預言者(よげんしゃ)だとお見受(みう)けします。 20わたしどもの先祖(せんぞ)はこの山(やま)で礼拝(れいはい)しましたが、あなたがたは、礼拝(れいはい)すべき場所(ばしょ)はエルサレムにあると言(い)っています。」 21イエスは言(い)われた。「婦人(ふじん)よ、わたしを信(しん)じなさい。あなたがたが、この山(やま)でもエルサレムでもない所(ところ)で、父(ちち)を礼拝(れいはい)する時(とき)が来(く)る。 22あなたがたは知(し)らないものを礼拝(れいはい)しているが、わたしたちは知(し)っているものを礼拝(れいはい)している。救(すく)いはユダヤ(ゆだや)人(じん)から来(く)るからだ。 23しかし、まことの礼拝(れいはい)をする者(もの)たちが、霊(れい)と真理(しんり)をもって父(ちち)を礼拝(れいはい)する時(とき)が来(く)る。今(いま)がその時(とき)である。なぜなら、父(ちち)はこのように礼拝(れいはい)する者(もの)を求(もと)めておられるからだ。 24神(かみ)は霊(れい)である。だから、神(かみ)を礼拝(れいはい)する者(もの)は、霊(れい)と真理(しんり)をもって礼拝(れいはい)しなければならない。」 25女(おんな)が言(い)った。「わたしは、キリストと呼(よ)ばれるメシアが来(こ)られることは知(し)っています。その方(かた)が来(こ)られるとき、わたしたちに一切(いっさい)のことを知(し)らせてくださいます。」 26イエスは言(い)われた。「それは、あなたと話(はなし)をしているこのわたしである。」
27ちょうどそのとき、弟子(でし)たちが帰(かえ)って来(き)て、イエスが女(おんな)の人(ひと)と話(はなし)をしておられるのに驚(おどろ)いた。しかし、「何(なに)か御用(ごよう)ですか」とか、「何(なに)をこの人(ひと)と話(はな)しておられるのですか」と言(い)う者(もの)はいなかった。 28女(おんな)は、水(みず)がめをそこに置(お)いたまま町(まち)に行(い)き、人々(ひとびと)に言(い)った。 29「さあ、見(み)に来(き)てください。わたしが行(おこな)ったことをすべて、言(い)い当(あ)てた人(ひと)がいます。もしかしたら、この方(かた)がメシアかもしれません。」 30人々(ひとびと)は町(まち)を出(で)て、イエスのもとへやって来(き)た。
31その間(あいだ)に、弟子(でし)たちが「ラビ、食事(しょくじ)をどうぞ」と勧(すす)めると、 32イエスは、「わたしにはあなたがたの知(し)らない食(た)べ物(もの)がある」と言(い)われた。 33弟子(でし)たちは、「だれかが食(た)べ物(もの)を持(も)って来(き)たのだろうか」と互(たが)いに言(い)った。 34イエスは言(い)われた。「わたしの食(た)べ物(もの)とは、わたしをお遣(つか)わしになった方(かた)の御心(みこころ)を行(おこな)い、その業(わざ)を成(な)し遂(と)げることである。 35あなたがたは、『刈(か)り入(い)れまでまだ四(よん)か月(げつ)もある』と言(い)っているではないか。わたしは言(い)っておく。目(め)を上(あ)げて畑(はたけ)を見(み)るがよい。色(いろ)づいて刈(か)り入(い)れを待(ま)っている。既(すで)に、 36刈(か)り入(い)れる人(ひと)は報酬(ほうしゅう)を受(う)け、永遠(えいえん)の命(いのち)に至(いた)る実(み)を集(あつ)めている。こうして、種(たね)を蒔(ま)く人(ひと)も刈(か)る人(ひと)も、共(とも)に喜(よろこ)ぶのである。 37そこで、『一人(ひとり)が種(たね)を蒔(ま)き、別(べつ)の人(ひと)が刈(か)り入(い)れる』ということわざのとおりになる。 38あなたがたが自分(じぶん)では労苦(ろうく)しなかったものを刈(か)り入(い)れるために、わたしはあなたがたを遣(つか)わした。他(た)の人々(ひとびと)が労苦(ろうく)し、あなたがたはその労苦(ろうく)の実(みの)りにあずかっている。」
39さて、その町(まち)の多(おお)くのサマリア人(じん)は、「この方(かた)が、わたしの行(おこな)ったことをすべて言(い)い当(あ)てました」と証言(しょうげん)した女(おんな)の言葉(ことば)によって、イエスを信(しん)じた。 40そこで、このサマリア人(じん)たちはイエスのもとにやって来(き)て、自分(じぶん)たちのところにとどまるようにと頼(たの)んだ。イエスは、二日間(ふつかかん)そこに滞在(たいざい)された。 41そして、更(さら)に多(おお)くの人々(ひとびと)が、イエスの言葉(ことば)を聞(き)いて信(しん)じた。 42彼(かれ)らは女(おんな)に言(い)った。「わたしたちが信(しん)じるのは、もうあなたが話(はな)してくれたからではない。わたしたちは自分(じぶん)で聞(き)いて、この方(かた)が本当(ほんとう)に世(よ)の救(すく)い主(しゅ)であると分(わ)かったからです。」
43二日(ふつか)後(ご)、イエスはそこを出発(しゅっぱつ)して、ガリラヤへ行(い)かれた。 44イエスは自(みずか)ら、「預言者(よげんしゃ)は自分(じぶん)の故郷(こきょう)では敬(うやま)われないものだ」とはっきり言(い)われたことがある。 45ガリラヤにお着(つ)きになると、ガリラヤの人(ひと)たちはイエスを歓迎(かんげい)した。彼(かれ)らも祭(まつ)りに行(い)ったので、そのときエルサレムでイエスがなさったことをすべて、見(み)ていたからである。
46イエスは、再(ふたた)びガリラヤのカナに行(い)かれた。そこは、前(まえ)にイエスが水(みず)をぶどう酒(しゅ)に変(か)えられた所(ところ)である。さて、カファルナウムに王(おう)の役人(やくにん)がいて、その息子(むすこ)が病気(びょうき)であった。 47この人(ひと)は、イエスがユダヤからガリラヤに来(こ)られたと聞(き)き、イエスのもとに行(い)き、カファルナウムまで下(くだ)って来(き)て息子(むすこ)をいやしてくださるように頼(たの)んだ。息子(むすこ)が死(し)にかかっていたからである。 48イエスは役人(やくにん)に、「あなたがたは、しるしや不思議(ふしぎ)な業(わざ)を見(み)なければ、決(けっ)して信(しん)じない」と言(い)われた。 49役人(やくにん)は、「主(しゅ)よ、子供(こども)が死(し)なないうちに、おいでください」と言(い)った。 50イエスは言(い)われた。「帰(かえ)りなさい。あなたの息子(むすこ)は生(い)きる。」その人(ひと)は、イエスの言(い)われた言葉(ことば)を信(しん)じて帰(かえ)って行(い)った。 51ところが、下(くだ)って行(い)く途中(とちゅう)、僕(しもべ)たちが迎(むか)えに来(き)て、その子(こ)が生(い)きていることを告(つ)げた。 52そこで、息子(むすこ)の病気(びょうき)が良(よ)くなった時刻(じこく)を尋(たず)ねると、僕(しもべ)たちは、「きのうの午後(ごご)一時(いちじ)に熱(ねつ)が下(さ)がりました」と言(い)った。 53それは、イエスが「あなたの息子(むすこ)は生(い)きる」と言(い)われたのと同(おな)じ時刻(じこく)であることを、この父親(ちちおや)は知(し)った。そして、彼(かれ)もその家族(かぞく)もこぞって信(しん)じた。 54これは、イエスがユダヤからガリラヤに来(き)てなされた、二回(にかい)目(め)のしるしである。

1 Therefore, when the Lord knew that the Pharisees had heard that Jesus made and baptized more disciples than John 2 (though Jesus Himself did not baptize, but His disciples), 3 He left Judea and departed again to Galilee. 4 But He needed to go through Samaria.

5 So He came to a city of Samaria which is called Sychar, near the plot of ground that Jacob gave to his son Joseph. 6 Now Jacob’s well was there. Jesus therefore, being wearied from His journey, sat thus by the well. It was about the sixth hour.

7 A woman of Samaria came to draw water. Jesus said to her, “Give Me a drink.” 8 For His disciples had gone away into the city to buy food.

9 Then the woman of Samaria said to Him, “How is it that You, being a Jew, ask a drink from me, a Samaritan woman?” For Jews have no dealings with Samaritans.

10 Jesus answered and said to her, “If you knew the gift of God, and who it is who says to you, ‘Give Me a drink,’ you would have asked Him, and He would have given you living water.”

11 The woman said to Him, “Sir, You have nothing to draw with, and the well is deep. Where then do You get that living water? 12 Are You greater than our father Jacob, who gave us the well, and drank from it himself, as well as his sons and his livestock?”

13 Jesus answered and said to her, “Whoever drinks of this water will thirst again, 14 but whoever drinks of the water that I shall give him will never thirst. But the water that I shall give him will become in him a fountain of water springing up into everlasting life.”

15 The woman said to Him, “Sir, give me this water, that I may not thirst, nor come here to draw.”

16 Jesus said to her, “Go, call your husband, and come here.”

17 The woman answered and said, “I have no husband.”

Jesus said to her, “You have well said, ‘I have no husband,’ 18 for you have had five husbands, and the one whom you now have is not your husband; in that you spoke truly.”

19 The woman said to Him, “Sir, I perceive that You are a prophet. 20 Our fathers worshiped on this mountain, and you Jews say that in Jerusalem is the place where one ought to worship.”

21 Jesus said to her, “Woman, believe Me, the hour is coming when you will neither on this mountain, nor in Jerusalem, worship the Father. 22 You worship what you do not know; we know what we worship, for salvation is of the Jews. 23 But the hour is coming, and now is, when the true worshipers will worship the Father in spirit and truth; for the Father is seeking such to worship Him. 24 God is Spirit, and those who worship Him must worship in spirit and truth.”

25 The woman said to Him, “I know that Messiah is coming” (who is called Christ). “When He comes, He will tell us all things.”

26 Jesus said to her, “I who speak to you am He.”

27 And at this point His disciples came, and they marveled that He talked with a woman; yet no one said, “What do You seek?” or, “Why are You talking with her?”

28 The woman then left her waterpot, went her way into the city, and said to the men, 29 “Come, see a Man who told me all things that I ever did. Could this be the Christ?” 30 Then they went out of the city and came to Him.

31 In the meantime His disciples urged Him, saying, “Rabbi, eat.”

32 But He said to them, “I have food to eat of which you do not know.”

33 Therefore the disciples said to one another, “Has anyone brought Him anything to eat?”

34 Jesus said to them, “My food is to do the will of Him who sent Me, and to finish His work. 35 Do you not say, ‘There are still four months and then comes the harvest’? Behold, I say to you, lift up your eyes and look at the fields, for they are already white for harvest! 36 And he who reaps receives wages, and gathers fruit for eternal life, that both he who sows and he who reaps may rejoice together. 37 For in this the saying is true: ‘One sows and another reaps.’ 38 I sent you to reap that for which you have not labored; others have labored, and you have entered into their labors.”

39 And many of the Samaritans of that city believed in Him because of the word of the woman who testified, “He told me all that I ever did.” 40 So when the Samaritans had come to Him, they urged Him to stay with them; and He stayed there two days. 41 And many more believed because of His own word.

42 Then they said to the woman, “Now we believe, not because of what you said, for we ourselves have heard Him and we know that this is indeed [a]the Christ, the Savior of the world.”

43 Now after the two days He departed from there and went to Galilee. 44 For Jesus Himself testified that a prophet has no honor in his own country. 45 So when He came to Galilee, the Galileans received Him, having seen all the things He did in Jerusalem at the feast; for they also had gone to the feast.

46 So Jesus came again to Cana of Galilee where He had made the water wine. And there was a certain [b]nobleman whose son was sick at Capernaum. 47 When he heard that Jesus had come out of Judea into Galilee, he went to Him and implored Him to come down and heal his son, for he was at the point of death. 48 Then Jesus said to him, “Unless you people see signs and wonders, you will by no means believe.”

49 The nobleman said to Him, “Sir, come down before my child dies!”

50 Jesus said to him, “Go your way; your son lives.” So the man believed the word that Jesus spoke to him, and he went his way. 51 And as he was now going down, his servants met him and told him, saying, “Your son lives!”

52 Then he inquired of them the hour when he got better. And they said to him, “Yesterday at the seventh hour the fever left him.” 53 So the father knew that it was at the same hour in which Jesus said to him, “Your son lives.” And he himself believed, and his whole household.

54 This again is the second sign Jesus did when He had come out of Judea into Galilee.


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