# Contenido de la demo Hotel Palacio de Santa Ines (Granada) (es/ca/en/fr). Hechos de palaciosantaines.es leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble estándar e individual','Doble con vistas a la Alhambra','Triple, Familiar y Suite'],'ca':['Doble estàndard i individual','Doble amb vistes a l\'Alhambra','Triple, Familiar i Suite'],'en':['Standard double and single use','Double with Alhambra views','Triple, Family and Suite'],'fr':['Double standard et usage individuel','Double avec vue sur l\'Alhambra','Triple, Familiale et Suite']}
RD={
'es':['Con techo de madera, baño con secador, televisión, wifi, minibar-nevera y aire acondicionado; también en uso individual con cama de matrimonio.','En el tercer piso, con cama de matrimonio, techo de madera y dos ventanas con vistas al Albayzín y a la Alhambra; con albornoz y zapatillas.','La Triple, tipo dúplex con altillo de madera; la Familiar, en dos plantas; la Suite, con artesonado mudéjar original y bañera de hidromasaje.'],
'ca':['Amb sostre de fusta, bany amb assecador, televisió, wifi, minibar-nevera i aire condicionat; també en ús individual amb llit de matrimoni.','Al tercer pis, amb llit de matrimoni, sostre de fusta i dues finestres amb vistes a l\'Albayzín i l\'Alhambra; amb barnús i sabatilles.','La Triple, tipus dúplex amb altell de fusta; la Familiar, en dues plantes; la Suite, amb enteixinat mudèjar original i banyera d\'hidromassatge.'],
'en':['With a wooden ceiling, bathroom with hairdryer, TV, wifi, minibar-fridge and air conditioning; also for single use with a double bed.','On the third floor, with a double bed, wooden ceiling and two windows overlooking the Albayzín and the Alhambra; bathrobe and slippers.','The Triple, a duplex with a wooden mezzanine; the Family room, on two levels; the Suite, with an original Mudéjar coffered ceiling and a hydromassage bath.'],
'fr':['Avec plafond en bois, salle de bain avec sèche-cheveux, télévision, wifi, minibar-réfrigérateur et climatisation ; aussi en usage individuel avec lit double.','Au troisième étage, avec lit double, plafond en bois et deux fenêtres donnant sur l\'Albayzín et l\'Alhambra ; peignoir et chaussons.','La Triple, en duplex avec mezzanine en bois ; la Familiale, sur deux niveaux ; la Suite, avec plafond mudéjar d\'origine et baignoire hydromassante.']}
ART={
'hero':('arches',9501,['#f3e8d7','#e9bb8b','#b04f2e','#76291a','#48170e']),
'intro':('columns',9502,['#efebe3','#f8f5ef','#af5130','#76291a','#48170e']),
'r1':('arches',9511,['#f0e5d3','#e3b380','#a6492a','#76291a','#48170e']),
'r2':('skyline',9512,['#76291a','#e7a568','#f5d5a3','#2c4a3e','#233e33','#162a22']),
'r3':('hills',9513,['#e6ece5','#f1e9d3','#edbb79','#a7bd9d','#7b9a81','#52735c']),
'g1':('skyline',9521,['#76291a','#e3a266','#f4d29f','#2a483c','#213b31','#152820']),
'g2':('arches',9522,['#eee2ce','#dfae7a','#a14526','#76291a','#48170e']),
'g3':('columns',9523,['#edeae2','#f7f4ee','#ab4e2f','#76291a','#48170e']),
'g4':('hills',9524,['#e3eae2','#eee6ce','#eab875','#a4ba9a','#78977e','#4f7059']),
'g5':('waves',9525,['#2c4a3e','#edbd83','#f6deb5','#3c6657','#2c4a3e','#1a3028']),
'g6':('arches',9526,['#ecdfca','#dcab76','#9e4224','#76291a','#48170e'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Palacio de Santa Inés · Albayzín, Granada',see_rooms='Ver habitaciones',hero_k='Granada · Albayzín',hero_t='Un palacio mudéjar frente a la Alhambra',hero_s='Dos edificios mudéjares del siglo XVI en la zona noble del Albayzín, Patrimonio de la Humanidad.',
 intro_t='Casa del Padre Eterno y Lavadero de Santa Inés',intro_p1='El hotel nació en 1995 con la rehabilitación de la Casa del Padre Eterno y se amplió en 2001 con el edificio colindante del Lavadero de Santa Inés.',
 intro_p2='Recepción 24 horas, wifi, desayuno buffet con opciones sin gluten y leche sin lactosa bajo petición, y salón para eventos.',
 stats=['Siglo XVI','Vistas a la Alhambra','Recepción 24 h','Admite perros y gatos'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Doble estándar, doble de uso individual, doble con vistas a la Alhambra, triple, familiar y suite.',
 svcs=['Recepción 24 horas','Wifi','Desayuno buffet','Sin gluten y sin lactosa bajo petición','Salón para eventos','Consigna de equipajes','Se admiten perros y gatos tranquilos','Taxi desde el parking concertado'],
 loc_p='Cuesta de Santa Inés, 9 · 18010 Granada. El acceso en coche está restringido: el hotel aconseja aparcar en un parking concertado y llegar en taxi.',
 chips=['¿Qué habitaciones tiene?','¿Tiene vistas a la Alhambra?','¿Cómo llego en coche?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Palacio de Santa Inés · Albayzín, Granada',see_rooms='Veure habitacions',hero_k='Granada · Albayzín',hero_t='Un palau mudèjar davant de l\'Alhambra',hero_s='Dos edificis mudèjars del segle XVI a la zona noble de l\'Albayzín, Patrimoni de la Humanitat.',
 intro_t='Casa del Padre Eterno i Lavadero de Santa Inés',intro_p1='L\'hotel va néixer el 1995 amb la rehabilitació de la Casa del Padre Eterno i es va ampliar el 2001 amb l\'edifici del costat, el Lavadero de Santa Inés.',
 intro_p2='Recepció 24 hores, wifi, esmorzar bufet amb opcions sense gluten i llet sense lactosa sota petició, i saló per a esdeveniments.',
 stats=['Segle XVI','Vistes a l\'Alhambra','Recepció 24 h','Admet gossos i gats'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Doble estàndard, doble d\'ús individual, doble amb vistes a l\'Alhambra, triple, familiar i suite.',
 svcs=['Recepció 24 hores','Wifi','Esmorzar bufet','Sense gluten i sense lactosa sota petició','Saló per a esdeveniments','Consigna d\'equipatges','S\'admeten gossos i gats tranquils','Taxi des del pàrquing concertat'],
 loc_p='Cuesta de Santa Inés, 9 · 18010 Granada. L\'accés en cotxe està restringit: l\'hotel aconsella aparcar en un pàrquing concertat i arribar-hi en taxi.',
 chips=['Quines habitacions té?','Té vistes a l\'Alhambra?','Com hi arribo en cotxe?','Com es reserva?']),
'en':dict(title='Hotel Palacio de Santa Inés · Albayzín, Granada',see_rooms='See the rooms',hero_k='Granada · Albayzín',hero_t='A Mudéjar palace facing the Alhambra',hero_s='Two 16th-century Mudéjar buildings in the noble part of the Albayzín, a World Heritage Site.',
 intro_t='Casa del Padre Eterno and Lavadero de Santa Inés',intro_p1='The hotel opened in 1995 with the restoration of the Casa del Padre Eterno and was extended in 2001 with the adjoining Lavadero de Santa Inés building.',
 intro_p2='24-hour reception, wifi, buffet breakfast with gluten-free food and lactose-free milk on request, and an events room.',
 stats=['16th century','Alhambra views','24 h reception','Dogs and cats welcome'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Standard double, double for single use, double with Alhambra views, triple, family room and suite.',
 svcs=['24-hour reception','Wifi','Buffet breakfast','Gluten- and lactose-free on request','Events room','Luggage storage','Calm dogs and cats allowed','Taxi from the partner car park'],
 loc_p='Cuesta de Santa Inés, 9 · 18010 Granada. Car access is restricted: the hotel advises parking at a partner car park and arriving by taxi.',
 chips=['What rooms does it have?','Does it have Alhambra views?','How do I arrive by car?','How do I book?']),
'fr':dict(title='Hotel Palacio de Santa Inés · Albayzín, Grenade',see_rooms='Voir les chambres',hero_k='Grenade · Albayzín',hero_t='Un palais mudéjar face à l\'Alhambra',hero_s='Deux bâtiments mudéjars du XVIe siècle dans la partie noble de l\'Albayzín, patrimoine mondial.',
 intro_t='Casa del Padre Eterno et Lavadero de Santa Inés',intro_p1='L\'hôtel est né en 1995 avec la réhabilitation de la Casa del Padre Eterno et s\'est agrandi en 2001 avec le bâtiment voisin du Lavadero de Santa Inés.',
 intro_p2='Réception 24h/24, wifi, petit-déjeuner buffet avec produits sans gluten et lait sans lactose sur demande, et salle pour événements.',
 stats=['XVIe siècle','Vue sur l\'Alhambra','Réception 24h/24','Chiens et chats admis'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Double standard, double à usage individuel, double avec vue sur l\'Alhambra, triple, familiale et suite.',
 svcs=['Réception 24h/24','Wifi','Petit-déjeuner buffet','Sans gluten et sans lactose sur demande','Salle pour événements','Consigne à bagages','Chiens et chats calmes admis','Taxi depuis le parking partenaire'],
 loc_p='Cuesta de Santa Inés, 9 · 18010 Grenade. L\'accès en voiture est restreint : l\'hôtel conseille de se garer dans un parking partenaire et de venir en taxi.',
 chips=['Quelles chambres a-t-il ?','A-t-il vue sur l\'Alhambra ?','Comment venir en voiture ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.palaciosantaines.es/bookingstep1/'; REN='https://www.palaciosantaines.es/en/bookingstep1/'; RFR='https://www.palaciosantaines.es/fr/bookingstep1/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':RFR})
D=dict(name='Hotel Palacio de Santa Inés',ac='#6b3a1f',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Cuesta de Santa Inés, 9 · 18010 Granada',phones=['+34 958 22 23 62'],emails=['reservas@palaciosantaines.es'],maps='Hotel Palacio de Santa Inés, Cuesta de Santa Inés 9, Granada',t=T)
META=dict(repo='demo-hotel-palacio-de-santa-ines-granada',name='Hotel Palacio de Santa Inés',legal_name='Instituto Andaluz de Ocio y Hostelería, S.L.',registry_ids=['CIF B18641563','Registro Mercantil de Granada, hoja GR-21928'],
 url='https://www.palaciosantaines.es/',domain='palaciosantaines.es',municipality='Granada',province='Granada',sector='hotel en dos edificios mudéjares del siglo XVI en el Albayzín (Granada)',
 read_at='2026-10-29T15:30:00+01:00',created_at='2026-10-29T15:30:00+01:00',built_at='2026-10-29T15:38:00+01:00',audit_date='2026-10-29T15:24:56+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T11:04:11+01:00',url='https://www.google.com/maps/place/Hotel+Palacio+de+Santa+Ines,+siglo+XVI/@37.1783259,-3.5939066,17z/data=!4m9!3m8!1s0xd71fcb87e0e7605:0x6a3b9943705ba645!5m2!4m1!1i2!8m2!3d37.1783259!4d-3.5939066!16s%2Fg%2F1tffl3nt'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio hotel (palaciosantaines.es/bookingstep1, pagina del propio dominio que carga el componente de tarifas de Mirai del hotel, data-mirai-id 58804861; versiones /en/ y /fr/); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Tiene vistas a la Alhambra?','K02'),('¿Tienen habitación para familias?','K03'),('¿Dónde está?','K04'),('¿Cómo llego en coche?','K05'),('¿Me devuelven el taxi?','K05'),('¿Tienen desayuno?','K06'),('¿Admiten mascotas?','K07'),('¿Hay wifi?','K08'),('¿Tienen salón para eventos?','K09'),('¿Cuándo se construyó?','K10'),('¿Cómo reservo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11'),('¿Tienen piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Té vistes a l\'Alhambra?','K02'),('Teniu habitació per a famílies?','K03'),('On és?','K04'),('Com hi arribo en cotxe?','K05'),('Em retornen el taxi?','K05'),('Teniu esmorzar?','K06'),('Admeteu mascotes?','K07'),('Hi ha wifi?','K08'),('Teniu saló per a esdeveniments?','K09'),('Quan es va construir?','K10'),('Com reservo?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11'),('Teniu piscina?',None)],
'en':[('What rooms does it have?','K01'),('Does it have Alhambra views?','K02'),('Do you have family rooms?','K03'),('Where is it?','K04'),('How do I arrive by car?','K05'),('Do you refund the taxi?','K05'),('Do you serve breakfast?','K06'),('Are pets allowed?','K07'),('Is there wifi?','K08'),('Do you have an events room?','K09'),('When was it built?','K10'),('How do I book?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11'),('Is there a pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('A-t-il vue sur l\'Alhambra ?','K02'),('Avez-vous des chambres familiales ?','K03'),('Où est-il ?','K04'),('Comment venir en voiture ?','K05'),('Le taxi est-il remboursé ?','K05'),('Servez-vous le petit-déjeuner ?','K06'),('Les animaux sont-ils admis ?','K07'),('Y a-t-il le wifi ?','K08'),('Avez-vous une salle pour événements ?','K09'),('Quand a-t-il été construit ?','K10'),('Comment réserver ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11'),('Y a-t-il une piscine ?',None)]}
