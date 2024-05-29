print("Hello This app helps you get your block number corresponding to the city name you entered")
user_city_name = input("Enter name of area: ")

def get_block_one_from_selected_city(block_name_user):

    block_one_cities = ["Braam Park ","Civic Centre ","Constitutional Court ","SAPS Hillbrow ","Civic Theater ","Thuso House ","Hillbrow ","Lenasia Ext 10 ","Lenasia Ext 11 ","Lenasia Ext 13 ","Lenasia Ext 3 ","Lenasia Ext 5"
,"Lenasia Ext 7 ","Lenasia Ext 8 ","Lenasia Ext 9 ","Lenasia Extension 2 ","Lenasia Extension 4 ","Lenasia Extension 6 ","Rietfontein AH","Thembelihle"
,"Blairgowrie ","Blairgowrie North ","Bordeaux ","Oerder Park ","Aeroton ","Booysens ","Booysens Reserve ","Chrisville ","Evans Park"
,"Frampton" ,"Gillview" ,"Glenanda West of Glen Rd ","Goldreef City ","Mondeor North ","Ophirton ","Ophirton Ext","Ormonde ","Ormonde Ext ","Ridgeway North" ,"Robertsham" ,"Robertsham Ext" ,"Southdale" ,"Winchester Hills" ,"Wolhuter","Glenanda North"]

    for block_one_city in block_one_cities:
        if block_name_user not in block_one_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_one_city}. ")
            break

def get_block_one_from_selected_city(block_name_user):
    block_two_cities = ["Berario","Blackheath","Emmarentia","Emmarentia And Ext","Emmerentia North","Emmerentia South","Fairlands","Fairlands West","Franklin Roosevelt Park","Franklin Roosevelt Park Ext 1","Greymont","Linden","Linden East","Linden North",
                        "Linden South","Montgomery Park","Northcliff","Northcliff And Exts","Northcliff Ext 12","Northcliff Ext 22","NorthCliff Ext 4","Northcliff Ext 6","Northcliff South","Residale","Residale Ext 6","Waterval Estate","Blairgowrie South",
                        "Craighall","Craighall Park","Forest Town","Greenside","Greenside East","Greenside South","Greenside West","Hyde Park","Hyde Park Ext 1","Hyde Park Ext 11","Parkhurst","Parktown North (West)","Parkview","Parkwood West","Pine Park",
                        "Rothesay Ave","Saxonwold West","Victory Park","Victory Park And Ext","Victory Park 8 And 11","Victory Park Ext 1","Victory Park Ext 2","Victory Park North","Victory Park South","Westcliff Ext","Driefontein","Kensington B","Multi Choice",
                        "Ferndale Ext.15","Albertville Ext","Pierneef Park","Willowild","Droste Park","Kazerne","Production Park","Prolecon","Berea","Water Park","Halfway Gardens","Halfway Gardens Ext","Carlswald ","Erand Gardens"]

    for block_two_city in block_two_cities:
        if block_name_user not in block_two_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_two_city}. ")
            break
def get_block_three_from_selected_city(block_name_user):
    block_three_cities = ['Hurst Hill', 'Melville', 'Newlands', 'University of Johannesburg (RAU)', 'Auckland Park', 'Rivasdale', 'Martindale', 'Montclare', 'Newclare', 'Sophiatown', 'Triomf', 'Crosby', 'Westdene', 'Boulders', 'Gallagher Estate', 'Zonkizizwe'
                          , 'Albertville', 'Albertville Ext', 'Albertville Ext 1', 'Claremont', 'Coronationville', 'Helen Joseph Hospital', 'Northcliff', 'Westbury', 'Westbury South', 'Coronation Hospital', 'Helen Joseph Hospital (JG Strydom Hospital)', 
                          'Brixton West (Hursthill)', 'Campus Square', 'Armadale Extension', 'Georginia (part)', 'Northcliff Extension', 'Finetown', 'Kiasha Park', 'Kiasha Park Ext', 'Lawley', 'Migson Manor', 'Migson Triangle', 'Unaville', 'Beverley Gardens'
                          , 'Bryanston', 'Daniel Brink Park', 'Ferndale Ext.15', 'HalfwayHouse', 'Grand Central Airport']
    for block_three_city in block_three_cities:
        if block_name_user not in block_three_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_three_city}. ")
            break

