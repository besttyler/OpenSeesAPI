############################################################################
##### This is a sample script that runs an SDOF analysis in OpenSees
##### using an Ibarra-Krawinkler Deterioation spring
##### Coded by Nasser Marafi (marafi@uw.edu)
##### Last Updated: 8/12/2015
##### Make sure to have a subfolder called /tcl/ with the OpenSees Executable File
############################################################################
__author__ = 'marafi'

import os
import numpy as np

########################## Input Parameters ##########################

# This is Elcentro's Ground Motion in g
GMData = 386.4*np.array([0.0063,0.00364,0.00099,0.00428,0.00758,0.01087,0.00682,0.00277,-0.00128,0.00368,0.00864,0.0136,0.00727,0.00094,0.0042,0.00221,0.00021,0.00444,0.00867,0.0129,0.01713,-0.00343,-0.024,-0.00992,0.00416,0.00528,0.01653,0.02779,0.03904,0.02449,0.00995,0.00961,0.00926,0.00892,-0.00486,-0.01864,-0.03242,-0.03365,-0.05723,-0.04534,-0.03346,-0.03201,-0.03056,-0.02911,-0.02766,-0.04116,-0.05466,-0.06816,-0.08166,-0.06846,-0.05527,-0.04208,-0.04259,-0.04311,-0.02428,-0.00545,0.01338,0.03221,0.05104,0.06987,0.0887,0.04524,0.00179,-0.04167,-0.08513,-0.12858,-0.17204,-0.12908,-0.08613,-0.08902,-0.09192,-0.09482,-0.09324,-0.09166,-0.09478,-0.09789,-0.12902,-0.07652,-0.02401,0.02849,0.08099,0.1335,0.186,0.2385,0.21993,0.20135,0.18277,0.1642,0.14562,0.16143,0.17725,0.13215,0.08705,0.04196,-0.00314,-0.04824,-0.09334,-0.13843,-0.18353,-0.22863,-0.27372,-0.31882,-0.25024,-0.18166,-0.11309,-0.04451,0.02407,0.09265,0.16123,0.22981,0.29839,0.23197,0.16554,0.09912,0.0327,-0.03372,-0.10014,-0.16656,-0.23299,-0.29941,-0.00421,0.29099,0.2238,0.15662,0.08943,0.02224,-0.04495,0.01834,0.08163,0.14491,0.2082,0.18973,0.17125,0.13759,0.10393,0.07027,0.03661,0.00295,-0.03071,-0.00561,0.01948,0.04458,0.06468,0.08478,0.10487,0.05895,0.01303,-0.03289,-0.07882,-0.03556,0.00771,0.05097,0.01013,-0.03071,-0.07156,-0.1124,-0.15324,-0.11314,-0.07304,-0.03294,0.00715,-0.0635,-0.13415,-0.2048,-0.12482,-0.04485,0.03513,0.1151,0.19508,0.12301,0.05094,-0.02113,-0.0932,-0.02663,0.03995,0.10653,0.17311,0.11283,0.05255,-0.00772,0.01064,0.029,0.04737,0.06573,0.02021,-0.0253,-0.07081,-0.04107,-0.01133,0.00288,0.01709,0.03131,-0.02278,-0.07686,-0.13095,-0.18504,-0.14347,-0.1019,-0.06034,-0.01877,0.0228,-0.00996,-0.04272,-0.02147,-0.00021,0.02104,-0.01459,-0.05022,-0.08585,-0.12148,-0.15711,-0.19274,-0.22837,-0.18145,-0.13453,-0.08761,-0.04069,0.00623,0.05316,0.10008,0.147,0.09754,0.04808,-0.00138,0.05141,0.1042,0.15699,0.20979,0.26258,0.16996,0.07734,-0.01527,-0.10789,-0.20051,-0.06786,0.06479,0.01671,-0.03137,-0.07945,-0.12753,-0.17561,-0.22369,-0.27177,-0.15851,-0.04525,0.06802,0.18128,0.14464,0.108,0.07137,0.03473,0.09666,0.1586,0.22053,0.18296,0.14538,0.1078,0.07023,0.03265,0.06649,0.10033,0.13417,0.10337,0.07257,0.04177,0.01097,-0.01983,0.04438,0.1086,0.17281,0.10416,0.03551,-0.03315,-0.1018,-0.07262,-0.04344,-0.01426,0.01492,-0.02025,-0.05543,-0.0906,-0.12578,-0.16095,-0.19613,-0.14784,-0.09955,-0.05127,-0.00298,-0.01952,-0.03605,-0.05259,-0.04182,-0.03106,-0.02903,-0.02699,0.02515,0.0177,0.02213,0.02656,0.00419,-0.01819,-0.04057,-0.06294,-0.02417,0.0146,0.05337,0.02428,-0.0048,-0.03389,-0.00557,0.02274,0.00679,-0.00915,-0.02509,-0.04103,-0.05698,-0.01826,0.02046,0.00454,-0.01138,-0.00215,0.00708,0.00496,0.00285,0.00074,-0.00534,-0.01141,0.00361,0.01863,0.03365,0.04867,0.0304,0.01213,-0.00614,-0.02441,0.01375,0.01099,0.00823,0.00547,0.00812,0.01077,-0.00692,-0.02461,-0.0423,-0.05999,-0.07768,-0.09538,-0.06209,-0.0288,0.00448,0.03777,0.01773,-0.00231,-0.02235,0.01791,0.05816,0.03738,0.0166,-0.00418,-0.02496,-0.04574,-0.02071,0.00432,0.02935,0.01526,0.01806,0.02086,0.00793,-0.00501,-0.01795,-0.03089,-0.01841,-0.00593,0.00655,-0.02519,-0.05693,-0.04045,-0.02398,-0.0075,0.00897,0.00384,-0.00129,-0.00642,-0.01156,-0.02619,-0.04082,-0.05545,-0.04366,-0.03188,-0.06964,-0.05634,-0.04303,-0.02972,-0.01642,-0.00311,0.0102,0.0235,0.03681,0.05011,0.02436,-0.00139,-0.02714,-0.00309,0.02096,0.04501,0.06906,0.05773,0.0464,0.03507,0.03357,0.03207,0.03057,0.0325,0.03444,0.03637,0.01348,-0.00942,-0.03231,-0.02997,-0.03095,-0.03192,-0.02588,-0.01984,-0.01379,-0.00775,-0.01449,-0.02123,0.01523,0.0517,0.08816,0.12463,0.16109,0.12987,0.09864,0.06741,0.03618,0.00495,0.0042,0.00345,0.00269,-0.05922,-0.12112,-0.18303,-0.12043,-0.05782,0.00479,0.0674,0.13001,0.08373,0.03745,0.06979,0.10213,-0.03517,-0.17247,-0.13763,-0.10278,-0.06794,-0.0331,-0.03647,-0.03984,-0.00517,0.0295,0.06417,0.09883,0.1335,0.05924,-0.01503,-0.08929,-0.16355,-0.06096,0.04164,0.01551,-0.01061,-0.03674,-0.06287,-0.08899,-0.0543,-0.01961,0.01508,0.04977,0.08446,0.05023,0.016,-0.01823,-0.05246,-0.08669,-0.06769,-0.0487,-0.0297,-0.01071,0.00829,-0.00314,0.02966,0.06246,-0.00234,-0.06714,-0.04051,-0.01388,0.01274,0.00805,0.03024,0.05243,0.02351,-0.00541,-0.03432,-0.06324,-0.09215,-0.12107,-0.0845,-0.04794,-0.01137,0.0252,0.06177,0.04028,0.0188,0.04456,0.07032,0.09608,0.12184,0.0635,0.00517,-0.05317,-0.03124,-0.0093,0.01263,0.03457,0.03283,0.03109,0.02935,0.04511,0.06087,0.07663,0.09239,0.05742,0.02245,-0.01252,0.0068,0.02611,0.04543,0.01571,-0.01402,-0.04374,-0.07347,-0.0399,-0.00633,0.02724,0.0608,0.03669,0.01258,-0.01153,-0.03564,-0.00677,0.0221,0.05098,0.07985,0.06915,0.05845,0.04775,0.03706,0.02636,0.05822,0.09009,0.12196,0.10069,0.07943,0.05816,0.03689,0.01563,-0.00564,-0.0269,-0.04817,-0.06944,-0.0907,-0.11197,-0.11521,-0.11846,-0.1217,-0.12494,-0.165,-0.20505,-0.15713,-0.10921,-0.06129,-0.01337,0.03455,0.08247,0.07576,0.06906,0.06236,0.08735,0.11235,0.13734,0.12175,0.10616,0.09057,0.07498,0.08011,0.08524,0.09037,0.06208,0.03378,0.00549,-0.02281,-0.05444,-0.0403,-0.02615,-0.01201,-0.02028,-0.02855,-0.06243,-0.03524,-0.00805,-0.04948,-0.03643,-0.02337,-0.03368,-0.01879,-0.00389,0.011,0.02589,0.01446,0.00303,-0.0084,0.00463,0.01766,0.03069,0.04372,0.02165,-0.00042,-0.02249,-0.04456,-0.03638,-0.02819,-0.02001,-0.01182,-0.02445,-0.03707,-0.04969,-0.05882,-0.06795,-0.07707,-0.0862,-0.09533,-0.06276,-0.03018,0.00239,0.03496,0.04399,0.05301,0.03176,0.01051,-0.01073,-0.03198,-0.05323,0.00186,0.05696,0.01985,-0.01726,-0.05438,-0.01204,0.03031,0.07265,0.11499,0.07237,0.02975,-0.01288,0.01212,0.03711,0.03517,0.03323,0.01853,0.00383,0.00342,-0.02181,-0.04704,-0.07227,-0.0975,-0.12273,-0.08317,-0.04362,-0.00407,0.03549,0.07504,0.1146,0.07769,0.04078,0.00387,0.00284,0.00182,-0.05513,0.04732,0.05223,0.05715,0.06206,0.06698,0.07189,0.02705,-0.01779,-0.06263,-0.10747,-0.15232,-0.12591,-0.0995,-0.07309,-0.04668,-0.02027,0.00614,0.03255,0.00859,-0.01537,-0.03932,-0.06328,-0.03322,-0.00315,0.02691,0.01196,-0.003,0.00335,0.0097,0.01605,0.02239,0.04215,0.06191,0.08167,0.03477,-0.01212,-0.01309,-0.01407,-0.05274,-0.02544,0.00186,0.02916,0.05646,0.08376,0.01754,-0.04869,-0.02074,0.00722,0.03517,-0.00528,-0.04572,-0.08617,-0.0696,-0.05303,-0.03646,-0.01989,-0.00332,0.01325,0.02982,0.01101,-0.00781,-0.02662,-0.00563,0.01536,0.03635,0.05734,0.03159,0.00584,-0.01992,-0.00201,0.01589,-0.01024,-0.03636,-0.06249,-0.0478,-0.03311,-0.04941,-0.0657,-0.082,-0.0498,-0.0176,0.0146,0.0468,0.079,0.0475,0.016,-0.0155,-0.00102,0.01347,0.02795,0.04244,0.05692,0.03781,0.0187,-0.00041,-0.01952,-0.00427,0.01098,0.02623,0.04148,0.01821,-0.00506,-0.00874,-0.03726,-0.06579,-0.026,0.0138,0.05359,0.09338,0.05883,0.02429,-0.01026,-0.0448,-0.01083,-0.01869,-0.02655,-0.03441,-0.02503,-0.01564,-0.00626,-0.01009,-0.01392,0.0149,0.04372,0.03463,0.02098,0.00733,-0.00632,-0.01997,0.00767,0.03532,0.03409,0.03287,0.03164,0.02403,0.01642,0.00982,0.00322,-0.00339,0.02202,-0.01941,-0.06085,-0.10228,-0.07847,-0.05466,-0.03084,-0.00703,0.01678,0.01946,0.02214,0.02483,0.01809,-0.00202,-0.02213,-0.00278,0.01656,0.0359,0.05525,0.07459,0.06203,0.04948,0.03692,-0.00145,0.04599,0.04079,0.03558,0.03037,0.03626,0.04215,0.04803,0.05392,0.04947,0.04502,0.04056,0.03611,0.03166,0.00614,-0.01937,-0.04489,-0.0704,-0.09592,-0.07745,-0.05899,-0.04052,-0.02206,-0.00359,0.01487,0.01005,0.00523,0.00041,-0.00441,-0.00923,-0.01189,-0.01523,-0.01856,-0.0219,-0.00983,0.00224,0.01431,0.00335,-0.0076,-0.01856,-0.00737,0.00383,0.01502,0.02622,0.01016,-0.0059,-0.02196,-0.00121,0.01953,0.04027,0.02826,0.01625,0.00424,0.00196,-0.00031,-0.00258,-0.00486,-0.00713,-0.00941,-0.01168,-0.01396,-0.0175,-0.02104,-0.02458,-0.02813,-0.03167,-0.03521,-0.04205,-0.04889,-0.03559,-0.02229,-0.00899,0.00431,0.01762,0.00714,-0.00334,-0.01383,0.01314,0.04011,0.06708,0.0482,0.02932,0.01043,-0.00845,-0.02733,-0.04621,-0.03155,-0.01688,-0.00222,0.01244,0.02683,0.04121,0.05559,0.03253,0.00946,-0.0136,-0.01432,-0.01504,-0.01576,-0.04209,-0.02685,-0.01161,0.00363,0.01887,0.03411,0.03115,0.02819,0.02917,0.03015,0.03113,0.00388,-0.02337,-0.05062,-0.0382,-0.02579,-0.01337,-0.00095,0.01146,0.02388,0.03629,0.01047,-0.01535,-0.04117,-0.06699,-0.05207,-0.03715,-0.02222,-0.0073,0.00762,0.02254,0.03747,0.04001,0.04256,0.04507,0.04759,0.0501,0.04545,0.0408,0.02876,0.01671,0.00467,-0.00738,-0.00116,0.00506,0.01128,0.0175,-0.00211,-0.02173,-0.04135,-0.06096,-0.08058,-0.06995,-0.05931,-0.04868,-0.03805,-0.02557,-0.0131,-0.00063,0.01185,0.02432,0.0368,0.04927,0.02974,0.01021,-0.00932,-0.02884,-0.04837,-0.0679,-0.04862,-0.02934,-0.01006,0.00922,0.02851,0.04779,0.02456,0.00133,-0.0219,-0.04513,-0.06836,-0.04978,-0.0312,-0.01262,0.00596,0.02453,0.04311,0.06169,0.08027,0.09885,0.06452,0.03019,-0.00414,-0.03848,-0.07281,-0.05999,-0.04717,-0.03435,-0.03231,-0.03028,-0.02824,-0.00396,0.02032,0.00313,-0.01406,-0.03124,-0.04843,-0.06562,-0.05132,-0.03702,-0.02272,-0.00843,0.00587,0.02017,0.02698,0.03379,0.04061,0.04742,0.05423,0.03535,0.01647,0.01622,0.01598,0.01574,0.00747,-0.0008,-0.00907,0.00072,0.01051,0.0203,0.03009,0.03989,0.03478,0.02967,0.02457,0.03075,0.03694,0.04313,0.04931,0.0555,0.06168,-0.00526,-0.0722,-0.06336,-0.05451,-0.04566,-0.03681,-0.03678,-0.03675,-0.03672,-0.01765,0.00143,0.02051,0.03958,0.05866,0.03556,0.01245,-0.01066,-0.03376,-0.05687,-0.04502,-0.03317,-0.02131,-0.00946,0.00239,-0.00208,-0.00654,-0.01101,-0.01548,-0.012,-0.00851,-0.00503,-0.00154,0.00195,0.00051,-0.00092,0.01135,0.02363,0.0359,0.04818,0.06045,0.07273,0.02847,-0.01579,-0.06004,-0.05069,-0.04134,-0.03199,-0.03135,-0.03071,-0.03007,-0.01863,-0.00719,0.00425,0.0157,0.02714,0.03858,0.02975,0.02092,0.02334,0.02576,0.02819,0.03061,0.03304,0.01371,-0.00561,-0.02494,-0.02208,-0.01923,-0.01638,-0.01353,-0.01261,-0.0117,-0.00169,0.00833,0.01834,0.02835,0.03836,0.04838,0.03749,0.0266,0.01571,0.00482,-0.00607,-0.01696,-0.0078,0.00136,0.01052,0.01968,0.02884,-0.00504,-0.03893,-0.02342,-0.00791,0.00759,0.0231,0.00707,-0.00895,-0.02498,-0.041,-0.05703,-0.0292,-0.00137,0.02645,0.05428,0.03587,0.01746,-0.00096,-0.01937,-0.03778,-0.02281,-0.00784,0.00713,0.0221,0.03707,0.05204,0.06701,0.08198,0.03085,-0.02027,-0.0714,-0.12253,-0.08644,-0.05035,-0.01426,0.02183,0.05792,0.094,0.13009,0.03611,-0.05787,-0.04802,-0.03817,-0.02832,-0.01846,-0.00861,-0.03652,-0.06444,-0.06169,-0.05894,-0.05618,-0.06073,-0.06528,-0.04628,-0.02728,-0.00829,0.01071,0.0297,0.03138,0.03306,0.03474,0.03642,0.04574,0.05506,0.06439,0.07371,0.08303,0.03605,-0.01092,-0.0579,-0.04696,-0.03602,-0.02508,-0.01414,-0.03561,-0.05708,-0.07855,-0.06304,-0.04753,-0.03203,-0.01652,-0.00102,0.00922,0.01946,0.0297,0.03993,0.05017,0.06041,0.07065,0.08089,-0.00192,-0.08473,-0.07032,-0.0559,-0.04148,-0.05296,-0.06443,-0.0759,-0.08738,-0.09885,-0.06798,-0.0371,-0.00623,0.02465,0.05553,0.0864,0.11728,0.14815,0.08715,0.02615,-0.03485,-0.09584,-0.071,-0.04616,-0.02132,0.00353,0.02837,0.05321,-0.00469,-0.06258,-0.12048,-0.0996,-0.07872,-0.05784,-0.03696,-0.01608,0.0048,0.02568,0.04656,0.06744,0.08832,0.1092,0.13008,0.10995,0.08982,0.06969,0.04955,0.04006,0.03056,0.02107,0.01158,0.0078,0.00402,0.00024,-0.00354,-0.00732,-0.0111,-0.0078,-0.0045,-0.0012,0.0021,0.0054,-0.00831,-0.02203,-0.03575,-0.04947,-0.06319,-0.05046,-0.03773,-0.025,-0.01227,0.00046,0.00482,0.00919,0.01355,0.01791,0.02228,0.00883,-0.00462,-0.01807,-0.03152,-0.02276,-0.01401,-0.00526,0.0035,0.01225,0.02101,0.01437,0.00773,0.0011,0.00823,0.01537,0.02251,0.01713,0.01175,0.00637,0.01376,0.02114,0.02852,0.03591,0.04329,0.03458,0.02587,0.01715,0.00844,-0.00027,-0.00898,-0.00126,0.00645,0.01417,0.02039,0.02661,0.03283,0.03905,0.04527,0.03639,0.0275,0.01862,0.00974,0.00086,-0.01333,-0.02752,-0.04171,-0.02812,-0.01453,-0.00094,0.01264,0.02623,0.0169,0.00756,-0.00177,-0.01111,-0.02044,-0.02977,-0.03911,-0.02442,-0.00973,0.00496,0.01965,0.03434,0.02054,0.00674,-0.00706,-0.02086,-0.03466,-0.02663,-0.0186,-0.01057,-0.00254,-0.00063,0.00128,0.00319,0.0051,0.00999,0.01488,0.00791,0.00093,-0.00605,0.00342,0.01288,0.02235,0.03181,0.04128,0.02707,0.01287,-0.00134,-0.01554,-0.02975,-0.04395,-0.03612,-0.02828,-0.02044,-0.0126,-0.00476,0.00307,0.01091,0.00984,0.00876,0.00768,0.00661,0.01234,0.01807,0.0238,0.02953,0.03526,0.02784,0.02042,0.013,-0.03415,-0.00628,-0.00621,-0.00615,-0.00609,-0.00602,-0.00596,-0.0059,-0.00583,-0.00577,-0.00571,-0.00564,-0.00558,-0.00552,-0.00545,-0.00539,-0.00532,-0.00526,-0.0052,-0.00513,-0.00507,-0.00501,-0.00494,-0.00488,-0.00482,-0.00475,-0.00469,-0.00463,-0.00456,-0.0045,-0.00444,-0.00437,-0.00431,-0.00425,-0.00418,-0.00412,-0.00406,-0.00399,-0.00393,-0.00387,-0.0038,-0.00374,-0.00368,-0.00361,-0.00355,-0.00349,-0.00342,-0.00336,-0.0033,-0.00323,-0.00317,-0.00311,-0.00304,-0.00298,-0.00292,-0.00285,-0.00279,-0.00273,-0.00266,-0.0026,-0.00254,-0.00247,-0.00241,-0.00235,-0.00228,-0.00222,-0.00216,-0.00209,-0.00203,-0.00197,-0.0019,-0.00184,-0.00178,-0.00171,-0.00165,-0.00158,-0.00152,-0.00146,-0.00139,-0.00133,-0.00127,-0.0012,-0.00114,-0.00108,-0.00101,-0.00095,-0.00089,-0.00082,-0.00076,-0.0007,-0.00063,-0.00057,-0.00051,-0.00044,-0.00038,-0.00032,-0.00025,-0.00019,-0.00013,-0.00006,0]+list(np.zeros(1000)))
Dt = 0.02
T = 1.0
Dy = 2
Zeta = 0.05
PY = 0.05
PC = 0.1
LamdaSCA = 100
LamdaK = 50
cRate = 1
Mu = 8
Kappa = 0.01

