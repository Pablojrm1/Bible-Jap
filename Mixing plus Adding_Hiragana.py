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
1ある病人(びょうにん)がいた。マリアとその姉妹(しまい)マルタの村(むら)、ベタニアの出身(しゅっしん)で、ラザロといった。 2このマリアは主(しゅ)に香油(こうゆ)を塗(ぬ)り、髪(かみ)の毛(け)で主(しゅ)の足(あし)をぬぐった女(おんな)である。その兄弟(きょうだい)ラザロが病気(びょうき)であった。 3姉妹(しまい)たちはイエスのもとに人(ひと)をやって、「主(しゅ)よ、あなたの愛(あい)しておられる者(もの)が病気(びょうき)なのです」と言(い)わせた。 4イエスは、それを聞(き)いて言(い)われた。「この病気(びょうき)は死(し)で終(お)わるものではない。神(かみ)の栄光(えいこう)のためである。神(かみ)の子(こ)がそれによって栄光(えいこう)を受(う)けるのである。」 5イエスは、マルタとその姉妹(しまい)とラザロを愛(あい)しておられた。 6ラザロが病気(びょうき)だと聞(き)いてからも、なお二日間(ふつかかん)同(おな)じ所(ところ)に滞在(たいざい)された。 7それから、弟子(でし)たちに言(い)われた。「もう一度(いちど)、ユダヤに行(い)こう。」 8弟子(でし)たちは言(い)った。「ラビ、ユダヤ人(じん)たちがついこの間(あいだ)もあなたを石(いし)で打(う)ち殺(ころ)そうとしたのに、またそこへ行(い)かれるのですか。」 9イエスはお答(こた)えになった。「昼間(ひるま)は十二時間(じゅうにじかん)あるではないか。昼(ひる)のうちに歩(ある)けば、つまずくことはない。この世(よ)の光(ひかり)を見(み)ているからだ。 10しかし、夜(よる)歩(ある)けば、つまずく。その人(ひと)の内(うち)に光(ひかり)がないからである。」 11こうお話(はな)しになり、また、その後(あと)で言(い)われた。「わたしたちの友(とも)ラザロが眠(ねむ)っている。しかし、わたしは彼(かれ)を起(お)こしに行(い)く。」 12弟子(でし)たちは、「主(しゅ)よ、眠(ねむ)っているのであれば、助(たす)かるでしょう」と言(い)った。 13イエスはラザロの死(し)について話(はな)されたのだが、弟子(でし)たちは、ただ眠(ねむ)りについて話(はな)されたものと思(おも)ったのである。 14そこでイエスは、はっきりと言(い)われた。「ラザロは死(し)んだのだ。 15わたしがその場(ば)に居合(いあ)わせなかったのは、あなたがたにとってよかった。あなたがたが信(しん)じるようになるためである。さあ、彼(かれ)のところへ行(い)こう。」 16すると、ディディモと呼(よ)ばれるトマスが、仲間(なかま)の弟子(でし)たちに、「わたしたちも行(い)って、一緒(いっしょ)に死(し)のうではないか」と言(い)った。 
17さて、イエスが行(い)って御覧(ごらん)になると、ラザロは墓(はか)に葬(ほうむ)られて既(すで)に四日(よっか)もたっていた。 18ベタニアはエルサレムに近(ちか)く、十五スタディオンほどのところにあった。 19マルタとマリアのところには、多(おお)くのユダヤ人(じん)が、兄弟(きょうだい)ラザロのことで慰(なぐさ)めに来(き)ていた。 20マルタは、イエスが来(き)られたと聞(き)いて、迎(むか)えに行(い)ったが、マリアは家(いえ)の中(なか)に座(すわ)っていた。 21マルタはイエスに言(い)った。「主(しゅ)よ、もしここにいてくださいましたら、わたしの兄弟(きょうだい)は死(し)ななかったでしょうに。 22しかし、あなたが神(かみ)にお願(ねが)いになることは何(なん)でも神(かみ)はかなえてくださると、わたしは今(いま)でも承知(しょうち)しています。」 23イエスが、「あなたの兄弟(きょうだい)は復活(ふっかつ)する」と言(い)われると、 24マルタは、「終(お)わりの日(ひ)の復活(ふっかつ)の時(とき)に復活(ふっかつ)することは存(ぞん)じております」と言(い)った。 25イエスは言(い)われた。「わたしは復活(ふっかつ)であり、命(いのち)である。わたしを信(しん)じる者(もの)は、死(し)んでも生(い)きる。 26生(い)きていてわたしを信(しん)じる者(もの)はだれも、決(けっ)して死(し)ぬことはない。このことを信(しん)じるか。」 27マルタは言(い)った。「はい、主(しゅ)よ、あなたが世(よ)に来(き)られるはずの神(かみ)の子(こ)、メシアであるとわたしは信(しん)じております。」 
28マルタは、こう言(い)ってから、家(いえ)に帰(かえ)って姉妹(しまい)のマリアを呼(よ)び、「先生(せんせい)がいらして、あなたをお呼(よ)びです」と耳打(みみう)ちした。 29マリアはこれを聞(き)くと、すぐに立(た)ち上(あ)がり、イエスのもとに行(い)った。 30イエスはまだ村(むら)には入(はい)らず、マルタが出迎(でむか)えた場所(ばしょ)におられた。 31家(いえ)の中(なか)でマリアと一緒(いっしょ)にいて、慰(なぐさ)めていたユダヤ人(じん)たちは、彼女(かのじょ)が急(きゅう)に立(た)ち上(あ)がって出(で)て行(い)くのを見(み)て、墓(はか)に泣(な)きに行(い)くのだろうと思(おも)い、後(あと)を追(お)った。 32マリアはイエスのおられる所(ところ)に来(き)て、イエスを見(み)るなり足(あし)もとにひれ伏(ふ)し、「主(しゅ)よ、もしここにいてくださいましたら、わたしの兄弟(きょうだい)は死(し)ななかったでしょうに」と言(い)った。 33イエスは、彼女(かのじょ)が泣(な)き、一緒(いっしょ)に来(き)たユダヤ人(じん)たちも泣(な)いているのを見(み)て、心(こころ)に憤(いきどお)りを覚(おぼ)え、興奮(こうふん)して、 34言(い)われた。「どこに葬(ほうむ)ったのか。」彼(かれ)らは、「主(しゅ)よ、来(き)て、御覧(ごらん)ください」と言(い)った。 35イエスは涙(なみだ)を流(なが)された。 36ユダヤ人(じん)たちは、「御覧(ごらん)なさい、どんなにラザロを愛(あい)しておられたことか」と言(い)った。 37しかし、中(なか)には、「盲人(もうじん)の目(め)を開(ひら)けたこの人(ひと)も、ラザロが死(し)なないようにはできなかったのか」と言(い)う者(もの)もいた。 
38イエスは、再(ふたた)び心(こころ)に憤(いきどお)りを覚(おぼ)えて、墓(はか)に来(き)られた。墓(はか)は洞穴(どうけつ)で、石(いし)でふさがれていた。 39イエスが、「その石(いし)を取(と)りのけなさい」と言(い)われると、死(し)んだラザロの姉妹(しまい)マルタが、「主(しゅ)よ、四日(よっか)もたっていますから、もうにおいます」と言(い)った。 40イエスは、「もし信(しん)じるなら、神(かみ)の栄光(えいこう)が見(み)られると、言(い)っておいたではないか」と言(い)われた。 41人々(ひとびと)が石(いし)を取(と)りのけると、イエスは天(てん)を仰(あお)いで言(い)われた。「父(ちち)よ、わたしの願(ねが)いを聞(き)き入(い)れてくださって感謝(かんしゃ)します。 42わたしの願(ねが)いをいつも聞(き)いてくださることを、わたしは知(し)っています。しかし、わたしがこう言(い)うのは、周(まわ)りにいる群衆(ぐんしゅう)のためです。あなたがわたしをお遣(つか)わしになったことを、彼(かれ)らに信(しん)じさせるためです。」 43こう言(い)ってから、「ラザロ、出(で)て来(き)なさい」と大声(おおごえ)で叫(さけ)ばれた。 44すると、死(し)んでいた人(ひと)が、手(て)と足(あし)を布(ぬの)で巻(ま)かれたまま出(で)て来(き)た。顔(かお)は覆(おお)いで包(つつ)まれていた。イエスは人々(ひとびと)に、「ほどいてやって、行(い)かせなさい」と言(い)われた。 
 45マリアのところに来(き)て、イエスのなさったことを目撃(もくげき)したユダヤ人(じん)の多(おお)くは、イエスを信(しん)じた。 46しかし、中(なか)には、ファリサイ派(は)の人々(ひとびと)のもとへ行(い)き、イエスのなさったことを告(つ)げる者(もの)もいた。 47そこで、祭司長(さいしちょう)たちとファリサイ派(は)の人々(ひとびと)は最高法院(さいこうほういん)を召集(しょうしゅう)して言(い)った。「この男(おとこ)は多(おお)くのしるしを行(おこな)っているが、どうすればよいか。 48このままにしておけば、皆(みな)が彼(かれ)を信(しん)じるようになる。そして、ローマ人(じん)が来(き)て、我々(われわれ)の神殿(しんでん)も国民(こくみん)も滅(ほろ)ぼしてしまうだろう。」 49彼(かれ)らの中(なか)の一人(ひとり)で、その年(とし)の大祭司(だいさいし)であったカイアファが言(い)った。「あなたがたは何(なに)も分(わ)かっていない。50一人(ひとり)の人間(にんげん)が民(たみ)の代わり(かわり)に死(し)に、国民(こくみん)全体(ぜんたい)が滅(ほろ)びないで済(す)む方(ほう)が、あなたがたに好都合(こうつごう)だとは考(かんが)えないのか。」 51これは、カイアファが自分(じぶん)の考(かんが)えから話(はな)したのではない。その年(とし)の大祭司(だいさいし)であったので預言(よげん)して、イエスが国民(こくみん)のために死(し)ぬ、と言(い)ったのである。 52国民(こくみん)のためばかりでなく、散(ち)らされている神(かみ)の子(こ)たちを一つ(ひとつ)に集(あつ)めるためにも死(し)ぬ、と言(い)ったのである。 53この日(ひ)から、彼(かれ)らはイエスを殺(ころ)そうとたくらんだ。 54それで、イエスはもはや公然(こうぜん)とユダヤ人(じん)たちの間(あいだ)を歩(ある)くことはなく、そこを去(さ)り、荒(あ)れ野(の)に近(ちか)い地方(ちほう)のエフライムという町(まち)に行(い)き、弟子(でし)たちとそこに滞在(たいざい)された。 55さて、ユダヤ人(じん)の過越祭(すぎこしさい)が近(ちか)づいた。多(おお)くの人(ひと)が身(み)を清(きよ)めるために、過越祭(すぎこしさい)の前(まえ)に地方(ちほう)からエルサレムへ上(あ)った。 56彼(かれ)らはイエスを捜(さが)し、神殿(しんでん)の境内(きょうない)で互(たが)いに言(い)った。「どう思(おも)うか。あの人(ひと)はこの祭(まつ)りには来(こ)ないのだろうか。」 57祭司長(さいしちょう)たちとファリサイ派(は)の人々(ひとびと)は、イエスの居(い)どころが分(わ)かれば届(とど)け出(で)よと、命令(めいれい)を出(だ)していた。イエスを逮捕(たいほ)するためである。



