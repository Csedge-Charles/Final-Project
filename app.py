from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
import random
import sys
sys.setrecursionlimit(5000)  # Increase the limit to 5000 (adjust as needed)

url_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']





db = TinyDB("./db.json")
personal = Query()

import func

def subtract(string1, string2):
    string1 = string1.split()
    string1.remove(string2)
    final = ""
    for i in string1:
        final += f'{i} '
    return final

def convert(number):
    number = int(number)
    first = int(number/10) * 7
    second = number - int(number/10) * 10
    return first + second - 1


def time_spot(number):
    number = int(number)
    number = int(number / 10)
    return str(number - 1) 



def listing(string):
    final_list = []
    word = ""
    for i in range(len(string)):
        if string[i] != "[" and string[i] != "]" and string[i] != "," and string[i] != '"' and string[i] != "'":
            if string[i] == " " and string[i - 1] == ",":
                pass
            else: 
                word += string[i]
        if string[i] == "," or string[i] == "]":
            final_list.append(word)
            word = ""
    return final_list


def between(time1, time2):
    time_list = ["8:00AM", "8:15AM", "8:30AM", "8:45AM", "9:00AM", "9:15AM", "9:30AM", "9:45AM", "10:00AM", "10:15AM", "10:30AM", "10:45AM", "11:00AM", "11:15AM", "11:30AM", "11:45PM", "12:00PM", "12:15PM", "12:30PM", "12:45PM", "1:00PM", "1:15PM", "1:30PM", "1:45PM", "2:00PM", "2:15PM", "2:30PM", "2:45PM", "3:00PM", "3:15PM", "3:30PM", "3:45PM", "4:00PM", "4:15PM", "4:30PM", "4:45PM", "5:00PM", "5:15PM", "5:30PM", "5:45PM", "6:00PM", "6:15PM", "6:30PM", "6:45PM", "7:00PM", "7:15PM", "7:30PM", "7:45PM", "8:00PM", "8:15PM", "8:30PM", "8:45PM"]
    final_list = []
    start = False
    for i in range(len(time_list)):
        if time_list[i] == time1:
            start = True
        if start == True:
            final_list.append(time_list[i])
        if time2 == time_list[i]:
            start = False
    if start == True:
        for i in range(len(time_list)):
            if start == True:
                final_list.append(time_list[i])
            if time2 == time_list[i]:
                start = False
        
    return final_list

