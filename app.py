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

def findPass(email):
    for i in db.all():
        if i['email'] == email:
            return str(i['password'])
        
def findKey(email):
    for i in db.all():
        if i['email'] == email:
            return str(i['key'])
        
def findActivity(key):
    for i in db.all():
        if i['key'] == key:
            return str(i['activity'])
        
def findColor(key):
    for i in db.all():
        if i['key'] == key:
            return str(i['color'])

def findValue(key, value):
    for i in db.all():
        if i['key'] == key:
            return str(i[value])
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def success():
    if request.method == 'POST':
        global email
        if request.form['submit'] == 'Create account':
            return redirect('/create-account', code=302)
        if request.form['email'] in getEmail():
            email = request.form['email']
            return redirect('/password', code=302)
        return render_template('email.html', reject='Email does not exist', email=request.form['email'])
    return render_template('email.html', reject='')


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
            db.insert({'email': email, 'password':password, 'key': key, "activity": activity, "color": color, "value11": "", 
                       "value12": "", "value13": "", "value14": "", "value15": "", "value16": "", "value17": "", "value21": "", 
                       "value22": "", "value23": "", "value24": "", "value25": "", "value26": "", "value27": "", "value31": "", 
                       "value32": "", "value33": "", "value34": "", "value35": "", "value36": "", "value37": "", "value41": "", 
                       "value42": "", "value43": "", "value44": "", "value45": "", "value46": "", "value47": "", "value51": "", 
                       "value52": "", "value53": "", "value54": "", "value55": "", "value56": "", "value57": "", "value61": "", 
                       "value62": "", "value63": "", "value64": "", "value65": "", "value66": "", "value67": "", "value71": "", 
                       "value72": "", "value73": "", "value74": "", "value75": "", "value76": "", "value77": "", "value81": "", 
                       "value82": "", "value83": "", "value84": "", "value85": "", "value86": "", "value87": "", "value91": "", 
                       "value92": "", "value93": "", "value94": "", "value95": "", "value96": "", "value97": "", "value101": "", 
                       "value102": "", "value103": "", "value104": "", "value105": "", "value106": "", "value107": "", "value111": "", 
                       "value112": "", "value113": "", "value114": "", "value115": "", "value116": "", "value117": "", "value121": "", 
                       "value122": "", "value123": "", "value124": "", "value125": "", "value126": "", "value127": "", "value131": "", 
                       "value132": "", "value133": "", "value134": "", "value135": "", "value136": "", "value137": "", "value141": "", 
                       "value142": "", "value143": "", "value144": "", "value145": "", "value146": "", "value147": "", "value151": "", 
                       "value152": "", "value153": "", "value154": "", "value155": "", "value156": "", "value157": "", "value161": "", 
                       "value162": "", "value163": "", "value164": "", "value165": "", "value166": "", "value167": "", "value171": "", 
                       "value172": "", "value173": "", "value174": "", "value175": "", "value176": "", "value177": "", "value181": "", 
                       "value182": "", "value183": "", "value184": "", "value185": "", "value186": "", "value187": "", "value191": "", 
                       "value192": "", "value193": "", "value194": "", "value195": "", "value196": "", "value197": "", "value201": "", 
                       "value202": "", "value203": "", "value204": "", "value205": "", "value206": "", "value207": "", "value211": "", 
                       "value212": "", "value213": "", "value214": "", "value215": "", "value216": "", "value217": "", "value221": "", 
                       "value222": "", "value223": "", "value224": "", "value225": "", "value226": "", "value227": "", "value231": "", 
                       "value232": "", "value233": "", "value234": "", "value235": "", "value236": "", "value237": "", "value241": "", 
                       "value242": "", "value243": "", "value244": "", "value245": "", "value246": "", "value247": "", "value251": "", 
                       "value252": "", "value253": "", "value254": "", "value255": "", "value256": "", "value257": "", "value261": "", 
                       "value262": "", "value263": "", "value264": "", "value265": "", "value266": "", "value267": "", "value271": "", 
                       "value272": "", "value273": "", "value274": "", "value275": "", "value276": "", "value277": "", "value281": "", 
                       "value282": "", "value283": "", "value284": "", "value285": "", "value286": "", "value287": "", "value291": "", 
                       "value292": "", "value293": "", "value294": "", "value295": "", "value296": "", "value297": "", "value301": "", 
                       "value302": "", "value303": "", "value304": "", "value305": "", "value306": "", "value307": "", "value311": "", 
                       "value312": "", "value313": "", "value314": "", "value315": "", "value316": "", "value317": "", "value321": "", 
                       "value322": "", "value323": "", "value324": "", "value325": "", "value326": "", "value327": "", "value331": "", 
                       "value332": "", "value333": "", "value334": "", "value335": "", "value336": "", "value337": "", "value341": "", 
                       "value342": "", "value343": "", "value344": "", "value345": "", "value346": "", "value347": "", "value351": "", 
                       "value352": "", "value353": "", "value354": "", "value355": "", "value356": "", "value357": "", "value361": "", 
                       "value362": "", "value363": "", "value364": "", "value365": "", "value366": "", "value367": "", "value371": "", 
                       "value372": "", "value373": "", "value374": "", "value375": "", "value376": "", "value377": "", "value381": "", 
                       "value382": "", "value383": "", "value384": "", "value385": "", "value386": "", "value387": "", "value391": "", 
                       "value392": "", "value393": "", "value394": "", "value395": "", "value396": "", "value397": "", "value401": "", 
                       "value402": "", "value403": "", "value404": "", "value405": "", "value406": "", "value407": "", "value411": "", 
                       "value412": "", "value413": "", "value414": "", "value415": "", "value416": "", "value417": "", "value421": "", 
                       "value422": "", "value423": "", "value424": "", "value425": "", "value426": "", "value427": "", "value431": "", 
                       "value432": "", "value433": "", "value434": "", "value435": "", "value436": "", "value437": "", "value441": "", 
                       "value442": "", "value443": "", "value444": "", "value445": "", "value446": "", "value447": "", "value451": "", 
                       "value452": "", "value453": "", "value454": "", "value455": "", "value456": "", "value457": "", "value461": "", 
                       "value462": "", "value463": "", "value464": "", "value465": "", "value466": "", "value467": "", "value471": "", 
                       "value472": "", "value473": "", "value474": "", "value475": "", "value476": "", "value477": "", "value481": "", 
                       "value482": "", "value483": "", "value484": "", "value485": "", "value486": "", "value487": "", "value491": "", 
                       "value492": "", "value493": "", "value494": "", "value495": "", "value496": "", "value497": "", "value501": "", 
                       "value502": "", "value503": "", "value504": "", "value505": "", "value506": "", "value507": "", "value511": "", 
                       "value512": "", "value513": "", "value514": "", "value515": "", "value516": "", "value517": "", "value521": "", 
                       "value522": "", "value523": "", "value524": "", "value525": "", "value526": "", "value527": "", })
            return redirect('/', code=302)
        else:
            if email in getEmail():
                print(getEmail())
                return render_template('create.html', wrong='username is already used', email=email, password=password)
    return render_template('create.html', wrong='')




        
    

@app.route('/password', methods=['POST', 'GET'])

def password():
    global inputs
    if request.method == 'POST':
        password = request.form['password']
        if request.form['password'] == findPass(email):
            inputs = []
            key = findKey(email)
            return redirect(url_for('home', key=key), code=302)
        else:
            return render_template('password.html', wrong='Password incorrect', reset=request.form['password'])
    return render_template('password.html', wrong='')

@app.route("/home/<key>", methods=['POST', 'GET'])