1 伯大尼村有個名叫拉撒路的人病倒了。伯大尼是瑪麗亞和她姐姐瑪大居住的村莊。 2 就是這個瑪麗亞後來用香膏抹主，又用自己的頭髮擦乾祂的腳，患病的拉撒路是她的弟弟。 3 她們姊妹兩個託人去告訴耶穌，說：「主啊，你所愛的人病了！」

4 耶穌聽見後，說：「這病不會致命，而是為了上帝的榮耀，使祂的兒子藉此得到榮耀。」 5 耶穌一向愛瑪大、瑪麗亞和拉撒路， 6 可是祂聽到拉撒路有病的消息後，仍逗留了兩天， 7 然後才對門徒說：「我們去猶太吧！」

8 門徒說：「老師，猶太人近來想拿石頭打你，你還要去那裡嗎？」

9 耶穌說：「白天不是有十二個小時嗎？人在白天走路，不會跌倒，因為他看得見這世上的光。 10 人在夜間走路，才會跌倒，因為沒有光。」 11 接著耶穌又說：「我們的朋友拉撒路已經睡了，我去叫醒他。」

12 門徒說：「主啊，如果他睡了，肯定會好的。」 13 其實耶穌是指他已經死了，門徒卻以為他真的睡了。

14 於是，耶穌清楚地對他們說：「拉撒路死了。 15 為了你們的緣故，我很高興自己不在那裡，好叫你們信我。現在我們可以去了。」 16 綽號「雙胞胎」的多馬對其他門徒說：「我們也去，好跟祂一塊兒死吧。」


