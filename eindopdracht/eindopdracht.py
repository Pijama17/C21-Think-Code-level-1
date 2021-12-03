#ik ben van plan om een quiz te maken.
#------------------------------------------------------------------- vraag de naam van gebruiker.
print("hallo, ho heet jij")
name = input ("type je naam ")
#------------------------------------------------------------------- vraag gebruiker of ze een quiz willen maken.
print("Welkom "+ name )
start = input("wil je een quiz maken " + name + " ") 

if start == "ja":
    print("mooi zo !. ")

    #------------------------------------------------------------------- eerste vraag en antwoord.
    eerste_vraag = input("vind je de opleiding leuk? ")

    if eerste_vraag == "ja":

        print("dat is mooi om te horen!")
    else:
        print("dat is jammer. helaas kan je het nie veranderen.")
    #------------------------------------------------------------------- tweede vraag en antwoord.
    tweede_vraag = input("heb je al je werk af? ")

    if tweede_vraag == "ja":
        print("goedzo!")
    else:
        print(" ga je werk maken!")
    #------------------------------------------------------------------- derde vraag en antwoord.
    laaste_vraag = input("ben je trots op je zelf? ")

    if laaste_vraag == "ja":
        print("ik ben ook trots op jouw")
    else:
        print("ik ben ook teleurgesteld in je")
    #------------------------------------------------------------------- zeg gedach tegen de gebruiker.
    print("quiz einde")

else:
    print("oke fijne dag")
