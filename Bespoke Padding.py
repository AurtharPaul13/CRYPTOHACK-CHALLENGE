from utils import listener
from Crypto.Util.number import bytes_to_long, getPrime
import random

FLAG = b'crypto{???????????????????????????}'


class Challenge():
    def __init__(self):
        self.before_input = "Come back as much as you want! You'll never get my flag.\n"
        self.p = getPrime(1024)
        self.q = getPrime(1024)
        self.N = self.p * self.q
        self.e = 11

    def pad(self, flag):
        m = bytes_to_long(flag)
        a = random.randint(2, self.N)
        b = random.randint(2, self.N)
        return (a, b), a*m+b

    def encrypt(self, flag):
        pad_var, pad_msg = self.pad(flag)
        encrypted = (pow(pad_msg, self.e, self.N), self.N)
        return pad_var, encrypted

    def challenge(self, your_input):
        if not 'option' in your_input:
            return {"error": "You must send an option to this server"}

        elif your_input['option'] == 'get_flag':
            pad_var, encrypted = self.encrypt(FLAG)
            return {"encrypted_flag": encrypted[0], "modulus": encrypted[1], "padding": pad_var}

        else:
            return {"error": "Invalid option"}

      from pwn import *
from json import *

def send(hsh):
    return r.sendline(dumps(hsh).encode())

option = {
    'option': 'get_flag'
}
r = connect('socket.cryptohack.org', 13386)
r.recv()

enc = []
padding = []
n = 0
e = 11
send(option)
get1 = loads(r.recvuntil('}'))
enc.append(get1['encrypted_flag'])
padding.append(get1['padding'])

send(option)
get2 = loads(r.recvuntil('}'))
enc.append(get2['encrypted_flag'])
padding2 = get2['padding']
padding.append(get2['padding'])
assert get1['modulus'] == get2['modulus']
n = get1['modulus']

print(f'{enc = }')
print(f'{padding = }')
print(f'{n = }')
print(f'{e = }')

from Crypto.Util.number import long_to_bytes

enc = [7100471843638722289145167976606910159773138627423709595150798616816912608359586319306293257214081804010823296916273940791849973540111317677759409336871392368452501475423097005481973798772513132512108238910607226635988637953448918956558791314214147588373238958078150608219388374961536924967344309464270442318214989658627354998075057311939720175613834278397259987715228276202347028144867033469003848173009494204872529617410272037690826989674454532694289648440508753070511166587890116097675346856531360458183388798905732132355729884794843178592142055260682264344749466187293896166061696494864346905075145951040056156431, 1409748709950292874622277704193051118536706855123389331208988530884888555436254109679692049085268311429053834076971118583135611341883468934673085267942820066425649527174801697020835725274754643531146509498092617910493035467181903185821151745479788200950904368266164263860030134767872880687877738564114369722170823700449880902918643618815515584584512422873798284015144097351700927100292287659169848139113977881478760075225152849069522323005405533282746808568265798714820762139744558585479705078746190546772467653352371893182805560879813528837887710010117866032966437167674799907344414942300756008747447846856407166254]
padding = [[7226432484418709728502788814115475985223860639771383288383579996661038444889262247347504216810795524345086752669604938430595531947830098206386511591129632388647065386548004976885110696215986426323004441894549658902838274207209403179666843222996526829702897197026489506149144566534572700797958111637472106929103798226354995777678422558608863713553052501290053721884856547866457851648313000381246431406822883943413220484483703686905696960366876341494750598855825895409079800829125846498148551965510867854980265291785015327913884923861624261197538456030251948926204486973415916172742127769438122239608668266302380845729, 2564483966134092537639306264886796121451516245052897813034116134977116567103115472476025566366180795847141098004098515752587165412622055351935097070251783598349802608982232342602952603678514440736323725685622352768463636508519644455176706737367920123909225097915906371641673031258908771855713799834702349110295937948920226933268259595016527412025500067731001496462783995072771101781061171247889053981544152138063697746642761786896616251380156839797067976177924804956139571431004343396336877898407811590817767646640374623552004658758504670308372891945264219468642058825597252028577164390280803718754640673954133028398], [9049001627949003065365662285805417665907116914698241870571300266402570316920417093017483568397571317830531219268110298124431432362933722871313445496058132876178670409011632232725082383831930845135338858596388340852687314620222433210031672052655795317051383376392229715324480186743070915829878785644188925474541174821983150642996173715888854507776161643730328814109313846059413927235410357963847508485604772163706991515756105382153300227426926150319712221826108190812314682247333483647783556331271609249806636793325437332179721252448924538212588007268567338250346479245346636685313538974804491075019882070799487218918, 10597969989623979121122092539160116893902580153808358757149248643804900854144954536559297235459340366638145059609140336995392902422492142546234398884650371898563594728967706990611675146186512832475486340373271444570075914431262056400826615565686820908927755451228432997471755971170796224070873123993350122348890616073797525015954553120137163497808083102622312838363146041630066722843651747118883415739634473585330350080819678239500816088193039037377334189335668532244406944498783120654610807980166668347633047654114636124066585337198959279152537765512515723338149483471071383554196872372958648946403441942674048034073]]
n = 11416779452654399252749863040595828556008489215719804758281310703773063470473354493555693465727247199282711340023343259632634967801836384147898950691525505584451538754856400419340929720593835601187204170137351576988380832259703680571023466109554972858605106302667769239197997819727587849399487837970185751881192400251681932810203185938934548488366319424840632271125354507512173564269402303700777356800669186223932707883165550956089104301583299768756868601171465891237691635234504186470464963716410242787197588203713070761931591842549972123168850965817306755850399724333601720382742316904547945153594270150910697537693
e = 11

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a.monic()

P.<x> = PolynomialRing(Zmod(n))
p1 = (padding[0][0] * x + padding[0][1]) ^ e - enc[0]
p2 = (padding[1][0] * x + padding[1][1]) ^ e - enc[1]
m = -gcd(p1, p2).coefficients()[0]
flag = long_to_bytes(int(m)).decode()
print(flag)