17 耶穌到了伯大尼，得知拉撒路已經在墳墓裡四天了。 18 伯大尼離耶路撒冷不遠，大約只有三公里的路， 19 很多猶太人來看瑪大和瑪麗亞，為她們兄弟的事來安慰她們。

20 瑪大聽說耶穌來了，就去迎接祂，瑪麗亞卻仍然坐在家裡。 21 瑪大對耶穌說：「主啊，你如果早在這裡，我弟弟就不會死了。 22 就是現在我也知道你無論向上帝求什麼，上帝必定賜給你。」

23 耶穌說：「你弟弟必定復活。」

24 瑪大說：「我知道，在末日復活的時候，他必復活。」

25 耶穌說：「我是復活，我是生命。信我的人雖然死了，也必復活。 26 凡活著信我的人必永遠不死。你相信嗎？」

27 瑪大說：「主啊，我信！我相信你是來到世界的基督，是上帝的兒子。」

28 瑪大說完了，就回去悄悄地告訴她妹妹瑪麗亞：「老師來了，祂叫你去。」

29 瑪麗亞聽了，急忙起來到耶穌那裡。 30 那時，耶穌還沒有進村子，仍在瑪大迎接祂的地方。 31 那些在家裡安慰瑪麗亞的猶太人，見她匆匆忙忙地跑了出去，以為她要去墳墓那裡哭，就跟著出去。

