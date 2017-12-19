# coding: utf-8

# author: Fei Gao
#
# Course Schedule Ii
#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
# For example:
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# click to show more hints.
# Hints:
# This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        node_in = [set() for _ in range(numCourses)]
        node_out = [set() for _ in range(numCourses)]

        for n2, n1 in prerequisites:
            node_in[n2].add(n1)
            node_out[n1].add(n2)
        found = list()
        frontier = list()
        for n in range(numCourses):
            if not node_in[n]:
                frontier.append(n)

        while frontier:
            # find a node with zero in-degree
            n = frontier.pop()
            found.append(n)
            for m in node_out[n]:
                node_in[m].remove(n)
                if not node_in[m]:
                    frontier.append(m)
            node_out[n] = set()

        return found if len(found) == numCourses else []


def main():
    solver = Solution()
    tests = [
        (2, [[1, 0]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
        (2000,
         [[995, 1232], [1232, 719], [719, 3], [3, 656], [656, 1379], [1379, 616], [616, 635], [635, 1806], [1806, 341],
          [341, 913], [913, 1273], [1273, 822], [822, 400], [400, 463], [463, 468], [468, 909], [909, 401], [401, 342],
          [342, 662], [662, 1535], [1535, 766], [766, 1503], [1503, 1252], [1252, 1431], [1431, 892], [892, 335],
          [335, 653], [653, 731], [731, 800], [800, 506], [506, 1208], [1208, 1977], [1977, 281], [281, 276],
          [276, 547], [547, 673], [673, 1124], [1124, 989], [989, 1380], [1380, 1882], [1882, 1619], [1619, 1442],
          [1442, 504], [504, 1628], [1628, 99], [99, 1012], [1012, 686], [686, 406], [406, 1388], [1388, 877],
          [877, 464], [464, 1553], [1553, 690], [690, 1921], [1921, 187], [187, 636], [636, 1905], [1905, 955],
          [955, 1932], [1932, 1490], [1490, 698], [698, 1286], [1286, 994], [994, 790], [790, 65], [65, 1551],
          [1551, 764], [764, 1139], [1139, 583], [583, 1392], [1392, 1566], [1566, 1329], [1329, 1798], [1798, 929],
          [929, 1016], [1016, 830], [830, 856], [856, 78], [78, 707], [707, 277], [277, 1944], [1944, 1367],
          [1367, 1226], [1226, 1320], [1320, 1218], [1218, 1138], [1138, 559], [559, 845], [845, 1091], [1091, 1579],
          [1579, 465], [465, 1051], [1051, 1509], [1509, 1384], [1384, 1445], [1445, 985], [985, 304], [304, 432],
          [432, 88], [88, 195], [195, 230], [230, 1261], [1261, 165], [165, 1875], [1875, 499], [499, 1095],
          [1095, 1552], [1552, 502], [502, 1775], [1775, 208], [208, 801], [801, 1892], [1892, 452], [452, 266],
          [266, 121], [121, 1492], [1492, 900], [900, 1948], [1948, 120], [120, 1656], [1656, 1160], [1160, 1583],
          [1583, 1862], [1862, 1744], [1744, 1064], [1064, 1735], [1735, 310], [310, 611], [611, 941], [941, 95],
          [95, 781], [781, 774], [774, 1428], [1428, 1618], [1618, 1254], [1254, 58], [58, 1754], [1754, 138],
          [138, 727], [727, 188], [188, 1528], [1528, 13], [13, 1183], [1183, 1251], [1251, 1240], [1240, 1790],
          [1790, 1586], [1586, 705], [705, 131], [131, 449], [449, 1491], [1491, 1111], [1111, 511], [511, 328],
          [328, 49], [49, 1640], [1640, 631], [631, 1360], [1360, 1991], [1991, 1912], [1912, 715], [715, 15],
          [15, 1507], [1507, 1961], [1961, 1556], [1556, 1165], [1165, 167], [167, 1801], [1801, 1456], [1456, 1670],
          [1670, 814], [814, 1500], [1500, 224], [224, 546], [546, 932], [932, 1766], [1766, 410], [410, 740],
          [740, 1253], [1253, 733], [733, 1348], [1348, 371], [371, 933], [933, 1478], [1478, 355], [355, 595],
          [595, 624], [624, 1039], [1039, 213], [213, 1419], [1419, 1477], [1477, 577], [577, 1555], [1555, 60],
          [60, 471], [471, 153], [153, 1081], [1081, 223], [223, 1271], [1271, 1400], [1400, 130], [130, 1159],
          [1159, 1061], [1061, 47], [47, 809], [809, 523], [523, 848], [848, 1333], [1333, 202], [202, 1592],
          [1592, 211], [211, 105], [105, 792], [792, 1243], [1243, 629], [629, 1563], [1563, 258], [258, 1284],
          [1284, 89], [89, 534], [534, 1169], [1169, 1085], [1085, 50], [50, 69], [69, 1632], [1632, 1884],
          [1884, 1927], [1927, 1588], [1588, 1239], [1239, 1953], [1953, 1763], [1763, 1651], [1651, 1518], [1518, 916],
          [916, 460], [460, 1854], [1854, 728], [728, 1031], [1031, 898], [898, 112], [112, 428], [428, 274],
          [274, 1151], [1151, 939], [939, 314], [314, 150], [150, 1483], [1483, 1714], [1714, 628], [628, 1734],
          [1734, 1700], [1700, 1915], [1915, 1647], [1647, 1573], [1573, 1038], [1038, 962], [962, 12], [12, 1955],
          [1955, 38], [38, 946], [946, 767], [767, 1345], [1345, 263], [263, 1900], [1900, 204], [204, 1835],
          [1835, 1976], [1976, 1840], [1840, 1075], [1075, 1994], [1994, 1447], [1447, 1625], [1625, 430], [430, 1841],
          [1841, 1325], [1325, 1308], [1308, 1010], [1010, 899], [899, 1339], [1339, 588], [588, 1723], [1723, 1545],
          [1545, 1990], [1990, 1598], [1598, 1495], [1495, 1207], [1207, 1767], [1767, 693], [693, 239], [239, 1179],
          [1179, 113], [113, 828], [828, 769], [769, 493], [493, 988], [988, 1247], [1247, 297], [297, 998],
          [998, 1880], [1880, 542], [542, 1873], [1873, 815], [815, 1230], [1230, 851], [851, 1974], [1974, 603],
          [603, 914], [914, 1246], [1246, 1357], [1357, 1919], [1919, 953], [953, 710], [710, 1613], [1613, 694],
          [694, 897], [897, 411], [411, 1381], [1381, 1960], [1960, 435], [435, 1541], [1541, 250], [250, 1721],
          [1721, 488], [488, 486], [486, 97], [97, 262], [262, 1080], [1080, 343], [343, 413], [413, 1936],
          [1936, 1349], [1349, 872], [872, 1978], [1978, 1090], [1090, 1843], [1843, 783], [783, 1606], [1606, 843],
          [843, 646], [646, 1161], [1161, 626], [626, 356], [356, 1587], [1587, 1211], [1211, 1105], [1105, 1660],
          [1660, 735], [735, 160], [160, 1561], [1561, 1356], [1356, 173], [173, 1181], [1181, 94], [94, 171],
          [171, 1283], [1283, 1550], [1550, 1867], [1867, 403], [403, 423], [423, 516], [516, 512], [512, 439],
          [439, 1557], [1557, 322], [322, 973], [973, 610], [610, 462], [462, 554], [554, 870], [870, 227], [227, 1593],
          [1593, 1163], [1163, 956], [956, 1052], [1052, 1154], [1154, 1049], [1049, 293], [293, 936], [936, 1989],
          [1989, 1517], [1517, 350], [350, 808], [808, 264], [264, 1321], [1321, 1577], [1577, 1601], [1601, 232],
          [232, 997], [997, 1705], [1705, 958], [958, 763], [763, 37], [37, 1053], [1053, 1404], [1404, 1474],
          [1474, 1390], [1390, 397], [397, 1255], [1255, 1493], [1493, 457], [457, 717], [717, 1166], [1166, 289],
          [289, 447], [447, 254], [254, 796], [796, 1393], [1393, 1504], [1504, 1526], [1526, 515], [515, 1397],
          [1397, 1907], [1907, 1920], [1920, 831], [831, 1178], [1178, 520], [520, 1747], [1747, 666], [666, 1695],
          [1695, 290], [290, 5], [5, 161], [161, 1311], [1311, 233], [233, 842], [842, 765], [765, 1918], [1918, 1486],
          [1486, 286], [286, 1693], [1693, 1558], [1558, 1709], [1709, 961], [961, 768], [768, 168], [168, 1678],
          [1678, 1690], [1690, 405], [405, 1569], [1569, 1193], [1193, 422], [422, 1519], [1519, 1857], [1857, 399],
          [399, 1117], [1117, 311], [311, 1473], [1473, 448], [448, 556], [556, 826], [826, 1814], [1814, 1899],
          [1899, 689], [689, 390], [390, 455], [455, 1171], [1171, 591], [591, 1094], [1094, 179], [179, 1501],
          [1501, 1707], [1707, 617], [617, 1148], [1148, 299], [299, 1443], [1443, 1409], [1409, 141], [141, 1940],
          [1940, 1425], [1425, 968], [968, 68], [68, 685], [685, 229], [229, 1338], [1338, 62], [62, 775], [775, 480],
          [480, 1594], [1594, 426], [426, 1688], [1688, 412], [412, 1234], [1234, 474], [474, 1644], [1644, 1987],
          [1987, 526], [526, 1508], [1508, 1722], [1722, 1176], [1176, 1684], [1684, 1889], [1889, 296], [296, 1290],
          [1290, 114], [114, 1724], [1724, 2], [2, 389], [389, 1847], [1847, 1909], [1909, 1741], [1741, 1757],
          [1757, 1546], [1546, 1002], [1002, 1043], [1043, 57], [57, 375], [375, 1315], [1315, 1760], [1760, 1062],
          [1062, 1654], [1654, 1266], [1266, 34], [34, 1399], [1399, 1925], [1925, 1162], [1162, 284], [284, 1576],
          [1576, 1758], [1758, 1260], [1260, 1293], [1293, 621], [621, 1834], [1834, 142], [142, 1947], [1947, 1469],
          [1469, 1147], [1147, 244], [244, 1487], [1487, 1391], [1391, 170], [170, 677], [677, 1856], [1856, 75],
          [75, 1793], [1793, 427], [427, 1567], [1567, 1626], [1626, 1623], [1623, 1547], [1547, 1089], [1089, 1926],
          [1926, 991], [991, 1997], [1997, 358], [358, 1902], [1902, 1291], [1291, 700], [700, 172], [172, 472],
          [472, 1058], [1058, 1946], [1946, 1370], [1370, 1534], [1534, 1662], [1662, 174], [174, 1985], [1985, 716],
          [716, 1730], [1730, 1699], [1699, 166], [166, 1003], [1003, 467], [467, 563], [563, 1209], [1209, 1227],
          [1227, 566], [566, 647], [647, 584], [584, 1901], [1901, 1784], [1784, 1717], [1717, 133], [133, 319],
          [319, 197], [197, 476], [476, 1324], [1324, 1923], [1923, 535], [535, 823], [823, 275], [275, 581],
          [581, 1471], [1471, 1334], [1334, 849], [849, 1177], [1177, 1000], [1000, 786], [786, 615], [615, 44],
          [44, 245], [245, 1728], [1728, 72], [72, 876], [876, 1452], [1452, 569], [569, 1231], [1231, 442],
          [442, 1225], [1225, 599], [599, 80], [80, 794], [794, 1667], [1667, 1543], [1543, 574], [574, 785],
          [785, 883], [883, 1802], [1802, 651], [651, 1414], [1414, 363], [363, 1076], [1076, 469], [469, 1355],
          [1355, 885], [885, 1030], [1030, 758], [758, 977], [977, 91], [91, 1217], [1217, 1296], [1296, 1056],
          [1056, 625], [625, 1104], [1104, 377], [377, 1605], [1605, 1011], [1011, 1332], [1332, 622], [622, 507],
          [507, 1189], [1189, 1352], [1352, 1446], [1446, 1191], [1191, 937], [937, 924], [924, 1642], [1642, 873],
          [873, 376], [376, 386], [386, 440], [440, 1523], [1523, 1389], [1389, 1274], [1274, 1344], [1344, 64],
          [64, 784], [784, 445], [445, 648], [648, 1560], [1560, 655], [655, 509], [509, 633], [633, 1077],
          [1077, 1285], [1285, 494], [494, 691], [691, 596], [596, 85], [85, 101], [101, 983], [983, 582], [582, 1749],
          [1749, 1106], [1106, 235], [235, 1303], [1303, 1559], [1559, 1433], [1433, 803], [803, 1807], [1807, 1808],
          [1808, 517], [517, 578], [578, 490], [490, 1458], [1458, 1881], [1881, 1725], [1725, 237], [237, 1199],
          [1199, 475], [475, 1484], [1484, 1776], [1776, 1434], [1434, 1554], [1554, 684], [684, 366], [366, 1753],
          [1753, 1648], [1648, 1572], [1572, 739], [739, 1562], [1562, 169], [169, 620], [620, 614], [614, 73],
          [73, 1496], [1496, 256], [256, 83], [83, 1451], [1451, 1164], [1164, 950], [950, 945], [945, 1294],
          [1294, 1532], [1532, 484], [484, 1499], [1499, 1800], [1800, 103], [103, 1781], [1781, 1891], [1891, 1745],
          [1745, 117], [117, 963], [963, 417], [417, 789], [789, 180], [180, 316], [316, 901], [901, 750], [750, 549],
          [549, 1565], [1565, 1895], [1895, 1527], [1527, 16], [16, 104], [104, 609], [609, 1184], [1184, 1059],
          [1059, 17], [17, 1578], [1578, 1017], [1017, 682], [682, 420], [420, 1299], [1299, 1574], [1574, 672],
          [672, 713], [713, 1677], [1677, 354], [354, 1652], [1652, 1071], [1071, 1288], [1288, 1472], [1472, 1022],
          [1022, 1405], [1405, 638], [638, 1634], [1634, 1133], [1133, 1228], [1228, 30], [30, 433], [433, 14],
          [14, 891], [891, 408], [408, 1962], [1962, 835], [835, 1536], [1536, 757], [757, 1906], [1906, 240],
          [240, 1568], [1568, 11], [11, 1236], [1236, 1142], [1142, 746], [746, 702], [702, 136], [136, 1657],
          [1657, 71], [71, 528], [528, 67], [67, 1516], [1516, 255], [255, 986], [986, 183], [183, 760], [760, 51],
          [51, 1796], [1796, 100], [100, 1746], [1746, 1200], [1200, 1931], [1931, 1939], [1939, 1406], [1406, 1025],
          [1025, 1197], [1197, 441], [441, 1988], [1988, 1863], [1863, 20], [20, 443], [443, 1256], [1256, 367],
          [367, 938], [938, 1610], [1610, 972], [972, 76], [76, 749], [749, 1371], [1371, 799], [799, 109], [109, 429],
          [429, 802], [802, 1789], [1789, 1448], [1448, 813], [813, 1109], [1109, 572], [572, 562], [562, 1799],
          [1799, 724], [724, 529], [529, 225], [225, 1823], [1823, 1353], [1353, 344], [344, 31], [31, 817],
          [817, 1241], [1241, 1585], [1585, 756], [756, 260], [260, 123], [123, 278], [278, 425], [425, 1515],
          [1515, 1006], [1006, 143], [143, 640], [640, 618], [618, 1350], [1350, 332], [332, 1307], [1307, 1959],
          [1959, 96], [96, 1865], [1865, 1933], [1933, 352], [352, 387], [387, 1485], [1485, 798], [798, 226],
          [226, 993], [993, 500], [500, 199], [199, 1343], [1343, 313], [313, 234], [234, 437], [437, 1727],
          [1727, 1911], [1911, 903], [903, 852], [852, 368], [368, 548], [548, 215], [215, 1680], [1680, 1674],
          [1674, 1475], [1475, 1917], [1917, 259], [259, 6], [6, 1063], [1063, 1836], [1836, 736], [736, 865],
          [865, 1581], [1581, 793], [793, 1175], [1175, 1687], [1687, 1531], [1531, 1180], [1180, 9], [9, 862],
          [862, 8], [8, 918], [918, 345], [345, 1774], [1774, 652], [652, 1359], [1359, 1427], [1427, 1982],
          [1982, 108], [108, 1459], [1459, 40], [40, 1128], [1128, 771], [771, 1103], [1103, 1896], [1896, 446],
          [446, 288], [288, 1013], [1013, 1852], [1852, 1732], [1732, 894], [894, 1394], [1394, 1533], [1533, 1810],
          [1810, 888], [888, 424], [424, 861], [861, 1819], [1819, 1421], [1421, 623], [623, 919], [919, 1272],
          [1272, 303], [303, 1645], [1645, 821], [821, 1194], [1194, 1943], [1943, 911], [911, 1134], [1134, 1916],
          [1916, 1950], [1950, 1599], [1599, 1971], [1971, 1964], [1964, 890], [890, 1502], [1502, 1467], [1467, 1309],
          [1309, 1494], [1494, 859], [859, 241], [241, 1815], [1815, 1795], [1795, 927], [927, 928], [928, 191],
          [191, 1617], [1617, 1876], [1876, 996], [996, 1646], [1646, 934], [934, 1949], [1949, 1858], [1858, 1952],
          [1952, 1172], [1172, 175], [175, 1087], [1087, 1079], [1079, 942], [942, 1866], [1866, 1729], [1729, 1220],
          [1220, 701], [701, 1001], [1001, 279], [279, 456], [456, 1958], [1958, 600], [600, 1633], [1633, 999],
          [999, 1890], [1890, 1233], [1233, 1464], [1464, 498], [498, 282], [282, 1326], [1326, 954], [954, 361],
          [361, 619], [619, 1886], [1886, 1440], [1440, 1750], [1750, 860], [860, 205], [205, 1805], [1805, 1014],
          [1014, 1453], [1453, 1050], [1050, 1060], [1060, 1019], [1019, 1268], [1268, 889], [889, 1304], [1304, 1341],
          [1341, 458], [458, 1223], [1223, 980], [980, 846], [846, 478], [478, 787], [787, 1712], [1712, 1580],
          [1580, 795], [795, 1461], [1461, 576], [576, 1347], [1347, 407], [407, 1317], [1317, 1196], [1196, 203],
          [203, 33], [33, 1292], [1292, 1136], [1136, 292], [292, 1848], [1848, 450], [450, 1620], [1620, 48],
          [48, 1313], [1313, 1954], [1954, 505], [505, 1570], [1570, 4], [4, 1007], [1007, 949], [949, 379],
          [379, 1412], [1412, 396], [396, 521], [521, 1679], [1679, 1715], [1715, 1941], [1941, 659], [659, 925],
          [925, 1736], [1736, 612], [612, 1265], [1265, 21], [21, 219], [219, 1513], [1513, 1942], [1942, 330],
          [330, 349], [349, 1204], [1204, 1694], [1694, 630], [630, 1904], [1904, 730], [730, 124], [124, 1983],
          [1983, 531], [531, 1733], [1733, 1759], [1759, 573], [573, 1861], [1861, 1468], [1468, 1424], [1424, 86],
          [86, 383], [383, 218], [218, 156], [156, 1034], [1034, 43], [43, 1282], [1282, 1980], [1980, 839], [839, 951],
          [951, 681], [681, 42], [42, 1600], [1600, 957], [957, 338], [338, 1655], [1655, 706], [706, 1008],
          [1008, 431], [431, 1337], [1337, 1410], [1410, 287], [287, 182], [182, 1740], [1740, 1100], [1100, 737],
          [737, 1054], [1054, 436], [436, 491], [491, 372], [372, 257], [257, 340], [340, 1342], [1342, 1782],
          [1782, 524], [524, 513], [513, 116], [116, 1676], [1676, 703], [703, 1066], [1066, 92], [92, 1463],
          [1463, 200], [200, 895], [895, 152], [152, 1212], [1212, 570], [570, 1088], [1088, 688], [688, 126],
          [126, 198], [198, 948], [948, 1093], [1093, 1664], [1664, 1924], [1924, 1996], [1996, 1701], [1701, 1638],
          [1638, 709], [709, 725], [725, 663], [663, 762], [762, 1182], [1182, 122], [122, 1903], [1903, 1205],
          [1205, 742], [742, 110], [110, 1883], [1883, 869], [869, 1804], [1804, 0], [0, 1851], [1851, 302],
          [302, 1026], [1026, 1967], [1967, 1718], [1718, 23], [23, 882], [882, 1120], [1120, 1118], [1118, 1672],
          [1672, 374], [374, 1185], [1185, 871], [871, 974], [974, 920], [920, 1029], [1029, 1441], [1441, 1963],
          [1963, 1731], [1731, 1738], [1738, 1786], [1786, 772], [772, 210], [210, 532], [532, 1415], [1415, 1488],
          [1488, 1928], [1928, 1057], [1057, 1168], [1168, 1072], [1072, 1306], [1306, 829], [829, 1686], [1686, 466],
          [466, 1850], [1850, 1454], [1454, 1616], [1616, 1778], [1778, 1755], [1755, 1403], [1403, 671], [671, 551],
          [551, 320], [320, 887], [887, 312], [312, 1158], [1158, 186], [186, 723], [723, 1083], [1083, 393],
          [393, 1938], [1938, 308], [308, 818], [818, 1377], [1377, 146], [146, 1123], [1123, 741], [741, 1221],
          [1221, 1708], [1708, 1822], [1822, 1809], [1809, 309], [309, 827], [827, 1506], [1506, 1235], [1235, 1287],
          [1287, 1429], [1429, 711], [711, 269], [269, 479], [479, 969], [969, 1937], [1937, 947], [947, 1877],
          [1877, 1537], [1537, 129], [129, 1042], [1042, 1663], [1663, 497], [497, 1752], [1752, 247], [247, 1682],
          [1682, 1675], [1675, 1465], [1465, 644], [644, 1511], [1511, 164], [164, 1673], [1673, 850], [850, 1289],
          [1289, 1009], [1009, 382], [382, 380], [380, 1055], [1055, 841], [841, 1602], [1602, 1132], [1132, 669],
          [669, 1756], [1756, 1222], [1222, 560], [560, 1069], [1069, 1611], [1611, 1751], [1751, 26], [26, 680],
          [680, 307], [307, 552], [552, 1036], [1036, 854], [854, 1514], [1514, 1979], [1979, 1529], [1529, 1156],
          [1156, 39], [39, 1366], [1366, 514], [514, 1082], [1082, 381], [381, 206], [206, 1245], [1245, 394],
          [394, 1584], [1584, 184], [184, 1466], [1466, 1817], [1817, 1249], [1249, 337], [337, 1530], [1530, 679],
          [679, 125], [125, 1710], [1710, 1275], [1275, 409], [409, 810], [810, 370], [370, 1263], [1263, 346],
          [346, 1157], [1157, 261], [261, 1548], [1548, 834], [834, 1210], [1210, 185], [185, 755], [755, 811],
          [811, 1691], [1691, 177], [177, 1930], [1930, 127], [127, 550], [550, 580], [580, 1372], [1372, 1639],
          [1639, 1150], [1150, 1998], [1998, 373], [373, 1855], [1855, 1259], [1259, 1258], [1258, 1897], [1897, 1811],
          [1811, 453], [453, 1328], [1328, 1826], [1826, 82], [82, 1115], [1115, 1726], [1726, 1020], [1020, 1829],
          [1829, 418], [418, 1973], [1973, 1129], [1129, 1812], [1812, 1549], [1549, 1631], [1631, 557], [557, 1589],
          [1589, 907], [907, 555], [555, 56], [56, 1186], [1186, 1262], [1262, 734], [734, 987], [987, 1202],
          [1202, 1995], [1995, 1885], [1885, 1864], [1864, 527], [527, 744], [744, 1141], [1141, 791], [791, 1167],
          [1167, 1137], [1137, 1986], [1986, 1215], [1215, 402], [402, 268], [268, 1067], [1067, 1312], [1312, 1711],
          [1711, 1375], [1375, 157], [157, 135], [135, 1604], [1604, 318], [318, 1772], [1772, 1110], [1110, 35],
          [35, 966], [966, 1833], [1833, 1297], [1297, 908], [908, 1327], [1327, 1420], [1420, 1028], [1028, 1330],
          [1330, 503], [503, 601], [601, 747], [747, 1913], [1913, 904], [904, 568], [568, 729], [729, 910], [910, 176],
          [176, 1540], [1540, 348], [348, 357], [357, 1112], [1112, 896], [896, 1874], [1874, 536], [536, 970],
          [970, 333], [333, 893], [893, 773], [773, 1629], [1629, 1910], [1910, 149], [149, 1018], [1018, 1153],
          [1153, 1364], [1364, 1525], [1525, 1040], [1040, 119], [119, 1713], [1713, 788], [788, 538], [538, 1607],
          [1607, 1119], [1119, 571], [571, 331], [331, 1114], [1114, 1368], [1368, 754], [754, 162], [162, 1386],
          [1386, 1279], [1279, 1116], [1116, 1125], [1125, 220], [220, 419], [419, 1346], [1346, 1480], [1480, 461],
          [461, 415], [415, 487], [487, 1305], [1305, 824], [824, 1957], [1957, 485], [485, 27], [27, 1821],
          [1821, 1831], [1831, 285], [285, 249], [249, 1993], [1993, 1683], [1683, 1046], [1046, 952], [952, 1596],
          [1596, 1213], [1213, 324], [324, 1192], [1192, 940], [940, 1298], [1298, 667], [667, 510], [510, 369],
          [369, 1608], [1608, 533], [533, 384], [384, 196], [196, 589], [589, 317], [317, 1497], [1497, 1438],
          [1438, 1037], [1037, 944], [944, 1376], [1376, 482], [482, 1361], [1361, 454], [454, 1685], [1685, 1575],
          [1575, 543], [543, 298], [298, 1935], [1935, 1336], [1336, 1302], [1302, 738], [738, 832], [832, 1248],
          [1248, 923], [923, 1872], [1872, 1430], [1430, 508], [508, 868], [868, 1187], [1187, 501], [501, 1435],
          [1435, 661], [661, 1816], [1816, 917], [917, 336], [336, 353], [353, 305], [305, 1951], [1951, 912],
          [912, 594], [594, 575], [575, 878], [878, 1086], [1086, 231], [231, 708], [708, 189], [189, 111], [111, 567],
          [567, 1322], [1322, 1510], [1510, 597], [597, 1649], [1649, 145], [145, 84], [84, 323], [323, 1719],
          [1719, 414], [414, 1462], [1462, 1270], [1270, 79], [79, 1070], [1070, 1706], [1706, 1669], [1669, 922],
          [922, 864], [864, 1966], [1966, 246], [246, 1794], [1794, 1972], [1972, 840], [840, 752], [752, 1300],
          [1300, 201], [201, 1319], [1319, 87], [87, 1637], [1637, 155], [155, 273], [273, 492], [492, 1387],
          [1387, 1571], [1571, 93], [93, 63], [63, 1460], [1460, 1489], [1489, 137], [137, 518], [518, 61], [61, 665],
          [665, 704], [704, 1659], [1659, 459], [459, 608], [608, 147], [147, 1860], [1860, 1126], [1126, 1102],
          [1102, 820], [820, 306], [306, 1914], [1914, 1505], [1505, 52], [52, 54], [54, 1615], [1615, 1122],
          [1122, 151], [151, 627], [627, 209], [209, 579], [579, 1818], [1818, 1385], [1385, 855], [855, 545],
          [545, 29], [29, 1146], [1146, 1777], [1777, 404], [404, 280], [280, 1033], [1033, 1614], [1614, 1839],
          [1839, 1395], [1395, 178], [178, 1242], [1242, 692], [692, 212], [212, 607], [607, 1641], [1641, 722],
          [722, 1704], [1704, 1035], [1035, 881], [881, 853], [853, 1522], [1522, 1692], [1692, 106], [106, 181],
          [181, 1975], [1975, 1887], [1887, 1894], [1894, 649], [649, 816], [816, 1], [1, 7], [7, 385], [385, 1665],
          [1665, 1121], [1121, 248], [248, 971], [971, 1281], [1281, 1764], [1764, 434], [434, 879], [879, 634],
          [634, 132], [132, 670], [670, 539], [539, 32], [32, 743], [743, 1363], [1363, 1737], [1737, 193], [193, 1622],
          [1622, 1354], [1354, 139], [139, 1762], [1762, 470], [470, 118], [118, 1879], [1879, 236], [236, 326],
          [326, 1698], [1698, 163], [163, 1785], [1785, 751], [751, 886], [886, 221], [221, 102], [102, 378],
          [378, 807], [807, 1824], [1824, 664], [664, 838], [838, 613], [613, 1084], [1084, 1078], [1078, 421],
          [421, 1653], [1653, 207], [207, 496], [496, 1595], [1595, 365], [365, 1101], [1101, 915], [915, 1015],
          [1015, 519], [519, 267], [267, 295], [295, 1603], [1603, 1888], [1888, 1383], [1383, 1813], [1813, 395],
          [395, 1643], [1643, 1702], [1702, 847], [847, 134], [134, 1564], [1564, 1280], [1280, 1870], [1870, 753],
          [753, 1630], [1630, 687], [687, 238], [238, 857], [857, 967], [967, 1418], [1418, 473], [473, 1591],
          [1591, 819], [819, 1149], [1149, 718], [718, 1922], [1922, 291], [291, 1402], [1402, 391], [391, 558],
          [558, 1316], [1316, 1984], [1984, 359], [359, 1439], [1439, 24], [24, 45], [45, 90], [90, 984], [984, 115],
          [115, 1073], [1073, 1956], [1956, 884], [884, 1411], [1411, 874], [874, 1065], [1065, 604], [604, 1871],
          [1871, 1945], [1945, 964], [964, 251], [251, 362], [362, 699], [699, 1214], [1214, 779], [779, 1237],
          [1237, 55], [55, 657], [657, 36], [36, 1970], [1970, 714], [714, 495], [495, 77], [77, 833], [833, 351],
          [351, 1277], [1277, 1382], [1382, 776], [776, 1696], [1696, 1791], [1791, 943], [943, 272], [272, 1934],
          [1934, 300], [300, 271], [271, 1797], [1797, 1401], [1401, 645], [645, 748], [748, 1512], [1512, 602],
          [602, 1981], [1981, 1295], [1295, 1229], [1229, 590], [590, 726], [726, 98], [98, 483], [483, 1145],
          [1145, 360], [360, 1323], [1323, 28], [28, 1005], [1005, 481], [481, 59], [59, 159], [159, 489], [489, 1845],
          [1845, 1627], [1627, 1761], [1761, 875], [875, 1539], [1539, 863], [863, 1362], [1362, 1097], [1097, 1278],
          [1278, 329], [329, 585], [585, 1828], [1828, 1827], [1827, 683], [683, 1092], [1092, 1023], [1023, 1423],
          [1423, 1250], [1250, 81], [81, 222], [222, 1893], [1893, 1108], [1108, 339], [339, 880], [880, 1449],
          [1449, 1188], [1188, 759], [759, 1310], [1310, 1965], [1965, 1830], [1830, 1099], [1099, 1661], [1661, 564],
          [564, 334], [334, 541], [541, 1144], [1144, 1301], [1301, 1314], [1314, 1219], [1219, 658], [658, 315],
          [315, 1621], [1621, 678], [678, 70], [70, 25], [25, 990], [990, 1358], [1358, 902], [902, 586], [586, 1658],
          [1658, 1748], [1748, 805], [805, 1803], [1803, 561], [561, 522], [522, 836], [836, 1195], [1195, 975],
          [975, 587], [587, 1544], [1544, 66], [66, 22], [22, 1135], [1135, 253], [253, 1787], [1787, 905], [905, 906],
          [906, 10], [10, 695], [695, 812], [812, 1768], [1768, 1769], [1769, 641], [641, 1820], [1820, 270],
          [270, 1590], [1590, 858], [858, 1365], [1365, 1609], [1609, 1351], [1351, 1048], [1048, 194], [194, 1992],
          [1992, 1398], [1398, 1155], [1155, 1444], [1444, 1771], [1771, 1173], [1173, 1318], [1318, 216], [216, 1396],
          [1396, 732], [732, 1140], [1140, 1378], [1378, 192], [192, 1703], [1703, 228], [228, 1340], [1340, 592],
          [592, 325], [325, 1170], [1170, 1720], [1720, 364], [364, 294], [294, 1689], [1689, 301], [301, 1582],
          [1582, 1450], [1450, 675], [675, 1524], [1524, 1783], [1783, 1739], [1739, 1636], [1636, 1842], [1842, 1457],
          [1457, 804], [804, 243], [243, 1844], [1844, 154], [154, 1538], [1538, 1426], [1426, 1671], [1671, 1455],
          [1455, 1520], [1520, 1666], [1666, 1269], [1269, 214], [214, 1825], [1825, 1369], [1369, 931], [931, 1898],
          [1898, 959], [959, 1716], [1716, 544], [544, 606], [606, 1074], [1074, 1859], [1859, 1770], [1770, 1021],
          [1021, 1837], [1837, 867], [867, 392], [392, 416], [416, 1408], [1408, 806], [806, 128], [128, 1374],
          [1374, 1107], [1107, 1198], [1198, 1521], [1521, 1481], [1481, 1849], [1849, 53], [53, 321], [321, 981],
          [981, 1853], [1853, 921], [921, 598], [598, 451], [451, 777], [777, 1206], [1206, 676], [676, 41], [41, 844],
          [844, 1437], [1437, 976], [976, 1681], [1681, 144], [144, 1335], [1335, 837], [837, 1868], [1868, 1244],
          [1244, 992], [992, 639], [639, 1773], [1773, 1869], [1869, 444], [444, 217], [217, 1838], [1838, 1216],
          [1216, 1203], [1203, 19], [19, 1096], [1096, 965], [965, 438], [438, 525], [525, 537], [537, 797], [797, 696],
          [696, 642], [642, 926], [926, 770], [770, 935], [935, 1130], [1130, 650], [650, 1470], [1470, 668],
          [668, 1742], [1742, 1422], [1422, 1999], [1999, 1098], [1098, 190], [190, 1788], [1788, 540], [540, 720],
          [720, 283], [283, 778], [778, 866], [866, 1929], [1929, 1068], [1068, 242], [242, 1041], [1041, 825],
          [825, 1267], [1267, 1238], [1238, 1908], [1908, 1113], [1113, 252], [252, 1668], [1668, 1476], [1476, 1131],
          [1131, 327], [327, 1436], [1436, 697], [697, 1743], [1743, 1264], [1264, 1635], [1635, 18], [18, 1224],
          [1224, 1413], [1413, 1027], [1027, 477], [477, 530], [530, 1432], [1432, 1257], [1257, 398], [398, 1004],
          [1004, 1201], [1201, 780], [780, 1174], [1174, 979], [979, 605], [605, 565], [565, 1331], [1331, 1612],
          [1612, 347], [347, 1407], [1407, 930], [930, 1127], [1127, 1968], [1968, 46], [46, 1697], [1697, 1792],
          [1792, 388], [388, 1044], [1044, 660], [660, 674], [674, 1482], [1482, 1152], [1152, 107], [107, 632],
          [632, 1597], [1597, 1780], [1780, 553], [553, 1032], [1032, 158], [158, 1417], [1417, 148], [148, 1650],
          [1650, 1479], [1479, 721], [721, 1047], [1047, 712], [712, 1846], [1846, 782], [782, 1624], [1624, 1024],
          [1024, 982], [982, 745], [745, 761], [761, 1190], [1190, 140], [140, 978], [978, 637], [637, 1373],
          [1373, 1276], [1276, 1416], [1416, 1832], [1832, 265], [265, 1498], [1498, 1779], [1779, 74], [74, 1542],
          [1542, 1045], [1045, 1765], [1765, 654], [654, 1878], [1878, 960], [960, 1969], [1969, 593], [593, 1143],
          [1143, 643]])
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.findOrder(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
