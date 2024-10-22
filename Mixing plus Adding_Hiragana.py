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

1さて、イエスは通(とお)りすがりに、生(う)まれつき目(め)の見(み)えない人(ひと)を見(み)かけられた。 2弟子(でし)たちがイエスに尋(たず)ねた。「ラビ、この人(ひと)が生(う)まれつき目(め)が見(み)えないのは、だれが罪(つみ)を犯(おか)したからですか。本人(ほんにん)ですか。それとも、両親(りょうしん)ですか。」 3イエスはお答(こた)えになった。「本人(ほんにん)が罪(つみ)を犯(おか)したからでも、両親(りょうしん)が罪(つみ)を犯(おか)したからでもない。神(かみ)の業(わざ)がこの人(ひと)に現(あらわ)れるためである。 4わたしたちは、わたしをお遣(つか)わしになった方(かた)の業(わざ)を、まだ日(ひ)のあるうちに行(おこな)わねばならない。だれも働(はたら)くことのできない夜(よる)が来(く)る。 5わたしは、世(よ)にいる間(あいだ)、世(よ)の光(ひかり)である。」 6こう言(い)ってから、イエスは地面(じめん)に唾(つば)をし、唾(つば)で土(つち)をこねてその人(ひと)の目(め)にお塗(ぬ)りになった。 7そして、「シロアム――『遣(つか)わされた者(もの)』という意味(いみ)――の池(いけ)に行(い)って洗(あら)いなさい」と言(い)われた。そこで、彼(かれ)は行(い)って洗(あら)い、目(め)が見(み)えるようになって、帰(かえ)って来(き)た。 8近所(きんじょ)の人々(ひとびと)や、彼(かれ)が物乞(ものご)いをしていたのを前(まえ)に見(み)ていた人々(ひとびと)が、「これは、座(すわ)って物乞(ものご)いをしていた人(ひと)ではないか」と言(い)った。 9「その人(ひと)だ」と言(い)う者(もの)もいれば、「いや違(ちが)う。似(に)ているだけだ」と言(い)う者(もの)もいた。本人(ほんにん)は、「わたしがそうなのです」と言(い)った。 10そこで人々(ひとびと)が、「では、お前(まえ)の目(め)はどのようにして開(ひら)いたのか」と言(い)うと、 11彼(かれ)は答(こた)えた。「イエスという方(かた)が、土(つち)をこねてわたしの目(め)に塗(ぬ)り、『シロアムに行(い)って洗(あら)いなさい』と言(い)われました。そこで、行(い)って洗(あら)ったら、見(み)えるようになったのです。」 12人々(ひとびと)が「その人(ひと)はどこにいるのか」と言(い)うと、彼(かれ)は「知(し)りません」と言(い)った。
13人々(ひとびと)は、前(まえ)に盲人(もうじん)であった人(ひと)をファリサイ派(は)の人々(ひとびと)のところへ連(つ)れて行(い)った。 14イエスが土(つち)をこねてその目(め)を開(あ)けられたのは、安息(あんそくび)のことであった。 15そこで、ファリサイ派(は)の人々(ひとびと)も、どうして見(み)えるようになったのかと尋(たず)ねた。彼(かれ)は言(い)った。「あの方(かた)が、わたしの目(め)にこねた土(つち)を塗(ぬ)りました。そして、わたしが洗(あら)うと、見(み)えるようになったのです。」 16ファリサイ派(は)の人々(ひとびと)の中(なか)には、「その人(ひと)は、安息(あんそくび)を守(まも)らないから、神(かみ)のもとから来(き)た者(もの)ではない」と言(い)う者(もの)もいれば、「どうして罪(つみ)のある人間(にんげん)が、こんなしるしを行(おこな)うことができるだろうか」と言(い)う者(もの)もいた。こうして、彼(かれ)らの間(あいだ)で意見(いけん)が分(わ)かれた。 17そこで、人々(ひとびと)は盲人(もうじん)であった人(ひと)に再(ふたた)び言(い)った。「目(め)を開(あ)けてくれたということだが、いったい、お前(まえ)はあの人(ひと)をどう思(おも)うのか。」彼(かれ)は「あの方(かた)は預言者(よげんしゃ)です」と言(い)った。
18それでも、ユダヤ(ゆだや)人(じん)たちはこの人(ひと)について、盲人(もうじん)であったのに目(め)が見(み)えるようになったということを信(しん)じなかった。ついに、目(め)が見(み)えるようになった人(ひと)の両親(りょうしん)を呼(よ)び出(だ)して、 19尋(たず)ねた。「この者(もの)はあなたたちの息子(むすこ)で、生(う)まれつき目(め)が見(み)えなかったと言(い)うのか。それが、どうして今(いま)は目(め)が見(み)えるのか。」 20両親(りょうしん)は答(こた)えて言(い)った。「これがわたしどもの息子(むすこ)で、生(う)まれつき目(め)が見(み)えなかったことは知(し)っています。 21しかし、どうして今(いま)、目(め)が見(み)えるようになったかは、分(わ)かりません。だれが目(め)を開(あ)けてくれたのかも、わたしどもは分(わ)かりません。本人(ほんにん)にお聞(き)きください。もう大人(おとな)ですから、自分(じぶん)のことは自分(じぶん)で話(はな)すでしょう。」 22両親(りょうしん)がこう言(い)ったのは、ユダヤ(ゆだや)人(じん)たちを恐(おそ)れていたからである。ユダヤ(ゆだや)人(じん)たちは既(すで)に、イエスをメシアであると公(おおやけ)に言(い)い表(あらわ)す者(もの)がいれば、会堂(かいどう)から追放(ついほう)すると決(き)めていたのである。 23両親(りょうしん)が、「もう大人(おとな)ですから、本人(ほんにん)にお聞(き)きください」と言(い)ったのは、そのためである。
24さて、ユダヤ(ゆだや)人(じん)たちは、盲人(もうじん)であった人(ひと)をもう一度(いちど)呼(よ)び出(だ)して言(い)った。「神(かみ)の前(まえ)で正直(しょうじき)に答(こた)えなさい。わたしたちは、あの者(もの)が罪(つみ)ある人間(にんげん)だと知(し)っているのだ。」 25彼(かれ)は答(こた)えた。「あの方(かた)が罪人(つみびと)かどうか、わたしには分(わ)かりません。ただ一(ひと)つ知(し)っているのは、目(め)の見(み)えなかったわたしが、今(いま)は見(み)えるということです。」 26すると、彼(かれ)らは言(い)った。「あの者(もの)はお前(まえ)にどんなことをしたのか。お前(まえ)の目(め)をどうやって開(あ)けたのか。」 27彼(かれ)は答(こた)えた。「もうお話(はな)ししたのに、聞(き)いてくださいませんでした。なぜまた、聞(き)こうとなさるのですか。あなたがたもあの方(かた)の弟子(でし)になりたいのですか。」 28そこで、彼(かれ)らはののしって言(い)った。「お前(まえ)はあの者(もの)の弟子(でし)だが、我々(われわれ)はモーセの弟子(でし)だ。 29我々(われわれ)は、神(かみ)がモーセに語(かた)られたことは知(し)っているが、あの者(もの)がどこから来(き)たのかは知(し)らない。」 30彼(かれ)は答(こた)えて言(い)った。「あの方(かた)がどこから来(こ)られたか、あなたがたがご存(ぞん)じないとは、実(じつ)に不思議(ふしぎ)です。あの方(かた)は、わたしの目(め)を開(あ)けてくださったのに。 31神(かみ)は罪人(ざいにん)の言(い)うことはお聞(き)きにならないと、わたしたちは承知(しょうち)しています。しかし、神(かみ)をあがめ、その御心(みこころ)を行(おこな)う人(ひと)の言(い)うことは、お聞(き)きになります。 32生(う)まれつき目(め)が見(み)えなかった者(もの)の目(め)を開(あ)けた人(ひと)がいるということなど、これまで一度(いちど)も聞(き)いたことがありません。 33あの方(かた)が神(かみ)のもとから来(こ)られたのでなければ、何(なに)もおできにならなかったはずです。」 34彼(かれ)らは、「お前(まえ)は全(まった)く罪(つみ)の中(なか)に生(う)まれたのに、我々(われわれ)に教(おし)えようというのか」と言(い)い返(かえ)し、彼(かれ)を外(そと)に追(お)い出(だ)した。
35イエスは彼(かれ)が外(そと)に追(お)い出(だ)されたことをお聞(き)きになった。そして彼(かれ)に出会(であ)うと、「あなたは人(ひと)の子(こ)を信(しん)じるか」と言(い)われた。 36彼(かれ)は答(こた)えて言(い)った。「主(しゅ)よ、その方(かた)はどんな人(ひと)ですか。その方(かた)を信(しん)じたいのですが。」 37イエスは言(い)われた。「あなたは、もうその人(ひと)を見(み)ている。あなたと話(はな)しているのが、その人(ひと)だ。」 38彼(かれ)が、「主(しゅ)よ、信(しん)じます」と言(い)って、ひざまずくと、 39イエスは言(い)われた。「わたしがこの世(よ)に来(き)たのは、裁(さば)くためである。こうして、見(み)えない者(もの)は見(み)えるようになり、見(み)える者(もの)は見(み)えないようになる。」
40イエスと一緒(いっしょ)に居合(いあ)わせたファリサイ派(は)の人々(ひとびと)は、これらのことを聞(き)いて、「我々(われわれ)も見(み)えないということか」と言(い)った。 41イエスは言(い)われた。「見(み)えなかったのであれば、罪(つみ)はなかったであろう。しかし、今(いま)、『見(み)える』とあなたたちは言(い)っている。だから、あなたたちの罪(つみ)は残(のこ)る。」