def home(key):
    global updater
    time_list = ["8:00AM", "8:15AM", "8:30AM", "8:45AM", "9:00AM", "9:15AM", "9:30AM", "9:45AM", "10:00AM", "10:15AM", "10:30AM", "10:45AM", "11:00AM", "11:15AM", "11:30AM", "11:45PM", "12:00PM", "12:15PM", "12:30PM", "12:45PM", "1:00PM", "1:15PM", "1:30PM", "1:45PM", "2:00PM", "2:15PM", "2:30PM", "2:45PM", "3:00PM", "3:15PM", "3:30PM", "3:45PM", "4:00PM", "4:15PM", "4:30PM", "4:45PM", "5:00PM", "5:15PM", "5:30PM", "5:45PM", "6:00PM", "6:15PM", "6:30PM", "6:45PM", "7:00PM", "7:15PM", "7:30PM", "7:45PM", "8:00PM", "8:15PM", "8:30PM", "8:45PM"]
    inputs = findActivity(key).split()
    colors = findColor(key).split()
    value11 = findValue(key, "value11")
    value12 = findValue(key, "value12")
    value13 = findValue(key, "value13")
    value14 = findValue(key, "value14")
    value15 = findValue(key, "value15")
    value16 = findValue(key, "value16")
    value17 = findValue(key, "value17")
    value21 = findValue(key, "value21")
    value22 = findValue(key, "value22")
    value23 = findValue(key, "value23")
    value24 = findValue(key, "value24")
    value25 = findValue(key, "value25")
    value26 = findValue(key, "value26")
    value27 = findValue(key, "value27")
    value31 = findValue(key, "value31")
    value32 = findValue(key, "value32")
    value33 = findValue(key, "value33")
    value34 = findValue(key, "value34")
    value35 = findValue(key, "value35")
    value36 = findValue(key, "value36")
    value37 = findValue(key, "value37")
    value41 = findValue(key, "value41")
    value42 = findValue(key, "value42")
    value43 = findValue(key, "value43")
    value44 = findValue(key, "value44")
    value45 = findValue(key, "value45")
    value46 = findValue(key, "value46")
    value47 = findValue(key, "value47")
    value51 = findValue(key, "value51")
    value52 = findValue(key, "value52")
    value53 = findValue(key, "value53")
    value54 = findValue(key, "value54")
    value55 = findValue(key, "value55")
    value56 = findValue(key, "value56")
    value57 = findValue(key, "value57")
    value61 = findValue(key, "value61")
    value62 = findValue(key, "value62")
    value63 = findValue(key, "value63")
    value64 = findValue(key, "value64")
    value65 = findValue(key, "value65")
    value66 = findValue(key, "value66")
    value67 = findValue(key, "value67")
    value71 = findValue(key, "value71")
    value72 = findValue(key, "value72")
    value73 = findValue(key, "value73")
    value74 = findValue(key, "value74")
    value75 = findValue(key, "value75")
    value76 = findValue(key, "value76")
    value77 = findValue(key, "value77")
    value81 = findValue(key, "value81")
    value82 = findValue(key, "value82")
    value83 = findValue(key, "value83")
    value84 = findValue(key, "value84")
    value85 = findValue(key, "value85")
    value86 = findValue(key, "value86")
    value87 = findValue(key, "value87")
    value91 = findValue(key, "value91")
    value92 = findValue(key, "value92")
    value93 = findValue(key, "value93")
    value94 = findValue(key, "value94")
    value95 = findValue(key, "value95")
    value96 = findValue(key, "value96")
    value97 = findValue(key, "value97")
    value101 = findValue(key, "value101")
    value102 = findValue(key, "value102")
    value103 = findValue(key, "value103")
    value104 = findValue(key, "value104")
    value105 = findValue(key, "value105")
    value106 = findValue(key, "value106")
    value107 = findValue(key, "value107")
    value111 = findValue(key, "value111")
    value112 = findValue(key, "value112")
    value113 = findValue(key, "value113")
    value114 = findValue(key, "value114")
    value115 = findValue(key, "value115")
    value116 = findValue(key, "value116")
    value117 = findValue(key, "value117")
    value121 = findValue(key, "value121")
    value122 = findValue(key, "value122")
    value123 = findValue(key, "value123")
    value124 = findValue(key, "value124")
    value125 = findValue(key, "value125")
    value126 = findValue(key, "value126")
    value127 = findValue(key, "value127")
    value131 = findValue(key, "value131")
    value132 = findValue(key, "value132")
    value133 = findValue(key, "value133")
    value134 = findValue(key, "value134")
    value135 = findValue(key, "value135")
    value136 = findValue(key, "value136")
    value137 = findValue(key, "value137")
    value141 = findValue(key, "value141")
    value142 = findValue(key, "value142")
    value143 = findValue(key, "value143")
    value144 = findValue(key, "value144")
    value145 = findValue(key, "value145")
    value146 = findValue(key, "value146")
    value147 = findValue(key, "value147")
    value151 = findValue(key, "value151")
    value152 = findValue(key, "value152")
    value153 = findValue(key, "value153")
    value154 = findValue(key, "value154")
    value155 = findValue(key, "value155")
    value156 = findValue(key, "value156")
    value157 = findValue(key, "value157")
    value161 = findValue(key, "value161")
    value162 = findValue(key, "value162")
    value163 = findValue(key, "value163")
    value164 = findValue(key, "value164")
    value165 = findValue(key, "value165")
    value166 = findValue(key, "value166")
    value167 = findValue(key, "value167")
    value171 = findValue(key, "value171")
    value172 = findValue(key, "value172")
    value173 = findValue(key, "value173")
    value174 = findValue(key, "value174")
    value175 = findValue(key, "value175")
    value176 = findValue(key, "value176")
    value177 = findValue(key, "value177")
    value181 = findValue(key, "value181")
    value182 = findValue(key, "value182")
    value183 = findValue(key, "value183")
    value184 = findValue(key, "value184")
    value185 = findValue(key, "value185")
    value186 = findValue(key, "value186")
    value187 = findValue(key, "value187")
    value191 = findValue(key, "value191")
    value192 = findValue(key, "value192")
    value193 = findValue(key, "value193")
    value194 = findValue(key, "value194")
    value195 = findValue(key, "value195")
    value196 = findValue(key, "value196")
    value197 = findValue(key, "value197")
    value201 = findValue(key, "value201")
    value202 = findValue(key, "value202")
    value203 = findValue(key, "value203")
    value204 = findValue(key, "value204")
    value205 = findValue(key, "value205")
    value206 = findValue(key, "value206")
    value207 = findValue(key, "value207")
    value211 = findValue(key, "value211")
    value212 = findValue(key, "value212")
    value213 = findValue(key, "value213")
    value214 = findValue(key, "value214")
    value215 = findValue(key, "value215")
    value216 = findValue(key, "value216")
    value217 = findValue(key, "value217")
    value221 = findValue(key, "value221")
    value222 = findValue(key, "value222")
    value223 = findValue(key, "value223")
    value224 = findValue(key, "value224")
    value225 = findValue(key, "value225")
    value226 = findValue(key, "value226")
    value227 = findValue(key, "value227")
    value231 = findValue(key, "value231")
    value232 = findValue(key, "value232")
    value233 = findValue(key, "value233")
    value234 = findValue(key, "value234")
    value235 = findValue(key, "value235")
    value236 = findValue(key, "value236")
    value237 = findValue(key, "value237")
    value241 = findValue(key, "value241")
    value242 = findValue(key, "value242")
    value243 = findValue(key, "value243")
    value244 = findValue(key, "value244")
    value245 = findValue(key, "value245")
    value246 = findValue(key, "value246")
    value247 = findValue(key, "value247")
    value251 = findValue(key, "value251")
    value252 = findValue(key, "value252")
    value253 = findValue(key, "value253")
    value254 = findValue(key, "value254")
    value255 = findValue(key, "value255")
    value256 = findValue(key, "value256")
    value257 = findValue(key, "value257")
    value261 = findValue(key, "value261")
    value262 = findValue(key, "value262")
    value263 = findValue(key, "value263")
    value264 = findValue(key, "value264")
    value265 = findValue(key, "value265")
    value266 = findValue(key, "value266")
    value267 = findValue(key, "value267")
    value271 = findValue(key, "value271")
    value272 = findValue(key, "value272")
    value273 = findValue(key, "value273")
    value274 = findValue(key, "value274")
    value275 = findValue(key, "value275")
    value276 = findValue(key, "value276")
    value277 = findValue(key, "value277")
    value281 = findValue(key, "value281")
    value282 = findValue(key, "value282")
    value283 = findValue(key, "value283")
    value284 = findValue(key, "value284")
    value285 = findValue(key, "value285")
    value286 = findValue(key, "value286")
    value287 = findValue(key, "value287")
    value291 = findValue(key, "value291")
    value292 = findValue(key, "value292")
    value293 = findValue(key, "value293")
    value294 = findValue(key, "value294")
    value295 = findValue(key, "value295")
    value296 = findValue(key, "value296")
    value297 = findValue(key, "value297")
    value301 = findValue(key, "value301")
    value302 = findValue(key, "value302")
    value303 = findValue(key, "value303")
    value304 = findValue(key, "value304")
    value305 = findValue(key, "value305")
    value306 = findValue(key, "value306")
    value307 = findValue(key, "value307")
    value311 = findValue(key, "value311")
    value312 = findValue(key, "value312")
    value313 = findValue(key, "value313")
    value314 = findValue(key, "value314")
    value315 = findValue(key, "value315")
    value316 = findValue(key, "value316")
    value317 = findValue(key, "value317")
    value321 = findValue(key, "value321")
    value322 = findValue(key, "value322")
    value323 = findValue(key, "value323")
    value324 = findValue(key, "value324")
    value325 = findValue(key, "value325")
    value326 = findValue(key, "value326")
    value327 = findValue(key, "value327")
    value331 = findValue(key, "value331")
    value332 = findValue(key, "value332")
    value333 = findValue(key, "value333")
    value334 = findValue(key, "value334")
    value335 = findValue(key, "value335")
    value336 = findValue(key, "value336")
    value337 = findValue(key, "value337")
    value341 = findValue(key, "value341")
    value342 = findValue(key, "value342")
    value343 = findValue(key, "value343")
    value344 = findValue(key, "value344")
    value345 = findValue(key, "value345")
    value346 = findValue(key, "value346")
    value347 = findValue(key, "value347")
    value351 = findValue(key, "value351")
    value352 = findValue(key, "value352")
    value353 = findValue(key, "value353")
    value354 = findValue(key, "value354")
    value355 = findValue(key, "value355")
    value356 = findValue(key, "value356")
    value357 = findValue(key, "value357")
    value361 = findValue(key, "value361")
    value362 = findValue(key, "value362")
    value363 = findValue(key, "value363")
    value364 = findValue(key, "value364")
    value365 = findValue(key, "value365")
    value366 = findValue(key, "value366")
    value367 = findValue(key, "value367")
    value371 = findValue(key, "value371")
    value372 = findValue(key, "value372")
    value373 = findValue(key, "value373")
    value374 = findValue(key, "value374")
    value375 = findValue(key, "value375")
    value376 = findValue(key, "value376")
    value377 = findValue(key, "value377")
    value381 = findValue(key, "value381")
    value382 = findValue(key, "value382")
    value383 = findValue(key, "value383")
    value384 = findValue(key, "value384")
    value385 = findValue(key, "value385")
    value386 = findValue(key, "value386")
    value387 = findValue(key, "value387")
    value391 = findValue(key, "value391")
    value392 = findValue(key, "value392")
    value393 = findValue(key, "value393")
    value394 = findValue(key, "value394")
    value395 = findValue(key, "value395")
    value396 = findValue(key, "value396")
    value397 = findValue(key, "value397")
    value401 = findValue(key, "value401")
    value402 = findValue(key, "value402")
    value403 = findValue(key, "value403")
    value404 = findValue(key, "value404")
    value405 = findValue(key, "value405")
    value406 = findValue(key, "value406")
    value407 = findValue(key, "value407")
    value411 = findValue(key, "value411")
    value412 = findValue(key, "value412")
    value413 = findValue(key, "value413")
    value414 = findValue(key, "value414")
    value415 = findValue(key, "value415")
    value416 = findValue(key, "value416")
    value417 = findValue(key, "value417")
    value421 = findValue(key, "value421")
    value422 = findValue(key, "value422")
    value423 = findValue(key, "value423")
    value424 = findValue(key, "value424")
    value425 = findValue(key, "value425")
    value426 = findValue(key, "value426")
    value427 = findValue(key, "value427")
    value431 = findValue(key, "value431")
    value432 = findValue(key, "value432")
    value433 = findValue(key, "value433")
    value434 = findValue(key, "value434")
    value435 = findValue(key, "value435")
    value436 = findValue(key, "value436")
    value437 = findValue(key, "value437")
    value441 = findValue(key, "value441")
    value442 = findValue(key, "value442")
    value443 = findValue(key, "value443")
    value444 = findValue(key, "value444")
    value445 = findValue(key, "value445")
    value446 = findValue(key, "value446")
    value447 = findValue(key, "value447")
    value451 = findValue(key, "value451")
    value452 = findValue(key, "value452")
    value453 = findValue(key, "value453")
    value454 = findValue(key, "value454")
    value455 = findValue(key, "value455")
    value456 = findValue(key, "value456")
    value457 = findValue(key, "value457")
    value461 = findValue(key, "value461")
    value462 = findValue(key, "value462")
    value463 = findValue(key, "value463")
    value464 = findValue(key, "value464")
    value465 = findValue(key, "value465")
    value466 = findValue(key, "value466")
    value467 = findValue(key, "value467")
    value471 = findValue(key, "value471")
    value472 = findValue(key, "value472")
    value473 = findValue(key, "value473")
    value474 = findValue(key, "value474")
    value475 = findValue(key, "value475")
    value476 = findValue(key, "value476")
    value477 = findValue(key, "value477")
    value481 = findValue(key, "value481")
    value482 = findValue(key, "value482")
    value483 = findValue(key, "value483")
    value484 = findValue(key, "value484")
    value485 = findValue(key, "value485")
    value486 = findValue(key, "value486")
    value487 = findValue(key, "value487")
    value491 = findValue(key, "value491")
    value492 = findValue(key, "value492")
    value493 = findValue(key, "value493")
    value494 = findValue(key, "value494")
    value495 = findValue(key, "value495")
    value496 = findValue(key, "value496")
    value497 = findValue(key, "value497")
    value501 = findValue(key, "value501")
    value502 = findValue(key, "value502")
    value503 = findValue(key, "value503")
    value504 = findValue(key, "value504")
    value505 = findValue(key, "value505")
    value506 = findValue(key, "value506")
    value507 = findValue(key, "value507")
    value511 = findValue(key, "value511")
    value512 = findValue(key, "value512")
    value513 = findValue(key, "value513")
    value514 = findValue(key, "value514")
    value515 = findValue(key, "value515")
    value516 = findValue(key, "value516")
    value517 = findValue(key, "value517")
    value521 = findValue(key, "value521")
    value522 = findValue(key, "value522")
    value523 = findValue(key, "value523")
    value524 = findValue(key, "value524")
    value525 = findValue(key, "value525")
    value526 = findValue(key, "value526")
    value527 = findValue(key, "value527")
    
    if request.method == "POST":
        submit = request.form['submit']
        if submit == "Remove":
            time1 = request.form['remove_time1']
            time2 = request.form['remove_time2']
            days = request.form.getlist('remove_days')
            
            if time1 == "8:00AM" and "Monday" in days:
                value11 = ""
            if time1 == "8:15AM" and "Monday" in days:
                value21 = ""
            if time1 == "8:30AM" and "Monday" in days:
                value31 = ""
            if time1 == "8:45AM" and "Monday" in days:
                value41 = ""
            if time1 == "9:00AM" and "Monday" in days:
                value51 = ""
            if time1 == "9:15AM" and "Monday" in days:
                value61 = ""
            if time1 == "9:30AM" and "Monday" in days:
                value71 = ""
            if time1 == "9:45AM" and "Monday" in days:
                value81 = ""
            if time1 == "10:00AM" and "Monday" in days:
                value91 = ""
            if time1 == "10:15AM" and "Monday" in days:
                value101 = ""
            if time1 == "10:30AM" and "Monday" in days:
                value111 = ""
            if time1 == "10:45AM" and "Monday" in days:
                value121 = ""
            if time1 == "11:00AM" and "Monday" in days:
                value131 = ""
            if time1 == "11:15AM" and "Monday" in days:
                value141 = ""
            if time1 == "11:30AM" and "Monday" in days:
                value151 = ""
            if time1 == "11:45AM" and "Monday" in days:
                value161 = ""
            if time1 == "12:00PM" and "Monday" in days:
                value171 = ""
            if time1 == "12:15PM" and "Monday" in days:
                value181 = ""
            if time1 == "12:30PM" and "Monday" in days:
                value191 = ""
            if time1 == "12:45PM" and "Monday" in days:
                value201 = ""
            if time1 == "1:00PM" and "Monday" in days:
                value211 = ""
            if time1 == "1:15PM" and "Monday" in days:
                value221 = ""
            if time1 == "1:30PM" and "Monday" in days:
                value231 = ""
            if time1 == "1:45PM" and "Monday" in days:
                value241 = ""
            if time1 == "2:00PM" and "Monday" in days:
                value251 = ""
            if time1 == "2:15PM" and "Monday" in days:
                value261 = ""
            if time1 == "2:30PM" and "Monday" in days:
                value271 = ""
            if time1 == "2:45PM" and "Monday" in days:
                value281 = ""
            if time1 == "3:00PM" and "Monday" in days:
                value291 = ""
            if time1 == "3:15PM" and "Monday" in days:
                value301 = ""
            if time1 == "3:30PM" and "Monday" in days:
                value311 = ""
            if time1 == "3:45PM" and "Monday" in days:
                value321 = ""
            if time1 == "4:00PM" and "Monday" in days:
                value331 = ""
            if time1 == "4:15PM" and "Monday" in days:
                value341 = ""
            if time1 == "4:30PM" and "Monday" in days:
                value351 = ""
            if time1 == "4:45PM" and "Monday" in days:
                value361 = ""
            if time1 == "5:00PM" and "Monday" in days:
                value371 = ""
            if time1 == "5:15PM" and "Monday" in days:
                value381 = ""
            if time1 == "5:30PM" and "Monday" in days:
                value391 = ""
            if time1 == "5:45PM" and "Monday" in days:
                value401 = ""
            if time1 == "6:00PM" and "Monday" in days:
                value411 = ""
            if time1 == "6:15PM" and "Monday" in days:
                value421 = ""
            if time1 == "6:30PM" and "Monday" in days:
                value431 = ""
            if time1 == "6:45PM" and "Monday" in days:
                value441 = ""
            if time1 == "7:00PM" and "Monday" in days:
                value451 = ""
            if time1 == "7:15PM" and "Monday" in days:
                value461 = ""
            if time1 == "7:30PM" and "Monday" in days:
                value471 = ""
            if time1 == "7:45PM" and "Monday" in days:
                value481 = ""
            if time1 == "8:00PM" and "Monday" in days:
                value491 = ""
            if time1 == "8:15PM" and "Monday" in days:
                value501 = ""
            if time1 == "8:30PM" and "Monday" in days:
                value511 = ""
            if time1 == "8:45PM" and "Monday" in days:
                value521 = ""
            
            
            
            if time1 == "8:00AM" and "Tuesday" in days:
                value12 = ""
            if time1 == "8:15AM" and "Tuesday" in days:
                value22 = ""
            if time1 == "8:30AM" and "Tuesday" in days:
                value32 = ""
            if time1 == "8:45AM" and "Tuesday" in days:
                value42 = ""
            if time1 == "9:00AM" and "Tuesday" in days:
                value52 = ""
            if time1 == "9:15AM" and "Tuesday" in days:
                value62 = ""
            if time1 == "9:30AM" and "Tuesday" in days:
                value72 = ""
            if time1 == "9:45AM" and "Tuesday" in days:
                value82 = ""
            if time1 == "10:00AM" and "Tuesday" in days:
                value92 = ""
            if time1 == "10:15AM" and "Tuesday" in days:
                value102 = ""
            if time1 == "10:30AM" and "Tuesday" in days:
                value112 = ""
            if time1 == "10:45AM" and "Tuesday" in days:
                value122 = ""
            if time1 == "11:00AM" and "Tuesday" in days:
                value132 = ""
            if time1 == "11:15AM" and "Tuesday" in days:
                value142 = ""
            if time1 == "11:30AM" and "Tuesday" in days:
                value152 = ""
            if time1 == "11:45AM" and "Tuesday" in days:
                value162 = ""
            if time1 == "12:00PM" and "Tuesday" in days:
                value172 = ""
            if time1 == "12:15PM" and "Tuesday" in days:
                value182 = ""
            if time1 == "12:30PM" and "Tuesday" in days:
                value192 = ""
            if time1 == "12:45PM" and "Tuesday" in days:
                value202 = ""
            if time1 == "1:00PM" and "Tuesday" in days:
                value212 = ""
            if time1 == "1:15PM" and "Tuesday" in days:
                value222 = ""
            if time1 == "1:30PM" and "Tuesday" in days:
                value232 = ""
            if time1 == "1:45PM" and "Tuesday" in days:
                value242 = ""
            if time1 == "2:00PM" and "Tuesday" in days:
                value252 = ""
            if time1 == "2:15PM" and "Tuesday" in days:
                value262 = ""
            if time1 == "2:30PM" and "Tuesday" in days:
                value272 = ""
            if time1 == "2:45PM" and "Tuesday" in days:
                value282 = ""
            if time1 == "3:00PM" and "Tuesday" in days:
                value292 = ""
            if time1 == "3:15PM" and "Tuesday" in days:
                value302 = ""
            if time1 == "3:30PM" and "Tuesday" in days:
                value312 = ""
            if time1 == "3:45PM" and "Tuesday" in days:
                value322 = ""
            if time1 == "4:00PM" and "Tuesday" in days:
                value332 = ""
            if time1 == "4:15PM" and "Tuesday" in days:
                value342 = ""
            if time1 == "4:30PM" and "Tuesday" in days:
                value352 = ""
            if time1 == "4:45PM" and "Tuesday" in days:
                value362 = ""
            if time1 == "5:00PM" and "Tuesday" in days:
                value372 = ""
            if time1 == "5:15PM" and "Tuesday" in days:
                value382 = ""
            if time1 == "5:30PM" and "Tuesday" in days:
                value392 = ""
            if time1 == "5:45PM" and "Tuesday" in days:
                value402 = ""
            if time1 == "6:00PM" and "Tuesday" in days:
                value412 = ""
            if time1 == "6:15PM" and "Tuesday" in days:
                value422 = ""
            if time1 == "6:30PM" and "Tuesday" in days:
                value432 = ""
            if time1 == "6:45PM" and "Tuesday" in days:
                value442 = ""
            if time1 == "7:00PM" and "Tuesday" in days:
                value452 = ""
            if time1 == "7:15PM" and "Tuesday" in days:
                value462 = ""
            if time1 == "7:30PM" and "Tuesday" in days:
                value472 = ""
            if time1 == "7:45PM" and "Tuesday" in days:
                value482 = ""
            if time1 == "8:00PM" and "Tuesday" in days:
                value492 = ""
            if time1 == "8:15PM" and "Tuesday" in days:
                value502 = ""
            if time1 == "8:30PM" and "Tuesday" in days:
                value512 = ""
            if time1 == "8:45PM" and "Tuesday" in days:
                value522 = ""
            
            
            if time1 == "8:00AM" and "Wednesday" in days:
                value13 = ""
            if time1 == "8:15AM" and "Wednesday" in days:
                value23 = ""
            if time1 == "8:30AM" and "Wednesday" in days:
                value33 = ""
            if time1 == "8:45AM" and "Wednesday" in days:
                value43 = ""
            if time1 == "9:00AM" and "Wednesday" in days:
                value53 = ""
            if time1 == "9:15AM" and "Wednesday" in days:
                value63 = ""
            if time1 == "9:30AM" and "Wednesday" in days:
                value73 = ""
            if time1 == "9:45AM" and "Wednesday" in days:
                value83 = ""
            if time1 == "10:00AM" and "Wednesday" in days:
                value93 = ""
            if time1 == "10:15AM" and "Wednesday" in days:
                value103 = ""
            if time1 == "10:30AM" and "Wednesday" in days:
                value113 = ""
            if time1 == "10:45AM" and "Wednesday" in days:
                value123 = ""
            if time1 == "11:00AM" and "Wednesday" in days:
                value133 = ""
            if time1 == "11:15AM" and "Wednesday" in days:
                value143 = ""
            if time1 == "11:30AM" and "Wednesday" in days:
                value153 = ""
            if time1 == "11:45AM" and "Wednesday" in days:
                value163 = ""
            if time1 == "12:00PM" and "Wednesday" in days:
                value173 = ""
            if time1 == "12:15PM" and "Wednesday" in days:
                value183 = ""
            if time1 == "12:30PM" and "Wednesday" in days:
                value193 = ""
            if time1 == "12:45PM" and "Wednesday" in days:
                value203 = ""
            if time1 == "1:00PM" and "Wednesday" in days:
                value213 = ""
            if time1 == "1:15PM" and "Wednesday" in days:
                value223 = ""
            if time1 == "1:30PM" and "Wednesday" in days:
                value233 = ""
            if time1 == "1:45PM" and "Wednesday" in days:
                value243 = ""
            if time1 == "2:00PM" and "Wednesday" in days:
                value253 = ""
            if time1 == "2:15PM" and "Wednesday" in days:
                value263 = ""
            if time1 == "2:30PM" and "Wednesday" in days:
                value273 = ""
            if time1 == "2:45PM" and "Wednesday" in days:
                value283 = ""
            if time1 == "3:00PM" and "Wednesday" in days:
                value293 = ""
            if time1 == "3:15PM" and "Wednesday" in days:
                value303 = ""
            if time1 == "3:30PM" and "Wednesday" in days:
                value313 = ""
            if time1 == "3:45PM" and "Wednesday" in days:
                value323 = ""
            if time1 == "4:00PM" and "Wednesday" in days:
                value333 = ""
            if time1 == "4:15PM" and "Wednesday" in days:
                value343 = ""
            if time1 == "4:30PM" and "Wednesday" in days:
                value353 = ""
            if time1 == "4:45PM" and "Wednesday" in days:
                value363 = ""
            if time1 == "5:00PM" and "Wednesday" in days:
                value373 = ""
            if time1 == "5:15PM" and "Wednesday" in days:
                value383 = ""
            if time1 == "5:30PM" and "Wednesday" in days:
                value393 = ""
            if time1 == "5:45PM" and "Wednesday" in days:
                value403 = ""
            if time1 == "6:00PM" and "Wednesday" in days:
                value413 = ""
            if time1 == "6:15PM" and "Wednesday" in days:
                value423 = ""
            if time1 == "6:30PM" and "Wednesday" in days:
                value433 = ""
            if time1 == "6:45PM" and "Wednesday" in days:
                value443 = ""
            if time1 == "7:00PM" and "Wednesday" in days:
                value453 = ""
            if time1 == "7:15PM" and "Wednesday" in days:
                value463 = ""
            if time1 == "7:30PM" and "Wednesday" in days:
                value473 = ""
            if time1 == "7:45PM" and "Wednesday" in days:
                value483 = ""
            if time1 == "8:00PM" and "Wednesday" in days:
                value493 = ""
            if time1 == "8:15PM" and "Wednesday" in days:
                value503 = ""
            if time1 == "8:30PM" and "Wednesday" in days:
                value513 = ""
            if time1 == "8:45PM" and "Wednesday" in days:
                value523 = ""
            
            
            if time1 == "8:00AM" and "Thursday" in days:
                value14 = ""
            if time1 == "8:15AM" and "Thursday" in days:
                value24 = ""
            if time1 == "8:30AM" and "Thursday" in days:
                value34 = ""
            if time1 == "8:45AM" and "Thursday" in days:
                value44 = ""
            if time1 == "9:00AM" and "Thursday" in days:
                value54 = ""
            if time1 == "9:15AM" and "Thursday" in days:
                value64 = ""
            if time1 == "9:30AM" and "Thursday" in days:
                value74 = ""
            if time1 == "9:45AM" and "Thursday" in days:
                value84 = ""
            if time1 == "10:00AM" and "Thursday" in days:
                value94 = ""
            if time1 == "10:15AM" and "Thursday" in days:
                value104 = ""
            if time1 == "10:30AM" and "Thursday" in days:
                value114 = ""
            if time1 == "10:45AM" and "Thursday" in days:
                value124 = ""
            if time1 == "11:00AM" and "Thursday" in days:
                value134 = ""
            if time1 == "11:15AM" and "Thursday" in days:
                value144 = ""
            if time1 == "11:30AM" and "Thursday" in days:
                value154 = ""
            if time1 == "11:45AM" and "Thursday" in days:
                value164 = ""
            if time1 == "12:00PM" and "Thursday" in days:
                value174 = ""
            if time1 == "12:15PM" and "Thursday" in days:
                value184 = ""
            if time1 == "12:30PM" and "Thursday" in days:
                value194 = ""
            if time1 == "12:45PM" and "Thursday" in days:
                value204 = ""
            if time1 == "1:00PM" and "Thursday" in days:
                value214 = ""
            if time1 == "1:15PM" and "Thursday" in days:
                value224 = ""
            if time1 == "1:30PM" and "Thursday" in days:
                value234 = ""
            if time1 == "1:45PM" and "Thursday" in days:
                value244 = ""
            if time1 == "2:00PM" and "Thursday" in days:
                value254 = ""
            if time1 == "2:15PM" and "Thursday" in days:
                value264 = ""
            if time1 == "2:30PM" and "Thursday" in days:
                value274 = ""
            if time1 == "2:45PM" and "Thursday" in days:
                value284 = ""
            if time1 == "3:00PM" and "Thursday" in days:
                value294 = ""
            if time1 == "3:15PM" and "Thursday" in days:
                value304 = ""
            if time1 == "3:30PM" and "Thursday" in days:
                value314 = ""
            if time1 == "3:45PM" and "Thursday" in days:
                value324 = ""
            if time1 == "4:00PM" and "Thursday" in days:
                value334 = ""
            if time1 == "4:15PM" and "Thursday" in days:
                value344 = ""
            if time1 == "4:30PM" and "Thursday" in days:
                value354 = ""
            if time1 == "4:45PM" and "Thursday" in days:
                value364 = ""
            if time1 == "5:00PM" and "Thursday" in days:
                value374 = ""
            if time1 == "5:15PM" and "Thursday" in days:
                value384 = ""
            if time1 == "5:30PM" and "Thursday" in days:
                value394 = ""
            if time1 == "5:45PM" and "Thursday" in days:
                value404 = ""
            if time1 == "6:00PM" and "Thursday" in days:
                value414 = ""
            if time1 == "6:15PM" and "Thursday" in days:
                value424 = ""
            if time1 == "6:30PM" and "Thursday" in days:
                value434 = ""
            if time1 == "6:45PM" and "Thursday" in days:
                value444 = ""
            if time1 == "7:00PM" and "Thursday" in days:
                value454 = ""
            if time1 == "7:15PM" and "Thursday" in days:
                value464 = ""
            if time1 == "7:30PM" and "Thursday" in days:
                value474 = ""
            if time1 == "7:45PM" and "Thursday" in days:
                value484 = ""
            if time1 == "8:00PM" and "Thursday" in days:
                value494 = ""
            if time1 == "8:15PM" and "Thursday" in days:
                value504 = ""
            if time1 == "8:30PM" and "Thursday" in days:
                value514 = ""
            if time1 == "8:45PM" and "Thursday" in days:
                value524 = ""
        
            if time1 == "8:00AM" and "Friday" in days:
                value15 =""
            if time1 == "8:15AM" and "Friday" in days:
                value25 =""
            if time1 == "8:30AM" and "Friday" in days:
                value35 =""
            if time1 == "8:45AM" and "Friday" in days:
                value45 =""
            if time1 == "9:00AM" and "Friday" in days:
                value55 =""
            if time1 == "9:15AM" and "Friday" in days:
                value65 =""
            if time1 == "9:30AM" and "Friday" in days:
                value75 =""
            if time1 == "9:45AM" and "Friday" in days:
                value85 =""
            if time1 == "10:00AM" and "Friday" in days:
                value95 =""
            if time1 == "10:15AM" and "Friday" in days:
                value105 =""
            if time1 == "10:30AM" and "Friday" in days:
                value115 =""
            if time1 == "10:45AM" and "Friday" in days:
                value125 =""
            if time1 == "11:00AM" and "Friday" in days:
                value135 =""
            if time1 == "11:15AM" and "Friday" in days:
                value145 =""
            if time1 == "11:30AM" and "Friday" in days:
                value155 =""
            if time1 == "11:45AM" and "Friday" in days:
                value165 =""
            if time1 == "12:00PM" and "Friday" in days:
                value175 =""
            if time1 == "12:15PM" and "Friday" in days:
                value185 =""
            if time1 == "12:30PM" and "Friday" in days:
                value195 =""
            if time1 == "12:45PM" and "Friday" in days:
                value205 =""
            if time1 == "1:00PM" and "Friday" in days:
                value215 =""
            if time1 == "1:15PM" and "Friday" in days:
                value225 =""
            if time1 == "1:30PM" and "Friday" in days:
                value235 =""
            if time1 == "1:45PM" and "Friday" in days:
                value245 =""
            if time1 == "2:00PM" and "Friday" in days:
                value255 =""
            if time1 == "2:15PM" and "Friday" in days:
                value265 =""
            if time1 == "2:30PM" and "Friday" in days:
                value275 =""
            if time1 == "2:45PM" and "Friday" in days:
                value285 =""
            if time1 == "3:00PM" and "Friday" in days:
                value295 =""
            if time1 == "3:15PM" and "Friday" in days:
                value305 =""
            if time1 == "3:30PM" and "Friday" in days:
                value315 =""
            if time1 == "3:45PM" and "Friday" in days:
                value325 =""
            if time1 == "4:00PM" and "Friday" in days:
                value335 =""
            if time1 == "4:15PM" and "Friday" in days:
                value345 =""
            if time1 == "4:30PM" and "Friday" in days:
                value355 =""
            if time1 == "4:45PM" and "Friday" in days:
                value365 =""
            if time1 == "5:00PM" and "Friday" in days:
                value375 =""
            if time1 == "5:15PM" and "Friday" in days:
                value385 =""
            if time1 == "5:30PM" and "Friday" in days:
                value395 =""
            if time1 == "5:45PM" and "Friday" in days:
                value405 =""
            if time1 == "6:00PM" and "Friday" in days:
                value415 =""
            if time1 == "6:15PM" and "Friday" in days:
                value425 =""
            if time1 == "6:30PM" and "Friday" in days:
                value435 =""
            if time1 == "6:45PM" and "Friday" in days:
                value445 =""
            if time1 == "7:00PM" and "Friday" in days:
                value455 =""
            if time1 == "7:15PM" and "Friday" in days:
                value465 =""
            if time1 == "7:30PM" and "Friday" in days:
                value475 =""
            if time1 == "7:45PM" and "Friday" in days:
                value485 =""
            if time1 == "8:00PM" and "Friday" in days:
                value495 =""
            if time1 == "8:15PM" and "Friday" in days:
                value505 =""
            if time1 == "8:30PM" and "Friday" in days:
                value515 =""
            if time1 == "8:45PM" and "Friday" in days:
                value525 =""
        
            if time1 == "8:00AM" and "Saturday" in days:
                value16 = ""
            if time1 == "8:15AM" and "Saturday" in days:
                value26 = ""
            if time1 == "8:30AM" and "Saturday" in days:
                value36 = ""
            if time1 == "8:45AM" and "Saturday" in days:
                value46 = ""
            if time1 == "9:00AM" and "Saturday" in days:
                value56 = ""
            if time1 == "9:15AM" and "Saturday" in days:
                value66 = ""
            if time1 == "9:30AM" and "Saturday" in days:
                value76 = ""
            if time1 == "9:45AM" and "Saturday" in days:
                value86 = ""
            if time1 == "10:00AM" and "Saturday" in days:
                value96 = ""
            if time1 == "10:15AM" and "Saturday" in days:
                value106 = ""
            if time1 == "10:30AM" and "Saturday" in days:
                value116 = ""
            if time1 == "10:45AM" and "Saturday" in days:
                value126 = ""
            if time1 == "11:00AM" and "Saturday" in days:
                value136 = ""
            if time1 == "11:15AM" and "Saturday" in days:
                value146 = ""
            if time1 == "11:30AM" and "Saturday" in days:
                value156 = ""
            if time1 == "11:45AM" and "Saturday" in days:
                value166 = ""
            if time1 == "12:00PM" and "Saturday" in days:
                value176 = ""
            if time1 == "12:15PM" and "Saturday" in days:
                value186 = ""
            if time1 == "12:30PM" and "Saturday" in days:
                value196 = ""
            if time1 == "12:45PM" and "Saturday" in days:
                value206 = ""
            if time1 == "1:00PM" and "Saturday" in days:
                value216 = ""
            if time1 == "1:15PM" and "Saturday" in days:
                value226 = ""
            if time1 == "1:30PM" and "Saturday" in days:
                value236 = ""
            if time1 == "1:45PM" and "Saturday" in days:
                value246 = ""
            if time1 == "2:00PM" and "Saturday" in days:
                value256 = ""
            if time1 == "2:15PM" and "Saturday" in days:
                value266 = ""
            if time1 == "2:30PM" and "Saturday" in days:
                value276 = ""
            if time1 == "2:45PM" and "Saturday" in days:
                value286 = ""
            if time1 == "3:00PM" and "Saturday" in days:
                value296 = ""
            if time1 == "3:15PM" and "Saturday" in days:
                value306 = ""
            if time1 == "3:30PM" and "Saturday" in days:
                value316 = ""
            if time1 == "3:45PM" and "Saturday" in days:
                value326 = ""
            if time1 == "4:00PM" and "Saturday" in days:
                value336 = ""
            if time1 == "4:15PM" and "Saturday" in days:
                value346 = ""
            if time1 == "4:30PM" and "Saturday" in days:
                value356 = ""
            if time1 == "4:45PM" and "Saturday" in days:
                value366 = ""
            if time1 == "5:00PM" and "Saturday" in days:
                value376 = ""
            if time1 == "5:15PM" and "Saturday" in days:
                value386 = ""
            if time1 == "5:30PM" and "Saturday" in days:
                value396 = ""
            if time1 == "5:45PM" and "Saturday" in days:
                value406 = ""
            if time1 == "6:00PM" and "Saturday" in days:
                value416 = ""
            if time1 == "6:15PM" and "Saturday" in days:
                value426 = ""
            if time1 == "6:30PM" and "Saturday" in days:
                value436 = ""
            if time1 == "6:45PM" and "Saturday" in days:
                value446 = ""
            if time1 == "7:00PM" and "Saturday" in days:
                value456 = ""
            if time1 == "7:15PM" and "Saturday" in days:
                value466 = ""
            if time1 == "7:30PM" and "Saturday" in days:
                value476 = ""
            if time1 == "7:45PM" and "Saturday" in days:
                value486 = ""
            if time1 == "8:00PM" and "Saturday" in days:
                value496 = ""
            if time1 == "8:15PM" and "Saturday" in days:
                value506 = ""
            if time1 == "8:30PM" and "Saturday" in days:
                value516 = ""
            if time1 == "8:45PM" and "Saturday" in days:
                value526 = ""
        
            if time1 == "8:00AM" and "Sunday" in days:
                value17 = ""
            if time1 == "8:15AM" and "Sunday" in days:
                value27 = ""
            if time1 == "8:30AM" and "Sunday" in days:
                value37 = ""
            if time1 == "8:45AM" and "Sunday" in days:
                value47 = ""
            if time1 == "9:00AM" and "Sunday" in days:
                value57 = ""
            if time1 == "9:15AM" and "Sunday" in days:
                value67 = ""
            if time1 == "9:30AM" and "Sunday" in days:
                value77 = ""
            if time1 == "9:45AM" and "Sunday" in days:
                value87 = ""
            if time1 == "10:00AM" and "Sunday" in days:
                value97 = ""
            if time1 == "10:15AM" and "Sunday" in days:
                value107 = ""
            if time1 == "10:30AM" and "Sunday" in days:
                value117 = ""
            if time1 == "10:45AM" and "Sunday" in days:
                value127 = ""
            if time1 == "11:00AM" and "Sunday" in days:
                value137 = ""
            if time1 == "11:15AM" and "Sunday" in days:
                value147 = ""
            if time1 == "11:30AM" and "Sunday" in days:
                value157 = ""
            if time1 == "11:45AM" and "Sunday" in days:
                value167 = ""
            if time1 == "12:00PM" and "Sunday" in days:
                value177 = ""
            if time1 == "12:15PM" and "Sunday" in days:
                value187 = ""
            if time1 == "12:30PM" and "Sunday" in days:
                value197 = ""
            if time1 == "12:45PM" and "Sunday" in days:
                value207 = ""
            if time1 == "1:00PM" and "Sunday" in days:
                value217 = ""
            if time1 == "1:15PM" and "Sunday" in days:
                value227 = ""
            if time1 == "1:30PM" and "Sunday" in days:
                value237 = ""
            if time1 == "1:45PM" and "Sunday" in days:
                value247 = ""
            if time1 == "2:00PM" and "Sunday" in days:
                value257 = ""
            if time1 == "2:15PM" and "Sunday" in days:
                value267 = ""
            if time1 == "2:30PM" and "Sunday" in days:
                value277 = ""
            if time1 == "2:45PM" and "Sunday" in days:
                value287 = ""
            if time1 == "3:00PM" and "Sunday" in days:
                value297 = ""
            if time1 == "3:15PM" and "Sunday" in days:
                value307 = ""
            if time1 == "3:30PM" and "Sunday" in days:
                value317 = ""
            if time1 == "3:45PM" and "Sunday" in days:
                value327 = ""
            if time1 == "4:00PM" and "Sunday" in days:
                value337 = ""
            if time1 == "4:15PM" and "Sunday" in days:
                value347 = ""
            if time1 == "4:30PM" and "Sunday" in days:
                value357 = ""
            if time1 == "4:45PM" and "Sunday" in days:
                value367 = ""
            if time1 == "5:00PM" and "Sunday" in days:
                value377 = ""
            if time1 == "5:15PM" and "Sunday" in days:
                value387 = ""
            if time1 == "5:30PM" and "Sunday" in days:
                value397 = ""
            if time1 == "5:45PM" and "Sunday" in days:
                value407 = ""
            if time1 == "6:00PM" and "Sunday" in days:
                value417 = ""
            if time1 == "6:15PM" and "Sunday" in days:
                value427 = ""
            if time1 == "6:30PM" and "Sunday" in days:
                value437 = ""
            if time1 == "6:45PM" and "Sunday" in days:
                value447 = ""
            if time1 == "7:00PM" and "Sunday" in days:
                value457 = ""
            if time1 == "7:15PM" and "Sunday" in days:
                value467 = ""
            if time1 == "7:30PM" and "Sunday" in days:
                value477 = ""
            if time1 == "7:45PM" and "Sunday" in days:
                value487 = ""
            if time1 == "8:00PM" and "Sunday" in days:
                value497 = ""
            if time1 == "8:15PM" and "Sunday" in days:
                value507 = ""
            if time1 == "8:30PM" and "Sunday" in days:
                value517 = ""
            if time1 == "8:45PM" and"Sunday" in days:
                value527 = ""
            
            updater = findActivity(key)
            new_schedule = days_and_time(time1, time2, days)
            for i in new_schedule:
                if i in inputs:
                    updater = subtract(updater, i)
                    inputs.remove(i)

        else:
            time1 = request.form['time1']
            time2 = request.form['time2']
            text = request.form['label']
            color = request.form.getlist('color')
            days = request.form.getlist('days')
            new_schedule = days_and_time(time1, time2, days)
            updater = findActivity(key)
            color_updater = findColor(key)
                
            
            
            
            if time1 == "8:00AM" and "Monday" in days:
                value11 = text
            if time1 == "8:15AM" and "Monday" in days:
                value21 = text
            if time1 == "8:30AM" and "Monday" in days:
                value31 = text
            if time1 == "8:45AM" and "Monday" in days:
                value41 = text
            if time1 == "9:00AM" and "Monday" in days:
                value51 = text
            if time1 == "9:15AM" and "Monday" in days:
                value61 = text
            if time1 == "9:30AM" and "Monday" in days:
                value71 = text
            if time1 == "9:45AM" and "Monday" in days:
                value81 = text
            if time1 == "10:00AM" and "Monday" in days:
                value91 = text
            if time1 == "10:15AM" and "Monday" in days:
                value101 = text
            if time1 == "10:30AM" and "Monday" in days:
                value111 = text
            if time1 == "10:45AM" and "Monday" in days:
                value121 = text
            if time1 == "11:00AM" and "Monday" in days:
                value131 = text
            if time1 == "11:15AM" and "Monday" in days:
                value141 = text
            if time1 == "11:30AM" and "Monday" in days:
                value151 = text
            if time1 == "11:45AM" and "Monday" in days:
                value161 = text
            if time1 == "12:00PM" and "Monday" in days:
                value171 = text
            if time1 == "12:15PM" and "Monday" in days:
                value181 = text
            if time1 == "12:30PM" and "Monday" in days:
                value191 = text
            if time1 == "12:45PM" and "Monday" in days:
                value201 = text
            if time1 == "1:00PM" and "Monday" in days:
                value211 = text
            if time1 == "1:15PM" and "Monday" in days:
                value221 = text
            if time1 == "1:30PM" and "Monday" in days:
                value231 = text
            if time1 == "1:45PM" and "Monday" in days:
                value241 = text
            if time1 == "2:00PM" and "Monday" in days:
                value251 = text
            if time1 == "2:15PM" and "Monday" in days:
                value261 = text
            if time1 == "2:30PM" and "Monday" in days:
                value271 = text
            if time1 == "2:45PM" and "Monday" in days:
                value281 = text
            if time1 == "3:00PM" and "Monday" in days:
                value291 = text
            if time1 == "3:15PM" and "Monday" in days:
                value301 = text
            if time1 == "3:30PM" and "Monday" in days:
                value311 = text
            if time1 == "3:45PM" and "Monday" in days:
                value321 = text
            if time1 == "4:00PM" and "Monday" in days:
                value331 = text
            if time1 == "4:15PM" and "Monday" in days:
                value341 = text
            if time1 == "4:30PM" and "Monday" in days:
                value351 = text
            if time1 == "4:45PM" and "Monday" in days:
                value361 = text
            if time1 == "5:00PM" and "Monday" in days:
                value371 = text
            if time1 == "5:15PM" and "Monday" in days:
                value381 = text
            if time1 == "5:30PM" and "Monday" in days:
                value391 = text
            if time1 == "5:45PM" and "Monday" in days:
                value401 = text
            if time1 == "6:00PM" and "Monday" in days:
                value411 = text
            if time1 == "6:15PM" and "Monday" in days:
                value421 = text
            if time1 == "6:30PM" and "Monday" in days:
                value431 = text
            if time1 == "6:45PM" and "Monday" in days:
                value441 = text
            if time1 == "7:00PM" and "Monday" in days:
                value451 = text
            if time1 == "7:15PM" and "Monday" in days:
                value461 = text
            if time1 == "7:30PM" and "Monday" in days:
                value471 = text
            if time1 == "7:45PM" and "Monday" in days:
                value481 = text
            if time1 == "8:00PM" and "Monday" in days:
                value491 = text
            if time1 == "8:15PM" and "Monday" in days:
                value501 = text
            if time1 == "8:30PM" and "Monday" in days:
                value511 = text
            if time1 == "8:45PM" and "Monday" in days:
                value521 = text
            
            
            
            if time1 == "8:00AM" and "Tuesday" in days:
                value12 = text
            if time1 == "8:15AM" and "Tuesday" in days:
                value22 = text
            if time1 == "8:30AM" and "Tuesday" in days:
                value32 = text
            if time1 == "8:45AM" and "Tuesday" in days:
                value42 = text
            if time1 == "9:00AM" and "Tuesday" in days:
                value52 = text
            if time1 == "9:15AM" and "Tuesday" in days:
                value62 = text
            if time1 == "9:30AM" and "Tuesday" in days:
                value72 = text
            if time1 == "9:45AM" and "Tuesday" in days:
                value82 = text
            if time1 == "10:00AM" and "Tuesday" in days:
                value92 = text
            if time1 == "10:15AM" and "Tuesday" in days:
                value102 = text
            if time1 == "10:30AM" and "Tuesday" in days:
                value112 = text
            if time1 == "10:45AM" and "Tuesday" in days:
                value122 = text
            if time1 == "11:00AM" and "Tuesday" in days:
                value132 = text
            if time1 == "11:15AM" and "Tuesday" in days:
                value142 = text
            if time1 == "11:30AM" and "Tuesday" in days:
                value152 = text
            if time1 == "11:45AM" and "Tuesday" in days:
                value162 = text
            if time1 == "12:00PM" and "Tuesday" in days:
                value172 = text
            if time1 == "12:15PM" and "Tuesday" in days:
                value182 = text
            if time1 == "12:30PM" and "Tuesday" in days:
                value192 = text
            if time1 == "12:45PM" and "Tuesday" in days:
                value202 = text
            if time1 == "1:00PM" and "Tuesday" in days:
                value212 = text
            if time1 == "1:15PM" and "Tuesday" in days:
                value222 = text
            if time1 == "1:30PM" and "Tuesday" in days:
                value232 = text
            if time1 == "1:45PM" and "Tuesday" in days:
                value242 = text
            if time1 == "2:00PM" and "Tuesday" in days:
                value252 = text
            if time1 == "2:15PM" and "Tuesday" in days:
                value262 = text
            if time1 == "2:30PM" and "Tuesday" in days:
                value272 = text
            if time1 == "2:45PM" and "Tuesday" in days:
                value282 = text
            if time1 == "3:00PM" and "Tuesday" in days:
                value292 = text
            if time1 == "3:15PM" and "Tuesday" in days:
                value302 = text
            if time1 == "3:30PM" and "Tuesday" in days:
                value312 = text
            if time1 == "3:45PM" and "Tuesday" in days:
                value322 = text
            if time1 == "4:00PM" and "Tuesday" in days:
                value332 = text
            if time1 == "4:15PM" and "Tuesday" in days:
                value342 = text
            if time1 == "4:30PM" and "Tuesday" in days:
                value352 = text
            if time1 == "4:45PM" and "Tuesday" in days:
                value362 = text
            if time1 == "5:00PM" and "Tuesday" in days:
                value372 = text
            if time1 == "5:15PM" and "Tuesday" in days:
                value382 = text
            if time1 == "5:30PM" and "Tuesday" in days:
                value392 = text
            if time1 == "5:45PM" and "Tuesday" in days:
                value402 = text
            if time1 == "6:00PM" and "Tuesday" in days:
                value412 = text
            if time1 == "6:15PM" and "Tuesday" in days:
                value422 = text
            if time1 == "6:30PM" and "Tuesday" in days:
                value432 = text
            if time1 == "6:45PM" and "Tuesday" in days:
                value442 = text
            if time1 == "7:00PM" and "Tuesday" in days:
                value452 = text
            if time1 == "7:15PM" and "Tuesday" in days:
                value462 = text
            if time1 == "7:30PM" and "Tuesday" in days:
                value472 = text
            if time1 == "7:45PM" and "Tuesday" in days:
                value482 = text
            if time1 == "8:00PM" and "Tuesday" in days:
                value492 = text
            if time1 == "8:15PM" and "Tuesday" in days:
                value502 = text
            if time1 == "8:30PM" and "Tuesday" in days:
                value512 = text
            if time1 == "8:45PM" and "Tuesday" in days:
                value522 = text
            
            
            if time1 == "8:00AM" and "Wednesday" in days:
                value13 = text
            if time1 == "8:15AM" and "Wednesday" in days:
                value23 = text
            if time1 == "8:30AM" and "Wednesday" in days:
                value33 = text
            if time1 == "8:45AM" and "Wednesday" in days:
                value43 = text
            if time1 == "9:00AM" and "Wednesday" in days:
                value53 = text
            if time1 == "9:15AM" and "Wednesday" in days:
                value63 = text
            if time1 == "9:30AM" and "Wednesday" in days:
                value73 = text
            if time1 == "9:45AM" and "Wednesday" in days:
                value83 = text
            if time1 == "10:00AM" and "Wednesday" in days:
                value93 = text
            if time1 == "10:15AM" and "Wednesday" in days:
                value103 = text
            if time1 == "10:30AM" and "Wednesday" in days:
                value113 = text
            if time1 == "10:45AM" and "Wednesday" in days:
                value123 = text
            if time1 == "11:00AM" and "Wednesday" in days:
                value133 = text
            if time1 == "11:15AM" and "Wednesday" in days:
                value143 = text
            if time1 == "11:30AM" and "Wednesday" in days:
                value153 = text
            if time1 == "11:45AM" and "Wednesday" in days:
                value163 = text
            if time1 == "12:00PM" and "Wednesday" in days:
                value173 = text
            if time1 == "12:15PM" and "Wednesday" in days:
                value183 = text
            if time1 == "12:30PM" and "Wednesday" in days:
                value193 = text
            if time1 == "12:45PM" and "Wednesday" in days:
                value203 = text
            if time1 == "1:00PM" and "Wednesday" in days:
                value213 = text
            if time1 == "1:15PM" and "Wednesday" in days:
                value223 = text
            if time1 == "1:30PM" and "Wednesday" in days:
                value233 = text
            if time1 == "1:45PM" and "Wednesday" in days:
                value243 = text
            if time1 == "2:00PM" and "Wednesday" in days:
                value253 = text
            if time1 == "2:15PM" and "Wednesday" in days:
                value263 = text
            if time1 == "2:30PM" and "Wednesday" in days:
                value273 = text
            if time1 == "2:45PM" and "Wednesday" in days:
                value283 = text
            if time1 == "3:00PM" and "Wednesday" in days:
                value293 = text
            if time1 == "3:15PM" and "Wednesday" in days:
                value303 = text
            if time1 == "3:30PM" and "Wednesday" in days:
                value313 = text
            if time1 == "3:45PM" and "Wednesday" in days:
                value323 = text
            if time1 == "4:00PM" and "Wednesday" in days:
                value333 = text
            if time1 == "4:15PM" and "Wednesday" in days:
                value343 = text
            if time1 == "4:30PM" and "Wednesday" in days:
                value353 = text
            if time1 == "4:45PM" and "Wednesday" in days:
                value363 = text
            if time1 == "5:00PM" and "Wednesday" in days:
                value373 = text
            if time1 == "5:15PM" and "Wednesday" in days:
                value383 = text
            if time1 == "5:30PM" and "Wednesday" in days:
                value393 = text
            if time1 == "5:45PM" and "Wednesday" in days:
                value403 = text
            if time1 == "6:00PM" and "Wednesday" in days:
                value413 = text
            if time1 == "6:15PM" and "Wednesday" in days:
                value423 = text
            if time1 == "6:30PM" and "Wednesday" in days:
                value433 = text
            if time1 == "6:45PM" and "Wednesday" in days:
                value443 = text
            if time1 == "7:00PM" and "Wednesday" in days:
                value453 = text
            if time1 == "7:15PM" and "Wednesday" in days:
                value463 = text
            if time1 == "7:30PM" and "Wednesday" in days:
                value473 = text
            if time1 == "7:45PM" and "Wednesday" in days:
                value483 = text
            if time1 == "8:00PM" and "Wednesday" in days:
                value493 = text
            if time1 == "8:15PM" and "Wednesday" in days:
                value503 = text
            if time1 == "8:30PM" and "Wednesday" in days:
                value513 = text
            if time1 == "8:45PM" and "Wednesday" in days:
                value523 = text
            
            
            if time1 == "8:00AM" and "Thursday" in days:
                value14 = text
            if time1 == "8:15AM" and "Thursday" in days:
                value24 = text
            if time1 == "8:30AM" and "Thursday" in days:
                value34 = text
            if time1 == "8:45AM" and "Thursday" in days:
                value44 = text
            if time1 == "9:00AM" and "Thursday" in days:
                value54 = text
            if time1 == "9:15AM" and "Thursday" in days:
                value64 = text
            if time1 == "9:30AM" and "Thursday" in days:
                value74 = text
            if time1 == "9:45AM" and "Thursday" in days:
                value84 = text
            if time1 == "10:00AM" and "Thursday" in days:
                value94 = text
            if time1 == "10:15AM" and "Thursday" in days:
                value104 = text
            if time1 == "10:30AM" and "Thursday" in days:
                value114 = text
            if time1 == "10:45AM" and "Thursday" in days:
                value124 = text
            if time1 == "11:00AM" and "Thursday" in days:
                value134 = text
            if time1 == "11:15AM" and "Thursday" in days:
                value144 = text
            if time1 == "11:30AM" and "Thursday" in days:
                value154 = text
            if time1 == "11:45AM" and "Thursday" in days:
                value164 = text
            if time1 == "12:00PM" and "Thursday" in days:
                value174 = text
            if time1 == "12:15PM" and "Thursday" in days:
                value184 = text
            if time1 == "12:30PM" and "Thursday" in days:
                value194 = text
            if time1 == "12:45PM" and "Thursday" in days:
                value204 = text
            if time1 == "1:00PM" and "Thursday" in days:
                value214 = text
            if time1 == "1:15PM" and "Thursday" in days:
                value224 = text
            if time1 == "1:30PM" and "Thursday" in days:
                value234 = text
            if time1 == "1:45PM" and "Thursday" in days:
                value244 = text
            if time1 == "2:00PM" and "Thursday" in days:
                value254 = text
            if time1 == "2:15PM" and "Thursday" in days:
                value264 = text
            if time1 == "2:30PM" and "Thursday" in days:
                value274 = text
            if time1 == "2:45PM" and "Thursday" in days:
                value284 = text
            if time1 == "3:00PM" and "Thursday" in days:
                value294 = text
            if time1 == "3:15PM" and "Thursday" in days:
                value304 = text
            if time1 == "3:30PM" and "Thursday" in days:
                value314 = text
            if time1 == "3:45PM" and "Thursday" in days:
                value324 = text
            if time1 == "4:00PM" and "Thursday" in days:
                value334 = text
            if time1 == "4:15PM" and "Thursday" in days:
                value344 = text
            if time1 == "4:30PM" and "Thursday" in days:
                value354 = text
            if time1 == "4:45PM" and "Thursday" in days:
                value364 = text
            if time1 == "5:00PM" and "Thursday" in days:
                value374 = text
            if time1 == "5:15PM" and "Thursday" in days:
                value384 = text
            if time1 == "5:30PM" and "Thursday" in days:
                value394 = text
            if time1 == "5:45PM" and "Thursday" in days:
                value404 = text
            if time1 == "6:00PM" and "Thursday" in days:
                value414 = text
            if time1 == "6:15PM" and "Thursday" in days:
                value424 = text
            if time1 == "6:30PM" and "Thursday" in days:
                value434 = text
            if time1 == "6:45PM" and "Thursday" in days:
                value444 = text
            if time1 == "7:00PM" and "Thursday" in days:
                value454 = text
            if time1 == "7:15PM" and "Thursday" in days:
                value464 = text
            if time1 == "7:30PM" and "Thursday" in days:
                value474 = text
            if time1 == "7:45PM" and "Thursday" in days:
                value484 = text
            if time1 == "8:00PM" and "Thursday" in days:
                value494 = text
            if time1 == "8:15PM" and "Thursday" in days:
                value504 = text
            if time1 == "8:30PM" and "Thursday" in days:
                value514 = text
            if time1 == "8:45PM" and "Thursday" in days:
                value524 = text
        
            if time1 == "8:00AM" and "Friday" in days:
                value15 =text
            if time1 == "8:15AM" and "Friday" in days:
                value25 =text
            if time1 == "8:30AM" and "Friday" in days:
                value35 =text
            if time1 == "8:45AM" and "Friday" in days:
                value45 =text
            if time1 == "9:00AM" and "Friday" in days:
                value55 =text
            if time1 == "9:15AM" and "Friday" in days:
                value65 =text
            if time1 == "9:30AM" and "Friday" in days:
                value75 =text
            if time1 == "9:45AM" and "Friday" in days:
                value85 =text
            if time1 == "10:00AM" and "Friday" in days:
                value95 =text
            if time1 == "10:15AM" and "Friday" in days:
                value105 =text
            if time1 == "10:30AM" and "Friday" in days:
                value115 =text
            if time1 == "10:45AM" and "Friday" in days:
                value125 =text
            if time1 == "11:00AM" and "Friday" in days:
                value135 =text
            if time1 == "11:15AM" and "Friday" in days:
                value145 =text
            if time1 == "11:30AM" and "Friday" in days:
                value155 =text
            if time1 == "11:45AM" and "Friday" in days:
                value165 =text
            if time1 == "12:00PM" and "Friday" in days:
                value175 =text
            if time1 == "12:15PM" and "Friday" in days:
                value185 =text
            if time1 == "12:30PM" and "Friday" in days:
                value195 =text
            if time1 == "12:45PM" and "Friday" in days:
                value205 =text
            if time1 == "1:00PM" and "Friday" in days:
                value215 =text
            if time1 == "1:15PM" and "Friday" in days:
                value225 =text
            if time1 == "1:30PM" and "Friday" in days:
                value235 =text
            if time1 == "1:45PM" and "Friday" in days:
                value245 =text
            if time1 == "2:00PM" and "Friday" in days:
                value255 =text
            if time1 == "2:15PM" and "Friday" in days:
                value265 =text
            if time1 == "2:30PM" and "Friday" in days:
                value275 =text
            if time1 == "2:45PM" and "Friday" in days:
                value285 =text
            if time1 == "3:00PM" and "Friday" in days:
                value295 =text
            if time1 == "3:15PM" and "Friday" in days:
                value305 =text
            if time1 == "3:30PM" and "Friday" in days:
                value315 =text
            if time1 == "3:45PM" and "Friday" in days:
                value325 =text
            if time1 == "4:00PM" and "Friday" in days:
                value335 =text
            if time1 == "4:15PM" and "Friday" in days:
                value345 =text
            if time1 == "4:30PM" and "Friday" in days:
                value355 =text
            if time1 == "4:45PM" and "Friday" in days:
                value365 =text
            if time1 == "5:00PM" and "Friday" in days:
                value375 =text
            if time1 == "5:15PM" and "Friday" in days:
                value385 =text
            if time1 == "5:30PM" and "Friday" in days:
                value395 =text
            if time1 == "5:45PM" and "Friday" in days:
                value405 =text
            if time1 == "6:00PM" and "Friday" in days:
                value415 =text
            if time1 == "6:15PM" and "Friday" in days:
                value425 =text
            if time1 == "6:30PM" and "Friday" in days:
                value435 =text
            if time1 == "6:45PM" and "Friday" in days:
                value445 =text
            if time1 == "7:00PM" and "Friday" in days:
                value455 =text
            if time1 == "7:15PM" and "Friday" in days:
                value465 =text
            if time1 == "7:30PM" and "Friday" in days:
                value475 =text
            if time1 == "7:45PM" and "Friday" in days:
                value485 =text
            if time1 == "8:00PM" and "Friday" in days:
                value495 =text
            if time1 == "8:15PM" and "Friday" in days:
                value505 =text
            if time1 == "8:30PM" and "Friday" in days:
                value515 =text
            if time1 == "8:45PM" and "Friday" in days:
                value525 =text
        
            if time1 == "8:00AM" and "Saturday" in days:
                value16 = text
            if time1 == "8:15AM" and "Saturday" in days:
                value26 = text
            if time1 == "8:30AM" and "Saturday" in days:
                value36 = text
            if time1 == "8:45AM" and "Saturday" in days:
                value46 = text
            if time1 == "9:00AM" and "Saturday" in days:
                value56 = text
            if time1 == "9:15AM" and "Saturday" in days:
                value66 = text
            if time1 == "9:30AM" and "Saturday" in days:
                value76 = text
            if time1 == "9:45AM" and "Saturday" in days:
                value86 = text
            if time1 == "10:00AM" and "Saturday" in days:
                value96 = text
            if time1 == "10:15AM" and "Saturday" in days:
                value106 = text
            if time1 == "10:30AM" and "Saturday" in days:
                value116 = text
            if time1 == "10:45AM" and "Saturday" in days:
                value126 = text
            if time1 == "11:00AM" and "Saturday" in days:
                value136 = text
            if time1 == "11:15AM" and "Saturday" in days:
                value146 = text
            if time1 == "11:30AM" and "Saturday" in days:
                value156 = text
            if time1 == "11:45AM" and "Saturday" in days:
                value166 = text
            if time1 == "12:00PM" and "Saturday" in days:
                value176 = text
            if time1 == "12:15PM" and "Saturday" in days:
                value186 = text
            if time1 == "12:30PM" and "Saturday" in days:
                value196 = text
            if time1 == "12:45PM" and "Saturday" in days:
                value206 = text
            if time1 == "1:00PM" and "Saturday" in days:
                value216 = text
            if time1 == "1:15PM" and "Saturday" in days:
                value226 = text
            if time1 == "1:30PM" and "Saturday" in days:
                value236 = text
            if time1 == "1:45PM" and "Saturday" in days:
                value246 = text
            if time1 == "2:00PM" and "Saturday" in days:
                value256 = text
            if time1 == "2:15PM" and "Saturday" in days:
                value266 = text
            if time1 == "2:30PM" and "Saturday" in days:
                value276 = text
            if time1 == "2:45PM" and "Saturday" in days:
                value286 = text
            if time1 == "3:00PM" and "Saturday" in days:
                value296 = text
            if time1 == "3:15PM" and "Saturday" in days:
                value306 = text
            if time1 == "3:30PM" and "Saturday" in days:
                value316 = text
            if time1 == "3:45PM" and "Saturday" in days:
                value326 = text
            if time1 == "4:00PM" and "Saturday" in days:
                value336 = text
            if time1 == "4:15PM" and "Saturday" in days:
                value346 = text
            if time1 == "4:30PM" and "Saturday" in days:
                value356 = text
            if time1 == "4:45PM" and "Saturday" in days:
                value366 = text
            if time1 == "5:00PM" and "Saturday" in days:
                value376 = text
            if time1 == "5:15PM" and "Saturday" in days:
                value386 = text
            if time1 == "5:30PM" and "Saturday" in days:
                value396 = text
            if time1 == "5:45PM" and "Saturday" in days:
                value406 = text
            if time1 == "6:00PM" and "Saturday" in days:
                value416 = text
            if time1 == "6:15PM" and "Saturday" in days:
                value426 = text
            if time1 == "6:30PM" and "Saturday" in days:
                value436 = text
            if time1 == "6:45PM" and "Saturday" in days:
                value446 = text
            if time1 == "7:00PM" and "Saturday" in days:
                value456 = text
            if time1 == "7:15PM" and "Saturday" in days:
                value466 = text
            if time1 == "7:30PM" and "Saturday" in days:
                value476 = text
            if time1 == "7:45PM" and "Saturday" in days:
                value486 = text
            if time1 == "8:00PM" and "Saturday" in days:
                value496 = text
            if time1 == "8:15PM" and "Saturday" in days:
                value506 = text
            if time1 == "8:30PM" and "Saturday" in days:
                value516 = text
            if time1 == "8:45PM" and "Saturday" in days:
                value526 = text
        
            if time1 == "8:00AM" and "Sunday" in days:
                value17 = text
            if time1 == "8:15AM" and "Sunday" in days:
                value27 = text
            if time1 == "8:30AM" and "Sunday" in days:
                value37 = text
            if time1 == "8:45AM" and "Sunday" in days:
                value47 = text
            if time1 == "9:00AM" and "Sunday" in days:
                value57 = text
            if time1 == "9:15AM" and "Sunday" in days:
                value67 = text
            if time1 == "9:30AM" and "Sunday" in days:
                value77 = text
            if time1 == "9:45AM" and "Sunday" in days:
                value87 = text
            if time1 == "10:00AM" and "Sunday" in days:
                value97 = text
            if time1 == "10:15AM" and "Sunday" in days:
                value107 = text
            if time1 == "10:30AM" and "Sunday" in days:
                value117 = text
            if time1 == "10:45AM" and "Sunday" in days:
                value127 = text
            if time1 == "11:00AM" and "Sunday" in days:
                value137 = text
            if time1 == "11:15AM" and "Sunday" in days:
                value147 = text
            if time1 == "11:30AM" and "Sunday" in days:
                value157 = text
            if time1 == "11:45AM" and "Sunday" in days:
                value167 = text
            if time1 == "12:00PM" and "Sunday" in days:
                value177 = text
            if time1 == "12:15PM" and "Sunday" in days:
                value187 = text
            if time1 == "12:30PM" and "Sunday" in days:
                value197 = text
            if time1 == "12:45PM" and "Sunday" in days:
                value207 = text
            if time1 == "1:00PM" and "Sunday" in days:
                value217 = text
            if time1 == "1:15PM" and "Sunday" in days:
                value227 = text
            if time1 == "1:30PM" and "Sunday" in days:
                value237 = text
            if time1 == "1:45PM" and "Sunday" in days:
                value247 = text
            if time1 == "2:00PM" and "Sunday" in days:
                value257 = text
            if time1 == "2:15PM" and "Sunday" in days:
                value267 = text
            if time1 == "2:30PM" and "Sunday" in days:
                value277 = text
            if time1 == "2:45PM" and "Sunday" in days:
                value287 = text
            if time1 == "3:00PM" and "Sunday" in days:
                value297 = text
            if time1 == "3:15PM" and "Sunday" in days:
                value307 = text
            if time1 == "3:30PM" and "Sunday" in days:
                value317 = text
            if time1 == "3:45PM" and "Sunday" in days:
                value327 = text
            if time1 == "4:00PM" and "Sunday" in days:
                value337 = text
            if time1 == "4:15PM" and "Sunday" in days:
                value347 = text
            if time1 == "4:30PM" and "Sunday" in days:
                value357 = text
            if time1 == "4:45PM" and "Sunday" in days:
                value367 = text
            if time1 == "5:00PM" and "Sunday" in days:
                value377 = text
            if time1 == "5:15PM" and "Sunday" in days:
                value387 = text
            if time1 == "5:30PM" and "Sunday" in days:
                value397 = text
            if time1 == "5:45PM" and "Sunday" in days:
                value407 = text
            if time1 == "6:00PM" and "Sunday" in days:
                value417 = text
            if time1 == "6:15PM" and "Sunday" in days:
                value427 = text
            if time1 == "6:30PM" and "Sunday" in days:
                value437 = text
            if time1 == "6:45PM" and "Sunday" in days:
                value447 = text
            if time1 == "7:00PM" and "Sunday" in days:
                value457 = text
            if time1 == "7:15PM" and "Sunday" in days:
                value467 = text
            if time1 == "7:30PM" and "Sunday" in days:
                value477 = text
            if time1 == "7:45PM" and "Sunday" in days:
                value487 = text
            if time1 == "8:00PM" and "Sunday" in days:
                value497 = text
            if time1 == "8:15PM" and "Sunday" in days:
                value507 = text
            if time1 == "8:30PM" and "Sunday" in days:
                value517 = text
            if time1 == "8:45PM" and "Sunday" in days:
                value527 = text

            
            
            
            for i in new_schedule:
                updater += f" {i}"
                inputs.append(i)
                if color == ["red"]:
                    color_updater += f' {i}'
                    colors.append(i)
                if color == [] and i in colors:
                    color_updater = subtract(color_updater, i)
                    colors.remove(i)
            db.update({"color": color_updater}, personal.email == email)
        
        db.update({"value11": value11}, personal.email == email)
        db.update({"value12": value12}, personal.email == email)
        db.update({"value13": value13}, personal.email == email)
        db.update({"value14": value14}, personal.email == email)
        db.update({"value15": value15}, personal.email == email)
        db.update({"value16": value16}, personal.email == email)
        db.update({"value17": value17}, personal.email == email)
        db.update({"value21": value21}, personal.email == email)
        db.update({"value22": value22}, personal.email == email)
        db.update({"value23": value23}, personal.email == email)
        db.update({"value24": value24}, personal.email == email)
        db.update({"value25": value25}, personal.email == email)
        db.update({"value26": value26}, personal.email == email)
        db.update({"value27": value27}, personal.email == email)
        db.update({"value31": value31}, personal.email == email)
        db.update({"value32": value32}, personal.email == email)
        db.update({"value33": value33}, personal.email == email)
        db.update({"value34": value34}, personal.email == email)
        db.update({"value35": value35}, personal.email == email)
        db.update({"value36": value36}, personal.email == email)
        db.update({"value37": value37}, personal.email == email)
        db.update({"value41": value41}, personal.email == email)
        db.update({"value42": value42}, personal.email == email)
        db.update({"value43": value43}, personal.email == email)
        db.update({"value44": value44}, personal.email == email)
        db.update({"value45": value45}, personal.email == email)
        db.update({"value46": value46}, personal.email == email)
        db.update({"value47": value47}, personal.email == email)
        db.update({"value51": value51}, personal.email == email)
        db.update({"value52": value52}, personal.email == email)
        db.update({"value53": value53}, personal.email == email)
        db.update({"value54": value54}, personal.email == email)
        db.update({"value55": value55}, personal.email == email)
        db.update({"value56": value56}, personal.email == email)
        db.update({"value57": value57}, personal.email == email)
        db.update({"value61": value61}, personal.email == email)
        db.update({"value62": value62}, personal.email == email)
        db.update({"value63": value63}, personal.email == email)
        db.update({"value64": value64}, personal.email == email)
        db.update({"value65": value65}, personal.email == email)
        db.update({"value66": value66}, personal.email == email)
        db.update({"value67": value67}, personal.email == email)
        db.update({"value71": value71}, personal.email == email)
        db.update({"value72": value72}, personal.email == email)
        db.update({"value73": value73}, personal.email == email)
        db.update({"value74": value74}, personal.email == email)
        db.update({"value75": value75}, personal.email == email)
        db.update({"value76": value76}, personal.email == email)
        db.update({"value77": value77}, personal.email == email)
        db.update({"value81": value81}, personal.email == email)
        db.update({"value82": value82}, personal.email == email)
        db.update({"value83": value83}, personal.email == email)
        db.update({"value84": value84}, personal.email == email)
        db.update({"value85": value85}, personal.email == email)
        db.update({"value86": value86}, personal.email == email)
        db.update({"value87": value87}, personal.email == email)
        db.update({"value91": value91}, personal.email == email)
        db.update({"value92": value92}, personal.email == email)
        db.update({"value93": value93}, personal.email == email)
        db.update({"value94": value94}, personal.email == email)
        db.update({"value95": value95}, personal.email == email)
        db.update({"value96": value96}, personal.email == email)
        db.update({"value97": value97}, personal.email == email)
        db.update({"value101": value101}, personal.email == email)
        db.update({"value102": value102}, personal.email == email)
        db.update({"value103": value103}, personal.email == email)
        db.update({"value104": value104}, personal.email == email)
        db.update({"value105": value105}, personal.email == email)
        db.update({"value106": value106}, personal.email == email)
        db.update({"value107": value107}, personal.email == email)
        db.update({"value111": value111}, personal.email == email)
        db.update({"value112": value112}, personal.email == email)
        db.update({"value113": value113}, personal.email == email)
        db.update({"value114": value114}, personal.email == email)
        db.update({"value115": value115}, personal.email == email)
        db.update({"value116": value116}, personal.email == email)
        db.update({"value117": value117}, personal.email == email)
        db.update({"value121": value121}, personal.email == email)
        db.update({"value122": value122}, personal.email == email)
        db.update({"value123": value123}, personal.email == email)
        db.update({"value124": value124}, personal.email == email)
        db.update({"value125": value125}, personal.email == email)
        db.update({"value126": value126}, personal.email == email)
        db.update({"value127": value127}, personal.email == email)
        db.update({"value131": value131}, personal.email == email)
        db.update({"value132": value132}, personal.email == email)
        db.update({"value133": value133}, personal.email == email)
        db.update({"value134": value134}, personal.email == email)
        db.update({"value135": value135}, personal.email == email)
        db.update({"value136": value136}, personal.email == email)
        db.update({"value137": value137}, personal.email == email)
        db.update({"value141": value141}, personal.email == email)
        db.update({"value142": value142}, personal.email == email)
        db.update({"value143": value143}, personal.email == email)
        db.update({"value144": value144}, personal.email == email)
        db.update({"value145": value145}, personal.email == email)
        db.update({"value146": value146}, personal.email == email)
        db.update({"value147": value147}, personal.email == email)
        db.update({"value151": value151}, personal.email == email)
        db.update({"value152": value152}, personal.email == email)
        db.update({"value153": value153}, personal.email == email)
        db.update({"value154": value154}, personal.email == email)
        db.update({"value155": value155}, personal.email == email)
        db.update({"value156": value156}, personal.email == email)
        db.update({"value157": value157}, personal.email == email)
        db.update({"value161": value161}, personal.email == email)
        db.update({"value162": value162}, personal.email == email)
        db.update({"value163": value163}, personal.email == email)
        db.update({"value164": value164}, personal.email == email)
        db.update({"value165": value165}, personal.email == email)
        db.update({"value166": value166}, personal.email == email)
        db.update({"value167": value167}, personal.email == email)
        db.update({"value171": value171}, personal.email == email)
        db.update({"value172": value172}, personal.email == email)
        db.update({"value173": value173}, personal.email == email)
        db.update({"value174": value174}, personal.email == email)
        db.update({"value175": value175}, personal.email == email)
        db.update({"value176": value176}, personal.email == email)
        db.update({"value177": value177}, personal.email == email)
        db.update({"value181": value181}, personal.email == email)
        db.update({"value182": value182}, personal.email == email)
        db.update({"value183": value183}, personal.email == email)
        db.update({"value184": value184}, personal.email == email)
        db.update({"value185": value185}, personal.email == email)
        db.update({"value186": value186}, personal.email == email)
        db.update({"value187": value187}, personal.email == email)
        db.update({"value191": value191}, personal.email == email)
        db.update({"value192": value192}, personal.email == email)
        db.update({"value193": value193}, personal.email == email)
        db.update({"value194": value194}, personal.email == email)
        db.update({"value195": value195}, personal.email == email)
        db.update({"value196": value196}, personal.email == email)
        db.update({"value197": value197}, personal.email == email)
        db.update({"value201": value201}, personal.email == email)
        db.update({"value202": value202}, personal.email == email)
        db.update({"value203": value203}, personal.email == email)
        db.update({"value204": value204}, personal.email == email)
        db.update({"value205": value205}, personal.email == email)
        db.update({"value206": value206}, personal.email == email)
        db.update({"value207": value207}, personal.email == email)
        db.update({"value211": value211}, personal.email == email)
        db.update({"value212": value212}, personal.email == email)
        db.update({"value213": value213}, personal.email == email)
        db.update({"value214": value214}, personal.email == email)
        db.update({"value215": value215}, personal.email == email)
        db.update({"value216": value216}, personal.email == email)
        db.update({"value217": value217}, personal.email == email)
        db.update({"value221": value221}, personal.email == email)
        db.update({"value222": value222}, personal.email == email)
        db.update({"value223": value223}, personal.email == email)
        db.update({"value224": value224}, personal.email == email)
        db.update({"value225": value225}, personal.email == email)
        db.update({"value226": value226}, personal.email == email)
        db.update({"value227": value227}, personal.email == email)
        db.update({"value231": value231}, personal.email == email)
        db.update({"value232": value232}, personal.email == email)
        db.update({"value233": value233}, personal.email == email)
        db.update({"value234": value234}, personal.email == email)
        db.update({"value235": value235}, personal.email == email)
        db.update({"value236": value236}, personal.email == email)
        db.update({"value237": value237}, personal.email == email)
        db.update({"value241": value241}, personal.email == email)
        db.update({"value242": value242}, personal.email == email)
        db.update({"value243": value243}, personal.email == email)
        db.update({"value244": value244}, personal.email == email)
        db.update({"value245": value245}, personal.email == email)
        db.update({"value246": value246}, personal.email == email)
        db.update({"value247": value247}, personal.email == email)
        db.update({"value251": value251}, personal.email == email)
        db.update({"value252": value252}, personal.email == email)
        db.update({"value253": value253}, personal.email == email)
        db.update({"value254": value254}, personal.email == email)
        db.update({"value255": value255}, personal.email == email)
        db.update({"value256": value256}, personal.email == email)
        db.update({"value257": value257}, personal.email == email)
        db.update({"value261": value261}, personal.email == email)
        db.update({"value262": value262}, personal.email == email)
        db.update({"value263": value263}, personal.email == email)
        db.update({"value264": value264}, personal.email == email)
        db.update({"value265": value265}, personal.email == email)
        db.update({"value266": value266}, personal.email == email)
        db.update({"value267": value267}, personal.email == email)
        db.update({"value271": value271}, personal.email == email)
        db.update({"value272": value272}, personal.email == email)
        db.update({"value273": value273}, personal.email == email)
        db.update({"value274": value274}, personal.email == email)
        db.update({"value275": value275}, personal.email == email)
        db.update({"value276": value276}, personal.email == email)
        db.update({"value277": value277}, personal.email == email)
        db.update({"value281": value281}, personal.email == email)
        db.update({"value282": value282}, personal.email == email)
        db.update({"value283": value283}, personal.email == email)
        db.update({"value284": value284}, personal.email == email)
        db.update({"value285": value285}, personal.email == email)
        db.update({"value286": value286}, personal.email == email)
        db.update({"value287": value287}, personal.email == email)
        db.update({"value291": value291}, personal.email == email)
        db.update({"value292": value292}, personal.email == email)
        db.update({"value293": value293}, personal.email == email)
        db.update({"value294": value294}, personal.email == email)
        db.update({"value295": value295}, personal.email == email)
        db.update({"value296": value296}, personal.email == email)
        db.update({"value297": value297}, personal.email == email)
        db.update({"value301": value301}, personal.email == email)
        db.update({"value302": value302}, personal.email == email)
        db.update({"value303": value303}, personal.email == email)
        db.update({"value304": value304}, personal.email == email)
        db.update({"value305": value305}, personal.email == email)
        db.update({"value306": value306}, personal.email == email)
        db.update({"value307": value307}, personal.email == email)
        db.update({"value311": value311}, personal.email == email)
        db.update({"value312": value312}, personal.email == email)
        db.update({"value313": value313}, personal.email == email)
        db.update({"value314": value314}, personal.email == email)
        db.update({"value315": value315}, personal.email == email)
        db.update({"value316": value316}, personal.email == email)
        db.update({"value317": value317}, personal.email == email)
        db.update({"value321": value321}, personal.email == email)
        db.update({"value322": value322}, personal.email == email)
        db.update({"value323": value323}, personal.email == email)
        db.update({"value324": value324}, personal.email == email)
        db.update({"value325": value325}, personal.email == email)
        db.update({"value326": value326}, personal.email == email)
        db.update({"value327": value327}, personal.email == email)
        db.update({"value331": value331}, personal.email == email)
        db.update({"value332": value332}, personal.email == email)
        db.update({"value333": value333}, personal.email == email)
        db.update({"value334": value334}, personal.email == email)
        db.update({"value335": value335}, personal.email == email)
        db.update({"value336": value336}, personal.email == email)
        db.update({"value337": value337}, personal.email == email)
        db.update({"value341": value341}, personal.email == email)
        db.update({"value342": value342}, personal.email == email)
        db.update({"value343": value343}, personal.email == email)
        db.update({"value344": value344}, personal.email == email)
        db.update({"value345": value345}, personal.email == email)
        db.update({"value346": value346}, personal.email == email)
        db.update({"value347": value347}, personal.email == email)
        db.update({"value351": value351}, personal.email == email)
        db.update({"value352": value352}, personal.email == email)
        db.update({"value353": value353}, personal.email == email)
        db.update({"value354": value354}, personal.email == email)
        db.update({"value355": value355}, personal.email == email)
        db.update({"value356": value356}, personal.email == email)
        db.update({"value357": value357}, personal.email == email)
        db.update({"value361": value361}, personal.email == email)
        db.update({"value362": value362}, personal.email == email)
        db.update({"value363": value363}, personal.email == email)
        db.update({"value364": value364}, personal.email == email)
        db.update({"value365": value365}, personal.email == email)
        db.update({"value366": value366}, personal.email == email)
        db.update({"value367": value367}, personal.email == email)
        db.update({"value371": value371}, personal.email == email)
        db.update({"value372": value372}, personal.email == email)
        db.update({"value373": value373}, personal.email == email)
        db.update({"value374": value374}, personal.email == email)
        db.update({"value375": value375}, personal.email == email)
        db.update({"value376": value376}, personal.email == email)
        db.update({"value377": value377}, personal.email == email)
        db.update({"value381": value381}, personal.email == email)
        db.update({"value382": value382}, personal.email == email)
        db.update({"value383": value383}, personal.email == email)
        db.update({"value384": value384}, personal.email == email)
        db.update({"value385": value385}, personal.email == email)
        db.update({"value386": value386}, personal.email == email)
        db.update({"value387": value387}, personal.email == email)
        db.update({"value391": value391}, personal.email == email)
        db.update({"value392": value392}, personal.email == email)
        db.update({"value393": value393}, personal.email == email)
        db.update({"value394": value394}, personal.email == email)
        db.update({"value395": value395}, personal.email == email)
        db.update({"value396": value396}, personal.email == email)
        db.update({"value397": value397}, personal.email == email)
        db.update({"value401": value401}, personal.email == email)
        db.update({"value402": value402}, personal.email == email)
        db.update({"value403": value403}, personal.email == email)
        db.update({"value404": value404}, personal.email == email)
        db.update({"value405": value405}, personal.email == email)
        db.update({"value406": value406}, personal.email == email)
        db.update({"value407": value407}, personal.email == email)
        db.update({"value411": value411}, personal.email == email)
        db.update({"value412": value412}, personal.email == email)
        db.update({"value413": value413}, personal.email == email)
        db.update({"value414": value414}, personal.email == email)
        db.update({"value415": value415}, personal.email == email)
        db.update({"value416": value416}, personal.email == email)
        db.update({"value417": value417}, personal.email == email)
        db.update({"value421": value421}, personal.email == email)
        db.update({"value422": value422}, personal.email == email)
        db.update({"value423": value423}, personal.email == email)
        db.update({"value424": value424}, personal.email == email)
        db.update({"value425": value425}, personal.email == email)
        db.update({"value426": value426}, personal.email == email)
        db.update({"value427": value427}, personal.email == email)
        db.update({"value431": value431}, personal.email == email)
        db.update({"value432": value432}, personal.email == email)
        db.update({"value433": value433}, personal.email == email)
        db.update({"value434": value434}, personal.email == email)
        db.update({"value435": value435}, personal.email == email)
        db.update({"value436": value436}, personal.email == email)
        db.update({"value437": value437}, personal.email == email)
        db.update({"value441": value441}, personal.email == email)
        db.update({"value442": value442}, personal.email == email)
        db.update({"value443": value443}, personal.email == email)
        db.update({"value444": value444}, personal.email == email)
        db.update({"value445": value445}, personal.email == email)
        db.update({"value446": value446}, personal.email == email)
        db.update({"value447": value447}, personal.email == email)
        db.update({"value451": value451}, personal.email == email)
        db.update({"value452": value452}, personal.email == email)
        db.update({"value453": value453}, personal.email == email)
        db.update({"value454": value454}, personal.email == email)
        db.update({"value455": value455}, personal.email == email)
        db.update({"value456": value456}, personal.email == email)
        db.update({"value457": value457}, personal.email == email)
        db.update({"value461": value461}, personal.email == email)
        db.update({"value462": value462}, personal.email == email)
        db.update({"value463": value463}, personal.email == email)
        db.update({"value464": value464}, personal.email == email)
        db.update({"value465": value465}, personal.email == email)
        db.update({"value466": value466}, personal.email == email)
        db.update({"value467": value467}, personal.email == email)
        db.update({"value471": value471}, personal.email == email)
        db.update({"value472": value472}, personal.email == email)
        db.update({"value473": value473}, personal.email == email)
        db.update({"value474": value474}, personal.email == email)
        db.update({"value475": value475}, personal.email == email)
        db.update({"value476": value476}, personal.email == email)
        db.update({"value477": value477}, personal.email == email)
        db.update({"value481": value481}, personal.email == email)
        db.update({"value482": value482}, personal.email == email)
        db.update({"value483": value483}, personal.email == email)
        db.update({"value484": value484}, personal.email == email)
        db.update({"value485": value485}, personal.email == email)
        db.update({"value486": value486}, personal.email == email)
        db.update({"value487": value487}, personal.email == email)
        db.update({"value491": value491}, personal.email == email)
        db.update({"value492": value492}, personal.email == email)
        db.update({"value493": value493}, personal.email == email)
        db.update({"value494": value494}, personal.email == email)
        db.update({"value495": value495}, personal.email == email)
        db.update({"value496": value496}, personal.email == email)
        db.update({"value497": value497}, personal.email == email)
        db.update({"value501": value501}, personal.email == email)
        db.update({"value502": value502}, personal.email == email)
        db.update({"value503": value503}, personal.email == email)
        db.update({"value504": value504}, personal.email == email)
        db.update({"value505": value505}, personal.email == email)
        db.update({"value506": value506}, personal.email == email)
        db.update({"value507": value507}, personal.email == email)
        db.update({"value511": value511}, personal.email == email)
        db.update({"value512": value512}, personal.email == email)
        db.update({"value513": value513}, personal.email == email)
        db.update({"value514": value514}, personal.email == email)
        db.update({"value515": value515}, personal.email == email)
        db.update({"value516": value516}, personal.email == email)
        db.update({"value517": value517}, personal.email == email)
        db.update({"value521": value521}, personal.email == email)
        db.update({"value522": value522}, personal.email == email)
        db.update({"value523": value523}, personal.email == email)
        db.update({"value524": value524}, personal.email == email)
        db.update({"value525": value525}, personal.email == email)
        db.update({"value526": value526}, personal.email == email)
        db.update({"value527": value527}, personal.email == email)
        db.update({"activity": updater}, personal.email == email) 
        
        
        
        
        
        
        
        
        
        return render_template("index.html", user=inputs, color=colors, value11=value11, value12=value12, value13=value13, value14=value14, value15=value15, value16=value16, value17=value17, 
                               value21=value21, value22=value22, value23=value23, value24=value24, value25=value25, value26=value26, value27=value27, 
                               value31=value31, value32=value32, value33=value33, value34=value34, value35=value35, value36=value36, value37=value37, 
                               value41=value41, value42=value42, value43=value43, value44=value44, value45=value45, value46=value46, value47=value47, 
                               value51=value51, value52=value52, value53=value53, value54=value54, value55=value55, value56=value56, value57=value57, 
                               value61=value61, value62=value62, value63=value63, value64=value64, value65=value65, value66=value66, value67=value67, 
                               value71=value71, value72=value72, value73=value73, value74=value74, value75=value75, value76=value76, value77=value77, 
                               value81=value81, value82=value82, value83=value83, value84=value84, value85=value85, value86=value86, value87=value87, 
                               value91=value91, value92=value92, value93=value93, value94=value94, value95=value95, value96=value96, value97=value97, 
                               value101=value101, value102=value102, value103=value103, value104=value104, value105=value105, value106=value106, value107=value107, 
                               value111=value111, value112=value112, value113=value113, value114=value114, value115=value115, value116=value116, value117=value117, 
                               value121=value121, value122=value122, value123=value123, value124=value124, value125=value125, value126=value126, value127=value127, 
                               value131=value131, value132=value132, value133=value133, value134=value134, value135=value135, value136=value136, value137=value137, 
                               value141=value141, value142=value142, value143=value143, value144=value144, value145=value145, value146=value146, value147=value147, 
                               value151=value151, value152=value152, value153=value153, value154=value154, value155=value155, value156=value156, value157=value157, 
                               value161=value161, value162=value162, value163=value163, value164=value164, value165=value165, value166=value166, value167=value167, 
                               value171=value171, value172=value172, value173=value173, value174=value174, value175=value175, value176=value176, value177=value177, 
                               value181=value181, value182=value182, value183=value183, value184=value184, value185=value185, value186=value186, value187=value187, 
                               value191=value191, value192=value192, value193=value193, value194=value194, value195=value195, value196=value196, value197=value197, 
                               value201=value201, value202=value202, value203=value203, value204=value204, value205=value205, value206=value206, value207=value207, 
                               value211=value211, value212=value212, value213=value213, value214=value214, value215=value215, value216=value216, value217=value217, 
                               value221=value221, value222=value222, value223=value223, value224=value224, value225=value225, value226=value226, value227=value227, 
                               value231=value231, value232=value232, value233=value233, value234=value234, value235=value235, value236=value236, value237=value237, 
                               value241=value241, value242=value242, value243=value243, value244=value244, value245=value245, value246=value246, value247=value247, 
                               value251=value251, value252=value252, value253=value253, value254=value254, value255=value255, value256=value256, value257=value257, 
                               value261=value261, value262=value262, value263=value263, value264=value264, value265=value265, value266=value266, value267=value267, 
                               value271=value271, value272=value272, value273=value273, value274=value274, value275=value275, value276=value276, value277=value277, 
                               value281=value281, value282=value282, value283=value283, value284=value284, value285=value285, value286=value286, value287=value287, 
                               value291=value291, value292=value292, value293=value293, value294=value294, value295=value295, value296=value296, value297=value297, 
                               value301=value301, value302=value302, value303=value303, value304=value304, value305=value305, value306=value306, value307=value307, 
                               value311=value311, value312=value312, value313=value313, value314=value314, value315=value315, value316=value316, value317=value317, 
                               value321=value321, value322=value322, value323=value323, value324=value324, value325=value325, value326=value326, value327=value327, 
                               value331=value331, value332=value332, value333=value333, value334=value334, value335=value335, value336=value336, value337=value337, 
                               value341=value341, value342=value342, value343=value343, value344=value344, value345=value345, value346=value346, value347=value347, 
                               value351=value351, value352=value352, value353=value353, value354=value354, value355=value355, value356=value356, value357=value357, 
                               value361=value361, value362=value362, value363=value363, value364=value364, value365=value365, value366=value366, value367=value367, 
                               value371=value371, value372=value372, value373=value373, value374=value374, value375=value375, value376=value376, value377=value377, 
                               value381=value381, value382=value382, value383=value383, value384=value384, value385=value385, value386=value386, value387=value387, 
                               value391=value391, value392=value392, value393=value393, value394=value394, value395=value395, value396=value396, value397=value397, 
                               value401=value401, value402=value402, value403=value403, value404=value404, value405=value405, value406=value406, value407=value407, 
                               value411=value411, value412=value412, value413=value413, value414=value414, value415=value415, value416=value416, value417=value417, 
                               value421=value421, value422=value422, value423=value423, value424=value424, value425=value425, value426=value426, value427=value427, 
                               value431=value431, value432=value432, value433=value433, value434=value434, value435=value435, value436=value436, value437=value437, 
                               value441=value441, value442=value442, value443=value443, value444=value444, value445=value445, value446=value446, value447=value447, 
                               value451=value451, value452=value452, value453=value453, value454=value454, value455=value455, value456=value456, value457=value457, 
                               value461=value461, value462=value462, value463=value463, value464=value464, value465=value465, value466=value466, value467=value467, 
                               value471=value471, value472=value472, value473=value473, value474=value474, value475=value475, value476=value476, value477=value477, 
                               value481=value481, value482=value482, value483=value483, value484=value484, value485=value485, value486=value486, value487=value487, 
                               value491=value491, value492=value492, value493=value493, value494=value494, value495=value495, value496=value496, value497=value497, 
                               value501=value501, value502=value502, value503=value503, value504=value504, value505=value505, value506=value506, value507=value507, 
                               value511=value511, value512=value512, value513=value513, value514=value514, value515=value515, value516=value516, value517=value517, 
                               value521=value521, value522=value522, value523=value523, value524=value524, value525=value525, value526=value526, value527=value527, 
                               )
        
    return render_template("index.html", user=inputs, color=colors, value11=value11, value12=value12, value13=value13, value14=value14, value15=value15, value16=value16, value17=value17, 
                               value21=value21, value22=value22, value23=value23, value24=value24, value25=value25, value26=value26, value27=value27, 
                               value31=value31, value32=value32, value33=value33, value34=value34, value35=value35, value36=value36, value37=value37, 
                               value41=value41, value42=value42, value43=value43, value44=value44, value45=value45, value46=value46, value47=value47, 
                               value51=value51, value52=value52, value53=value53, value54=value54, value55=value55, value56=value56, value57=value57, 
                               value61=value61, value62=value62, value63=value63, value64=value64, value65=value65, value66=value66, value67=value67, 
                               value71=value71, value72=value72, value73=value73, value74=value74, value75=value75, value76=value76, value77=value77, 
                               value81=value81, value82=value82, value83=value83, value84=value84, value85=value85, value86=value86, value87=value87, 
                               value91=value91, value92=value92, value93=value93, value94=value94, value95=value95, value96=value96, value97=value97, 
                               value101=value101, value102=value102, value103=value103, value104=value104, value105=value105, value106=value106, value107=value107, 
                               value111=value111, value112=value112, value113=value113, value114=value114, value115=value115, value116=value116, value117=value117, 
                               value121=value121, value122=value122, value123=value123, value124=value124, value125=value125, value126=value126, value127=value127, 
                               value131=value131, value132=value132, value133=value133, value134=value134, value135=value135, value136=value136, value137=value137, 
                               value141=value141, value142=value142, value143=value143, value144=value144, value145=value145, value146=value146, value147=value147, 
                               value151=value151, value152=value152, value153=value153, value154=value154, value155=value155, value156=value156, value157=value157, 
                               value161=value161, value162=value162, value163=value163, value164=value164, value165=value165, value166=value166, value167=value167, 
                               value171=value171, value172=value172, value173=value173, value174=value174, value175=value175, value176=value176, value177=value177, 
                               value181=value181, value182=value182, value183=value183, value184=value184, value185=value185, value186=value186, value187=value187, 
                               value191=value191, value192=value192, value193=value193, value194=value194, value195=value195, value196=value196, value197=value197, 
                               value201=value201, value202=value202, value203=value203, value204=value204, value205=value205, value206=value206, value207=value207, 
                               value211=value211, value212=value212, value213=value213, value214=value214, value215=value215, value216=value216, value217=value217, 
                               value221=value221, value222=value222, value223=value223, value224=value224, value225=value225, value226=value226, value227=value227, 
                               value231=value231, value232=value232, value233=value233, value234=value234, value235=value235, value236=value236, value237=value237, 
                               value241=value241, value242=value242, value243=value243, value244=value244, value245=value245, value246=value246, value247=value247, 
                               value251=value251, value252=value252, value253=value253, value254=value254, value255=value255, value256=value256, value257=value257, 
                               value261=value261, value262=value262, value263=value263, value264=value264, value265=value265, value266=value266, value267=value267, 
                               value271=value271, value272=value272, value273=value273, value274=value274, value275=value275, value276=value276, value277=value277, 
                               value281=value281, value282=value282, value283=value283, value284=value284, value285=value285, value286=value286, value287=value287, 
                               value291=value291, value292=value292, value293=value293, value294=value294, value295=value295, value296=value296, value297=value297, 
                               value301=value301, value302=value302, value303=value303, value304=value304, value305=value305, value306=value306, value307=value307, 
                               value311=value311, value312=value312, value313=value313, value314=value314, value315=value315, value316=value316, value317=value317, 
                               value321=value321, value322=value322, value323=value323, value324=value324, value325=value325, value326=value326, value327=value327, 
                               value331=value331, value332=value332, value333=value333, value334=value334, value335=value335, value336=value336, value337=value337, 
                               value341=value341, value342=value342, value343=value343, value344=value344, value345=value345, value346=value346, value347=value347, 
                               value351=value351, value352=value352, value353=value353, value354=value354, value355=value355, value356=value356, value357=value357, 
                               value361=value361, value362=value362, value363=value363, value364=value364, value365=value365, value366=value366, value367=value367, 
                               value371=value371, value372=value372, value373=value373, value374=value374, value375=value375, value376=value376, value377=value377, 
                               value381=value381, value382=value382, value383=value383, value384=value384, value385=value385, value386=value386, value387=value387, 
                               value391=value391, value392=value392, value393=value393, value394=value394, value395=value395, value396=value396, value397=value397, 
                               value401=value401, value402=value402, value403=value403, value404=value404, value405=value405, value406=value406, value407=value407, 
                               value411=value411, value412=value412, value413=value413, value414=value414, value415=value415, value416=value416, value417=value417, 
                               value421=value421, value422=value422, value423=value423, value424=value424, value425=value425, value426=value426, value427=value427, 
                               value431=value431, value432=value432, value433=value433, value434=value434, value435=value435, value436=value436, value437=value437, 
                               value441=value441, value442=value442, value443=value443, value444=value444, value445=value445, value446=value446, value447=value447, 
                               value451=value451, value452=value452, value453=value453, value454=value454, value455=value455, value456=value456, value457=value457, 
                               value461=value461, value462=value462, value463=value463, value464=value464, value465=value465, value466=value466, value467=value467, 
                               value471=value471, value472=value472, value473=value473, value474=value474, value475=value475, value476=value476, value477=value477, 
                               value481=value481, value482=value482, value483=value483, value484=value484, value485=value485, value486=value486, value487=value487, 
                               value491=value491, value492=value492, value493=value493, value494=value494, value495=value495, value496=value496, value497=value497, 
                               value501=value501, value502=value502, value503=value503, value504=value504, value505=value505, value506=value506, value507=value507, 
                               value511=value511, value512=value512, value513=value513, value514=value514, value515=value515, value516=value516, value517=value517, 
                               value521=value521, value522=value522, value523=value523, value524=value524, value525=value525, value526=value526, value527=value527)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=75, debug=True)