32 瑪麗亞來到耶穌那裡，俯伏在祂腳前說：「主啊，你如果早在這裡，我弟弟就不會死了。」

33 耶穌看見她和陪她來的猶太人都在哭，心中感動，十分難過， 34 便問：「你們把他葬在哪裡了？」

他們答道：「主啊，你來看。」

35 耶穌哭了。

36 猶太人說：「你看！祂多麼愛拉撒路啊！」

37 其中也有人說：「祂既然能醫好瞎眼的人，難道不能叫這個人不死嗎？」

38 耶穌又十分感動地來到墳墓前。那墳墓是個洞，洞口堵著一塊大石頭。

39 耶穌說：「把石頭挪開。」

死者的姐姐瑪大對祂說：「主啊，他死了四天了，已經臭了。」

40 耶穌說：「我不是跟你說過，只要你信，就會看見上帝的榮耀嗎？」

41 於是，他們把石頭挪開，耶穌望著天說：「父啊，我感謝你，因為你已垂聽了我的禱告， 42 我知道你常常垂聽我的禱告。我這樣說是為了周圍站著的眾人，好叫他們相信是你差了我來。」

43 說完，就大聲呼喊：「拉撒路，出來！」 44 那死者就出來了，手腳都纏著布條，臉上也包著布。

耶穌對他們說：「給他解開，讓他走！」


45 許多來看瑪麗亞的猶太人看見耶穌所行的事，就信了祂， 46 但也有些人去見法利賽人，把耶穌所行的事告訴他們。 47 祭司長和法利賽人便召開公會會議，說：「這人行了這麼多神蹟，我們該怎麼辦呢？ 48 如果讓祂這樣繼續下去，所有的人都會信祂，那時羅馬人一定會來奪取我們的土地，擄掠我們的人民。」

49 當年擔任大祭司的該亞法對他們說：「你們什麼都不懂！ 50 你們沒有認識到，祂一個人替眾人死，而不是整個民族滅亡，對你們來說更好。」 51 其實這句話不是出於他自己，只因那年他是大祭司，上帝藉著他預言耶穌將要替猶太民族死。 52 祂不單是要替猶太民族死，也要把散居在各處的上帝的兒女聚集在一起。

53 從那天起，他們就計劃要殺害耶穌， 54 所以耶穌不再公開地在猶太人中間露面。祂離開伯大尼，前往靠近曠野的地方，到了以法蓮城，就和門徒住下來。

55 猶太人的逾越節快到了，有很多人從鄉下上耶路撒冷，預備在過節前潔淨自己。 56 他們四處尋找耶穌，又彼此在聖殿裡談論：「你們怎麼想？祂不會來過節吧？」 57 當時祭司長和法利賽人早已下令，如果有人知道耶穌在哪裡，就來報告，他們好去抓祂。

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