# OpenSeesCommand = os.getcwd()+'//tcl//OpenSees' # Path to the OpenSees Executable File
OpenSeesCommand = 'OpenSees'

########################## Pre-Initialization ##########################
import OpenSeesAPI
import os
import numpy as np

g=386.1
#Mass
m = 1
wn = 2*np.pi/T

#Stiffness
k = wn**2.0*m

#Damping 2%
c=Zeta*2*m*wn

########################## Initializing ##########################

### Create OpenSees Database

import time
import uuid
randomnumber = str(uuid.uuid4().get_hex().upper()[0:12])
timestamp = time.strftime("%y%m%d-%H%M%S")+randomnumber
ModelName = 'ExampleScript'
FileName = '%s-%s.tcl'%(ModelName,timestamp)
TCLFileDirectory = os.getcwd()+'/tcl/'
ResultDirectory = os.getcwd()+'/tcl/Results/'

if not os.path.exists(TCLFileDirectory): #Make Directory is unavailable
    os.makedirs(TCLFileDirectory)
if not os.path.exists(ResultDirectory): #Make Directory is unavailable
    os.makedirs(ResultDirectory)

OData = OpenSeesAPI.Database.Collector(OpenSeesCommand, TCLFileDirectory, FileName)

########################## Setup and Source Definition ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Initialization'))
OData.AddObject(OpenSeesAPI.Model.BasicBuilder(2,3))

