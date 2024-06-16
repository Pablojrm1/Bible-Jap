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
1イエスはオリーブ山(やま)へ行(い)かれた。 2朝早(あさはや)く、再(ふたた)び神殿(しんでん)の境内(けいだい)に入(はい)られると、民衆(みんしゅう)が皆(みな)、御自分(ごじぶん)のところにやって来(き)たので、座(すわ)って教(おし)え始(はじ)められた。 3そこへ、律法(りっぽう)学者(がくしゃ)たちやファリサイ派(は)の人々(ひとびと)が、姦通(かんつう)の現場(げんば)で捕(と)らえられた女(おんな)を連(つ)れて来(き)て、真(ま)ん中(なか)に立(た)たせ、 4イエスに言(い)った。「先生(せんせい)、この女(おんな)は姦通(かんつう)をしているときに捕(つか)まりました。 5こういう女(おんな)は石(いし)で打(う)ち殺(ころ)せと、モーセは律法(りっぽう)の中(なか)で命(めい)じています。ところで、あなたはどうお考(かんが)えになりますか。」 6イエスを試(ため)して、訴(うった)える口実(こうじつ)を得(え)るために、こう言(い)ったのである。イエスはかがみ込(こ)み、指(ゆび)で地面(じめん)に何(なに)か書(か)き始(はじ)められた。 7しかし、彼(かれ)らがしつこく問(と)い続(つづ)けるので、イエスは身(み)を起(お)こして言(い)われた。「あなたたちの中(なか)で罪(つみ)を犯(おか)したことのない者(もの)が、まず、この女(おんな)に石(いし)を投(な)げなさい。」 8そしてまた、身(み)をかがめて地面(じめん)に書(か)き続(つづ)けられた。 9これを聞(き)いた者(もの)は、年長者(ねんちょうしゃ)から始(はじ)まって、一人(ひとり)また一人(ひとり)と、立(た)ち去(さ)ってしまい、イエスひとりと、真(ま)ん中(なか)にいた女(おんな)が残(のこ)った。 10イエスは、身(み)を起(お)こして言(い)われた。「婦人(ふじん)よ、あの人(ひと)たちはどこにいるのか。だれもあなたを罪(つみ)に定(さだ)めなかったのか。」 11女(おんな)が、「主(しゅ)よ、だれも」と言(い)うと、イエスは言(い)われた。「わたしもあなたを罪(つみ)に定(さだ)めない。行(い)きなさい。これからは、もう罪(つみ)を犯(おか)してはならない。」〕
12イエスは再(ふたた)び言(い)われた。「わたしは世(よ)の光(ひかり)である。わたしに従(したが)う者(もの)は暗闇(くらやみ)の中(なか)を歩(ある)かず、命(いのち)の光(ひかり)を持(も)つ。」 13それで、ファリサイ派(は)の人々(ひとびと)が言(い)った。「あなたは自分(じぶん)について証(あか)しをしている。その証(あか)しは真実(しんじつ)ではない。」 14イエスは答(こた)えて言(い)われた。「たとえわたしが自分(じぶん)について証(あか)しをするとしても、その証(あか)しは真実(しんじつ)である。自分(じぶん)がどこから来(き)たのか、そしてどこへ行(い)くのか、わたしは知(し)っているからだ。しかし、あなたたちは、わたしがどこから来(き)てどこへ行(い)くのか、知(し)らない。 15あなたたちは肉(にく)に従(したが)って裁(さば)くが、わたしはだれをも裁(さば)かない。 16しかし、もしわたしが裁(さば)くとすれば、わたしの裁(さば)きは真実(しんじつ)である。なぜならわたしはひとりではなく、わたしをお遣(つか)わしになった父(ちち)と共(とも)にいるからである。 17あなたたちの律法(りっぽう)には、二人(ふたり)が行(おこな)う証(あか)しは真実(しんじつ)であると書(か)いてある。 18わたしは自分(じぶん)について証(あか)しをしており、わたしをお遣(つか)わしになった父(ちち)もわたしについて証(あか)しをしてくださる。」 19彼(かれ)らが「あなたの父(ちち)はどこにいるのか」と言(い)うと、イエスはお答(こた)えになった。「あなたたちは、わたしもわたしの父(ちち)も知(し)らない。もし、わたしを知(し)っていたら、わたしの父(ちち)をも知(し)るはずだ。」 20イエスは神殿(しんでん)の境内(けいだい)で教(おし)えておられたとき、宝物殿(ほうもつでん)の近(ちか)くでこれらのことを話(はな)された。しかし、だれもイエスを捕(と)らえなかった。イエスの時(とき)がまだ来(き)ていなかったからである。
21そこで、イエスはまた言(い)われた。「わたしは去(さ)って行(い)く。あなたたちはわたしを捜(さが)すだろう。だが、あなたたちは自分(じぶん)の罪(つみ)のうちに死(し)ぬことになる。わたしの行(い)く所(ところ)に、あなたたちは来(く)ることができない。」 22ユダヤ人(じん)たちが、「『わたしの行(い)く所(ところ)に、あなたたちは来(く)ることができない』と言(い)っているが、自殺(じさつ)でもするつもりなのだろうか」と話(はな)していると、 23イエスは彼(かれ)らに言(い)われた。「あなたたちは下(した)のものに属(ぞく)しているが、わたしは上(うえ)のものに属(ぞく)している。あなたたちはこの世(よ)に属(ぞく)しているが、わたしはこの世(よ)に属(ぞく)していない。 24だから、あなたたちは自分(じぶん)の罪(つみ)のうちに死(し)ぬことになると、わたしは言(い)ったのである。『わたしはある』ということを信(しん)じないならば、あなたたちは自分(じぶん)の罪(つみ)のうちに死(し)ぬことになる。」 25彼(かれ)らが、「あなたは、いったい、どなたですか」と言(い)うと、イエスは言(い)われた。「それは初(はじ)めから話(はな)しているではないか。 26あなたたちについては、言(い)うべきこと、裁(さば)くべきことがたくさんある。しかし、わたしをお遣(つか)わしになった方(かた)は真実(しんじつ)であり、わたしはその方(かた)から聞(き)いたことを、世(よ)に向(む)かって話(はな)している。」 27彼(かれ)らは、イエスが御父(おんちち)について話(はな)しておられることを悟(さと)らなかった。 28そこで、イエスは言(い)われた。「あなたたちは、人(ひと)の子(こ)を上(あ)げたときに初(はじ)めて、『わたしはある』ということ、また、わたしが、自分勝手(じぶんかって)には何(なに)もせず、ただ、父(ちち)に教(おし)えられたとおりに話(はな)していることが分(わ)かるだろう。 29わたしをお遣(つか)わしになった方(かた)は、わたしと共(とも)にいてくださる。わたしをひとりにしてはおかれない。わたしは、いつもこの方(かた)の御心(みこころ)に適(かな)うことを行(おこな)うからである。」 30これらのことを語(かた)られたとき、多(おお)くの人々(ひとびと)がイエスを信(しん)じた。
31イエスは、御自分(ごじぶん)を信(しん)じたユダヤ人(じん)たちに言(い)われた。「わたしの言葉(ことば)にとどまるならば、あなたたちは本当(ほんとう)にわたしの弟子(でし)である。 32あなたたちは真(しん)理(り)を知(し)り、真理(しんり)はあなたたちを自由(じゆう)にする。」 33すると、彼(かれ)らは言(い)った。「わたしたちはアブラハムの子孫(しそん)です。今(いま)までだれかの奴隷(どれい)になったことはありません。『あなたたちは自由(じゆう)になる』とどうして言(い)われるのですか。」 34イエスはお答(こた)えになった。「はっきり言(い)っておく。罪(つみ)を犯(おか)す者(もの)はだれでも罪(つみ)の奴隷(どれい)である。 35奴隷(どれい)は家(いえ)にいつまでもいるわけにはいかないが、子(こ)はいつまでもいる。 36だから、もし子(こ)があなたたちを自由(じゆう)にすれば、あなたたちは本当(ほんとう)に自由(じゆう)になる。 37あなたたちがアブラハムの子孫(しそん)だということは、分(わ)かっている。だが、あなたたちはわたしを殺(ころ)そうとしている。わたしの言葉(ことば)を受(う)け入(い)れないからである。 38わたしは父(ちち)のもとで見(み)たことを話(はな)している。ところが、あなたたちは父(ちち)から聞(き)いたことを行(おこな)っている。」
39彼(かれ)らが答(こた)えて、「わたしたちの父(ちち)はアブラハムです」と言(い)うと、イエスは言(い)われた。「アブラハムの子(こ)なら、アブラハムと同(おな)じ業(わざ)をするはずだ。 40ところが、今(いま)、あなたたちは、神(かみ)から聞(き)いた真理(しんり)をあなたたちに語(かた)っているこのわたしを、殺(ころ)そうとしている。アブラハムはそんなことはしなかった。 41あなたたちは、自分(じぶん)の父(ちち)と同(おな)じ業(わざ)をしている。」そこで彼(かれ)らが、「わたしたちは姦淫(かんいん)によって生(う)まれたのではありません。わたしたちにはただひとりの父(ちち)がいます。それは神(かみ)です」と言(い)うと、 42イエスは言(い)われた。「神(かみ)があなたたちの父(ちち)であれば、あなたたちはわたしを愛(あい)するはずである。なぜなら、わたしは神(かみ)のもとから来(き)て、ここにいるからだ。わたしは自分勝手(じぶんかって)に来(き)たのではなく、神(かみ)がわたしをお遣(つか)わしになったのである。 43わたしの言(い)っていることが、なぜ分(わ)からないのか。それは、わたしの言葉(ことば)を聞(き)くことができないからだ。 44あなたたちは、悪魔(あくま)である父(ちち)から出(で)た者(もの)であって、その父(ちち)の欲望(よくぼう)を満(み)たしたいと思(おも)っている。悪魔(あくま)は最初(さいしょ)から人殺(ひとごろ)しであって、真理(しんり)をよりどころとしていない。彼(かれ)の内(うち)には真理(しんり)がないからだ。悪魔(あくま)が偽(いつわ)りを言(い)うときは、その本性(ほんせい)から言(い)っている。自分(じぶん)が偽(いつわ)り者(もの)であり、その父(ちち)だからである。 45しかし、わたしが真理(しんり)を語(かた)るから、あなたたちはわたしを信(しん)じない。 46あなたたちのうち、いったいだれが、わたしに罪(つみ)があると責(せ)めることができるのか。わたしは真理(しんり)を語(かた)っているのに、なぜわたしを信(しん)じないのか。 47神(かみ)に属(ぞく)する者(もの)は神(かみ)の言葉(ことば)を聞(き)く。あなたたちが聞(き)かないのは神(かみ)に属(ぞく)していないからである。」
48ユダヤ人(じん)たちが、「あなたはサマリア人(じん)で悪霊(あくれい)に取(と)りつかれていると、我々(われわれ)が言(い)うのも当然(とうぜん)ではないか」と言(い)い返(かえ)すと、 49イエスはお答(こた)えになった。「わたしは悪霊(あくれい)に取(と)りつかれてはいない。わたしは父(ちち)を重(おも)んじているのに、あなたたちはわたしを重(おも)んじない。 50わたしは、自分(じぶん)の栄光(えいこう)は求(もと)めていない。わたしの栄光(えいこう)を求(もと)め、裁(さば)きをなさる方(かた)が、ほかにおられる。 51はっきり言(い)っておく。わたしの言葉(ことば)を守(まも)るなら、その人(ひと)は決(けっ)して死(し)ぬことがない。」 52ユダヤ人(じん)たちは言(い)った。「あなたが悪霊(あくれい)に取(と)りつかれていることが、今(いま)はっきりした。アブラハムは死(し)んだし、預言者(よげんしゃ)たちも死(し)んだ。ところが、あなたは、『わたしの言葉(ことば)を守(まも)るなら、その人(ひと)は決(けっ)して死(し)を味(あじ)わうことがない』と言(い)う。 53わたしたちの父(ちち)アブラハムよりも、あなたは偉大(いだい)なのか。彼(かれ)は死(し)んだではないか。預言者(よげんしゃ)たちも死(し)んだ。いったい、あなたは自分(じぶん)を何者(なにもの)だと思(おも)っているのか。」 54イエスはお答(こた)えになった。「わたしが自分(じぶん)自身(じしん)のために栄光(えいこう)を求(もと)めようとしているのであれば、わたしの栄光(えいこう)はむなしい。わたしに栄光(えいこう)を与(あた)えてくださるのはわたしの父(ちち)であって、あなたたちはこの方(かた)について、『我々(われわれ)の神(かみ)だ』と言(い)っている。 55あなたたちはその方(かた)を知(し)らないが、わたしは知(し)っている。わたしがその方(かた)を知(し)らないと言(い)えば、あなたたちと同(おな)じくわたしも偽(いつわ)り者(もの)になる。しかし、わたしはその方(かた)を知(し)っており、その言葉(ことば)を守(まも)っている。 56あなたたちの父(ちち)アブラハムは、わたしの日(ひ)を見(み)るのを楽(たの)しみにしていた。そして、それを見(み)て、喜(よろこ)んだのである。」 57ユダヤ人(じん)たちが、「あなたは、まだ五十歳(さい)にもならないのに、アブラハムを見(み)たのか」と言(い)うと、 58イエスは言(い)われた。「はっきり言(い)っておく。アブラハムが生(う)まれる前(まえ)から、『わたしはある。』」 59すると、ユダヤ人(じん)たちは、石(いし)を取(と)り上(あ)げ、イエスに投(な)げつけようとした。しかし、イエスは身(み)を隠(かく)して、神殿(しんでん)の境内(けいだい)から出(で)て行(い)かれた。