def get_block_four_from_selected_city(block_name_user):
    block_four_cities = ['Allen Lakes','Allen Manor', 'Kibler Heights', 'Meredale', 'Meredale Ext', 'Mondeor', 'Mondeor Ext', 'Patlynn AH', 'South Gate', 'Suideroord', 'Barrowdale', 'New Brighton', 'Parkmore', 'SANDHURST', 'Industria North', 'Maraisburg', 'Fleurhof', 
                         'Robertville', 'Stormill', 'Discovery', 'Florida', 'Florida CBD', 'Florida Cliffe', 'Florida Hills', 'Florida North', 'Florida Park', 'Selwyn', 'Geluksdal', 'Lenasia South', 'Lenasia South Ext 1', 'Lenasia South Ext 2', 
                         'Lenasia South Extension 4', 'Lenasia South Extension 7', 'Parkmore Extension 1', 'Bryanston East', 'River Club', 'Moodie Hill', 'Kyalami Hills', 'Kyalami Park', 'Kyalami Estates']
    
    for block_four_city in block_four_cities:
        if block_name_user not in block_four_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_four_city}. ")
            break
def get_block_five_from_selected_city(block_name_user):
    block_five_cities = [ "Allen Lakes", "Aspen Hills", "Bassonia", "Bassonia Rock", "Glenvista", "Glenvista Ext",
    "Liefde n Vrede", "Mulbarton", "Rispark AH", "Glenanda South", "11 Shaft", "Breaunanda",
    "Helderkruin", "Lewisham", "Roodekrans", "Roodekrans Ext", "Silverfields", "WilroPark",
    "MTN Campus", "White Ridge", "Carenvale", "Honey Hills", "Horizon", "Horizon Park",
    "Horizon View", "Ontdekkers Park", "Roodepoort North", "Kloofendal", "Selwyn", "Hurlingham",
    "Hurlingham Manor", "Hunters Hill A.H", "Hyperion", "Johannesburg North", "Jukskei Park",
    "Jukskei Park Ext 1,2,3,6,9", "Olivedale", "Sonneglans", "Vandia Grove", "Windsorway",
    "Bromhof Ext 66,67,68", "Bromhof Ext 10,11,12,15,22,23,27,30,35,38,46,50,63,64",
    "Ferndale Ext 15", "Golden Harvest A.H", "Meadowhurst", "Meadowhurst A.H", "Mill Hill Ext 2",
    "Noordhang Ext 20,23,25,26,29,3,33,36,4,42,44,45,46", "Noordhang Ext 49,50,51,54,58,67,7,8",
    "North Riding A.H", "North Riding Ext 1,13,16,17,2,20,21,23,26,27,29,30","North Riding Ext 38,4,42,43,46,5,51,53,54,55,59,6,60,61", 
    "North Riding Ext 62,63,64,67,69,71,72,73,75,76,79,80,82","North Riding Ext 84,86,91,92,93"
]
    
    for block_five_city in block_five_cities:
        if block_name_user not in block_five_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_five_city}. ")
            break

def get_block_six_from_selected_city(block_name_user):
    block_six_cities = [
    "City West", "Edgardale", "Fordsburg", "Marshalltown", "Newtown", "Westgate", "Westgate Ext","Founders Hill", "Greenstone Hill", "Longmeadow", "Longmeadow Business Estate",
    "Longmeadow Business Estate Ext", "Modderfontein Ext", "Thorn Hill", "WestField","Westlake View", "Westlake View Ext", "Longlake", "Longlake Ext", "Long Lakes",
    "Modderfontein", "Sebenza", "Glenadrienne", "Kya Sand Ext 101", "Kya Sand Ext 102","NORTH RIDING ESTATES", "NORTH RIDING ESTATES EXT", "NORTHGATE", "Northgate Ext",
    "Northgate Ext 4", "Northriding", "Northriding AH", "Northriding Ext", "Northumberland","Northwold", "Northwold Gardens", "Northworld Ext", "Sharonlea", "Sundowner", "Sundowner Ext",
    "Sundowner Ext 10", "Sundowner Ext 6", "Boundry Park", "Riverbend"
]
    for block_six_city in block_six_cities:
        if block_name_user not in block_six_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_six_city}. ")
            break