########################## Define Building Geometry, Nodes and Constraints ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Geometry Setup'))

SupportNode = OData.CreateNode(0,0)
MassNode = OData.CreateNode(0,0)
OData.AddConstraint(OpenSeesAPI.Model.Node.Mass(MassNode,[m,1e-6,1e-6]))

########################## Define Geometric Transformations ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Geometric Transformations'))

#Define Geometry Transformations for Beams and Column
GeoTransfLinear = OpenSeesAPI.Model.Element.GeomTransf.Linear(1)
OData.AddObject(GeoTransfLinear)

##############################################################################
### All OpenSEES Objects are adding directly to the Database Beyond This Point
##############################################################################

########################## Define Materials and Sections ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Materials and Sections'))

########################## Define Rotational Springs for Plastic Hinge ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Rotational Springs for Plastic Hinge'))

#Define Rotational Spring
#### Collector Should Give ID

ThetaP = Dy*Mu - Dy
Ult = k*Dy + k*PY*ThetaP
ThetaPC = Ult/(k*PC)
Spring = OpenSeesAPI.Model.Element.Material.UniaxialMaterial.ModIMKPinched(1,k,PY,PY,k*Dy,-1*k*Dy, 0.1, 0.1, 0.5, LamdaSCA,LamdaSCA,LamdaSCA,LamdaK,cRate,cRate,cRate,cRate,ThetaP, ThetaP, ThetaPC, ThetaPC, Kappa, Kappa, (ThetaPC+ThetaP+Dy)*2, (ThetaPC+ThetaP+Dy)*2, 1.0, 1.0)
OData.AddMaterial(Spring)