1 But Jesus went to the Mount of Olives.

2 Now [a]early in the morning He came again into the temple, and all the people came to Him; and He sat down and taught them. 3 Then the scribes and Pharisees brought to Him a woman caught in adultery. And when they had set her in the midst, 4 they said to Him, “Teacher, [b]this woman was caught in adultery, in the very act. 5 Now [c]Moses, in the law, commanded us [d]that such should be stoned. But what do You [e]say?” 6 This they said, testing Him, that they might have something of which to accuse Him. But Jesus stooped down and wrote on the ground with His finger, [f]as though He did not hear.

7 So when they continued asking Him, He [g]raised Himself up and said to them, “He who is without sin among you, let him throw a stone at her first.” 8 And again He stooped down and wrote on the ground. 9 Then those who heard it, being[h] convicted by their conscience, went out one by one, beginning with the oldest even to the last. And Jesus was left alone, and the woman standing in the midst. 10 When Jesus had raised Himself up [i]and saw no one but the woman, He said to her, “Woman, where are those accusers [j]of yours? Has no one condemned you?”

11 She said, “No one, Lord.”

And Jesus said to her, “Neither do I condemn you; go [k]and sin no more.”

12 Then Jesus spoke to them again, saying, “I am the light of the world. He who follows Me shall not walk in darkness, but have the light of life.”