def get_block_seven_from_selected_city(block_name_user):

    block_seven_cities = [
    "Bushkoppies", "Devland", "Eldorado Estate", "Eldorado Park", "Eldorado Park Ext","Eldorado Park Ext 1 And 3", "Eldorado Park South", "Freedom Park", "Goldev", "Goudkoppies",
    "Klipriviersoog", "Klipriviersoog Estate", "Klipspruit West", "Kliptown", "Nancefield","Nancefield Ext", "Nancefield Industria", "Oliefantsvlei", "Race Course", "Slovo Park",
    "Baragwanath", "Doornkop", "Ellias Motswaledi", "Orlando Ekhaya", "SAP 13", "Santa","UJ Soweto Campus", "Baragwanath Academic Hospital", "Kliptown RDP", "Soweto Military Base",
    "Bruma", "Cyrildene", "De Wetshof", "Lorentzville", "Observatory", "Reynolds View","Bezuidenhout Valley", "Kensington", "Troyville", "Malvern", "Bertrams"
]
    for block_seven_city in block_seven_cities:
        if block_name_user not in block_seven_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_seven_city}. ")
            break

def get_block_eight_from_selected_city(block_name_user):

    block_eight_cities = [
    "Sandringham", "Alexandra Ext", "Alexandra South", "East Bank", "Far East Bank","Alexandra Mall", "Setswetla", "Tsutsumani", "Bellevue", "Bellevue East",
    "Bellevue Ext", "Linksfield Ridge", "Yeoville", "Houghton West"
]
    for block_eight_city in block_eight_cities:
        if block_name_user not in block_eight_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_eight_city}. ")
            break

def get_block_nine_from_selected_city(block_name_user):
    block_nine_cities = [
    "Atholl", "Atholl Gardens", "Birnam", "Bramley Park", "Bramley View","Corlett Gardens", "Crystal Gardens", "Dunsevern", "Fairmount", "Fairvale",
    "Glenhazel", "Glenkay", "Highlands North", "Lombardy East (West Side)", "Lombardy West", "Lyndhurst", "Percelia Estate", "Percilia", "Percilia Ext",
    "Raedene", "Rembrandt Park", "Rembrandt Ridge", "Savoy", "Savoy Estate","Silvamont", "Talboton", "View Crest", "Waverley", "Whitney Gardens",
    "Abbotsford", "Athollhurst Ext", "Birdhaven", "Bramely", "Bramley Gardens","Bramley North", "Casey Park", "Cheltondale", "Chislehurston", "Dunkeld",
    "Elton Hill", "Fairways", "Far East Bank", "Geluksdal", "Glensan", "Grassmere","Gresswold", "Hawkins Estates", "Houghton Estate", "Houghton South",
    "Hyde Park East", "Illovo", "Inanda", "Kent Park", "Kent View", "Kew","Kiasha Park", "Kiasha Park Ext", "Lombardy East (East Side)", "Melrose",
    "Melrose Arch", "Melrose Estate", "Melrose Ext 1", "Melrose Ext 2","Melrose North", "Migson Manor", "Migson Triangle", "Moodey Hill",
    "Mountainview", "Norwood", "Oaklands", "Raumarais Park", "River Park","Riviera", "Rosebank East", "Sandhurst", "Sunningdale", "Sunningdale Ridge",
    "Unaville", "Wierda Valley", "Winston Ridge", "Wynberg"
]
    for block_nine_city in block_nine_cities:
        if block_name_user not in block_nine_city:
            continue
        else:
            print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_nine_city}. ")
            break