########################## Define Elements ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Elements'))
OData.AddElement(OpenSeesAPI.Model.Element.Element.ZeroLength(OData.GetFreeElementId(9,1),SupportNode, MassNode, [Spring],[1]))

##############################################################################
### Start Writing Elements to the Executible File
##############################################################################

# Setting Nodes as Used
for object in set(OData._Elements):
    object._NodeI.__setattr__('Used',True)
    object._NodeJ.__setattr__('Used',True)

#Writing Nodes to File
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Defining Nodes'))
for obj in OData._Nodes:
    try:
        if obj.Used:
            OData.Executable.AddCommand(obj.CommandLine)
    except:
        continue

#Defining Fixity
OData.AddConstraint(OpenSeesAPI.Model.Constraint.Fix(SupportNode,[1,1,1]))
OData.AddConstraint(OpenSeesAPI.Model.Constraint.Fix(MassNode,[0,1,1]))

#Defining Masses

#Write Element from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Materials'))
for obj in OData._Materials:
    OData.Executable.AddCommand(obj.CommandLine)

#Write Sections from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Sections'))
for obj in OData._Sections:
    OData.Executable.AddCommand(obj.CommandLine)

#Write Elements from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Elements'))
for obj in OData._Elements:
    OData.Executable.AddCommand(obj.CommandLine)

