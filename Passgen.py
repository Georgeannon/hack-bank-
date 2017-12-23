
print (" ___     _     ___   ___    ___   ___   _  _")
print ("| _ \   /_\   / __| / __|  / __| | __| | \| |")
print ("|  _/  / _ \  \__ \ \__ \ | (_ | | _|  | .` |")
print ("|_|   /_/ \_\ |___/ |___/  \___| |___| |_|\_|")
print ("")
print ('''          _______________________________
          |        Git Hub |            |
          |                v            |
          | https://github.com/T0xCisCo |
          |                             |
          |           Code by T0xCi$co  |
          |_____________________________|
                                         ''')

print ("PASSGEN is a wordlist maker based on your target informations")
print("")
name    = raw_input ("NAME : ")
surname = raw_input ("SURNAME : ")
hobies  = raw_input ("HOBIES : ")
dates   = raw_input ("DATES : ")
numbers  = raw_input ("NUMBERS : ")
print ('''passwords :

    |  %s%s
    |  %s%s
    |  %s%s%s
    |  %s%s
    |  %s%s
    |  %s%s
    |  %s%s
    |  %s%s
    |  %s%s
    |  %s%s

Thanks for using PASSGEN!!''')%(name,surname,hobies,dates,
                                surname,numbers,dates,hobies,numbers,dates,
                                name,surname,dates,hobies,name,numbers,hobies,
                                surname,hobies,name,dates)
