from time import sleep
import random
from PIL import Image
import requests
from io import BytesIO
import streamlit as st

st.title("Welkom, dit is de kringverjaardag simulator 2.0 🎂")

if 'key' not in st.session_state:
    st.session_state['key'] = 0

image_placeholder = st.empty()
question_placeholder = st.empty()
choice_placeholder = st.empty()
response_placeholder = st.empty()

            
class Event:
    def __init__(self, start_bericht, opties, image_url = "", eenmalig = True, gesprek = False, eind_optie = ("", ""), finale = False):
        self.start_bericht = start_bericht
        self.image_url = image_url
        self.eenmalig = eenmalig
        self.gesprek = gesprek
        self.finale = finale
        self.choice = " "
        
        self.opties = opties
        
        if not self.eenmalig:
            self.opties += [eind_optie]
        
        if self.opties != None:
            self.answers = [" "] + [i[0] for i in opties]
            self.responses = [" "] + [i[1] for i in opties]
            #self.menu = self.maak_keuze_menu(opties)

    def show_image(self):
        try:
            response = requests.get(self.image_url)
            img = Image.open(BytesIO(response.content))
            width, height = img.size
            img = img.resize((min(width, 500), min(height, 500)))
            image_placeholder.image(img)
        except:
            st.write("afbeelding niet beschikbaar")
        
    def maak_keuze_menu(self, opties):
        opties_dic = {key: optie for key, optie in zip(range(len(opties)), opties)}
        
        menu = ""
        
        for key in opties_dic.keys():
            keuze = opties_dic[key][0]
            menu += f"{key}) {keuze} \n"
            
        return menu

            
    def optie_check(self):
        
        self.choice = choice_placeholder.selectbox("Maak je keuze", self.answers)
        
    def start(self):
        question_placeholder.markdown(self.start_bericht)
        
        if self.opties == None:
            sleep(5)
            st.session_state['key'] +=1
            st.experimental_rerun()
        
        self.optie_check()
        self.show_image()

        if self.choice != " ":
            
            
            answer_id = self.answers.index(self.choice)
            if self.finale:
                st.session_state['finale_id'] = answer_id
            response_placeholder.markdown(self.responses[answer_id])
            
            if self.eenmalig or answer_id+1 == len(self.answers):
            
                if st.button("Volgende"):
                    st.session_state['key'] +=1
                    st.experimental_rerun()
            
           
        


        

###WELKOM###

if st.session_state['key'] == 0:


    welkom_image = "https://www.simosupport.nl/Media/Images/feestje.jpg"

    welkom_bericht = "Jarige: Welkom op mijn feestje! Je bent wel laat, het is al 4 uur."
    
    welkom = Event(welkom_bericht, None, welkom_image)
    welkom.start()
###BEGROETING###
if st.session_state['key'] == 1:

    groet_opties = [("3 kussen te geven.", 
                     "De jarige heeft net een tante begroet die uit een land komt waar ze maar 2 kussen geven. De derde kus komt op de mond. " \
                         "Het ijs is gebroken"),
                         ("een hand te geven.", 
                          "Traditioneel, misschien wat te vroom, maar in ieder geval een veilige optie."),
                         ("een compliment te geven",
                          "Je kijkt de jarige van onder naar boven, maar komt tot de realisatie dat er weinig valt te complimenteren. Nu je inmiddels naar boven kijkt, "\
                              "complimenteer je maar het plafond."),
                              ("een buiging te maken.",
                               "Gewaagd, maar stijlvol.")]

    groet_bericht = "Je begroet de jarige door:"  
    groet_image = "https://image.shutterstock.com/image-photo/people-joy-fun-happiness-concept-600w-696053446.jpg"
    begroeting = Event(groet_bericht, groet_opties, groet_image)


    begroeting.start()