def days_and_time(time1, time2, days):
    time_between = between(time1, time2)
    final = []
    time_list = ["8:00AM", "8:15AM", "8:30AM", "8:45AM", "9:00AM", "9:15AM", "9:30AM", "9:45AM", "10:00AM", "10:15AM", "10:30AM", "10:45AM", "11:00AM", "11:15AM", "11:30AM", "11:45PM", "12:00PM", "12:15PM", "12:30PM", "12:45PM", "1:00PM", "1:15PM", "1:30PM", "1:45PM", "2:00PM", "2:15PM", "2:30PM", "2:45PM", "3:00PM", "3:15PM", "3:30PM", "3:45PM", "4:00PM", "4:15PM", "4:30PM", "4:45PM", "5:00PM", "5:15PM", "5:30PM", "5:45PM", "6:00PM", "6:15PM", "6:30PM", "6:45PM", "7:00PM", "7:15PM", "7:30PM", "7:45PM", "8:00PM", "8:15PM", "8:30PM", "8:45PM"]
    if 'Monday' in days:
        corresponding_list = ["11", "21", "31", "41", "51", "61", "71", "81", "91", "101", "111", "121", "131", "141", "151", "161", "171", "181", "191", "201", "211", "221", "231", "241", "251", "261", "271", "281", "291", "301", "311", "321", "331", "341", "351", "361", "371", "381", "391", "401", "411", "421", "431", "441", "451", "461", "471", "481", "491", "501", "511", "521"]
        for i in range(len(time_list)):
            if time_list[i] in time_between:
                final.append(corresponding_list[i])
    if 'Tuesday' in days:
        corresponding_list = ["12", "22", "32", "42", "52", "62", "72", "82", "92", "102", "112", "122", "132", "142", "152", "162", "172", "182", "192", "202", "212", "222", "232", "242", "252", "262", "272", "282", "292", "302", "312", "322", "332", "342", "352", "362", "372", "382", "392", "402", "412", "422", "432", "442", "452", "462", "472", "482", "492", "502", "512", "522"]
        for i in range(len(time_list)):
            if time_list[i] in time_between:
                final.append(corresponding_list[i])
    if 'Wednesday' in days:
        corresponding_list = ["13", "23", "33", "43", "53", "63", "73", "83", "93", "103", "113", "123", "133", "143", "153", "163", "173", "183", "193", "203", "213", "223", "233", "243", "253", "263", "273", "283", "293", "303", "313", "323", "333", "343", "353", "363", "373", "383", "393", "403", "413", "423", "433", "443", "453", "463", "473", "483", "493", "503", "513", "523"]
        for i in range(len(time_list)):
            if time_list[i] in time_between:
                final.append(corresponding_list[i])
    if 'Thursday' in days:
        corresponding_list = ["14", "24", "34", "44", "54", "64", "74", "84", "94", "104", "114", "124", "134", "144", "154", "164", "174", "184", "194", "204", "214", "224", "234", "244", "254", "264", "274", "284", "294", "304", "314", "324", "334", "344", "354", "364", "374", "384", "394", "404", "414", "424", "434", "444", "454", "464", "474", "484", "494", "504", "514", "524"]
        for i in range(len(time_list)):
            if time_list[i] in time_between:
                final.append(corresponding_list[i])
    if 'Friday' in days:
        corresponding_list = ["15", "25", "35", "45", "55", "65", "75", "85", "95", "105", "115", "125", "135", "145", "155", "165", "175", "185", "195", "205", "215", "225", "235", "245", "255", "265", "275", "285", "295", "305", "315", "325", "335", "345", "355", "365", "375", "385", "395", "405", "415", "425", "435", "445", "455", "465", "475", "485", "495", "505", "515", "525"]
        for i in range(len(time_list)):
            if time_list[i] in time_between:
                final.append(corresponding_list[i])
    if 'Saturday' in days:
        corresponding_list = ["16", "26", "36", "46", "56", "66", "76", "86", "96", "106", "116", "126", "136", "146", "156", "166", "176", "186", "196", "206", "216", "226", "236", "246", "256", "266", "276", "286", "296", "306", "316", "326", "336", "346", "356", "366", "376", "386", "396", "406", "416", "426", "436", "446", "456", "466", "476", "486", "496", "506", "516", "526"]
        for i in range(len(time_list)):
            if time_list[i] in time_between:
                final.append(corresponding_list[i])
    if 'Sunday' in days:
        corresponding_list = ["17", "27", "37", "47", "57", "67", "77", "87", "97", "107", "117", "127", "137", "147", "157", "167", "177", "187", "197", "207", "217", "227", "237", "247", "257", "267", "277", "287", "297", "307", "317", "327", "337", "347", "357", "367", "377", "387", "397", "407", "417", "427", "437", "447", "457", "467", "477", "487", "497", "507", "517", "527"]
        for i in range(len(time_list)):
            if time_list[i] in time_between:
                final.append(corresponding_list[i])
    return final


def getEmail():
    EmailList = []
    for i in db.all():
        EmailList.append(i['email'])
    return EmailList


def findValue(email, value):
    for i in db.all():
        if i['email'] == email:
            return str(i[value])
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def sign_in():
    if request.method == 'POST':
        global email
        global password
        global key
        
        email = request.form['email']
        password = request.form['password']
        
        if request.form.getlist('create') == ['Create Account']:
            return redirect('/create-account', code=302)
        if email in getEmail():
            if password == findValue(email, "password"):
                key = findValue(email, "key")
                return redirect(url_for('home', key=key), code=302)
            return render_template("signin.html", reject2="Incorrect Password", email=email, password=password)
        return render_template("signin.html",reject1="Username does not exist", reject2="Incorrect Password", email=email, password=password)
    return render_template("signin.html")



