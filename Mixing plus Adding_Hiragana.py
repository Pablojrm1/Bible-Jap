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

1 Now a certain man was sick, Lazarus of Bethany, the town of Mary and her sister Martha. 2 It was that Mary who anointed the Lord with fragrant oil and wiped His feet with her hair, whose brother Lazarus was sick. 3 Therefore the sisters sent to Him, saying, “Lord, behold, he whom You love is sick.”

4 When Jesus heard that, He said, “This sickness is not unto death, but for the glory of God, that the Son of God may be glorified through it.”

5 Now Jesus loved Martha and her sister and Lazarus. 6 So, when He heard that he was sick, He stayed two more days in the place where He was. 7 Then after this He said to the disciples, “Let us go to Judea again.”

8 The disciples said to Him, “Rabbi, lately the Jews sought to stone You, and are You going there again?”

9 Jesus answered, “Are there not twelve hours in the day? If anyone walks in the day, he does not stumble, because he sees the light of this world. 10 But if one walks in the night, he stumbles, because the light is not in him.” 11 These things He said, and after that He said to them, “Our friend Lazarus sleeps, but I go that I may wake him up.”

12 Then His disciples said, “Lord, if he sleeps he will get well.” 13 However, Jesus spoke of his death, but they thought that He was speaking about taking rest in sleep.

14 Then Jesus said to them plainly, “Lazarus is dead. 15 And I am glad for your sakes that I was not there, that you may believe. Nevertheless let us go to him.”

16 Then Thomas, who is called the Twin, said to his fellow disciples, “Let us also go, that we may die with Him.”


17 So when Jesus came, He found that he had already been in the tomb four days. 18 Now Bethany was near Jerusalem, about [a]two miles away. 19 And many of the Jews had joined the women around Martha and Mary, to comfort them concerning their brother.

20 Then Martha, as soon as she heard that Jesus was coming, went and met Him, but Mary was sitting in the house. 21 Now Martha said to Jesus, “Lord, if You had been here, my brother would not have died. 22 But even now I know that whatever You ask of God, God will give You.”

23 Jesus said to her, “Your brother will rise again.”

24 Martha said to Him, “I know that he will rise again in the resurrection at the last day.”

25 Jesus said to her, “I am the resurrection and the life. He who believes in Me, though he may die, he shall live. 26 And whoever lives and believes in Me shall never die. Do you believe this?”

27 She said to Him, “Yes, Lord, I believe that You are the Christ, the Son of God, who is to come into the world.”


28 And when she had said these things, she went her way and secretly called Mary her sister, saying, “The Teacher has come and is calling for you.” 29 As soon as she heard that, she arose quickly and came to Him. 30 Now Jesus had not yet come into the town, but [b]was in the place where Martha met Him. 31 Then the Jews who were with her in the house, and comforting her, when they saw that Mary rose up quickly and went out, followed her, [c]saying, “She is going to the tomb to weep there.”

32 Then, when Mary came where Jesus was, and saw Him, she fell down at His feet, saying to Him, “Lord, if You had been here, my brother would not have died.”

33 Therefore, when Jesus saw her weeping, and the Jews who came with her weeping, He groaned in the spirit and was troubled. 34 And He said, “Where have you laid him?”

They said to Him, “Lord, come and see.”

35 Jesus wept. 36 Then the Jews said, “See how He loved him!”

37 And some of them said, “Could not this Man, who opened the eyes of the blind, also have kept this man from dying?”


38 Then Jesus, again groaning in Himself, came to the tomb. It was a cave, and a stone lay against it. 39 Jesus said, “Take away the stone.”

Martha, the sister of him who was dead, said to Him, “Lord, by this time there is a stench, for he has been dead four days.”

40 Jesus said to her, “Did I not say to you that if you would believe you would see the glory of God?” 41 Then they took away the stone [d]from the place where the dead man was lying. And Jesus lifted up His eyes and said, “Father, I thank You that You have heard Me. 42 And I know that You always hear Me, but because of the people who are standing by I said this, that they may believe that You sent Me.” 43 Now when He had said these things, He cried with a loud voice, “Lazarus, come forth!” 44 And he who had died came out bound hand and foot with graveclothes, and his face was wrapped with a cloth. Jesus said to them, “Loose him, and let him go.”


45 Then many of the Jews who had come to Mary, and had seen the things Jesus did, believed in Him. 46 But some of them went away to the Pharisees and told them the things Jesus did. 47 Then the chief priests and the Pharisees gathered a council and said, “What shall we do? For this Man works many signs. 48 If we let Him alone like this, everyone will believe in Him, and the Romans will come and take away both our place and nation.”

49 And one of them, Caiaphas, being high priest that year, said to them, “You know nothing at all, 50 nor do you consider that it is expedient for [e]us that one man should die for the people, and not that the whole nation should perish.” 51 Now this he did not say on his own authority; but being high priest that year he prophesied that Jesus would die for the nation, 52 and not for that nation only, but also that He would gather together in one the children of God who were scattered abroad.

53 Then, from that day on, they plotted to put Him to death. 54 Therefore Jesus no longer walked openly among the Jews, but went from there into the country near the wilderness, to a city called Ephraim, and there remained with His disciples.

55 And the Passover of the Jews was near, and many went from the country up to Jerusalem before the Passover, to purify themselves. 56 Then they sought Jesus, and spoke among themselves as they stood in the temple, “What do you think—that He will not come to the feast?” 57 Now both the chief priests and the Pharisees had given a command, that if anyone knew where He was, he should report it, that they might seize Him.


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