#Write Shells from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Shells'))
for obj in OData._Quadrilaterals:
    OData.Executable.AddCommand(obj.CommandLine)

#Write Constraints from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Constraints'))
for obj in OData._Constraints:
    OData.Executable.AddCommand(obj.CommandLine)

########################## Eigenvalue Analysis ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Eigenvalue Analysis'))
OData.AddObject(OpenSeesAPI.Analysis.Eigen(1, fullGenLapack=True))

########################## Rayleigh Damping ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Rayleigh Damping'))
# Adding Rayleigh Damping to the Mass Matrix Only
OData.AddObject(OpenSeesAPI.Model.Node.Raleigh(2*Zeta*2*np.pi/T,0,0,0))

########################## Loads ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Loads'))

########################## Time Series ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Time Series'))

TimeSeries = OpenSeesAPI.Model.TimeSeries.Path(1,Dt, GMData)
OData.AddObject(TimeSeries)

########################## Recorders ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Recorder Setup'))

OutputFolder = 'Results'

Displacement_File_Name = '%s-NodeD-%s.dat'%(ModelName,timestamp)
OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+'/'+Displacement_File_Name, [MassNode], [1], 'disp'))

Velocity_File_Name = '%s-NodeV-%s.dat'%(ModelName,timestamp)
OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+'/'+Velocity_File_Name, [MassNode], [1], 'vel'))

