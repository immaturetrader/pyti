import unittest
import numpy as np

from sample_data import SampleData
from technical_indicators import directional_indicators


class TestDirectionalIndicators(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.close_data = SampleData().get_sample_close_data()
        self.high_data = SampleData().get_sample_high_data()
        self.low_data = SampleData().get_sample_low_data()

        self.positive_directional_movement_expected = [0, 10.389999999999986,
        1.9500000000000455, 5.6299999999999955, 0, 1.92999999999995,
        2.6100000000000136, 2.6200000000000045, 0, 0, 6.409999999999968,
        1.9300000000000637, 0, 0, 2.4200000000000728, 0, 0, 0,
        2.2999999999999545, 0, 0, 11.530000000000086, 13.739999999999895, 0, 0,
        0, 5.439999999999941, 0, 0, 9.81000000000006, 0, 0, 0,
        18.379999999999995, 8.43999999999994, 25.600000000000023,
        6.1299999999999955, 0, 0, 0.34000000000003183, 6.659999999999968,
        17.519999999999982, 3.9500000000000455, 9.620000000000005, 0,
        4.9500000000000455, 6.67999999999995, 6.899999999999977, 0, 0,
        4.769999999999982, 0, 0, 0, 0, 7.8700000000000045, 0, 4.310000000000059,
        0, 2.509999999999991, 0, 1.6499999999999773, 0, 3.5699999999999363, 0,
        7.279999999999973, 0.20000000000004547, 0, 12.670000000000073,
        0.67999999999995, 0, 0, 0, 2.2100000000000364, 3.599999999999909, 0, 0,
        9.470000000000027, 0, 14.670000000000073, 5.009999999999991,
        0.36000000000001364, 0, 0, 0, 1.490000000000009, 4.1099999999999, 0, 0,
        2.1000000000000227, 2.7200000000000273, 0.5099999999999909,
        2.8799999999999955, 3.6299999999999955, 2.67999999999995, 0,
        4.1099999999999, 1.1200000000000045, 1.25, 0.6200000000000045, 0, 0,
        1.2099999999999227, 0, 1.740000000000009, 0.9099999999999682,
        1.2300000000000182, 0, 0, 0, 0, 0, 1.3100000000000591, 0,
        2.6299999999999955, 0, 0, 0, 0.16999999999995907, 0, 2.7000000000000455,
        0, 0, 0, 1.9099999999999682, 0, 5.7000000000000455]

        self.negative_directional_movement_expected = [0, 0, 0, 0,
        2.1700000000000728, 0, 0, 0, 2.240000000000009, 2.8600000000000136, 0,
        0, 2.439999999999941, 7.600000000000023, 0, 14.430000000000064,
        4.209999999999923, 14.6400000000001, 0, 13.569999999999936,
        0.6399999999999864, 0, 0, 3.240000000000009, 5.5, 1.3199999999999363, 0,
        0, 9.350000000000023, 0, 5.8599999999999, 5.440000000000055,
        21.75999999999999, 0, 0, 0, 0, 10.100000000000023, 21.129999999999995,
        0, 0, 0, 0, 0, 2.730000000000018, 0, 0, 0, 11.100000000000023,
        2.5299999999999727, 0, 5.399999999999977, 15.5, 1.7100000000000364,
        1.080000000000041, 0, 2.1200000000000045, 0, 13.170000000000073, 0,
        0.9800000000000182, 0, 2.3899999999999864, 0, 1.7900000000000773, 0, 0,
        7.57000000000005, 0, 0, 10.839999999999918, 5.490000000000009,
        3.9700000000000273, 0, 0, 10.419999999999959, 1.9800000000000182, 0,
        10.120000000000005, 0, 0, 0, 10.709999999999923, 6.050000000000068,
        1.759999999999991, 0, 0, 3.1299999999999955, 1.4800000000000182, 0, 0,
        0, 0, 0, 0, 3.689999999999941, 0, 0, 0, 0, 1.7000000000000455,
        2.1100000000000136, 0, 9.81000000000006, 0, 0, 0, 9.040000000000077,
        25.879999999999995, 3.6499999999999773, 4.82000000000005, 0, 0,
        4.710000000000036, 0, 3.3799999999999955, 0.6399999999999864,
        17.360000000000014, 0, 6.349999999999909, 0, 5.340000000000032,
        9.17999999999995, 10.670000000000073, 0, 3.67999999999995, 0]

        self.pdi_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, 14.252100038182405,
        6.7457510560959983, 2.7588984544127357, 2.0695918883909363,
        6.9121971437892515, 2.1375933334635855, 0.71346697155916028,
        0.30631578171994084, 2.3699585826215515, 0.44022336188142758,
        0.20617931523498917, 8.6083839668776498, 11.311550111262845,
        2.4777221688988962, 2.2805727912596203, 2.2885945102679672,
        6.8657637055113137, 2.077300913583402, 0.64751735204052696,
        11.103354828408515, 2.1241537989741528, 2.2509974081418025,
        1.2236000683270618, 17.732223591512994, 9.8226371119898612,
        19.673091380203214, 7.2015878138537994, 3.6336998906038205,
        3.5867205034126566, 2.7042951613768755, 5.6065142029799695,
        10.378567655355003, 3.881153526824773, 7.1624602047058143,
        2.5090582921893114, 5.1964113805392307, 6.3846133721604783,
        5.9632589257762776, 2.2074285284817887, 1.5504880538227932,
        5.2522290450999085, 1.8039791216077987, 1.1053824733028641,
        0.4578992028657925, 0.46141926428026186, 6.7472493933611188,
        0.8019926616682076, 4.8530845732391468, 1.4518765202857231,
        4.1157915838547261, 1.9322555998260202, 2.7859354707281554,
        1.19632708857326, 5.42322806392104, 1.4308378397009911,
        12.486285157207933, 2.784732561213489, 2.2203888725997438,
        22.832572928990853, 4.9919508956916605, 3.9659720954267303,
        2.445381894791419, 2.1892900013851402, 4.7961892963836856,
        4.6642824103498457, 0.84947749782169635, 0.88026274993719478,
        13.039270318609212, 2.4439619891759246, 21.358610235466418,
        9.8700289060331539, 4.6432994109568027, 4.1167771778436926,
        2.7152985664347211, 2.686839758603095, 2.3376732442172918,
        4.6914709623132209, 0.82106069113532831, 0.91599883522823544,
        4.1307199129332721, 6.0193428432941376, 2.8750407112589973,
        6.5760569157223401, 8.4531905370174627, 7.3596333851054467,
        2.7817875305224655, 9.9332870199132692, 5.3867770630335015,
        5.4707640147837191, 3.7047839789656547, 1.9037070209709803,
        2.1240370391936843, 4.2750776297389788, 0.92598344922662734,
        4.4952570266562182, 2.798310532272466, 3.6722802768412151,
        1.1872605274176744, 0.63608118495178056, 0.49182103056283871,
        0.2208214587192735, 0.10980039047923498, 0.91264677061251576,
        0.12321957097911006, 2.4326224013607223, 0.47704516032566846,
        0.53822145710316516, 0.50492500663172246, 0.50006115219458824,
        0.32209651657435889, 2.4879656990859749, 0.30712800691897535,
        0.3159179190941675, 0.29816905982252812, 1.8662130851303866,
        0.45249518197902194, 4.8186057488022573]

        self.pdi_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        4.228942066862766, 1.1418072449883061, 1.0092631923107418,
        0.8187444876127874, 1.8075447881537603, 0.26148736255889143,
        0.23695350716891075, 5.64454023283787, 7.0660458153460413,
        1.2852252131286719, 1.3087546312764229, 1.3300611059342595,
        3.9371000259824869, 1.5222012550235018, 1.6254989546065757,
        6.6815268735871074, 0.92570389251380325, 0.98894836416634568,
        0.92398900433797793, 11.555283547273556, 6.2240812618844377,
        14.254266464435739, 5.280385618111417, 2.2530223315855533,
        2.0827965462550297, 2.0687097855090593, 4.22857811426059,
        7.7378780182188205, 3.4091188558167205, 4.6809218305076667,
        1.3495822291667634, 3.1042256493460139, 3.8037974584281264,
        4.0038447672058251, 1.7197634831417123, 1.1626762055137527,
        2.961857207005234, 0.95922288010655798, 0.97503940383789167,
        0.77242027443548211, 0.49278840852901251, 3.7061892074151137,
        0.57257349838050642, 2.630977268840732, 0.59004635478061362,
        1.950916005027552, 0.81107338698902554, 1.8400794961057558,
        1.0083651201471779, 2.8938401353997873, 0.81513660566110779,
        5.9069133644804435, 1.3077046284678064, 1.0285910136171437,
        11.635013742844301, 2.5422964575551235, 2.0757776145138851,
        1.7707010685528644, 1.7111625297671176, 2.8701034899562798,
        4.0541984947015877, 1.4119921516482767, 0.45185875085320137,
        7.2455215799000285, 1.1346164397571432, 12.528084512109267,
        6.0985981253596, 2.7217194970066676, 2.1876866659699852,
        2.1715283550177178, 2.157584377190426, 2.5557943444630764,
        4.6156819694520559, 0.80393382567765637, 0.43820360041357614,
        2.1446756314344908, 3.0444588720825316, 1.4449417891751071,
        3.9331781969937158, 4.9251967638013179, 3.8941758210281523,
        1.4434556210677243, 5.6592812583655903, 2.8911401662587379,
        2.9155425727271465, 2.414623647712808, 1.5548415998682015,
        1.1906476104773367, 2.4664051825366253, 1.0518302862906928,
        2.7514989093556403, 1.7616034589397647, 2.1177742073057568,
        0.60014784703419644, 0.45536330201775432, 0.36641690204648331,
        0.24080214358925445, 0.2147378781576568, 0.77994427820323742,
        0.11780257799808681, 1.2581938941621027, 0.19127254704683985,
        0.20928672715997237, 0.21143121384211835, 0.3067110318285341,
        0.21764550667286678, 1.5848133861900982, 0.28353605450045721,
        0.14186325231228017, 0.13103745441733075, 1.0215451141077487,
        0.21848353167642781, 2.8808669546554788]

        self.pdi_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 1.6426714562555931, 0.48203147106950173,
        0.21921575335316165, 4.3786064104820239, 5.2660030172197123,
        0.82774995350381253, 0.76510351179071523, 0.77779272915926911,
        2.6938470527523526, 0.97052172463274433, 0.91942335378840445,
        4.5514272884697364, 1.3040353746570359, 0.98097717444356491,
        0.50401644718867811, 7.6996621955318023, 4.3178190097794626,
        10.315408173805999, 3.6636330199254918, 1.706692518569638,
        1.6055405112539047, 1.3973155457606463, 2.9759420763958566,
        5.6992279937000099, 2.7086971178555364, 3.868590458225416,
        1.474647670917651, 2.208499663396494, 2.597105539861837,
        2.7189151348815965, 1.1308213066438797, 1.118428625886885,
        2.207365192806368, 0.79023855051159453, 0.72828267217314535,
        0.52784189346306765, 0.53878334650298276, 2.6783141251862101,
        0.46844246349933438, 1.6170066440780373, 0.43439931882291177,
        1.2444328267655063, 0.40188658054873228, 1.0081539071714467,
        0.50298854332605802, 1.9362266964017372, 0.68127200651636244,
        3.6001695111468361, 0.81789134329947177, 0.60658174955662081,
        6.9729473656463412, 1.4301027467814496, 1.1386071709022307,
        1.0898883765380487, 1.0876689325010889, 2.1177664825250551,
        2.9602759488546533, 0.83836759502423519, 0.80474441027533095,
        5.4737501037024732, 0.63686257514339717, 7.9099896057872687,
        3.7570655276101417, 1.6465242863308014, 1.4925841299631439,
        1.4108331057239718, 1.2669219579989217, 2.0556104246503439,
        3.5132239468458928, 1.121410124483444, 1.1346863781722856,
        1.628362944364357, 1.8520278277251379, 0.80122652346787682,
        2.3216617147969885, 3.010323713525378, 2.6482981961080463,
        1.0056032126058734, 3.5130061779026405, 1.7667688013521652,
        1.9358821348096238, 1.5054475397590614, 0.98417018509428511,
        0.9966095221640362, 1.8080444605797965, 0.7221389352763653,
        1.9660059379145816, 1.433407149254591, 1.5019551775295774,
        0.46597042560827961, 0.31405027742148667, 0.23762518334554333,
        0.20562486807844013, 0.18330165995577713, 0.66224619328350598,
        0.16216504351552841, 1.0390956167287133, 0.14418102469177094,
        0.1079165019948758, 0.10879348447762004, 0.16888511612769888,
        0.11649795776978532, 1.0498323659778561, 0.19390157590193238,
        0.15288187924074195, 0.1450670853885753, 0.66247831691808323,
        0.11746576454285343, 1.8426669384749923]

        self.ndi_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, 1.2170675830469666,
        1.2525788387857393, 6.3202940139957535, 17.335933971581603,
        3.1637575629747099, 25.501329539348053, 9.6755962267163778,
        18.8255097453067, 4.5528151718783203, 13.482213528264261,
        4.6702304196141995, 2.9386156779316921, 2.5797895675025324,
        3.664728132149417, 5.6450268339251766, 1.8297888201603816,
        0.98843102088559986, 1.0895540766761778, 10.323378665896252,
        2.0905573644694386, 8.17931536940055, 8.8295188826378475,
        24.831472864697911, 4.6847464118962998, 3.3341175683523856,
        2.7472856341535725, 1.9075939128685884, 6.4903900010136386,
        11.232836751985753, 1.9659932466548591, 2.0199284575697947,
        2.0671879528345296, 2.1298264741299766, 1.4097544956446313,
        1.4746069553413033, 0.18108505321511528, 0.1919264722735893,
        0.19906697074308363, 7.3515603746063336, 2.8931287074461243,
        1.2418965006715694, 5.6931025031230424, 13.841434517887583,
        4.6607803139497213, 3.2885554105811305, 2.3063941205229894,
        4.185647596614996, 2.292221052943864, 13.458347015298804,
        2.0565138949912214, 3.0681956515685509, 2.227379366523226,
        4.766664295769802, 2.6829033970585607, 3.3407194477263542,
        0.9925015621910509, 0.8232094841493881, 13.313089987803174,
        1.8592782799916157, 1.8162427265674865, 18.365325798399827,
        11.446913861463427, 9.2579908418125054, 3.0936274376139932,
        2.9214727840204833, 15.460782879459204, 5.4718708221569967,
        2.5574242202102995, 15.256208794211837, 3.6066397416296856,
        3.4079459532652527, 1.7501689263154034, 13.663347690693426,
        9.5441931646538087, 4.1820312250672247, 2.4615481284343876,
        2.4439143289278444, 6.4784620890189579, 3.7745694860227319,
        1.1530537180273819, 0.92484903704792421, 1.010825021270908,
        1.0473164645021791, 0.32943759202617434, 0.0, 6.7770794765336309,
        0.84451935633104769, 0.88406010329983142, 0.92643961516988238,
        0.95974816641274563, 4.7270922224956911, 5.6846411012336961,
        1.2614657504109783, 25.329856352027324, 3.8032923781251209,
        3.6604868852816481, 3.1387911157283379, 19.578835785930682,
        37.880601825275349, 8.2202561422680596, 8.0583322416930638,
        3.8733649942227206, 3.6864404558625359, 6.8638004072421772,
        1.4015546096316862, 4.5096507719516818, 1.8220298971679887,
        19.361695393891601, 3.2421956910432224, 8.4492818365667173,
        3.0923930450763257, 7.291668339876364, 11.483781472967918,
        11.258115678957676, 3.2055528104244098, 5.4344573200542925,
        2.8594686118791417]

        self.ndi_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        1.8032641838179198, 17.137871860484896, 6.5687865392267897,
        13.481238894548255, 2.8290058403084042, 10.025080418491839,
        3.0593824643821095, 2.2032178068997146, 2.1904840867212205,
        3.0731127356358292, 4.1714816121926948, 1.7530838049458093,
        1.1877788848297306, 0.53036644183495307, 5.5521938754197109,
        1.092744148578157, 4.7861709545211859, 5.0068116479035538,
        14.703759448422845, 2.4299384632182495, 2.319624143786033,
        2.0403296441661478, 1.403227733847024, 5.2141923678309947,
        8.9508162518369527, 1.768120280971617, 1.0444242524020277,
        1.0746247171816579, 1.1054100757491698, 1.1060032439498513,
        2.0876184022710924, 0.83883602115222733, 0.093726558139360289,
        0.091571489182469212, 3.9966899327080805, 1.4303970193690241,
        0.633151436097664, 2.928364539930453, 7.3753271790855157,
        2.1835831066797624, 1.9928703469414448, 1.635039294354778,
        2.1617755749208007, 1.2049447721398543, 7.7215378827459755,
        1.7405485108049452, 1.547057610853144, 1.0158998763617013,
        2.5000190660197226, 1.208573342134311, 2.3489822901865067,
        1.3273718520403084, 0.39602826511492395, 6.6365525253168149,
        0.96814256411317345, 0.9756620177021007, 10.149920565207303,
        6.4507146327727574, 5.2712631060660966, 2.224056600951557,
        2.1697947556549599, 9.2847011510710242, 3.5370902262473769,
        2.3259563133051575, 9.2451721382380576, 2.0226574064938769,
        1.700479355599418, 1.6838109238574979, 9.7226399946445543,
        6.1940646625528624, 3.2704788700482275, 2.0822759791033234,
        1.3522033140191916, 3.6838155390180858, 2.6954983215277566,
        1.8441021321590894, 1.0715134577720642, 0.59028817571524173,
        0.45170169905330398, 0.46206384152068314, 0.46004193053368131,
        3.8678191499192178, 0.37153192248972811, 0.3825137043203517,
        0.3896743488230438, 0.4057623370009833, 2.4270900141546226,
        3.2616718210476772, 0.9548430947804637, 13.076545065149107,
        1.7152341180722426, 1.7076896164242326, 1.7011424123728334,
        12.416979788848717, 25.358738811777798, 5.8850894292765545,
        6.0367217793465686, 2.4014114776445261, 2.1936519642435486,
        4.2280392083069298, 2.1625006848615675, 3.5605266734534529,
        1.2244563558568731, 10.176066264182841, 1.412727257070588,
        4.7922862553745516, 1.7031681199055462, 4.2217413829191566,
        6.2371107451402157, 6.7159793586535166, 2.245824615023039,
        3.1477038637160359, 1.6253951964683033]

        self.ndi_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 1.9644562083471211, 7.6648089139322968,
        2.1308796796702882, 1.7449382652724728, 1.5882481133199038,
        2.3938230565983907, 3.2563691036828377, 1.6302520557012368,
        1.1215901977236127, 0.71355838403019289, 4.1168636860286458,
        0.61032716114110241, 2.9086911670704696, 3.0845267109032379,
        9.7249652163094513, 1.5936549440008361, 1.3899250203895768,
        1.2424269085051285, 1.1385169733727616, 4.1127450443829447,
        7.0240701116574353, 1.4334865479912815, 1.2460357973759268,
        1.0873684595221988, 0.64619455339222653, 0.65253472886290809,
        1.357920570832605, 0.71998318679989048, 0.71160337899682302,
        0.48672021546247468, 2.7394422434410162, 0.88375557376799363,
        0.3362742765091003, 1.7523705964151821, 4.63433391776333,
        1.3132615692727176, 1.1404632896792888, 0.87938390620300066,
        1.5102248328533128, 0.98358783031777008, 4.8141012416180127,
        1.0244800400945155, 1.3911154581523517, 1.0048586531007191,
        1.4777383390726437, 0.64154503978578292, 1.3802991348053575,
        0.73469995844966374, 0.6895315561330333, 4.3872933759662311,
        0.52630611605493438, 0.54173209356506957, 6.2518251105742983,
        3.9789859254921982, 3.2884649865427025, 1.3197230946989309,
        1.2380385758490464, 6.6717681986716615, 2.6154193333948377,
        1.3372331472682404, 6.1956211727505179, 1.7554068666484004,
        1.3257792655543528, 1.1092682691989502, 6.433071407256163,
        4.5381111731888657, 2.6014855943909332, 1.3235633664138771,
        1.2456410742087363, 2.9105831420387793, 1.7513487923107345,
        1.0346314871297695, 1.0447580968444512, 1.1166320237685572,
        0.6294485592180491, 0.33191372124088458, 0.24467331468006737,
        2.6610970682484796, 0.45349086956180695, 0.28371959388064111,
        0.2047472792898942, 0.21034968358884962, 1.4222951530751231,
        1.8931570283247257, 0.48318552969016143, 8.2996696009790742,
        1.158192720997218, 0.92652946823261884, 0.94067885582248156,
        8.2418147086278335, 18.485271884825288, 4.3297995370085474,
        4.3979303535162515, 1.9158444616203401, 1.7842748148338992,
        3.138107104125142, 1.4157890358865082, 2.4830246874276467,
        1.6223386599951375, 6.9950590205750522, 0.97295844638569018,
        3.0560321260430401, 0.92519864037818711, 2.7651142987405133,
        4.1405972239456048, 4.5228107381511409, 1.3482829364231652,
        2.3126720886217083, 1.3126006271452442]

        self.adx_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, 93.894071353385868, 44.971605082564075, 38.951227517463273,
        55.383750741539458, 34.147821756615656, 24.33691778769597,
        167.5681613968236, 239.01721092849581, 87.723934507855546,
        82.177670584916328, 89.823893894777456, 185.27953482862046,
        86.509569442215181, 37.438116716647471, 235.94323387650803,
        75.149068622672885, 76.30983779758877, 41.608074258439906,
        365.70363177662693, 254.60831347313672, 440.88436534360056,
        244.68414453962703, 181.58612809030075, 184.77669434515701,
        140.40898800572964, 181.59492215082551, 241.15925575563836,
        121.71027983424459, 188.83489546730274, 106.25286630034414,
        163.3155064688878, 185.54042419145037, 168.55492550858858,
        88.843832873391463, 65.744346014265304, 141.86817321974721,
        65.395591621945115, 36.677972392845142, 28.551821493425315,
        25.565688867553554, 139.79543744263759, 20.578133926510809,
        103.56933903012539, 38.041746858837811, 99.639268783593721,
        60.664269493490821, 68.105314306851028, 36.526542968579264,
        116.07783436661052, 43.805368528417347, 258.48140185038972,
        97.078829102091731, 74.926958670954633, 483.25267222088792,
        181.86802366893843, 161.09321006011285, 110.74409537862491,
        104.00737058754075, 161.43858183106266, 116.5830084214669,
        36.194364971725975, 27.634531956031537, 267.95950569590661,
        80.204927177190314, 446.31886988720674, 265.32030560240793,
        187.81029514101979, 178.49673312149335, 129.65057605545806,
        133.15226661669919, 84.048884134506395, 113.93271950016421,
        32.596730814168602, 25.850706336990065, 93.777617009796558,
        135.48721879022347, 82.795462402373488, 151.36213016130739,
        203.63913028384974, 202.8169330450726, 110.44456675815954,
        249.33363078038732, 178.60477168371708, 177.36479233393052,
        135.53507272506317, 82.785019697774302, 84.639104569581917,
        115.38181826788491, 36.520377735313488, 100.17325981241495,
        67.149604542512947, 88.158293671597576, 36.042353726414156,
        29.194113656548286, 31.88877642332718, 29.298906785959506,
        27.965530082002555, 8.2630153803543305, 22.153580272673846,
        46.266560333396981, 18.88018723494406, 14.453539180825739,
        17.475815820738383, 16.344183416633303, 20.420787996988107,
        41.656071446870627, 20.821364636526283, 21.882752396706362,
        22.672474309949216, 33.983825345738303, 20.863494343100331,
        92.938264309078448]

        self.adx_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        83.954303200124073, 106.23843336745693, 28.636160450853552,
        28.783215452797062, 32.328370936437025, 72.555623955365306,
        42.789516947336473, 37.861297782137754, 110.58325683333288,
        20.701212843699452, 20.944974167851292, 18.506887891974564,
        175.08460856677263, 110.29510728102463, 230.09019308980939,
        122.62493113592416, 71.86169228633085, 69.940418932987626,
        76.13225468221934, 111.90246093468299, 151.57201752327487,
        92.113963348066363, 95.504526004007531, 42.742314693483642,
        71.435722803900006, 85.968148338401079, 91.735003886852269,
        50.608940055034942, 35.912528624751005, 62.578560280377715,
        24.474564839387174, 22.158356966691713, 17.525265048589056,
        16.220456582285642, 54.064475640840335, 13.191617270709443,
        41.759140705851266, 13.690276054440981, 29.686904043893346,
        13.218470997557114, 31.818632407085811, 16.943256263037167,
        44.641600318108473, 12.861936281679748, 88.15279211144329,
        31.057286620546765, 17.851265201439183, 175.88422592638301,
        60.78597053673375, 49.342089100760354, 43.892995060067413,
        44.727768139449523, 58.695891806986047, 78.192870636494533,
        39.194236953196722, 22.6224152449598, 111.19515012132275,
        25.343398423085862, 192.74782117315459, 118.12386734575358,
        73.732271725501519, 58.439099385846575, 60.398702907263726,
        63.479792592644088, 63.683616097514786, 97.879107218578838,
        26.311864000654602, 23.911858553930248, 38.768298964516305,
        54.472000104480919, 33.729112255439922, 70.280317253200025,
        86.632053335299219, 72.674627881728142, 35.21316256686233,
        103.31993612516206, 69.520554415244376, 69.830932366132188,
        64.770384708917248, 44.258253126353878, 32.177536791053186,
        51.603930724994861, 25.035791628363164, 48.634764463249532,
        32.850713918278785, 36.349048978964909, 17.245952206699688,
        18.839642942657552, 19.599142581594979, 19.41754569589655,
        19.985554314377296, 8.544655599308161, 18.138956278188918,
        13.844974735468274, 16.043988015892726, 14.792405516739565,
        16.600023447087398, 13.152180557283625, 16.00104856292716,
        21.500638280898158, 16.058997462775665, 18.625547811478448,
        18.925525531507404, 12.055590154199242, 16.765231487759532,
        42.051282797283427]

        self.adx_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 18.562354032040755, 13.217573035460504,
        60.106560001683498, 21.843979436050155, 14.446617163233622,
        12.562200272498128, 90.076020445131391, 59.163967062807068,
        129.59645935275077, 62.706820487655726, 38.848846720766453,
        37.385730354199595, 35.191056474293774, 54.950408134834717,
        88.317407575535725, 59.950638683168265, 68.608870772232862,
        38.547643055135282, 40.800824183857344, 44.054677246285195,
        47.315548318165519, 25.543028121477413, 27.890819575635785,
        41.327039155303211, 16.691604340587954, 14.898178917592805,
        12.208752711114009, 10.988446897697283, 34.317769143198163,
        11.076014356252642, 19.320341503488109, 11.814631477172213,
        15.019610044522505, 9.2992166886414296, 11.016365765416868,
        8.4537865147990505, 24.248296988848118, 7.3763630076572824,
        42.465444563627024, 11.822373105406081, 10.067078413555461,
        82.153148363381433, 25.005380809554467, 16.305256058534258,
        16.243915092187624, 16.640848309188645, 30.659006969964981,
        42.36270022259481, 13.16622997850544, 12.778220188436162,
        69.656903741007554, 13.61245940013994, 94.112618113136591,
        54.674416378240764, 32.997308743216216, 27.676585867183366,
        26.370143063703495, 23.970646696050892, 36.118192468502635,
        54.883926267667725, 21.97449546703908, 23.489754505363614,
        24.769979745764477, 25.480857345954682, 11.834666505616998,
        32.013098980827301, 42.076274140144641, 40.375723236783145,
        16.291388746965431, 47.612069407765887, 31.015307930410586,
        34.31477281057834, 29.869659141774868, 18.984131807316761,
        18.577826001431312, 30.674484233507066, 14.239183305491053,
        27.342311188891582, 22.482261796974761, 21.189089798833034,
        13.792702416385289, 14.626078512978879, 14.431870121923632,
        15.146380959275124, 15.292160527668589, 7.2919605007820003,
        15.040085408811784, 10.757203143144142, 13.926994895345462,
        13.956316994527086, 14.773939569575539, 12.859682320987856,
        14.618191276094111, 11.812734847535289, 13.41465492071193,
        14.794064204899499, 14.949155385156237, 6.3822708236697485,
        14.673622142143818, 21.135546113068049]

    def test_positive_directional_movement(self):
        pdm = directional_indicators.positive_directional_movement(self.high_data, self.low_data)
        np.testing.assert_array_equal(pdm, self.positive_directional_movement_expected)

    def test_negative_directional_movement(self):
        ndm = directional_indicators.negative_directional_movement(self.high_data, self.low_data)
        np.testing.assert_array_equal(ndm, self.negative_directional_movement_expected)

    def test_pdi_period_6(self):
        period = 6
        pdi = directional_indicators.positive_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(pdi, self.pdi_period_6_expected)

    def test_pdi_period_8(self):
        period = 8
        pdi = directional_indicators.positive_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(pdi, self.pdi_period_8_expected)

    def test_pdi_period_10(self):
        period = 10
        pdi = directional_indicators.positive_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(pdi, self.pdi_period_10_expected)

    def test_pdi_invalid_period(self):
        period = 128
        with self.assertRaises(Exception):
            directional_indicators.positive_directional_index(self.data, period)

    def test_ndi_period_6(self):
        period = 6
        ndi = directional_indicators.negative_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(ndi, self.ndi_period_6_expected)

    def test_ndi_period_8(self):
        period = 8
        ndi = directional_indicators.negative_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(ndi, self.ndi_period_8_expected)

    def test_ndi_period_10(self):
        period = 10
        ndi = directional_indicators.negative_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(ndi, self.ndi_period_10_expected)

    def test_ndi_invalid_period(self):
        period = 128
        with self.assertRaises(Exception):
            directional_indicators.negative_directional_index(self.data, period)

    def test_adx_period_6(self):
        period = 6
        adx = directional_indicators.average_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(adx, self.adx_period_6_expected)

    def test_adx_period_8(self):
        period = 8
        adx = directional_indicators.average_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(adx, self.adx_period_8_expected)

    def test_adx_period_10(self):
        period = 10
        adx = directional_indicators.average_directional_index(self.close_data, self.high_data, self.low_data, period)
        np.testing.assert_array_equal(adx, self.adx_period_10_expected)

    def test_adx_invalid_period(self):
        period = 128
        with self.assertRaises(Exception):
            directional_indicators.average_directional_index(self.data, period)