1 Now as Jesus passed by, He saw a man who was blind from birth. 2 And His disciples asked Him, saying, “Rabbi, who sinned, this man or his parents, that he was born blind?”

3 Jesus answered, “Neither this man nor his parents sinned, but that the works of God should be revealed in him. 4 I[a] must work the works of Him who sent Me while it is day; the night is coming when no one can work. 5 As long as I am in the world, I am the light of the world.”

6 When He had said these things, He spat on the ground and made clay with the saliva; and He anointed the eyes of the blind man with the clay. 7 And He said to him, “Go, wash in the pool of Siloam” (which is translated, Sent). So he went and washed, and came back seeing.

8 Therefore the neighbors and those who previously had seen that he was [b]blind said, “Is not this he who sat and begged?”

9 Some said, “This is he.” Others said, [c]“He is like him.”

He said, “I am he.”

10 Therefore they said to him, “How were your eyes opened?”

11 He answered and said, “A Man called Jesus made clay and anointed my eyes and said to me, ‘Go to [d]the pool of Siloam and wash.’ So I went and washed, and I received sight.”

12 Then they said to him, “Where is He?”

He said, “I do not know.”


13 They brought him who formerly was blind to the Pharisees. 14 Now it was a Sabbath when Jesus made the clay and opened his eyes. 15 Then the Pharisees also asked him again how he had received his sight. He said to them, “He put clay on my eyes, and I washed, and I see.”