Acceleration_File_Name = '%s-NodeA-%s.dat'%(ModelName,timestamp)
OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+'/'+Acceleration_File_Name, [MassNode], [1], 'accel','-timeSeries %d'%TimeSeries.id))

Reaction_File_Name = '%s-NodeReact-%s.dat'%(ModelName,timestamp)
OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+'/'+Reaction_File_Name, [SupportNode], [1], 'reaction'))

########################## Display Results ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Display Results'))

########################## Gravity Analysis ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Gravity Analysis'))

########################## Pushover Analysis ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Pushover Analysis'))

########################## Time History Analysis ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Time History Analysis'))

#Analysis Options
OData.AddObject(OpenSeesAPI.Analysis.Constraints.Transformation())
OData.AddObject(OpenSeesAPI.Analysis.Numberer.RCM())
OData.AddObject(OpenSeesAPI.Analysis.System.BandGeneral())
OData.AddObject(OpenSeesAPI.Analysis.Test.EnergyIncr(1e-6, 10))
OData.AddObject(OpenSeesAPI.Analysis.Algorithm.KrylovNewton())
OData.AddObject(OpenSeesAPI.Analysis.Integrator.Transient.Newmark(0.5,0.25))
OData.AddObject(OpenSeesAPI.Analysis.Analysis.Transient())

