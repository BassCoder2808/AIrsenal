"""
map between different conventions used in different data sources.
"""


positions = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}

alternative_team_names = {
    "ARS": ["1", "Arsenal", "Arsenal FC"],
    "AVL": ["2", "Aston Villa","Aston Villa FC"],
    "BOU": ["3", "Bournemouth", "AFC Bournemouth"],
    "BHA": ["4", "Brighton and Hove Albion", "Brighton", "Brighton & Hove Albion FC"],
    "BUR": ["5", "Burnley", "Burnley FC"],
    "CHE": ["6", "Chelsea", "Chelsea FC"],
    "CRY": ["7", "Crystal Palace", "Crystal Palace FC"],
    "EVE": ["8", "Everton", "Everton FC"],
    "LEI": ["9", "Leicester City", "Leicester", "Leicester City FC"],
    "LIV": ["10", "Liverpool", "Liverpool FC"],
    "MCI": ["11", "Manchester City", "Man City", "Manchester City FC"],
    "MUN": ["12", "Manchester United", "Man Utd", "Manchester United FC", "Manchester Utd"],
    "NEW": ["13", "Newcastle United", "Newcastle", "Newcastle United FC", "Newcastle Utd"],
    "NOR": ["14", "Norwich City","Norwich"],
    "SHU": ["15", "Sheffield United"],
    "SOU": ["16", "Southampton", "Southampton FC"],
    "TOT": ["17", "Tottenham Hotspur", "Spurs", "Tottenham Hotspur FC"],
    "WAT": ["18", "Watford", "Watford FC"],
    "WHU": ["19", "West Ham United", "West Ham", "West Ham United FC"],
    "WOL": ["20", "Wolves", "Wolverhampton Wanderers", "Wolverhampton Wanderers FC"],
    "SUN": ["Sunderland"],
    "WBA": ["West Bromwich Albion"],
    "SWA": ["Swansea City"],
    "STK": ["Stoke City", "Stoke"],
    "MID": ["Middlesbrough"],
    "HUL": ["Hull City"],
    "QPR": ["Queens Park Rangers"],
    "CAR": ["Cardiff", "Cardiff City", "Cardiff City FC"],
    "FUL": ["Fulham", "Fulham FC"],
    "HUD": ["Huddersfield Town", "Huddersfield", "Huddersfield Town AFC"],
}