def get_block_ten_from_selected_city(block_name_user):

    block_ten_cities = [
    "Johannesburg High Court", "HalfwayHouse", "Liquid Telecommunications", "Klipfontein View", "Doornfontein", "Ellis Park", "Fairview", "New Doornfontein",
    "Siemert", "Troyville", "New Centre", "Park Central", "Salisbury Claims", "Salisbury Claims Ext", "Salisbury Claims Ext 1", "Selby", "Selby Ext",
    "Village Deep", "Village Main", "Jeppe West", "Johannesburg CBD", "Troyevvile","Klipfontein", "Beverley Gardens", "Boskruin", "Boskruin Ext", "Bromhof",
    "Bush Hill Estate", "Daniel Brink Park", "Ferndale", "Grosvenor", "Kelland","Malanshof", "Moret", "President Ridge", "Rand Park Ridge", "RandPark",
    "RandPark Ridge", "Ruiterhof", "SonneGlans", "SonneGlans Ext", "SonneGlans Ext 17","Strydom Park", "Strydom Park Ext", "Ennerdale", "Ennerdale Ext", "Ennerdale Ext 1",
    "Ennerdale Ext 2", "Ennerdale Ext 3", "Ennerdale Ext 4", "Ennerdale Ext 5 And 6","Ennerdale South", "HalfwayHouse Ext 41"
]

    for block_ten_city in block_ten_cities:
            if block_name_user not in block_ten_city:
                continue
            else:
                print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_ten_city}. ")
                break
def get_block_eleven_from_selected_city(block_name_user):
    block_eleven_cities = [
    "Mill Hill", "Allen'snek", "Amarosa", "Boundary Park", "Boundary Park Ext","Bush Hill", "Constantia Kloof", "Harveston", "Honeydew", "Honeydew Ext",
    "Kelly Ridge", "Laser Park", "Panorama", "Poortview", "Radiokop", "Ruimsig","Strubens Valley", "Weltevreden Park", "Wilgeheuwel", "Clearwater", "Eagle Canyon",
    "Tresjolie", "Alsef", "Kimbult", "Zonnehoeve", "Willowbrook", "Little Falls","Douglasdale", "Bryanston Ext.25", "Bryanston Ext.27", "Bryanston Ext.3",
    "Bryanston Ext.39", "Bryanston Ext.45", "Hopefield", "Lawley Ext 1", "Commercia","Mayibuye", "Rabie Ridge", "Rabie Ridge Ext 4 And 5", "Austin View"
]
    for block_eleven_city in block_eleven_cities:
            if block_name_user not in block_eleven_city:
                continue
            else:
                print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_eleven_city}. ")
                break
def get_block_twelve_from_selected_city(block_name_user):
    block_twelve_cities = [
    "Bryanston North", "Bryanston North East", "Bryanston", "Bellavista Estate","Eastcliff", "Elands Park", "ELCEDES", "Elladoone", "Frampton East",
    "GLENEAGLES", "GLENEAGLES EXT", "Glenesk", "Haddon", "Kenilworth", "Kenilworth Ext","Klipriviersberg", "La Rochelle", "Lindberg Park", "Linmeyer", "Oakdene", "Oospoort Ext 1",
    "Pioneer", "Regency", "Regents Park", "Reuven", "Rewlatch", "Rewlatch Ext", "Ridgeway","Ridgeway South", "Risana", "Roseacre", "Rosettenville", "Rosettenville And Ext",
    "Rosherville", "South Hills", "Southcrest", "Spes Bona", "Springfield", "Stafford","The Gables", "The Gables Ext", "The Hill", "The Hill Ext", "Towerby", "Townsview",
    "Trojan", "Tulisa Park", "Turf Club", "Turffontein", "Unigrey", "Wemmer", "West Turffontein","West Turffontein Ext", "Wychwood", "Wychwood Ext", "Winchester Hills Ext", "Paarlshoop",
    "Bosmont", "Croesus", "Industria", "Industria West", "Longdale", "Riverlea", "Rossmore","Langlaagte", "Bergbron", "Delarey", "Florida Glen", "Quellerina", "West Lake", "Glen Lea",
    "Devon Valley", "Northcliff Ext 19", "Banfield", "Granville", "Florida", "Mechanical Workshop","Fleurhof", "Forest Hill", "Bryanbrink", "Country Life Park", "Cramerview", "Moffatview"
]

    for block_twelve_city in block_twelve_cities:
            if block_name_user not in block_twelve_city:
                continue
            else:
                print(f"Your city name {block_name_user} is in Block 1 and its full name is {block_twelve_city}. ")
                break












get_block_one_from_selected_city(user_city_name)