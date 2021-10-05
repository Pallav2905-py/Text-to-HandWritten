'''Author: Pallav'''


#Open Terminal(with "ctrl+alt+t" on linux), and write 'pip install pywhatkit'

#Next import pywhatkit as <Whatever name u want, here I have used 'pallavtexttowritting'>
import pywhatkit as pallavtexttowritting

#Input from user, by which name the file is to be saved!
nameoffile = input("By what name you want to save the file:- ")

#Input from user, what they want to convert into written text!
maincontent = input("Enter your content that you want to convert into Hand-Written Format:- ")

#Main command! #The default color is set to blue, If u want to change color of your written document, then toggle "rgb=(0,0,0)"

#Color combinations for "rgb=(0,0,0)" Is given in file named as "Color-combinations.txt" for your hand-written document!
pallavtexttowritting.text_to_handwriting(maincontent, save_to= nameoffile + ".png", rgb=(0,0,100))

#Final statement that code ran sucessfully, and text converted to hand-written format!
print("File Converted to Hand-Written Format sucessfully, Thanku for using the code!")


#Note-
#1]Do not touch 'pywhatkit_dbs_txt' file, modifying it or renameing it may cause errors!
#2]If u get any error using the code, just remove excess spaces from your text!
#3]The Hand-Written file will be saved as a .png file, In the same folder!