alternative_player_names = {
    "Petr Cech": ["Cech"],
    "Bernd Leno": ["Leno"],
    "Laurent Koscielny": ["Koscielny"],
    "H\u00e9ctor Beller\u00edn": ["Beller\u00edn"],
    "Nacho Monreal": ["Monreal"],
    "Rob Holding": ["Holding"],
    "Shkodran Mustafi": ["Mustafi"],
    "Sead Kolasinac": ["Kolasinac"],
    "Calum Chambers": ["Chambers"],
    "Konstantinos Mavropanos": ["Mavropanos"],
    "Stephan Lichtsteiner": ["Lichtsteiner"],
    "Sokratis Papastathopoulos": ["Sokratis"],
    "Mesut \u00d6zil": ["\u00d6zil"],
    "Aaron Ramsey": ["Ramsey"],
    "Alex Iwobi": ["Iwobi"],
    "Mohamed Elneny": ["Elneny"],
    "Granit Xhaka": ["Xhaka"],
    "Henrikh Mkhitaryan": ["Mkhitaryan"],
    "Reiss Nelson": ["Nelson"],
    "Ainsley Maitland-Niles": ["Maitland-Niles"],
    "Danny Welbeck": ["Welbeck"],
    "Alexandre Lacazette": ["Lacazette"],
    "Pierre-Emerick Aubameyang": ["Aubameyang"],
    "Lucas Torreira": ["Torreira"],
    "Matteo Guendouzi": ["Guendouzi"],
    "Asmir Begovic": ["Begovic"],
    "Artur Boruc": ["Boruc"],
    "Simon Francis": ["Francis"],
    "Steve Cook": ["Steve Cook"],
    "Charlie Daniels": ["Daniels"],
    "Adam Smith": ["Adam Smith"],
    "Tyrone Mings": ["Mings"],
    "Nathan Ak\u00e9": ["Ak\u00e9"],
    "Jack Simpson": ["Simpson"],
    "Harry Arter": ["Arter"],
    "Marc Pugh": ["Pugh"],
    "Andrew Surman": ["Surman"],
    "Junior Stanislas": ["Stanislas"],
    "Dan Gosling": ["Gosling"],
    "Jordon Ibe": ["Ibe"],
    "Lewis Cook": ["Lewis Cook"],
    "Ryan Fraser": ["Fraser"],
    "Emerson Hyndman": ["Hyndman"],
    "David Brooks": ["Brooks"],
    "Callum Wilson": ["Wilson"],
    "Lys Mousset": ["Mousset"],
    "Joshua King": ["King"],
    "Jermain Defoe": ["Defoe"],
    "Diego Rico": ["Rico"],
    "Mathew Ryan": ["Ryan"],
    "Lewis Dunk": ["Dunk"],
    "Shane Duffy": ["Duffy"],
    "Bruno Saltor Grau": ["Bruno"],
    "Ga\u00ebtan Bong": ["Bong"],
    "Markus Suttner": ["Suttner"],
    "Ezequiel Schelotto": ["Schelotto"],
    "Leon Balogun": ["Balogun"],
    "Anthony Knockaert": ["Knockaert"],
    "Dale Stephens": ["Stephens"],
    "Beram Kayal": ["Kayal"],
    "Solomon March": ["March"],
    "Pascal Gro\u00df": ["Gro\u00df"],
    "Davy Pr\u00f6pper": ["Pr\u00f6pper"],
    "Jos\u00e9 Heriberto Izquierdo Mena": ["Izquierdo"],
    "Glenn Murray": ["Murray", "Murray"],
    "Tomer Hemed": ["Hemed"],
    "Sam Baldock": ["Baldock"],
    "J\u00fcrgen Locadia": ["Locadia"],
    "Florin Andone": ["Andone"],
    "David Button": ["Button"],
    "Jason Steele": ["Steele"],
    "Bernardo Fernandes da Silva Junior": ["Bernardo"],
    "Yves Bissouma": ["Bissouma"],
    "Alireza Jahanbakhsh": ["Jahanbakhsh"],
    "Tom Heaton": ["Heaton"],
    "Nick Pope": ["Pope"],
    "Matthew Lowton": ["Lowton"],
    "Ben Mee": ["Mee"],
    "Stephen Ward": ["Ward", "Ward"],
    "James Tarkowski": ["Tarkowski"],
    "Kevin Long": ["Long"],
    "Charlie Taylor": ["Taylor"],
    "Phil Bardsley": ["Bardsley"],
    "Johann Berg Gudmundsson": ["Gudmundsson"],
    "Steven Defour": ["Defour"],
    "Jeff Hendrick": ["Hendrick"],
    "Robbie Brady": ["Brady"],
    "Ashley Westwood": ["Westwood"],
    "Jonathan Walters": ["Walters"],
    "Jack Cork": ["Cork"],
    "Aaron Lennon": ["Lennon"],
    "Sam Vokes": ["Vokes"],
    "Ashley Barnes": ["Barnes"],
    "Nahki Wells": ["Wells"],
    "Chris Wood": ["Wood"],
    "Anders Lindegaard": ["Lindegaard"],
    "Neil Etheridge": ["Etheridge"],
    "Alex Smithies": ["Smithies"],
    "Sean Morrison": ["Morrison"],
    "Sol Bamba": ["Bamba"],
    "Bruno Ecuele Manga": ["Ecuele Manga"],
    "Matthew Connolly": ["Connolly", "Connolly"],
    "Joe Bennett": ["Bennett"],
    "Lee Peltier": ["Peltier"],
    "Ashley Darel Jazz Richards": ["Jazz Richards", "Richards"],
    "Greg Halford": ["Halford"],
    "Joe Ralls": ["Ralls"],
    "David Junior Hoilett": ["Hoilett"],
    "Nathaniel Mendez-Laing": ["Mendez-Laing"],
    "Callum Paterson": ["Paterson"],
    "Aron Gunnarsson": ["Gunnarsson"],
    "Anthony Pilkington": ["Pilkington"],
    "Lo\u00efc Damour": ["Damour"],
    "Danny Ward": ["Ward"],
    "Josh Murphy": ["Murphy"],
    "Kenneth Zohore": ["Zohore"],
    "Omar Bogle": ["Bogle"],
    "Gary Madine": ["Madine"],
    "Bobby Reid": ["Reid"],
    "Greg Cunninghamm": ["Cunningham"],
    "Thibaut Courtois": ["Courtois"],
    "Willy Caballero": ["Caballero"],
    "C\u00e9sar Azpilicueta": ["Azpilicueta"],
    "Gary Cahill": ["Cahill"],
    "Marcos Alonso": ["Alonso"],
    "David Luiz Moreira Marinho": ["David Luiz"],
    "Victor Moses": ["Moses"],
    "Antonio R\u00fcdiger": ["R\u00fcdiger"],
    "Andreas Christensen": ["Christensen"],
    "Davide Zappacosta": ["Zappacosta"],
    "Emerson Palmieri dos Santos": ["Emerson"],
    "Eden Hazard": ["Hazard"],
    "Cesc F\u00e0bregas": ["F\u00e0bregas"],
    "Willian Borges Da Silva": ["Willian"],
    "Pedro Rodr\u00edguez Ledesma": ["Pedro"],
    "N'Golo Kant\u00e9": ["Kant\u00e9"],
    "Ross Barkley": ["Barkley"],
    "Daniel Drinkwater": ["Drinkwater"],
    "Tiemou\u00e9 Bakayoko": ["Bakayoko"],
    "Ethan Ampadu": ["Ampadu"],
    "Callum Hudson-Odoi": ["Hudson-Odoi"],
    "Ruben Loftus-Cheek": ["Loftus-Cheek"],
    "Olivier Giroud": ["Giroud"],
    "\u00c1lvaro Morata": ["Morata"],
    "Jorge Luiz Frello Filho": ["Jorginho"],
    "Wayne Hennessey": ["Hennessey"],
    "Julian Speroni": ["Speroni"],
    "Vicente Guaita": ["Guaita"],
    "James Tomkins": ["Tomkins"],
    "Scott Dann": ["Dann"],
    "Martin Kelly": ["Kelly"],
    "Jeffrey Schlupp": ["Schlupp"],
    "Patrick van Aanholt": ["van Aanholt"],
    "Mamadou Sakho": ["Sakho"],
    "Jairo Riedewald": ["Riedewald"],
    "Aaron Wan-Bissaka": ["Wan-Bissaka"],
    "Jason Puncheon": ["Puncheon"],
    "James McArthur": ["McArthur"],
    "Bakary Sako": ["Sako"],
    "Andros Townsend": ["Townsend"],
    "Luka Milivojevic": ["Milivojevic"],
    "Wilfried Zaha": ["Zaha"],
    "Christian Benteke": ["Benteke"],
    "Alexander S\u00f8rloth": ["S\u00f8rloth"],
    "Cheikhou Kouyat\u00e9": ["Kouyat\u00e9"],
    "Joel Ward": ["Ward"],
    "Jaroslaw Jach": ["Jach"],
    "Pape Souar\u00e9": ["Souar\u00e9"],
    "Connor Wickham": ["Wickham"],
    "Sullay Kaikai": ["Kaikai"],
    "Max Meyer": ["Meyer"],
    "Jordan Pickford": ["Pickford"],
    "Maarten Stekelenburg": ["Stekelenburg"],
    "Leighton Baines": ["Baines"],
    "Seamus Coleman": ["Coleman"],
    "Phil Jagielka": ["Jagielka"],
    "Ashley Williams": ["Williams"],
    "Mason Holgate": ["Holgate"],
    "Jonjoe Kenny": ["Kenny"],
    "Michael Keane": ["Keane"],
    "Cuco Martina": ["Martina"],
    "Theo Walcott": ["Walcott"],
    "Yannick Bolasie": ["Bolasie"],
    "James McCarthy": ["McCarthy"],
    "Morgan Schneiderlin": ["Schneiderlin"],
    "Idrissa Gueye": ["Gueye"],
    "Tom Davies": ["Davies"],
    "Ademola Lookman": ["Lookman"],
    "Davy Klaassen": ["Klaassen"],
    "Gylfi Sigurdsson": ["Sigurdsson"],
    "Nikola Vlasic": ["Vlasic"],
    "Beni Baningime": ["Baningime"],
    "Dominic Calvert-Lewin": ["Calvert-Lewin"],
    "Oumar Niasse": ["Niasse"],
    "Cenk Tosun": ["Tosun"],
    "Richarlison de Andrade": ["Richarlison"],
    "Kevin Mirallas": ["Mirallas"],
    "Sandro Ram\u00edrez": ["Sandro", "Sandro"],
    "Lucas Digne": ["Digne"],
    "Marcus Bettinelli": ["Bettinelli"],
    "Tim Ream": ["Ream"],
    "Denis Odoi": ["Odoi"],
    "Tom Cairney": ["Cairney"],
    "Kevin McDonald": ["McDonald"],
    "Ryan Sessegnon": ["Sessegnon"],
    "Stefan Johansen": ["Johansen"],
    "Floyd Ayit\u00e9": ["Ayit\u00e9"],
    "Neeskens Kebano": ["Kebano"],
    "Rui Pedro da Rocha Fonte": ["Fonte"],
    "Aboubakar Kamara": ["Kamara"],
    "Maxime Le Marchand": ["Le Marchand"],
    "Jean Michael Seri": ["Seri"],
    "Cyrus Christie": ["Christie"],
    "Fabricio Agosto Ram\u00edrez": ["Fabri"],
    "Andr\u00e9 Sch\u00fcrrle": ["Sch\u00fcrrle"],
    "Aleksandar Mitrovic": ["Mitrovic"],
    "Alfie Mawson": ["Mawson"],
    "Ben Hamer": ["Hamer"],
    "Jonas L\u00f6ssl": ["L\u00f6ssl"],
    "Christopher Schindler": ["Schindler"],
    "Chris L\u00f6we": ["L\u00f6we"],
    "Tommy Smith": ["Smith"],
    "Mathias Jorgensen": ["Zanka"],
    "Scott Malone": ["Malone"],
    "Florent Hadergjonaj": ["Hadergjonaj"],
    "Terence Kongolo": ["Kongolo"],
    "Aaron Mooy": ["Mooy"],
    "Rajiv van La Parra": ["van La Parra"],
    "Jonathan Hogg": ["Hogg"],
    "Philip Billing": ["Billing"],
    "Tom Ince": ["Ince"],
    "Danny Williams": ["Williams"],
    "Abdelhamid Sabiri": ["Sabiri"],
    "Alex Pritchard": ["Pritchard"],
    "Ramadan Sobhi": ["Sobhi"],
    "Juninho Bacuna": ["Bacuna", "Bacuna"],
    "Collin Quaner": ["Quaner"],
    "Laurent Depoitre": ["Depoitre"],
    "Steve Mounie": ["Mounie"],
    "Elias Kachunga": ["Kachunga"],
    "Erik Durm": ["Durm"],
    "Adama Diakhaby": ["Diakhaby"],
    "Kasper Schmeichel": ["Schmeichel"],
    "Eldin Jakupovic": ["Jakupovic"],
    "Wes Morgan": ["Morgan"],
    "Christian Fuchs": ["Fuchs"],
    "Danny Simpson": ["Simpson"],
    "Yohan Benalouane": ["Benalouane"],
    "Benjamin Chilwell": ["Chilwell"],
    "Harry Maguire": ["Maguire"],
    "Ricardo Domingos Barbosa Pereira": ["Pereira"],
    "Jonny Evans": ["Evans"],
    "Marc Albrighton": ["Albrighton"],
    "Demarai Gray": ["Gray"],
    "Daniel Amartey": ["Amartey"],
    "Wilfred Ndidi": ["Ndidi"],
    "Vicente Iborra": ["Iborra"],
    "Matty James": ["James"],
    "Hamza Choudhury": ["Choudhury"],
    "Adrien Sebastian Perruchet Silva": ["Silva"],
    "Fousseni Diabat\u00e9": ["Diabat\u00e9"],
    "James Maddison": ["Maddison"],
    "Jamie Vardy": ["Vardy"],
    "Shinji Okazaki": ["Okazaki"],
    "Kelechi Iheanacho": ["Iheanacho"],
    "Simon Mignolet": ["Mignolet"],
    "Loris Karius": ["Karius"],
    "Dejan Lovren": ["Lovren"],
    "Alberto Moreno": ["Moreno"],
    "Nathaniel Clyne": ["Clyne"],
    "Joseph Gomez": ["Gomez"],
    "Joel Matip": ["Matip"],
    "Ragnar Klavan": ["Klavan"],
    "Trent Alexander-Arnold": ["Alexander-Arnold"],
    "Virgil van Dijk": ["van Dijk"],
    "Andrew Robertson": ["Robertson"],
    "Alex Oxlade-Chamberlain": ["Chamberlain"],
    "Jordan Henderson": ["Henderson"],
    "Adam Lallana": ["Lallana"],
    "Sadio Man\u00e9": ["Man\u00e9"],
    "Georginio Wijnaldum": ["Wijnaldum"],
    "Mohamed Salah": ["Salah"],
    "James Milner": ["Milner"],
    "Fabio Henrique Tavares": ["Fabinho"],
    "Naby Keita": ["Keita"],
    "Roberto Firmino": ["Firmino"],
    "Danny Ings": ["Ings"],
    "Dominic Solanke": ["Solanke"],
    "Xherdan Shaqiri": ["Shaqiri"],
    "Alisson Ramses Becker": ["Alisson"],
    "Daniel Sturridge": ["Sturridge"],
    "Riyad Mahrez": ["Mahrez"],
    "Ederson Santana de Moraes": ["Ederson"],
    "Claudio Bravo": ["Bravo"],
    "John Stones": ["Stones"],
    "Vincent Kompany": ["Kompany"],
    "Nicol\u00e1s Otamendi": ["Otamendi"],
    "Kyle Walker": ["Walker"],
    "Danilo Luiz da Silva": ["Danilo"],
    "Benjamin Mendy": ["Mendy"],
    "Aymeric Laporte": ["Laporte"],
    "Fabian Delph": ["Delph"],
    "Raheem Sterling": ["Sterling"],
    "David Silva": ["David Silva"],
    "Fernando Luiz Rosa": ["Fernandinho"],
    "Kevin De Bruyne": ["De Bruyne"],
    "Ilkay G\u00fcndogan": ["G\u00fcndogan"],
    "Leroy San\u00e9": ["San\u00e9"],
    "Bernardo Mota Veiga de Carvalho e Silva": ["Bernardo Silva"],
    "Phil Foden": ["Foden"],
    "Brahim Diaz": ["Diaz"],
    "Oleksandr Zinchenko": ["Zinchenko"],
    "Sergio Ag\u00fcero": ["Ag\u00fcero"],
    "Gabriel Fernando de Jesus": ["Jesus"],
    "David De Gea": ["De Gea", "David de Gea"],
    "Sergio Romero": ["Romero"],
    "Chris Smalling": ["Smalling"],
    "Phil Jones": ["Jones"],
    "Luke Shaw": ["Shaw"],
    "Marcos Rojo": ["Rojo"],
    "Antonio Valencia": ["Valencia"],
    "Matteo Darmian": ["Darmian"],
    "Daley Blind": ["Blind"],
    "Eric Bailly": ["Bailly"],
    "Victor Lindel\u00f6f": ["Lindel\u00f6f"],
    "Ashley Young": ["Young"],
    "Jos\u00e9 Diogo Dalot Teixeira": ["Dalot"],
    "Alexis S\u00e1nchez": ["S\u00e1nchez"],
    "Nemanja Matic": ["Matic"],
    "Juan Mata": ["Mata"],
    "Marouane Fellaini": ["Fellaini"],
    "Ander Herrera": ["Herrera"],
    "Jesse Lingard": ["Lingard"],
    "Anthony Martial": ["Martial"],
    "Paul Pogba": ["Pogba"],
    "Scott McTominay": ["McTominay"],
    "Frederico Rodrigues de Paula Santos": ["Fred"],
    "Marcus Rashford": ["Rashford"],
    "Romelu Lukaku": ["Lukaku"],
    "Andreas Pereira": ["Pereira"],
    "Robert Elliot": ["Elliot"],
    "Karl Darlow": ["Darlow", "Darlow"],
    "Martin Dubravka": ["Dubravka", "Martin"],
    "DeAndre Yedlin": ["Yedlin"],
    "Ciaran Clark": ["Clark"],
    "Jamaal Lascelles": ["Lascelles"],
    "Paul Dummett": ["Dummett"],
    "Florian Lejeune": ["Lejeune"],
    "Javier Manquillo": ["Manquillo"],
    "Chancel Mbemba": ["Mbemba"],
    "Matt Ritchie": ["Ritchie"],
    "Jonjo Shelvey": ["Shelvey"],
    "Mohamed Diam\u00e9": ["Diam\u00e9"],
    "Christian Atsu": ["Atsu"],
    "Jacob Murphy": ["Murphy"],
    "Mikel Merino": ["Merino"],
    "Isaac Hayden": ["Hayden"],
    "Sung-yueng Ki": ["Ki Sung-yueng"],
    "Dwight Gayle": ["Gayle"],
    "Ayoze P\u00e9rez": ["P\u00e9rez", "Ayoze"],
    "Jose Luis Mato Sanmart\u00edn": ["Joselu"],
    "Robert Kenedy Nunes do Nascimento": ["Kenedy"],
    "Fabian Sch\u00e4r": ["Sch\u00e4r"],
    "Yoshinori Muto": ["Muto"],
    "Alex McCarthy": ["McCarthy"],
    "Fraser Forster": ["Forster"],
    "Ryan Bertrand": ["Bertrand"],
    "Maya Yoshida": ["Yoshida"],
    "C\u00e9dric Soares": ["C\u00e9dric"],
    "Jack Stephens": ["Stephens"],
    "Sam McQueen": ["McQueen"],
    "Jan Bednarek": ["Bednarek"],
    "Wesley Hoedt": ["Hoedt"],
    "Steven Davis": ["Davis"],
    "James Ward-Prowse": ["Ward-Prowse"],
    "Oriol Romeu Vidal": ["Oriol Romeu"],
    "Pierre-Emile H\u00f8jbjerg": ["H\u00f8jbjerg"],
    "Sofiane Boufal": ["Boufal"],
    "Joshua Sims": ["Sims"],
    "Nathan Redmond": ["Redmond"],
    "Mario Lemina": ["Lemina"],
    "Stuart Armstrong": ["Armstrong"],
    "Mohamed Elyounoussi": ["Elyounoussi"],
    "Shane Long": ["Long"],
    "Charlie Austin": ["Austin"],
    "Manolo Gabbiadini": ["Gabbiadini"],
    "Guido Carrillo": ["Carrillo"],
    "Angus Gunn": ["Gunn"],
    "Jannik Vestergaard": ["Vestergaard"],
    "Matt Targett": ["Targett"],
    "Hugo Lloris": ["Lloris"],
    "Michel Vorm": ["Vorm"],
    "Toby Alderweireld": ["Alderweireld"],
    "Danny Rose": ["Rose"],
    "Jan Vertonghen": ["Vertonghen"],
    "Ben Davies": ["Davies"],
    "Kieran Trippier": ["Trippier"],
    "Kyle Walker-Peters": ["Walker-Peters"],
    "Davinson S\u00e1nchez": ["S\u00e1nchez"],
    "Serge Aurier": ["Aurier"],
    "Eric Dier": ["Dier"],
    "Mousa Demb\u00e9l\u00e9": ["Demb\u00e9l\u00e9"],
    "Erik Lamela": ["Lamela"],
    "Christian Eriksen": ["Eriksen"],
    "Bamidele Alli": ["Alli"],
    "Victor Wanyama": ["Wanyama"],
    "Heung-Min Son": ["Son"],
    "Harry Winks": ["Winks"],
    "Moussa Sissoko": ["Sissoko"],
    "Lucas Rodrigues Moura da Silva": ["Lucas Moura"],
    "Fernando Llorente": ["Llorente"],
    "Harry Kane": ["Kane"],
    "Heurelho Gomes": ["Gomes"],
    "Pontus Dahlberg": ["Dahlberg"],
    "Younes Kaboul": ["Kaboul"],
    "Craig Cathcart": ["Cathcart"],
    "Sebastian Pr\u00f6dl": ["Pr\u00f6dl"],
    "Jos\u00e9 Holebas": ["Holebas"],
    "Miguel Britos": ["Britos"],
    "Christian Kabasele": ["Kabasele"],
    "Daryl Janmaat": ["Janmaat"],
    "Adrian Mariappa": ["Mariappa"],
    "Francisco Femen\u00eda Far": ["Kiko Femen\u00eda"],
    "Marvin Zeegelaar": ["Zeegelaar"],
    "Marc Navarro": ["Navarro"],
    "Adam Masina": ["Masina"],
    "Nathaniel Chalobah": ["Chalobah"],
    "Tom Cleverley": ["Cleverley"],
    "Etienne Capoue": ["Capoue"],
    "Abdoulaye Doucour\u00e9": ["Doucour\u00e9"],
    "Roberto Pereyra": ["Pereyra"],
    "Will Hughes": ["Hughes"],
    "Gerard Deulofeu": ["Deulofeu"],
    "Andre Gray": ["Gray"],
    "Troy Deeney": ["Deeney"],
    "Stefano Okaka": ["Okaka"],
    "Jerome Sinclair": ["Sinclair"],
    "Ben Foster": ["Foster"],
    "Ken Sema": ["Sema"],
    "Adri\u00e1n San Miguel del Castillo": ["Adri\u00e1n"],
    "Lukasz Fabianski": ["Fabianski"],
    "Winston Reid": ["Reid"],
    "Aaron Cresswell": ["Cresswell"],
    "Angelo Ogbonna": ["Ogbonna"],
    "Sam Byram": ["Byram"],
    "Pablo Zabaleta": ["Zabaleta"],
    "Declan Rice": ["Rice"],
    "Reece Oxford": ["Oxford"],
    "Ryan Fredericks": ["Fredericks"],
    "Issa Diop": ["Diop"],
    "Arthur Masuaku": ["Masuaku"],
    "Mark Noble": ["Noble"],
    "Pedro Obiang": ["Obiang"],
    "Manuel Lanzini": ["Lanzini"],
    "Michail Antonio": ["Antonio"],
    "Edimilson Fernandes": ["Fernandes"],
    "Marko Arnautovic": ["Arnautovic"],
    "Andy Carroll": ["Carroll"],
    "Javier Hern\u00e1ndez Balc\u00e1zar": ["Chicharito", "Javier Hern\u00e1ndez"],
    "Jordan Hugill": ["Hugill"],
    "Jack Wilshere": ["Wilshere"],
    "Andriy Yarmolenko": ["Yarmolenko"],
    "Fabi\u00e1n Balbuena": ["Balbuena"],
    "Felipe Anderson Pereira Gomes": ["Felipe Anderson"],
    "Robert Snodgrass": ["Snodgrass"],
    "John Ruddy": ["Ruddy", "Rudd"],
    "Will Norris": ["Norris"],
    "Willy Boly": ["Boly"],
    "Barry Douglas": ["Douglas"],
    "Matt Doherty": ["Doherty"],
    "Romain Sa\u00efss": ["Sa\u00efss"],
    "Ryan Bennett": ["Bennett"],
    "Danny Batth": ["Batth"],
    "Roderick Jefferson Gon\u00e7alves Miranda": ["Miranda"],
    "Conor Coady": ["Coady"],
    "R\u00faben Gon\u00e7alo Silva Nascimento Vinagre": ["Vinagre"],
    "Diogo Jota": ["Jota"],
    "R\u00faben Diogo da Silva Neves": ["Neves"],
    "Ivan Cavaleiro": ["Cavaleiro"],
    "H\u00e9lder Costa": ["Costa"],
    "Bright Enobakhare": ["Enobakhare"],
    "Ra\u00fal Jim\u00e9nez": ["Jim\u00e9nez"],
    "Bonatini Lohner Maia Bonatini": ["Bonatini"],
    "Morgan Gibbs-White": ["Gibbs-White"],
    "Rafa Mir": ["Mir"],
    "Rui Pedro dos Santos Patr\u00edcio": ["Patr\u00edcio"],
    "Jo\u00e3o Filipe Iria Santos Moutinho": ["Moutinho"],
    "Jonathan Castro Otto": ["Jonny"],
}