16 Therefore some of the Pharisees said, “This Man is not from God, because He does not [e]keep the Sabbath.”

Others said, “How can a man who is a sinner do such signs?” And there was a division among them.

17 They said to the blind man again, “What do you say about Him because He opened your eyes?”

He said, “He is a prophet.”

18 But the Jews did not believe concerning him, that he had been blind and received his sight, until they called the parents of him who had received his sight. 19 And they asked them, saying, “Is this your son, who you say was born blind? How then does he now see?”

20 His parents answered them and said, “We know that this is our son, and that he was born blind; 21 but by what means he now sees we do not know, or who opened his eyes we do not know. He is of age; ask him. He will speak for himself.” 22 His parents said these things because they feared the Jews, for the Jews had agreed already that if anyone confessed that He was Christ, he would be put out of the synagogue. 23 Therefore his parents said, “He is of age; ask him.”

24 So they again called the man who was blind, and said to him, “Give God the glory! We know that this Man is a sinner.”

25 He answered and said, “Whether He is a sinner or not I do not know. One thing I know: that though I was blind, now I see.”

26 Then they said to him again, “What did He do to you? How did He open your eyes?”

27 He answered them, “I told you already, and you did not listen. Why do you want to hear it again? Do you also want to become His disciples?”

28 Then they reviled him and said, “You are His disciple, but we are Moses’ disciples. 29 We know that God spoke to Moses; as for this fellow, we do not know where He is from.”

30 The man answered and said to them, “Why, this is a marvelous thing, that you do not know where He is from; yet He has opened my eyes! 31 Now we know that God does not hear sinners; but if anyone is a worshiper of God and does His will, He hears him. 32 Since the world began it has been unheard of that anyone opened the eyes of one who was born blind. 33 If this Man were not from God, He could do nothing.”

34 They answered and said to him, “You were completely born in sins, and are you teaching us?” And they [f]cast him out.

35 Jesus heard that they had cast him out; and when He had found him, He said to him, “Do you believe in the Son of [g]God?”

36 He answered and said, “Who is He, Lord, that I may believe in Him?”

37 And Jesus said to him, “You have both seen Him and it is He who is talking with you.”

38 Then he said, “Lord, I believe!” And he worshiped Him.

39 And Jesus said, “For judgment I have come into this world, that those who do not see may see, and that those who see may be made blind.”

40 Then some of the Pharisees who were with Him heard these words, and said to Him, “Are we blind also?”

41 Jesus said to them, “If you were blind, you would have no sin; but now you say, ‘We see.’ Therefore your sin remains.



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