13 The Pharisees therefore said to Him, “You bear witness of Yourself; Your witness is not [l]true.”

14 Jesus answered and said to them, “Even if I bear witness of Myself, My witness is true, for I know where I came from and where I am going; but you do not know where I come from and where I am going. 15 You judge according to the flesh; I judge no one. 16 And yet if I do judge, My judgment is true; for I am not alone, but I am with the Father who sent Me. 17 It is also written in your law that the testimony of two men is true. 18 I am One who bears witness of Myself, and the Father who sent Me bears witness of Me.”

19 Then they said to Him, “Where is Your Father?”

Jesus answered, “You know neither Me nor My Father. If you had known Me, you would have known My Father also.”

20 These words Jesus spoke in the treasury, as He taught in the temple; and no one laid hands on Him, for His hour had not yet come.

21 Then Jesus said to them again, “I am going away, and you will seek Me, and will die in your sin. Where I go you cannot come.”

22 So the Jews said, “Will He kill Himself, because He says, ‘Where I go you cannot come’?”

23 And He said to them, “You are from beneath; I am from above. You are of this world; I am not of this world. 24 Therefore I said to you that you will die in your sins; for if you do not believe that I am He, you will die in your sins.”

25 Then they said to Him, “Who are You?”

And Jesus said to them, “Just what I have been saying to you from the beginning. 26 I have many things to say and to judge concerning you, but He who sent Me is true; and I speak to the world those things which I heard from Him.”