###KADO###
if st.session_state['key'] == 2:

    kado_opties = [("Stop wat geld in je hand en geef dit aan de jarige als je een hand geeft.",
                    "Het geld valt uit je hand terwijl je de jarige een hand probeert te geven. "\
                        "Iedereen ziet dat je kado geld is en de Nederlandse krentigerheid stijgt met 20%."),
                   ("Geef een fles wijn die je een paar jaar geleden hebt gekregen", 
                    "De jarige kijkt naar de fles wijn alsof die deze fles al eerder heeft gezien. "\
                        "Je herrinert ineens wie je die fles al die jaren geleden heeft gegeven."),
                     ("Je geeft een kadokaart die je onderweg bij een tankstation hebt gehaald.",
                      "Zodra je de bon hebt overhandigd kom je erachter dat je in alle haast de verkeerde kaart hebt gekocht. "\
                          "Je hebt een bon van €25 voor Netflix gegeven, terwijl de jarige al van jouw account gebruikt maakt. "\
                              "Wat voor indruk denk je hier mee te maken?"),
                              ('Je geeft niks.', 
                               "De jarige blijft je vragend aankijken. ..... Andere mensen krijgen het in de gaten "\
                               ".... Je houdt oogcontact vol .... Wat er al over was van de sfeer is nu echt kapot.")]


    kado_bericht = "Jarige: Kado's gaan op het dressoir. Kan ik wat van je aannemen?"  

    kado_image = "https://image.shutterstock.com/image-vector/falling-gift-box-happy-new-600w-1186272829.jpg"
    kado = Event(kado_bericht, kado_opties, kado_image)


    kado.start()

###FELICEREN###
if st.session_state['key'] == 3:
    felicitatie_bericht = "Het komt er nu echt op aan, dit gaat het feest maken of kraken, tradities voorzetten of verbreken: "\
    "Ga je iedere aanwezige feliciteren met de jarige of niet?"

    felicitatie_opties = [("Ja.", "Je gaat iedereen langs. Sommige gasten tolereren het, sommige gasten zijn overduidelijk geërgerd en hoopten dat deze gewoonte "\
                           "al lang uitgestorven was. Halverwege de kring is je arm gevoelloos en merk je de onheilspellende sfeer bij de ene helft die zich " \
                           "aan het voorbereiden is op jouw fellicitatie. Je kan nu niet meer terug, als je nu stopt sla je een enorme flater. Je schudt en " \
                           "feliciteert dapper door."),
                          ("Nee.", "Oke.")]


    felicitatie_image = "https://i.imgur.com/xr5xLkn.png"


    felicitatie = Event(felicitatie_bericht, felicitatie_opties, felicitatie_image)


    felicitatie.start()

    
###GEBAK###
if st.session_state['key'] == 4:
    gebak_opties = ["Kersenvlaai", "Bossche bol", 'Monchou', "Kruimelvlaai", "Appeltaart"]

    gebak_opties = [(optie, "Sorry, die is helaas op.") for optie in gebak_opties]

    gebak_bericht = "Jarige: Wil je een stukje taart? We hebben keuze uit:" 

    gebak_image = "https://image.shutterstock.com/image-photo/gift-box-tasty-cupcakes-present-600w-1785512870.jpg"
    gebak = Event(gebak_bericht, gebak_opties, gebak_image)


    gebak.start()

###TIENER###
if st.session_state['key'] == 5:
    tiener_bericht = "Je gaat zitten op een plastic tuinstoel tussen een tiener en een student. "\
                    "De tiener kijkt naar filmpje van mensen waar je nog nooit van gehoord hebt, die meer verdienen dan jij "\
                    "met zichzelf filmen terwijl ze fastfood eten in hun auto op een openbare parkeerplaats. Tijd om te kijken naar waar de jeugd van tegenwoordig zich mee bezig houdt."

    tiener_opties = [("Hoe gaat het op school?", 'Tiener: Goed...'),
                     ("Heb je een bijbaantje?", "Tiener: Ja..." ),
                     ("En heb je al een vriendinnetje?", "Tiener: Misschien..."),
                      ("En hoe is om eindelijk bij de grote mensen mogen te zitten?", "Tiener: Ja, prima..."),

                      ("Heel je leven ligt aan je voeten.", "Tiener: Ja dat zeggen ze allemaal...")]

    tiener_image = "https://st3.depositphotos.com/3332767/17829/i/1600/depositphotos_178291818-stock-photo-teenager-using-a-phone.jpg"
    tiener = Event(tiener_bericht, tiener_opties, tiener_image, eenmalig = False, gesprek = True, eind_optie = ("Peace out kiddo.", ""))

    tiener.start()