@app.route("/create-account", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        global email
        global password
        global key
        global activity
        global color
        global updater
        
        color = ""
        updater = ""
        activity = updater
        email = request.form['email']
        password = request.form['password']
        if email not in getEmail():
            key = f'{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}'
            db.insert({'email': email, 'password':password, 'key': key, "activity": activity, "color": color, "value11": "", "text": [" ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ", " ", " ", " ", " ", " "," "," "," ", " ", " ",  " ", " ", " ", " "]})
            return redirect('/', code=302)
        else:
            if email in getEmail():
                return render_template('create.html', wrong='username is already used', email=email, password=password)
    return render_template('create.html', wrong='')

@app.route("/home/<key>", methods=['POST', 'GET'])


def home(key):
    global updater
    time_list = ["8:00AM", "8:15AM", "8:30AM", "8:45AM", "9:00AM", "9:15AM", "9:30AM", "9:45AM", "10:00AM", "10:15AM", "10:30AM", "10:45AM", "11:00AM", "11:15AM", "11:30AM", "11:45PM", "12:00PM", "12:15PM", "12:30PM", "12:45PM", "1:00PM", "1:15PM", "1:30PM", "1:45PM", "2:00PM", "2:15PM", "2:30PM", "2:45PM", "3:00PM", "3:15PM", "3:30PM", "3:45PM", "4:00PM", "4:15PM", "4:30PM", "4:45PM", "5:00PM", "5:15PM", "5:30PM", "5:45PM", "6:00PM", "6:15PM", "6:30PM", "6:45PM", "7:00PM", "7:15PM", "7:30PM", "7:45PM", "8:00PM", "8:15PM", "8:30PM", "8:45PM"]
    inputs = findValue(email, "activity").split()
    colors = findValue(email, "color").split()
    values = listing(findValue(email, "text"))
    if request.method == "POST":
        submit = request.form['submit']
        if submit == "Remove":  
            time1 = request.form['remove_time1']
            time2 = request.form['remove_time2']
            days = request.form.getlist('remove_days')
            
            new_schedule = days_and_time(time1, time2, days)
            color_updater = findValue(email, "color") 
            updater = findValue(email, "activity")
            
            if len(new_schedule) >= 1:
                label_location = time_spot(new_schedule[0]) 
                if "Monday" in days:
                    values[convert(int(label_location + "1"))] = " "
                if "Tuesday" in days:
                    values[convert(int(label_location + "2"))] = " "
                if "Wednesday" in days:
                    values[convert(int(label_location + "3"))] = " "
                if "Thursday" in days:
                    values[convert(int(label_location + "4"))] = " "
                if "Friday" in days:
                    values[convert(int(label_location + "5"))] = " "
                if "Saturday" in days:
                    values[convert(int(label_location + "6"))] = " "
                if "Sunday" in days:
                    values[convert(int(label_location + "7"))] = " "
        
            for i in new_schedule:
                if i in inputs:
                    updater = subtract(updater, i)
                    inputs.remove(i)
                if i in colors:
                    color_updater = subtract(color_updater, i)
                    colors.remove(i)
                
        else:
            time1 = request.form['time1']
            time2 = request.form['time2']
            text = request.form['label']
            color = request.form.getlist('color')
            days = request.form.getlist('days')
            
            
             
            new_schedule = days_and_time(time1, time2, days)
            updater = findValue(email, "activity")
            color_updater = findValue(email, "color")  
              
            if len(new_schedule) >= 1:
                label_location = time_spot(new_schedule[0])
                if "Monday" in days:
                    values[convert(int(label_location + "1"))] = text
                if "Tuesday" in days:
                    values[convert(int(label_location + "2"))] = text
                if "Wednesday" in days:
                    values[convert(int(label_location + "3"))] = text
                if "Thursday" in days:
                    values[convert(int(label_location + "4"))] = text
                if "Friday" in days:
                    values[convert(int(label_location + "5"))] = text
                if "Saturday" in days:
                    values[convert(int(label_location + "6"))] = text
                if "Sunday" in days:
                    values[convert(int(label_location + "7"))] = text
              
            for i in new_schedule:
                if i not in inputs:
                    updater += f" {i}"
                    inputs.append(i)
                if color == ["red"] and i not in colors:
                    color_updater += f' {i}'
                    colors.append(i)
                if color == [] and i in colors:
                    color_updater = subtract(color_updater, i)
                    colors.remove(i)
                    
        db.update({"color": color_updater}, personal.email == email)
        db.update({"text": values}, personal.email == email)
        db.update({"activity": updater}, personal.email == email)
        return render_template("index.html", user=inputs, color=colors, value11=values[0], value12=values[1], value13=values[2], value14=values[3], value15=values[4], value16=values[5], value17=values[6], value21=values[7], value22=values[8], value23=values[9], value24=values[10], value25=values[11], value26=values[12], value27=values[13], value31=values[14], value32=values[15], value33=values[16], value34=values[17], value35=values[18], value36=values[19], value37=values[20], value41=values[21], value42=values[22], value43=values[23], value44=values[24], value45=values[25], value46=values[26], value47=values[27], value51=values[28], value52=values[29], value53=values[30], value54=values[31], value55=values[32], value56=values[33], value57=values[34], value61=values[35], value62=values[36], value63=values[37], value64=values[38], value65=values[39], value66=values[40], value67=values[41], value71=values[42], value72=values[43], value73=values[44], value74=values[45], value75=values[46], value76=values[47], value77=values[48], value81=values[49], value82=values[50], value83=values[51], value84=values[52], value85=values[53], value86=values[54], value87=values[55], value91=values[56], value92=values[57], value93=values[58], value94=values[59], value95=values[60], value96=values[61], value97=values[62], value101=values[63], value102=values[64], value103=values[65], value104=values[66], value105=values[67], value106=values[68], value107=values[69], value111=values[70], value112=values[71], value113=values[72], value114=values[73], value115=values[74], value116=values[75], value117=values[76], value121=values[77], value122=values[78], value123=values[79], value124=values[80], value125=values[81], value126=values[82], value127=values[83], value131=values[84], value132=values[85], value133=values[86], value134=values[87], value135=values[88], value136=values[89], value137=values[90], value141=values[91], value142=values[92], value143=values[93], value144=values[94], value145=values[95], value146=values[96], value147=values[97], value151=values[98], value152=values[99], value153=values[100], value154=values[101], value155=values[102], value156=values[103], value157=values[104], value161=values[105], value162=values[106], value163=values[107], value164=values[108], value165=values[109], value166=values[110], value167=values[111], value171=values[112], value172=values[113], value173=values[114], value174=values[115], value175=values[116], value176=values[117], value177=values[118], value181=values[119], value182=values[120], value183=values[121], value184=values[122], value185=values[123], value186=values[124], value187=values[125], value191=values[126], value192=values[127], value193=values[128], value194=values[129], value195=values[130], value196=values[131], value197=values[132], value201=values[133], value202=values[134], value203=values[135], value204=values[136], value205=values[137], value206=values[138], value207=values[139], value211=values[140], value212=values[141], value213=values[142], value214=values[143], value215=values[144], value216=values[145], value217=values[146], value221=values[147], value222=values[148], value223=values[149], value224=values[150], value225=values[151], value226=values[152], value227=values[153], value231=values[154], value232=values[155], value233=values[156], value234=values[157], value235=values[158], value236=values[159], value237=values[160], value241=values[161], value242=values[162], value243=values[163], value244=values[164], value245=values[165], value246=values[166], value247=values[167], value251=values[168], value252=values[169], value253=values[170], value254=values[171], value255=values[172], value256=values[173], value257=values[174], value261=values[175], value262=values[176], value263=values[177], value264=values[178], value265=values[179], value266=values[180], value267=values[181], value271=values[182], value272=values[183], value273=values[184], value274=values[185], value275=values[186], value276=values[187], value277=values[188], value281=values[189], value282=values[190], value283=values[191], value284=values[192], value285=values[193], value286=values[194], value287=values[195], value291=values[196], value292=values[197], value293=values[198], value294=values[199], value295=values[200], value296=values[201], value297=values[202], value301=values[203], value302=values[204], value303=values[205], value304=values[206], value305=values[207], value306=values[208], value307=values[209], value311=values[210], value312=values[211], value313=values[212], value314=values[213], value315=values[214], value316=values[215], value317=values[216], value321=values[217], value322=values[218], value323=values[219], value324=values[220], value325=values[221], value326=values[222], value327=values[223], value331=values[224], value332=values[225], value333=values[226], value334=values[227], value335=values[228], value336=values[229], value337=values[230], value341=values[231], value342=values[232], value343=values[233], value344=values[234], value345=values[235], value346=values[236], value347=values[237], value351=values[238], value352=values[239], value353=values[240], value354=values[241], value355=values[242], value356=values[243], value357=values[244], value361=values[245], value362=values[246], value363=values[247], value364=values[248], value365=values[249], value366=values[250], value367=values[251],value371=values[252], value372=values[253], value373=values[254], value374=values[255], value375=values[256], value376=values[257], value377=values[258], value381=values[259], value382=values[260], value383=values[261], value384=values[262], value385=values[263], value386=values[264], value387=values[265], value391=values[266], value392=values[267], value393=values[268], value394=values[269], value395=values[270], value396=values[271], value397=values[272], value401=values[273], value402=values[274], value403=values[275], value404=values[276], value405=values[277], value406=values[278], value407=values[279], value411=values[280], value412=values[281], value413=values[282], value414=values[283], value415=values[284], value416=values[285], value417=values[286], value421=values[287], value422=values[288], value423=values[289], value424=values[290], value425=values[291], value426=values[292], value427=values[293], value431=values[294], value432=values[295], value433=values[296], value434=values[297], value435=values[298], value436=values[299], value437=values[300], value441=values[301], value442=values[302], value443=values[303], value444=values[304], value445=values[305], value446=values[306], value447=values[307], value451=values[308], value452=values[309], value453=values[310], value454=values[311], value455=values[312], value456=values[313], value457=values[314], value461=values[315], value462=values[316], value463=values[317], value464=values[318], value465=values[319], value466=values[320], value467=values[321], value471=values[322], value472=values[323], value473=values[324], value474=values[325], value475=values[326], value476=values[327], value477=values[328], value481=values[329], value482=values[330], value483=values[331], value484=values[332], value485=values[333], value486=values[334], value487=values[335], value491=values[336], value492=values[337], value493=values[338], value494=values[339], value495=values[340], value496=values[341], value497=values[342], value501=values[343], value502=values[344], value503=values[345], value504=values[346], value505=values[347], value506=values[348], value507=values[349], value511=values[350], value512=values[351], value513=values[352], value514=values[353], value515=values[354], value516=values[355], value517=values[356], value521=values[357], value522=values[358], value523=values[359], value524=values[360], value525=values[361], value526=values[362], value527=values[363])
        
    return render_template("index.html", user=inputs, color=colors, value11=values[0], value12=values[1], value13=values[2], value14=values[3], value15=values[4], value16=values[5], value17=values[6], value21=values[7], value22=values[8], value23=values[9], value24=values[10], value25=values[11], value26=values[12], value27=values[13], value31=values[14], value32=values[15], value33=values[16], value34=values[17], value35=values[18], value36=values[19], value37=values[20], value41=values[21], value42=values[22], value43=values[23], value44=values[24], value45=values[25], value46=values[26], value47=values[27], value51=values[28], value52=values[29], value53=values[30], value54=values[31], value55=values[32], value56=values[33], value57=values[34], value61=values[35], value62=values[36], value63=values[37], value64=values[38], value65=values[39], value66=values[40], value67=values[41], value71=values[42], value72=values[43], value73=values[44], value74=values[45], value75=values[46], value76=values[47], value77=values[48], value81=values[49], value82=values[50], value83=values[51], value84=values[52], value85=values[53], value86=values[54], value87=values[55], value91=values[56], value92=values[57], value93=values[58], value94=values[59], value95=values[60], value96=values[61], value97=values[62], value101=values[63], value102=values[64], value103=values[65], value104=values[66], value105=values[67], value106=values[68], value107=values[69], value111=values[70], value112=values[71], value113=values[72], value114=values[73], value115=values[74], value116=values[75], value117=values[76], value121=values[77], value122=values[78], value123=values[79], value124=values[80], value125=values[81], value126=values[82], value127=values[83], value131=values[84], value132=values[85], value133=values[86], value134=values[87], value135=values[88], value136=values[89], value137=values[90], value141=values[91], value142=values[92], value143=values[93], value144=values[94], value145=values[95], value146=values[96], value147=values[97], value151=values[98], value152=values[99], value153=values[100], value154=values[101], value155=values[102], value156=values[103], value157=values[104], value161=values[105], value162=values[106], value163=values[107], value164=values[108], value165=values[109], value166=values[110], value167=values[111], value171=values[112], value172=values[113], value173=values[114], value174=values[115], value175=values[116], value176=values[117], value177=values[118], value181=values[119], value182=values[120], value183=values[121], value184=values[122], value185=values[123], value186=values[124], value187=values[125], value191=values[126], value192=values[127], value193=values[128], value194=values[129], value195=values[130], value196=values[131], value197=values[132], value201=values[133], value202=values[134], value203=values[135], value204=values[136], value205=values[137], value206=values[138], value207=values[139], value211=values[140], value212=values[141], value213=values[142], value214=values[143], value215=values[144], value216=values[145], value217=values[146], value221=values[147], value222=values[148], value223=values[149], value224=values[150], value225=values[151], value226=values[152], value227=values[153], value231=values[154], value232=values[155], value233=values[156], value234=values[157], value235=values[158], value236=values[159], value237=values[160], value241=values[161], value242=values[162], value243=values[163], value244=values[164], value245=values[165], value246=values[166], value247=values[167], value251=values[168], value252=values[169], value253=values[170], value254=values[171], value255=values[172], value256=values[173], value257=values[174], value261=values[175], value262=values[176], value263=values[177], value264=values[178], value265=values[179], value266=values[180], value267=values[181], value271=values[182], value272=values[183], value273=values[184], value274=values[185], value275=values[186], value276=values[187], value277=values[188], value281=values[189], value282=values[190], value283=values[191], value284=values[192], value285=values[193], value286=values[194], value287=values[195], value291=values[196], value292=values[197], value293=values[198], value294=values[199], value295=values[200], value296=values[201], value297=values[202], value301=values[203], value302=values[204], value303=values[205], value304=values[206], value305=values[207], value306=values[208], value307=values[209], value311=values[210], value312=values[211], value313=values[212], value314=values[213], value315=values[214], value316=values[215], value317=values[216], value321=values[217], value322=values[218], value323=values[219], value324=values[220], value325=values[221], value326=values[222], value327=values[223], value331=values[224], value332=values[225], value333=values[226], value334=values[227], value335=values[228], value336=values[229], value337=values[230], value341=values[231], value342=values[232], value343=values[233], value344=values[234], value345=values[235], value346=values[236], value347=values[237], value351=values[238], value352=values[239], value353=values[240], value354=values[241], value355=values[242], value356=values[243], value357=values[244], value361=values[245], value362=values[246], value363=values[247], value364=values[248], value365=values[249], value366=values[250], value367=values[251],value371=values[252], value372=values[253], value373=values[254], value374=values[255], value375=values[256], value376=values[257], value377=values[258], value381=values[259], value382=values[260], value383=values[261], value384=values[262], value385=values[263], value386=values[264], value387=values[265], value391=values[266], value392=values[267], value393=values[268], value394=values[269], value395=values[270], value396=values[271], value397=values[272], value401=values[273], value402=values[274], value403=values[275], value404=values[276], value405=values[277], value406=values[278], value407=values[279], value411=values[280], value412=values[281], value413=values[282], value414=values[283], value415=values[284], value416=values[285], value417=values[286], value421=values[287], value422=values[288], value423=values[289], value424=values[290], value425=values[291], value426=values[292], value427=values[293], value431=values[294], value432=values[295], value433=values[296], value434=values[297], value435=values[298], value436=values[299], value437=values[300], value441=values[301], value442=values[302], value443=values[303], value444=values[304], value445=values[305], value446=values[306], value447=values[307], value451=values[308], value452=values[309], value453=values[310], value454=values[311], value455=values[312], value456=values[313], value457=values[314], value461=values[315], value462=values[316], value463=values[317], value464=values[318], value465=values[319], value466=values[320], value467=values[321], value471=values[322], value472=values[323], value473=values[324], value474=values[325], value475=values[326], value476=values[327], value477=values[328], value481=values[329], value482=values[330], value483=values[331], value484=values[332], value485=values[333], value486=values[334], value487=values[335], value491=values[336], value492=values[337], value493=values[338], value494=values[339], value495=values[340], value496=values[341], value497=values[342], value501=values[343], value502=values[344], value503=values[345], value504=values[346], value505=values[347], value506=values[348], value507=values[349], value511=values[350], value512=values[351], value513=values[352], value514=values[353], value515=values[354], value516=values[355], value517=values[356], value521=values[357], value522=values[358], value523=values[359], value524=values[360], value525=values[361], value526=values[362], value527=values[363])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=75, debug=True)