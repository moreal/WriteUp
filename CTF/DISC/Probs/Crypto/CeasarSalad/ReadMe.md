# CeasarSalad
200 point

## Overview
카이사르 암호(Caesar cipher) 또는 시저 암호는 암호학에서 다루는 간단한 치환암호의 일종이다. 암호화하고자 하는 내용을 알파벳별로 일정한 거리만큼 밀어서 다른 알파벳으로 치환하는 방식이다.
예를 들어 3글자씩 밀어내는 카이사르 암호로 'COME TO ROME'을 암호화하면 'FRPH WR URPH'가 된다.  
Ceasar 암호로 암호화된 문장을 복호화해 Flag를 찾자!

Download!

## Solution
해당 파일의 내용은 다음과 같이 되어있다.

> Gur fnynq'f perngvba vf trarenyyl nggevohgrq gb erfgnhengrhe Pnrfne Pneqvav, na Vgnyvna vzzvtenag jub bcrengrq erfgnhenagf va Zrkvpb naq gur Havgrq Fgngrf. Pneqvav jnf yvivat va Fna Qvrtb ohg ur jnf nyfb jbexvat va Gvwhnan jurer ur nibvqrq gur erfgevpgvbaf bs Cebuvovgvba. Uvf qnhtugre Ebfn erpbhagrq gung ure sngure vairagrq gur fnynq jura n Sbhegu bs Whyl 1924 ehfu qrcyrgrq gur xvgpura'f fhccyvrf. Naq gur Synt vf QVFP{prnfne_fnynq_jvgu_ab_prnfne}. Pneqvav znqr qb jvgu jung ur unq, nqqvat gur qenzngvp synve bs gur gnoyr-fvqr gbffvat "ol gur purs." N ahzore bs Pneqvav'f fgnss unir fnvq gung gurl vairagrq gur qvfu. Whyvn Puvyq fnvq gung fur unq rngra n Pnrfne fnynq ng Pneqvav'f erfgnhenag jura fur jnf n puvyq va gur 1920f. Va 1946, arjfcncre pbyhzavfg Qbebgul Xvytnyyra jebgr bs n Pnrfne pbagnvavat napubivrf, qvssrevat sebz Pneqvav'f irefvba: Gur ovt sbbq entr va Ubyyljbbq—gur Pnrfne fnynq—jvyy or vagebqhprq gb Arj Lbexref ol Tvyzber'f Fgrnx Ubhfr. Vg'f na vagevpngr pbapbpgvba gung gnxrf ntrf gb cercner naq pbagnvaf ybgf bs tneyvp, enj be fyvtugyl pbqqyrq rttf, pebhgbaf, ebznvar, napubivrf, cnezrnfna purrfr, byvir bvy, ivartne naq cyragl bs oynpx crccre.

그냥 저기 보이는 QVFP{...} 부분이 저 플래그에요~~!! 말하고 있지만 일단은,  
이것들을 카이사르 방식으로 돌려보면은 플래그가 나오리라 짐작할 수 있다.  

https://www.dcode.fr/caesar-cipher  
이곳에서 부르트 포싱을 돌려보니  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Crypto/CeasarSalad/Image/CaesarBruteForce.PNG)  

13만큼 시프트 했음을 알 수 있었다.  

평문은 다음과 같다.  

> The salad's creation is generally attributed to restaurateur Caesar Cardini, an Italian immigrant who operated restaurants in Mexico and the United States. Cardini was living in San Diego but he was also working in Tijuana where he avoided the restrictions of Prohibition. His daughter Rosa recounted that her father invented the salad when a Fourth of July 1924 rush depleted the kitchen's supplies. And the Flag is DISC{ceasar_salad_with_no_ceasar}. Cardini made do with what he had, adding the dramatic flair of the table-side tossing "by the chef." A number of Cardini's staff have said that they invented the dish. Julia Child said that she had eaten a Caesar salad at Cardini's restaurant when she was a child in the 1920s. In 1946, newspaper columnist Dorothy Kilgallen wrote of a Caesar containing anchovies, differing from Cardini's version: The big food rage in Hollywood—the Caesar salad—will be introduced to New Yorkers by Gilmore's Steak House. It's an intricate concoction that takes ages to prepare and contains lots of garlic, raw or slightly coddled eggs, croutons, romaine, anchovies, parmeasan cheese, olive oil, vinegar and plenty of black pepper.  

저기  Flag is DISC{ceasar_salad_with_no_ceasar}. 부분이 보인다.  

클리어!!  

## Flag
DISC{ceasar_salad_with_no_ceasar}