###STUDENT###
if st.session_state['key'] == 6:
    student_bericht = "Ach, je bent zelf ook niet meer de jongste. Wellicht kan de studente een meer inhoudelijk gesprek bieden."

    student_opties = [("Wat studeer je?", 'Lifestyle Informatics, maar ik overweeg een switch te maken naar Keltische talen en cultuur, daar valt toch meer werk in te vinden.'),
                     ("Wat doe je naast je studie?", "Na het uithangen van een matige collegehengst, tik ik aardig wat goudgele pret cilinder weg en bak ik grondpizza's." ),
                     ("En heb je al een relatie?", "Nee ik doe me louter goed aan krokante natte tosti's."),
                      ("Hoe vind je het feestje?", "Echt een HDP'tje. Na een avond in de bakkentrein aan de bijstandstokjes en de herstelbiertjes met een gezelschap taaier dan de AVG van menig huisgenoot.")]

    student_image = "https://thumbs.dreamstime.com/z/vrouwelijke-student-met-laptop-een-middelbare-schoolbibliotheek-89817561.jpg"
    student = Event(student_bericht, student_opties, student_image, eenmalig = False, gesprek = True, eind_optie = ("Je geeft de hoop in de volgende generaties op.", ""))

    student.start()

###GESPREKKEN###
if st.session_state['key'] == 7:
    random_woorden = ["boem", "zieke", "plaatst", "kunsten", "begrippen", "geschrokken", "verdienste", "aanrecht", "zwelling", "en", "oudsher", \
        "vergissing", "krakende", "muiden", "ontwikkelingen", "gering", "aanvullende", "middeleeuws", "afwachting", "uitzenddagen", "verbouwen", \
            "inter", "laf", "rauwprins", "teneinde", "boven", "toon", "directeur", "ongeduldig"]

    gesprekken_opties = [("Links", "".join([random_woorden[i]+"...." for i in random.sample(range(len(random_woorden)), 10)])),
                         ("Rechts", "".join([random_woorden[i]+"...." for i in random.sample(range(len(random_woorden)), 10)])),
                         ("De andere kant van de kring", "".join([random_woorden[i]+"...." for i in random.sample(range(len(random_woorden)), 10)]))]

    gesprekken_bericht = "Meeluisteren met andere mensen. Dit is een unieke kans om een kijkje te nemen in de levens van dit bonte gezelschap. "\
        "Van welke kant in de kring wil je meeluisteren?"

    gesprekken_image = "https://www.thebestsocial.media/nl/wp-content/uploads/sites/2/2019/10/kringverjaardag.jpeg"
    gesprekken = Event(gesprekken_bericht, gesprekken_opties, gesprekken_image, eenmalig = False, eind_optie = ("Een gesprek naast de A50 van Eindhoven richting Veghel op vrijdag om 18:00 is beter te verstaan dan deze woordenbrij.", ""))

    gesprekken.start()

###HAPJES###
if st.session_state['key'] == 8:
    hapjes_opties = [("Een cocktailprikker met kaas, augurk en een cocktailworstje",
                      "De kaas smaakt naar augurk, de augurk smaakt naar worst en de worst smaakt naar worst."),
                      ("Een toastje met eiersalade",
                      "Je neemt een hap waardoor het toastje door midden breekt en kruimels en eiersalade op je broek komt. "\
                          "De jarige is te druk met koffie zetten, dus je kruist je benen maar om het ongelukje te verbergen"),
                          ("Een soesje", 
                           "Het soesje is duidelijk pas een halfuur geleden uit de vriezer gehaald. Je laat je niet kennen en kauwt daadkrachtig door."),
                     ("Een plakje leverworst.", "Iemand die jou het plakje ziet eten kan zich niet inhouden door te melden dat hij een "\
                      "Keuringsdienst van Waarde aflevering heeft gezien over leverworst en besteed vervolgens het komende halfuur "\
                      "aan een ongevraagde samenvatting."),
                     ("Een stukje tortilla met kruidenkaas en gerookte zalm.", "Culinairder dan dit gaat het niet worden.")]

    hapjes_bericht = "Wellicht is een hapje een goed idee. Met een volle mond hoef je immers niet te praten."                   

    hapjes_image = "https://www.24kitchen.nl/files/styles/960h_960w/public/2020-01/borreltaart_L.jpg"                   
    hapjes = Event(hapjes_bericht, hapjes_opties, hapjes_image, eenmalig = False, eind_optie = ("Je besluit dat je toch nooit echt een fan bent geweest van de Nederlandse keuken.", ""))

    hapjes.start()