27 They did not understand that He spoke to them of the Father.

28 Then Jesus said to them, “When you lift[m] up the Son of Man, then you will know that I am He, and that I do nothing of Myself; but as My Father taught Me, I speak these things. 29 And He who sent Me is with Me. The Father has not left Me alone, for I always do those things that please Him.” 30 As He spoke these words, many believed in Him.

31 Then Jesus said to those Jews who believed Him, “If you abide in My word, you are My disciples indeed. 32 And you shall know the truth, and the truth shall make you free.”

33 They answered Him, “We are Abraham’s descendants, and have never been in bondage to anyone. How can You say, ‘You will be made free’?”

34 Jesus answered them, “Most assuredly, I say to you, whoever commits sin is a slave of sin. 35 And a slave does not abide in the house forever, but a son abides forever. 36 Therefore if the Son makes you free, you shall be free indeed.

37 “I know that you are Abraham’s descendants, but you seek to kill Me, because My word has no place in you. 38 I speak what I have seen with My Father, and you do what you have [n]seen with your father.”

39 They answered and said to Him, “Abraham is our father.”

Jesus said to them, “If you were Abraham’s children, you would do the works of Abraham. 40 But now you seek to kill Me, a Man who has told you the truth which I heard from God. Abraham did not do this. 41 You do the deeds of your father.”