#Load Pattern
OData.AddObject(OpenSeesAPI.Model.Pattern.UniformExcitation(400,1,TimeSeries))

#Run Analysis
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0;'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set Nsteps %d;'%len(GMData)))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set step 0;'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('while {$ok == 0 & $step < [expr $Nsteps +1]} {'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze 1 %f]'%Dt))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Running Time History Step: $step out of %d"'%len(GMData)))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set step [expr $step+1]'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))

########################## Close File ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Close File'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('wipe;'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Models Run Complete";'))

##############################################################################
### Start Running OpenSees File
##############################################################################

########################## Plot Geometry ##########################


########################## Run OpenSees Script ##########################
OData.Executable.StartAnalysis(SuppressOutput=False)

########################## Plot Results ##########################
Displ = np.loadtxt(ResultDirectory+'/'+Displacement_File_Name)
Vel = np.loadtxt(ResultDirectory+'/'+Velocity_File_Name)
Acc = np.loadtxt(ResultDirectory+'/'+Acceleration_File_Name)
Reac = np.loadtxt(ResultDirectory+'/'+Reaction_File_Name)

MaxD = max(abs(Displ[:,1]))
MaxV = max(abs(Vel[:,1]))
MaxA = max(abs(Acc[:,1]))

try:
    os.remove(TCLFileDirectory+'/%s-%s.out'%(ModelName,timestamp))