###EXIT###
if st.session_state['key'] == 9:
    finale_bericht = "Je hebt alles geprobeerd om het draagelijk te maken: praten met andere, eten en naar andere luisteren. Je kan het niet meer aan. " \
                          "Dit is niet jouw definitie van een feestje. Hoe maak jij je exit?"

    finale_opties = [("Je probeert te ontsnapppen via de achterdeur in de keuken.", "Zodra je in de keuken komt, wordt je aangesproken door een groepje "\
                  "gasten die aan het bier zitten. Ze bieden je een biertje aan en je kan het niet weerstaan. Nu je met hen aan de praat raakt, kom" \
                  "je erachter dat ze in hetzelfde schuitje zitten als jij. Echter hebben deze gasten zich strategisch gepositioneerd tussen de koelkast met "\
                  "drank en de frituurplan. Je blijft hangen. De ontsnapping is mislukt, maar je hebt alsnog een leuke avond."),
                   ("Je probeert te ontsnappen via de garage.", "De jarige ziet je naar de garage lopen en vraagt je of dat je wat flessen huismerk frisdrank " \
                    "kunt meenemen. Zodra je terug komt van de garage, vragen verschillende mensen of je wat voor hen kunt inschenken. 'Doe mij maar koffie,' wordt " \
                    "er geroepen. De koffie is op, dus je gaat maar nieuwe zetten. Je krijgt het commentaar dat de thee te lang is getrokken, dus je zet maar nieuwe. " \
                    "Voor je het weet is de koffie weer op, dus voel je genoodzaakt weer nieuwe te zetten. Er lijkt geen einde te komen aan verzoekjes van de gasten; ze lijken "\
                    "onverzadigbaar. Je loopt de jarige tegemoet en wisselt een blik. In de ogen van de jarige zie je hetzelfde als wat de jarige in jouw ogen ziet: " \
                    "de angst dat je tot het einde van het feest moet blijven."),
                   ("Je spreekt je gevoelens uit over het feest.", "Er valt een doodse stilte en er komt een collectief gevoel van ongemak en herkenning. "\
                    "Blijkbaar heeft niemand het echt naar z'n zin, inclusief de jarige. Mensen beginnen rustig op te staan en lopen de deur uit. Jij blijft " \
                    "in verbazing zitten tot dat iedereen weg is tot dat alleen jij en de jarige overblijven. De jarige pakt je handen vast en er loopt een traan de wang. "\
                    "'Bedankt dat je me hebt gered!"),
                   ("Je begint over het huidige kabinet.", "Verschillende gasten ontwaken uit een kaas-coma en beginnen hevig te discussiëren. " \
                    "Alle gasten zijn gefocust op het gesprek en plaatsvervangende schaamte. Dit is je kans om onopgemerkt weg te komen. Succes!")
                   ]


    finale_image = "http://veiligwinkel.files.wordpress.com/2014/06/download.jpg"


    finale = Event(finale_bericht, finale_opties, finale_image, finale = True)


    finale.start()
    
if st.session_state['key'] == 10:
    final_images = ["https://www.ctvnews.ca/polopoly_fs/1.4408891.1557076891!/httpImage/image.jpg_gen/derivatives/landscape_1020/image.jpg",
                    "http://teafloor.com/blog/wp-content/uploads/2019/08/beverages1.jpg",
                    "https://st3.depositphotos.com/1594308/14134/i/1600/depositphotos_141344482-stock-photo-empty-room-after-party.jpg",
                    "https://c8.alamy.com/comp/R5K7GK/business-people-arguing-in-meeting-R5K7GK.jpg"]
 


    response = requests.get(final_images[st.session_state['finale_id']])
    img = Image.open(BytesIO(response.content))
    width, height = img.size
    img = img.resize((min(width, 500), min(height, 500)))
    image_placeholder.image(img)
    
    st.balloons()
    
    if st.button("Nog een keer spelen?"):
        st.session_state['key'] = 0
        st.experimental_rerun()