Then they said to Him, “We were not born of fornication; we have one Father—God.”

42 Jesus said to them, “If God were your Father, you would love Me, for I proceeded forth and came from God; nor have I come of Myself, but He sent Me. 43 Why do you not understand My speech? Because you are not able to listen to My word. 44 You are of your father the devil, and the desires of your father you want to do. He was a murderer from the beginning, and does not stand in the truth, because there is no truth in him. When he speaks a lie, he speaks from his own resources, for he is a liar and the father of it. 45 But because I tell the truth, you do not believe Me. 46 Which of you convicts Me of sin? And if I tell the truth, why do you not believe Me? 47 He who is of God hears God’s words; therefore you do not hear, because you are not of God.”

48 Then the Jews answered and said to Him, “Do we not say rightly that You are a Samaritan and have a demon?”

49 Jesus answered, “I do not have a demon; but I honor My Father, and you dishonor Me. 50 And I do not seek My own glory; there is One who seeks and judges. 51 Most assuredly, I say to you, if anyone keeps My word he shall never see death.”

52 Then the Jews said to Him, “Now we know that You have a demon! Abraham is dead, and the prophets; and You say, ‘If anyone keeps My word he shall never taste death.’ 53 Are You greater than our father Abraham, who is dead? And the prophets are dead. Who do You make Yourself out to be?”

54 Jesus answered, “If I honor Myself, My honor is nothing. It is My Father who honors Me, of whom you say that He is [o]your God. 55 Yet you have not known Him, but I know Him. And if I say, ‘I do not know Him,’ I shall be a liar like you; but I do know Him and keep His word. 56 Your father Abraham rejoiced to see My day, and he saw it and was glad.”

57 Then the Jews said to Him, “You are not yet fifty years old, and have You seen Abraham?”

58 Jesus said to them, “Most assuredly, I say to you, before Abraham was, I AM.”

59 Then they took up stones to throw at Him; but Jesus hid Himself and went out of the temple, going[p] through the midst of them, and so passed by.



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