except:
    pass

os.remove(TCLFileDirectory+'/%s-%s.tcl'%(ModelName,timestamp))
os.remove(ResultDirectory+'/'+Displacement_File_Name)
os.remove(ResultDirectory+'/'+Velocity_File_Name)
os.remove(ResultDirectory+'/'+Acceleration_File_Name)
os.remove(ResultDirectory+'/'+Reaction_File_Name)

DataPoints = len(GMData)

t = Acc[0:DataPoints,0]
ag = GMData[:]/g
a = Acc[0:DataPoints,1]
fs = -1*Reac[0:DataPoints,1]/(k*Dy)
u = Displ[0:DataPoints,1]/Dy

MaxU = max(abs(Displ[0:DataPoints,1]))
MaxV = max(abs(Vel[0:DataPoints,1]))
MaxA = max(abs(Acc[0:DataPoints,1]))
MaxF = max(abs(Reac[0:DataPoints,1]))

DArray = Displ[:,1]
for i in range(0,len(DArray)):
    if abs(DArray[i]) == max(abs(DArray)):
        TimeAtMax = float(i)/float(len(DArray))
        break

Stiffness = []
Collapse = 0

for i in range(1,len(Displ[0:DataPoints,1])):
    if (Displ[i,1]-Displ[i-1,1]) != 0.0:
        Stiffness.append(abs(Reac[i,1]-Reac[i-1,1])/abs(Displ[i,1]-Displ[i-1,1]))
    else:
        Stiffness.append(k)

import matplotlib.pylab as plt
plt.figure(figsize=(12,12))
plt.subplot(2,2,1)
plt.plot(t,ag,color='#000000')
plt.xlabel('Time, s')
plt.ylabel('$a_g$, g')

plt.subplot(2,2,2)
plt.plot(u,fs,color='#000000')
plt.xlabel('$u/\delta_y$')
plt.ylabel('$f_s/f_y$')

plt.subplot(2,2,3)
plt.plot(t,a,color='#000000')
plt.xlabel('Time, t')
plt.ylabel('$a$, g')

plt.subplot(2,2,4)
plt.plot(u,t,color='#000000')
plt.xlabel('$u/\delta_y$')
plt.ylabel('Time, t')

plt.show()
