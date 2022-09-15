import re
import sys
import streamlit as st
import numpy as np

def arab_to_unicode(word):
    return ' '.join(r'U{:04X}'.format(ord(chr)) for chr in word)

def arab_to_unicode_connected(word):
    return ''.join(r'U{:04X}'.format(ord(chr)) for chr in word)

def unicode_to_arab(arab):
    return re.subn('(U[0-9A-F]{4})', lambda cp: chr(int(cp.groups()[0][1:],16)), arab)

def arab_to_braille_unicode(character):
    unicode_to_replace = {
    '0627':'2801','0628':'2803','062A':'281E','062B':'2839','062C':'281A','062D':'2831','062E':'282D','062F':'2819','0630':'282E','0631':'2817',
    '0632':'2835','0633':'280E','0634':'2829','0635':'282F','0636':'282B','0637':'283E','0638':'283F','0639':'2837','063A':'2823','0641':'2808',
    '0642':'281F','0643':'2805','0644':'2807','0645':'280D','0646':'281D','0648':'283A','0647':'2813','064A':'280A','0623':'280C','0625':'280C',
    '0676':'2833','0649':'2815','0629':'2821','0653':'282A','064E':'2802','064F':'2825','0650':'2811','0670':'2808','0657':'282C','0656':'2818',
    '064B':'2806','064C':'2822','064D':'2814','0652':'2812','0651':'2821','060C':'2810','0028':'2836','0029':'2836',}

    for key, value in unicode_to_replace.items():
        character = character.replace(key, value)
    character = np.array(character.split())
    return character

def unicode_to_braille(unicode):
    braille_array = []
    for char in unicode:
        braille_array.append(chr(int(char[1:],16)))
    return braille_array

def main():
    st.title('Arabic to Braille Converter')

    # word = 'وَالْجِبَالَ أوْتَادًا تَمْسُكُ الْ أرْضَ لِئَلَّا تَضْطَرِبَ بِكُمْ وَتَمِيدَ'
    # word = str(sys.argv[1:])
    word = st.text_input('Arabic Letters')

    arab_unicode       = arab_to_unicode(word)
    arab_unicode_array = arab_to_braille_unicode(arab_unicode)
    braille            = unicode_to_braille(arab_unicode_array)

    st.header('Result : ')
    st.write(f"1.  Raw Arabic Text    \n{word}")
    st.write(f"2.  Arabic to Unicode  \n{arab_unicode}")
    st.write(f"3.  Unicode to Arabic  \n{unicode_to_arab(arab_unicode)}")
    st.write(f"4.  Arabic Braille     \n{'|'.join(braille)}")

    # print(f"+ Raw Arabic Text   : {word}")
    # print(f"+ Arabic to Unicode : {arab_unicode}")
    # print(f"+ Unicode to Arabic : {unicode_to_arab(arab_unicode)}")
    # print(f"+ Arabic Braille    : {'|'.join(braille)}")

if __name__ == "__main__":
    main()
