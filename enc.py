import codecs
import os
banner = """
+> | Encode / Decode Rot13 ++ Coded by HeadlessMan | <+
+> | Github : https://github.com/africode7         | <+
+> | Telegram : t.me/headlessman7                  | <+

"""

menu = """
++++++++++++++++++++++++++++++++++++++++++++++
   1. Encode ROT13
   2. Decode ROR13
   3. Exit Program
++++++++++++++++++++++++++++++++++++++++++++++
"""

if os.name == "nt":
   os.system("cls")
else:
   os.system("clear")
print(banner)
print(menu)
inputuser = input("Enter Number +> ")
                
if inputuser == "1":
   if os.name == "nt":
      os.system("cls")
   else:
      os.system("clear")
   inputen = input("Enter Text For Encode +> ")
   afteren = codecs.encode(inputen, "rot13")
   print("Result Encode :",afteren)
elif inputuser == "2":
   if os.name == "nt":
      os.system("cls")
   else:
      os.system("clear")
   inputdec = input("Enter Text For Decode +> ")
   afterdec = codecs.decode(inputdec, "rot13")
   print("Result Decode :",afterdec)
elif inputuser == "3":
   print(" ** Thanks .. Good Bye :) ** ")
   exit()
else:
   print("\n[!] Number Not Found ")

