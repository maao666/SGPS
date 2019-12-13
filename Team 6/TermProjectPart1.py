################################################
# Class: EECS 118                              #
# Term Project Part 1                          #
# Team Number: 6                               #
# Team Members:                                #
# Nathaniel Aponte, aponten@uci.edu, 41858361  #
# Guy Darel, gdarel@uci.edu, 86251615          #
################################################


class MainClass:
    def __init__(self):
        # required values
        self.parallel = []  # line only              HAS WORKS
        self.perpendicular = []  # line only              HAS WORKS
        self.equal = []  # line angle and area    HAS WORKS
        self.fraction = []  # line angle and area    HAS PARTIALLY WORKS
        self.sum_value = []  # line angle and area    HAS PARTIALLY WORKS
        self.similar = []  # area only              HAS WORKS
        self.congruent = []  # area only              HAS WORKS
        self.tan = []  # unused
        #
        self.right = []  # angle only             HAS DOESN'T WORKS

    def has(self, type_name, name1, name2):#checks if both names exist as an entry in specified attribute list, order doesnt matter
        temp_name = getattr(self, type_name)
        for p in temp_name:
            if p[0] in (name1, name2) and p[1] in (name1, name2):
                return True
        return False

    def has_3(self, type_name, name1, name2, num):#checks if both names and the num exist as an entry in specified attribute list, order doesnt matter
        temp_name = getattr(self, type_name)
        for p in temp_name:
            if p[0] in (name1, name2, num) and p[1] in (name1, name2, num) and p[2] in (name1, name2, num):
                return True
        return False

    def has_right(self, name):#checks if the name exists as an entry in self.right attribute list, order doesnt matter
        for p in self.right:
            if p == name:
                return True
        return False

    def set_right(self, name):#adds entry to right artibute list
        self.right.append(name)

    def set_parallel(self, name1, name2):#adds entry to parallel artibute list
        if self.has("parallel", name1, name2):
            return 0
        tmp_name1 = "know_" + name1
        tmp_name2 = "know_" + name2
        self.parallel.append((name1, name2))
        getattr(self, tmp_name1)()
        getattr(self, tmp_name2)()
        return 0

    def set_perpendicular(self, name1, name2):#adds entry to perpendicular artibute list
        if self.has("perpendicular", name1, name2):
            return 0
        tmp_name1 = "know_" + name1
        tmp_name2 = "know_" + name2
        self.perpendicular.append((name1, name2))
        getattr(self, tmp_name1)()
        getattr(self, tmp_name2)()
        return 0

    def set_equal(self, name1, name2):#adds entry to equal artibute list
        if self.has("equal", name1, name2):
            return 0
        tmp_name1 = "know_" + name1
        tmp_name2 = "know_" + name2
        self.equal.append((name1, name2))
        getattr(self, tmp_name1)()
        getattr(self, tmp_name2)()
        return 0

    def set_fraction(self, name1, name2, fraction):#adds entry to fraction artibute list
        if self.has("fraction", name1, name2):
            return 0
        tmp_name1 = "know_" + name1
        tmp_name2 = "know_" + name2
        self.fraction.append("Null")
        getattr(self, tmp_name1)()
        getattr(self, tmp_name2)()
        return 0

    def set_sum_value(self, name1, name2, sum_value):#adds entry to sum_value artibute list
        if self.has("sum_value", name1, name2):
            return 0
        tmp_name1 = "know_" + name1
        tmp_name2 = "know_" + name2
        self.sum_value.append((name1, name2, sum_value))
        getattr(self, tmp_name1)()
        getattr(self, tmp_name2)()
        return 0

    def set_similar(self, name1, name2):#adds entry to similar artibute list
        if self.has("similar", name1, name2):
            return 0
        tmp_name1 = "know_" + name1
        tmp_name2 = "know_" + name2
        self.similar.append((name1, name2))
        getattr(self, tmp_name1)()
        getattr(self, tmp_name2)()
        return 0

    def set_congruent(self, name1, name2):#adds entry to congruent artibute list
        if self.has("congruent", name1, name2):
            return 0
        tmp_name1 = "know_" + name1
        tmp_name2 = "know_" + name2
        self.congruent.append((name1, name2))
        getattr(self, tmp_name1)()
        getattr(self, tmp_name2)()
        return 0

    # ############################  SIDES  ###################################
    #                                                                        #
    # Sides 20 total                                                         #
    #                                                                        #
    # ########################################################################

    def know_sa6(self):
        #set angles along parrallel lines
        if self.has("parallel", "sa6", "sa7") and not self.has("equal", "c2", "c4"):
            self.set_equal("c2", "c4")
            self.know_sa6()
            self.know_c2()
            self.know_c4()
        if self.has("parallel", "sa6", "sc7") and not self.has("equal", "c5", "c4"):
            self.set_equal("c5", "c4")
            self.know_sa6()
            self.know_c5()
            self.know_c4()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa6", "sc6") and not self.has_right("a4"):
            self.set_right("a4")
            self.set_perpendicular("sa4", "sb4")
            self.set_sum_value("b2", "c4", "90")
            self.know_sc6()
            self.know_sa4()
            self.know_sb4()
            self.know_b2()
            self.know_c4()
            self.know_a4()
            self.know_sa6()
        if self.has("perpendicular", "sa6", "sb6") and not self.has_right("c4"):
            self.set_right("c4")
            self.set_perpendicular("sa4", "sd4")
            self.set_sum_value("a4", "b2", "90")
            self.know_sb6()
            self.know_sa4()
            self.know_sd4()
            self.know_a4()
            self.know_b2()
            self.know_c4()
            self.know_sa6()
        return 0

    def know_sb6(self):
        #set angles along parrallel lines
        if self.has("parallel", "sb7", "sb6") and not self.has("equal", "b5", "b3"):
            self.set_equal("b5", "b3")
            self.set_parallel("sd3", "sb3")
            self.know_sb6()
            self.know_b5()
            self.know_b3()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa6", "sb6") and not self.has_right("c4"):
            self.set_right("c4")
            self.set_perpendicular("sa4", "sd4")
            self.set_sum_value("a4", "b2", "90")
            self.know_sa4()
            self.know_sd4()
            self.know_a4()
            self.know_b2()
            self.know_c4()
            self.know_sa6()
            self.know_sb6()
        if self.has("perpendicular", "sb6", "sc6") and not self.has_right("b2"):
            self.set_right("b2")
            self.set_perpendicular("sa2", "sb2")
            self.set_sum_value("a4", "c4", "90")
            self.know_sc6()
            self.know_sa2()
            self.know_sb2()
            self.know_a4()
            self.know_c4()
            self.know_b2()
            self.know_sb6()
        return 0

    def know_sc6(self):
        #set angles along parrallel lines
        if self.has("parallel", "sb7", "sc6") and not self.has("equal", "b1", "b3"):
            self.set_equal("b1", "b3")
            self.set_parallel("sc1", "sb3")
            self.know_sc6()
            self.know_b1()
            self.know_b3()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa6", "sc6") and not self.has_right("a4"):
            self.set_right("a4")
            self.set_perpendicular("sa4", "sb4")
            self.set_sum_value("b2", "c4", "90")
            self.know_sa4()
            self.know_sb4()
            self.know_b2()
            self.know_c4()
            self.know_a4()
            self.know_sa6()
            self.know_sc6()
        if self.has("perpendicular", "sb6", "sc6") and not self.has_right("b2"):
            self.set_right("b2")
            self.set_perpendicular("sa2", "sb2")
            self.set_sum_value("a4", "c4", "90")
            self.know_sa2()
            self.know_sb2()
            self.know_a4()
            self.know_c4()
            self.know_b2()
            self.know_sb6()
            self.know_sc6()
        return 0

    def know_sa7(self):
        #set angles along parrallel lines
        if self.has("parallel", "sa6", "sa7") and not self.has("equal", "a2", "a4"):
            self.set_equal("a2", "a4")
            self.set_parallel("sc2", "sa4")
            self.know_sa7()
            self.know_a2()
            self.know_a4()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa7", "sc7") and not self.has_right("a1"):
            self.set_right("a1")
            self.set_perpendicular("sa1", "sb1")
            self.set_sum_value("b3", "c3", "90")
            self.know_sc7()
            self.know_sa1()
            self.know_sb1()
            self.know_b3()
            self.know_c3()
            self.know_a1()
            self.know_sa7()
        if self.has("perpendicular", "sa7", "sb7") and not self.has_right("b3"):
            self.set_right("b3")
            self.set_perpendicular("sa3", "sb3")
            self.set_sum_value("a1", "c3", "90")
            self.know_sb7()
            self.know_sa3()
            self.know_sb3()
            self.know_a1()
            self.know_c3()
            self.know_b3()
            self.know_sa7()
        return 0

    def know_sb7(self):
        #set angles along parrallel lines
        if self.has("parallel", "sb7", "sc6") and not self.has("equal", "c1", "c3"):
            self.set_equal("c1", "c3")
            self.know_sb7()
            self.know_c1()
            self.know_c3()
        if self.has("parallel", "sb7", "sb6") and not self.has("equal", "c5", "c3"):
            self.set_equal("c5", "c3")
            self.know_sb7()
            self.know_c5()
            self.know_c3()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa7", "sb7") and not self.has_right("b3"):
            self.set_right("b3")
            self.set_perpendicular("sa3", "sb3")
            self.set_sum_value("a1", "c3", "90")
            self.know_sa3()
            self.know_sb3()
            self.know_a1()
            self.know_c3()
            self.know_b3()
            self.know_sa7()
            self.know_sb7()
        if self.has("perpendicular", "sb7", "sc7") and not self.has_right("c3"):
            self.set_right("c3")
            self.set_perpendicular("sb3", "sc3")
            self.set_sum_value("a1", "b3", "90")
            self.know_sc7()
            self.know_sb3()
            self.know_sc3()
            self.know_b3()
            self.know_a1()
            self.know_c3()
            self.know_sb7()
        return 0

    def know_sc7(self):
        #set angles along parrallel lines
        if self.has("parallel", "sa6", "sc7") and not self.has("equal", "d5", "a4"):
            self.set_equal("d5", "a4")
            self.set_parallel("sc4", "sa4")
            self.know_sc7()
            self.know_d5()
            self.know_a4()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa7", "sc7") and not self.has_right("a1"):
            self.set_right("a1")
            self.set_perpendicular("sa1", "sb1")
            self.set_sum_value("b3", "c3", "90")
            self.know_sa1()
            self.know_sb1()
            self.know_b3()
            self.know_c3()
            self.know_a1()
            self.know_sa7()
            self.know_sc7()
        if self.has("perpendicular", "sb7", "sc7") and not self.has_right("c3"):
            self.set_right("c3")
            self.set_perpendicular("sb3", "sc3")
            self.set_sum_value("a1", "b3", "90")
            self.know_sb3()
            self.know_sc3()
            self.know_b3()
            self.know_a1()
            self.know_c3()
            self.know_sb7()
            self.know_sc7()
        return 0

    def know_sa1(self):
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa1", "sb1") and not self.has_right("a1"):
            self.set_right("a1")
            self.set_perpendicular("sa7", "sc7")
            self.set_sum_value("b3", "c3", "90")
            self.know_sa7()
            self.know_sc7()
            self.know_b3()
            self.know_c3()
            self.know_a1()
            self.know_sb1()
            self.know_sa1()
        return 0

    def know_sb1(self):
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa1", "sb1") and not self.has_right("a1"):
            self.set_right("a1")
            self.set_perpendicular("sa7", "sc7")
            self.set_sum_value("b3", "c3", "90")
            self.know_sa7()
            self.know_sc7()
            self.know_b3()
            self.know_c3()
            self.know_a1()
            self.know_sa1()
            self.know_sb1()
        return 0

    def know_sc1(self):
        #set angles along parrallel lines
        if self.has("parallel", "sb3", "sc1") and not self.has("equal", "b1", "b3"):
            self.set_equal("b1", "b3")
            self.set_parallel("sb7", "sc6")
            self.know_sc1()
            self.know_b1()
            self.know_b3()
        return 0

    def know_sa2(self):
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa2", "sb2") and not self.has_right("b2"):
            self.set_right("b2")
            self.set_perpendicular("sb6", "sc6")
            self.set_sum_value("a4", "c4", "90")
            self.know_sc6()
            self.know_sb6()
            self.know_sb2()
            self.know_a4()
            self.know_c4()
            self.know_b2()
            self.know_sa2()
        return 0

    def know_sb2(self):
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa2", "sb2") and not self.has_right("b2"):
            self.set_right("b2")
            self.set_perpendicular("sb6", "sc6")
            self.set_sum_value("a4", "c4", "90")
            self.know_sc6()
            self.know_sb6()
            self.know_sa2()
            self.know_a4()
            self.know_c4()
            self.know_b2()
            self.know_sb2()
        return 0

    def know_sc2(self):
        #set angles along parrallel lines
        if self.has("parallel", "sa4", "sc2") and not self.has("equal", "a2", "a4"):
            self.set_equal("a2", "a4")
            self.set_parallel("sa6", "sa7")
            self.know_sc2()
            self.know_a2()
            self.know_a4()
        return 0

    def know_sa3(self):
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa3", "sb3") and not self.has_right("b3"):
            self.set_right("b3")
            self.set_perpendicular("sa7", "sb7")
            self.set_sum_value("a1", "c3", "90")
            self.know_sb7()
            self.know_sb3()
            self.know_a1()
            self.know_c3()
            self.know_b3()
            self.know_sa7()
            self.know_sa3()
        return 0

    def know_sb3(self):
        #set angles along parrallel lines
        if self.has("parallel", "sb3", "sc1") and not self.has("equal", "c1", "c3"):
            self.set_equal("c1", "c3")
            self.know_sb3()
            self.know_c1()
            self.know_c3()
        if self.has("parallel", "sb3", "sd3") and not self.has("equal", "c5", "c3"):
            self.set_equal("c5", "c3")
            self.know_sb3()
            self.know_c5()
            self.know_c3()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa3", "sb3") and not self.has_right("b3"):
            self.set_right("b3")
            self.set_perpendicular("sa7", "sb7")
            self.set_sum_value("a1", "c3", "90")
            self.know_sb7()
            self.know_a1()
            self.know_c3()
            self.know_b3()
            self.know_sa7()
            self.know_sa3()
            self.know_sb3()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sb3", "sc3") and not self.has_right("c3"):
            self.set_right("c3")
            self.set_perpendicular("sb7", "sc7")
            self.set_sum_value("a1", "b3", "90")
            self.know_sc7()
            self.know_sb7()
            self.know_sc3()
            self.know_b3()
            self.know_a1()
            self.know_c3()
            self.know_sb3()
        return 0

    def know_sc3(self):
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sb3", "sc3") and not self.has_right("c3"):
            self.set_right("c3")
            self.set_perpendicular("sb7", "sc7")
            self.set_sum_value("a1", "b3", "90")
            self.know_sc7()
            self.know_sb7()
            self.know_b3()
            self.know_a1()
            self.know_c3()
            self.know_sb3()
            self.know_sc3()
        return 0

    def know_sd3(self):
        #set angles along parrallel lines
        if self.has("parallel", "sb3", "sd3") and not self.has("equal", "b5", "b3"):
            self.set_equal("b5", "b3")
            self.set_parallel("sb7", "sb6")
            self.know_sd3()
            self.know_b5()
            self.know_b3()
        return 0

    def know_sa4(self):
        #set angles along parrallel lines
        if self.has("parallel", "sa4", "sc2") and not self.has("equal", "c2", "c4"):
            self.set_equal("c2", "c4")
            self.know_sa4()
            self.know_c2()
            self.know_c4()
        if self.has("parallel", "sa4", "sc4") and not self.has("equal", "c5", "c4"):
            self.set_equal("c5", "c4")
            self.know_sa4()
            self.know_c5()
            self.know_c4()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sb4", "sa4") and not self.has_right("a4"):
            self.set_right("a4")
            self.set_perpendicular("sa6", "sc6")
            self.set_sum_value("b2", "c4", "90")
            self.know_sc6()
            self.know_sa6()
            self.know_b2()
            self.know_c4()
            self.know_a4()
            self.know_sb4()
            self.know_sa4()
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa4", "sd4") and not self.has_right("c4"):
            self.set_right("c4")
            self.set_perpendicular("sa6", "sb6")
            self.set_sum_value("a4", "b2", "90")
            self.know_sb6()
            self.know_sa6()
            self.know_sd4()
            self.know_a4()
            self.know_b2()
            self.know_c4()
            self.know_sa4()
        return 0

    def know_sb4(self):
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sb4", "sa4") and not self.has_right("a4"):
            self.set_right("a4")
            self.set_perpendicular("sa6", "sc6")
            self.set_sum_value("b2", "c4", "90")
            self.know_sc6()
            self.know_sa4()
            self.know_sa6()
            self.know_b2()
            self.know_c4()
            self.know_a4()
            self.know_sb4()
        return 0

    def know_sc4(self):
        #set angles along parrallel lines
        if self.has("parallel", "sa4", "sc4") and not self.has("equal", "d5", "a4"):
            self.set_equal("d5", "a4")
            self.set_parallel("sa6", "sc7")
            self.know_sc4()
            self.know_d5()
            self.know_a4()
        return 0

    def know_sd4(self):
        #set info for perp intersections at the corners of large triangles
        if self.has("perpendicular", "sa4", "sd4") and not self.has_right("c4"):
            self.set_right("c4")
            self.set_perpendicular("sa6", "sb6")
            self.set_sum_value("a4", "b2", "90")
            self.know_sb6()
            self.know_sa6()
            self.know_sa4()
            self.know_a4()
            self.know_b2()
            self.know_c4()
            self.know_sd4()
        return 0

    # ############################  Angles  ##################################
    #                                                                        #
    # angles 18 total                                                        #
    #                                                                        #
    ##########################################################################

    def know_a5(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "a5", "a2") and not self.has_right("a5"):
            self.set_right("a5")
            self.know_a2()
            self.know_a5()
        if self.has("equal", "a5", "b1") and not self.has_right("a5"):
            self.set_right("a5")
            self.know_a5()
        return 0

    def know_b5(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "b5", "c2") and not self.has_right("b5"):
            self.set_right("b5")
            self.know_b5()
        if self.has("equal", "b5", "a3") and not self.has_right("b5"):
            self.set_right("b5")
            self.know_b5()
        if self.has("equal", "b5", "b3") and not self.has("parallel", "sb6", "sb7"):
            self.set_parallel("sb6", "sb7")
            self.know_sb6()
            self.know_sb7()
            self.know_b3()
            self.know_b5()
        return 0

    def know_c5(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "c5", "d3") and not self.has_right("c5"):
            self.set_right("c5")
            self.know_c5()
        if self.has("equal", "c5", "d4") and not self.has_right("c5"):
            self.set_right("c5")
            self.know_c5()
        if self.has("equal", "c5", "c4") and not self.has("parallel", "sc7", "sa6"):
            self.set_parallel("sc7", "sa6")
            self.know_sc7()
            self.know_sa6()
            self.know_c4()
            self.know_c5()
        if self.has("equal", "c5", "c3") and not self.has("parallel", "sb6", "sb7"):
            self.set_parallel("sb6", "sb7")
            self.know_sb6()
            self.know_sb7()
            self.know_c3()
            self.know_c5()
        return 0

    def know_d5(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "d5", "c1") and not self.has_right("d5"):
            self.set_right("d5")
            self.know_d5()
        if self.has("equal", "d5", "b4") and not self.has_right("d5"):
            self.set_right("d5")
            self.know_d5()
        if self.has("equal", "d5", "a4") and not self.has("parallel", "sc7", "sa6"):
            self.set_parallel("sc7", "sa6")
            self.know_sc7()
            self.know_sa6()
            self.know_a4()
            self.know_d5()
        if self.has_right("d5") and not self.has_right("c1"):
            self.set_right("c1")
            self.know_c1()
            self.know_d5()
        return 0

    def know_a1(self):
        #check if triangle is right and adjuusts info
        if self.has_right("a1") and (not self.has("perpendicular", "sa7", "sc7")):
            self.set_perpendicular("sa7", "sc7")
            self.set_perpendicular("sa1", "sb1")
            self.set_sum_value("b3", "c3", "90")
            self.know_sa7()
            self.know_sc7()
            self.know_sa1()
            self.know_sb1()
            self.know_b3()
            self.know_c3()
            self.know_a1()
        if self.has_3("sum_value", "a1", "b3", "90") and not self.has_right("c3"):
            self.set_right("c3")
            self.know_c3()
            self.know_b3()
            self.know_a1()
        if self.has_3("sum_value", "a1", "c3", "90") and not self.has_right("b3"):
            self.set_right("b3")
            self.know_c3()
            self.know_b3()
            self.know_a1()
        if self.has_3("sum_value", "b1", "a1", "90") and not self.has_right("c1"):
            self.set_right("c1")
            self.know_c1()
            self.know_a1()
            self.know_b1()
        if self.has_3("sum_value", "c1", "a1", "90") and not self.has_right("b1"):
            self.set_right("b1")
            self.know_b1()
            self.know_a1()
            self.know_c1()
        return 0

    def know_b1(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "a5", "b1") and not self.has_right("b1"):
            self.set_right("b1")
            self.know_b1()
        if self.has("equal", "b1", "b3") and not self.has("parallel", "sc6", "sb7"):
            self.set_parallel("sc6", "sb7")
            self.know_sc6()
            self.know_sb7()
            self.know_b3()
            self.know_b1()
        if self.has_3("sum_value", "c1", "b1", "90") and not self.has_right("a1"):
            self.set_right("a1")
            self.know_a1()
            self.know_b1()
            self.know_c1()
        if self.has_3("sum_value", "b1", "a1", "90") and not self.has_right("c1"):
            self.set_right("c1")
            self.know_c1()
            self.know_a1()
            self.know_b1()
        return 0

    def know_c1(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "d5", "c1") and not self.has_right("c1"):
            self.set_right("c1")
            self.know_c1()
        if self.has("equal", "c1", "c3") and not self.has("parallel", "sc6", "sb7"):
            self.set_parallel("sc6", "sb7")
            self.know_sc6()
            self.know_sb7()
            self.know_c3()
            self.know_c1()
        if self.has_3("sum_value", "c1", "b1", "90") and not self.has_right("a1"):
            self.set_right("a1")
            self.know_a1()
            self.know_b1()
            self.know_c1()
        if self.has_right("c1") and not self.has_3("sum_value", "a1", "b1", "90"):
            self.set_sum_value("a1", "b1", "90")
            self.know_a1()
            self.know_b1()
            self.know_c1()
        if self.has_3("sum_value", "c1", "a1", "90") and not self.has_right("b1"):
            self.set_right("b1")
            self.know_b1()
            self.know_a1()
            self.know_c1()
        return 0

    def know_a2(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "a5", "a2") and not self.has_right("a2"):
            self.set_right("a2")
            self.know_a5()
            self.know_a2()
        if self.has("equal", "a4", "a2") and not self.has("parallel", "sa7", "sa6"):
            self.set_parallel("sa7", "sa6")
            self.know_sa7()
            self.know_sa6()
            self.know_a4()
            self.know_a2()
        if self.has_3("sum_value", "a2", "c2", "90") and not self.has_right("b2"):
            self.set_right("b2")
            self.know_b2()
            self.know_c2()
            self.know_a2()
        if self.has_3("sum_value", "a2", "b2", "90") and not self.has_right("c2"):
            self.set_right("c2")
            self.know_c2()
            self.know_b2()
            self.know_a2()
        return 0

    def know_b2(self):
        #check if triangle is right and adjuusts info
        if self.has_right("b2") and not self.has("perpendicular", "sb6", "sc6"):
            self.set_perpendicular("sb6", "sc6")
            self.set_perpendicular("sa2", "sb2")
            self.set_sum_value("a4", "c4", "90")
            self.know_sb6()
            self.know_sc6()
            self.know_sa2()
            self.know_sb2()
            self.know_a4()
            self.know_c4()
            self.know_b2()
        if self.has_3("sum_value", "c4", "b2", "90") and not self.has_right("a4"):
            self.set_right("a4")
            self.know_a4()
            self.know_c4()
            self.know_b2()
        if self.has_3("sum_value", "a4", "b2", "90") and not self.has_right("c4"):
            self.set_right("c4")
            self.know_c4()
            self.know_b2()
            self.know_a4()
        if self.has_3("sum_value", "b2", "c2", "90") and not self.has_right("a2"):
            self.set_right("a2")
            self.know_a2()
            self.know_c2()
            self.know_b2()
        if self.has_3("sum_value", "a2", "b2", "90") and not self.has_right("c2"):
            self.set_right("c2")
            self.know_c2()
            self.know_b2()
            self.know_a2()

        return 0

    def know_c2(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "b5", "c2") and not self.has_right("c2"):
            self.set_right("c2")
            self.know_c2()
        if self.has("equal", "c4", "c2") and not self.has("parallel", "sa7", "sa6"):
            self.set_parallel("sa7", "sa6")
            self.know_sa7()
            self.know_sa6()
            self.know_c4()
            self.know_c2()
        if self.has_3("sum_value", "b2", "c2", "90") and not self.has_right("a2"):
            self.set_right("a2")
            self.know_a2()
            self.know_c2()
            self.know_b2()
        if self.has_3("sum_value", "a2", "c2", "90") and not self.has_right("b2"):
            self.set_right("b2")
            self.know_b2()
            self.know_c2()
            self.know_a2()
        return 0

    def know_a3(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "b5", "a3") and not self.has_right("a3"):
            self.set_right("a3")
            self.know_a3()
        return 0

    def know_b3(self):
        #adjusts equal angles to be right if other is right
        if (self.has("equal", "b5", "b3")
                and not self.has_right("b3")
                and self.has_right("b5")):
            self.set_right("b3")
            self.know_b3()

        #check if triangle is right and adjuusts info
        if self.has_right("b3") and not self.has("perpendicular", "sa7", "sb7"):
            self.set_perpendicular("sa7", "sb7")
            self.set_perpendicular("sa3", "sb3")
            self.set_sum_value("a1", "c3", "90")
            self.know_sa7()
            self.know_sb7()
            self.know_sa3()
            self.know_sb3()
            self.know_a1()
            self.know_c3()
            self.know_b3()
        if self.has("equal", "b1", "b3") and not self.has("parallel", "sc6", "sb7"):
            self.set_parallel("sc6", "sb7")
            self.know_sc6()
            self.know_sb7()
            self.know_b1()
            self.know_b3()
        if self.has_3("sum_value", "a1", "b3", "90") and not self.has_right("c3"):
            self.set_right("c3")
            self.know_c3()
            self.know_a1()
            self.know_b3()
        if self.has_3("sum_value", "b3", "c3", "90") and not self.has_right("a1"):
            self.set_right("a1")
            self.know_a1()
            self.know_c3()
            self.know_b3()

        return 0

    def know_c3(self):
        #adjusts equal angles to be right if other is right
        if (self.has("equal", "c5", "c3")
                and not self.has_right("c3")
                and self.has_right("c5")):
            self.set_right("c3")
            self.know_c3()
        #check if triangle is right and adjuusts info
        if self.has_right("c3") and not self.has("perpendicular", "sb7", "sc7"):
            self.set_perpendicular("sb7", "sc7")
            self.set_perpendicular("sb3", "sc3")
            self.set_sum_value("a1", "b3", "90")
            self.know_sb7()
            self.know_sc7()
            self.know_sb3()
            self.know_sc3()
            self.know_b3()
            self.know_a1()
            self.know_c3()
        if self.has("equal", "c1", "c3") and not self.has("parallel", "sc6", "sb7"):
            self.set_parallel("sc6", "sb7")
            self.know_sc6()
            self.know_sb7()
            self.know_c1()
            self.know_c3()
        if self.has("equal", "c5", "c3") and not self.has("parallel", "sb6", "sb7"):
            self.set_parallel("sb6", "sb7")
            self.know_sb6()
            self.know_sb7()
            self.know_c5()
            self.know_c3()
        if self.has_3("sum_value", "b3", "c3", "90") and not self.has_right("a1"):
            self.set_right("a1")
            self.know_a1()
            self.know_c3()
            self.know_b3()
        if self.has_3("sum_value", "a1", "c3", "90") and not self.has_right("b3"):
            self.set_right("b3")
            self.know_c3()
            self.know_b3()
            self.know_a1()
        return 0

    def know_d3(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "c5", "d3") and not self.has_right("d3"):
            self.set_right("d3")
            self.know_d3()
        return 0

    def know_a4(self):
        #adjusts equal angles to be right if other is right
        if (self.has("equal", "d5", "a4")
                and not self.has_right("a4")
                and self.has_right("d5")):
            self.set_right("a4")
            self.know_a4()

        #check if triangle is right and adjuusts info
        if self.has_right("a4") and not self.has("perpendicular", "sa6", "sc6"):
            self.set_perpendicular("sa6", "sc6")
            self.set_perpendicular("sa4", "sb4")
            self.set_sum_value("b2", "c4", "90")
            self.know_sa6()
            self.know_sc6()
            self.know_sa4()
            self.know_sb4()
            self.know_b2()
            self.know_c4()
            self.know_a4()
        if self.has("equal", "a4", "a2") and not self.has("parallel", "sa7", "sa6"):
            self.set_parallel("sa7", "sa6")
            self.know_sa7()
            self.know_sa6()
            self.know_a2()
            self.know_a4()
        if self.has("equal", "d5", "a4") and not self.has("parallel", "sc7", "sa6"):
            self.set_parallel("sc7", "sa6")
            self.know_sc7()
            self.know_sa6()
            self.know_d5()
            self.know_a4()
        if self.has_3("sum_value", "a4", "c4", "90") and not self.has_right("b2"):
            self.set_right("b2")
            self.know_b2()
            self.know_c4()
            self.know_a4()
        if self.has_3("sum_value", "a4", "b2", "90") and not self.has_right("c4"):
            self.set_right("c4")
            self.know_c4()
            self.know_b2()
            self.know_a4()

        return 0

    def know_b4(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "d5", "b4") and not self.has_right("b4"):
            self.set_right("b4")
            self.know_b4()
        return 0

    def know_c4(self):
        #adjusts equal angles to be right if other is right
        if (self.has("equal", "c5", "c4")
                and not self.has_right("c4")
                and self.has_right("c5")):
            self.set_right("c4")
            self.know_c4()

        #check if triangle is right and adjuusts info
        if self.has_right("c4") and not self.has("perpendicular", "sa6", "sb6"):
            self.set_perpendicular("sa6", "sb6")
            self.set_perpendicular("sa4", "sd4")
            self.set_sum_value("a4", "b2", "90")
            self.know_sa6()
            self.know_sb6()
            self.know_sa4()
            self.know_sd4()
            self.know_a4()
            self.know_b2()
            self.know_c4()
        if self.has("equal", "c4", "c2") and not self.has("parallel", "sa7", "sa6"):
            self.set_parallel("sa7", "sa6")
            self.know_sa7()
            self.know_sa6()
            self.know_c2()
            self.know_c4()
        if self.has("equal", "c5", "c4") and not self.has("parallel", "sc7", "sa6"):
            self.set_parallel("sc7", "sa6")
            self.know_sc7()
            self.know_sa6()
            self.know_c5()
            self.know_c4()
        if self.has_3("sum_value", "a4", "c4", "90") and not self.has_right("b2"):
            self.set_right("b2")
            self.know_b2()
            self.know_a4()
            self.know_c4()
        if self.has_3("sum_value", "c4", "b2", "90") and not self.has_right("a4"):
            self.set_right("a4")
            self.know_a4()
            self.know_b2()
            self.know_c4()

        return 0

    def know_d4(self):
        #checks a pair of angles cumulating to 180 deg and sets angle to right if equal
        if self.has("equal", "c5", "d4") and not self.has_right("d4"):
            self.set_right("d4")
            self.know_d4()
        return 0

    # ############################  Areas  ##################################
    #                                                                       #
    # Areas 7 total                                                         #
    #                                                                       #
    #########################################################################
    def know_ar1(self):  # triangle a1,b1,c1
        #check similar by checking if any 2 angles of triangle match any 2 angles of anouther triangle
        if not self.has("similar", "ar1", "ar2"):
            my_triangle = ["a1", "b1", "c1"]
            their_triangle = ["a2", "b2", "c2"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar1", "ar2")
                self.know_ar1()
                self.know_ar2()
                self.know_a1()
                self.know_b1()
                self.know_c1()
                self.know_a2()
                self.know_b2()
                self.know_c2()
        if not self.has("similar", "ar1", "ar6"):
            my_triangle = ["a1", "b1", "c1"]
            their_triangle = ["a4", "b2", "c4"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar1", "ar6")
                self.know_ar1()
                self.know_ar6()
                self.know_a1()
                self.know_b1()
                self.know_c1()
                self.know_a4()
                self.know_b2()
                self.know_c4()
        if not self.has("similar", "ar1", "ar7"):
            my_triangle = ["a1", "b1", "c1"]
            their_triangle = ["a1", "b3", "c3"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar1", "ar7")
                self.know_ar1()
                self.know_ar7()
                self.know_a1()
                self.know_b1()
                self.know_c1()
                self.know_a1()
                self.know_b3()
                self.know_c3()
        if not self.has("congruent", "ar1", "ar2"):
            my_triangle = ["sa1", "sb1", "sc1"]
            their_triangle = ["sa2", "sb2", "sc2"]
            for i in range(3):
                repeat = False
                for my_side in my_triangle:
                    for their_side in their_triangle:
                        if self.has("equal", my_side, their_side):
                            my_triangle.remove(my_side)
                            their_triangle.remove(their_side)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 0:
                self.set_similar("ar1", "ar2")
                self.set_congruent("ar1", "ar2")
                self.know_ar1()
                self.know_ar2()
                self.know_sa1()
                self.know_sb1()
                self.know_sc1()
                self.know_sa2()
                self.know_sb2()
                self.know_sc2()
        return 0

    def know_ar2(self):  # triangle a2,b2,c2
        #check similar by checking if any 2 angles of triangle match any 2 angles of anouther triangle
        if not self.has("similar", "ar2", "ar1"):
            my_triangle = ["a2", "b2", "c2"]
            their_triangle = ["a1", "b1", "c1"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar2", "ar1")
                self.know_ar2()
                self.know_ar1()
                self.know_a2()
                self.know_b2()
                self.know_c2()
                self.know_a1()
                self.know_b1()
                self.know_c1()
        if not self.has("similar", "ar2", "ar6"):
            my_triangle = ["a2", "b2", "c2"]
            their_triangle = ["a4", "b2", "c4"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar2", "ar6")
                self.know_ar2()
                self.know_ar6()
                self.know_a2()
                self.know_b2()
                self.know_c2()
                self.know_a4()
                self.know_b2()
                self.know_c4()
        if not self.has("similar", "ar2", "ar7"):
            my_triangle = ["a2", "b2", "c2"]
            their_triangle = ["a1", "b3", "c3"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar2", "ar7")
                self.know_ar2()
                self.know_ar7()
                self.know_a2()
                self.know_b2()
                self.know_c2()
                self.know_a1()
                self.know_b3()
                self.know_c3()
        #check congruent by checking if all sides are equal to any other all sides
        if not self.has("congruent", "ar1", "ar2"):
            my_triangle = ["sa1", "sb1", "sc1"]
            their_triangle = ["sa2", "sb2", "sc2"]
            for i in range(3):
                repeat = False
                for my_side in my_triangle:
                    for their_side in their_triangle:
                        if self.has("equal", my_side, their_side):
                            my_triangle.remove(my_side)
                            their_triangle.remove(their_side)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 0:
                self.set_similar("ar1", "ar2")
                self.set_congruent("ar1", "ar2")
                self.know_ar1()
                self.know_ar2()
                self.know_sa1()
                self.know_sb1()
                self.know_sc1()
                self.know_sa2()
                self.know_sb2()
                self.know_sc2()

        return 0

    def know_ar3(self):  # trapizoid a3, b3, c3, d3
        #check similar by checking if any 3 angles of trapizoid match any 3 angles of anouther trapizoid
        if not self.has("similar", "ar3", "ar4"):
            my_trapazoid = ["a3", "b3", "c3", "d3"]
            their_trapazoid = ["a4", "b4", "c4", "d4"]
            for i in range(3):
                repeat = False
                for my_angle in my_trapazoid:
                    for their_angle in their_trapazoid:
                        if self.has("equal", my_angle, their_angle):
                            my_trapazoid.remove(my_angle)
                            their_trapazoid.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_trapazoid) == 1:
                self.set_similar("ar3", "ar4")
                self.know_ar3()
                self.know_ar4()
                self.know_sa3()
                self.know_sb3()
                self.know_sc3()
                self.know_sa4()
                self.know_sb4()
                self.know_sc4()
        #check congruent by checking if all sides are equal to any other all sides
        if not self.has("congruent", "ar3", "ar4"):
            my_trapazoid = ["sa3", "sb3", "sc3", "sd3"]
            their_trapazoid = ["sa4", "sb4", "sc4", "sd4"]
            for i in range(4):
                repeat = False
                for my_side in my_trapazoid:
                    for their_side in their_trapazoid:
                        if self.has("equal", my_side, their_side):
                            my_trapazoid.remove(my_side)
                            their_trapazoid.remove(their_side)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_trapazoid) == 0:
                self.set_similar("ar3", "ar4")
                self.set_congruent("ar3", "ar4")
                self.know_ar3()
                self.know_ar4()
                self.know_sa3()
                self.know_sb3()
                self.know_sc3()
                self.know_sa4()
                self.know_sb4()
                self.know_sc4()
        return 0

    def know_ar4(self):  # trapizoid a4, b4, c4, d4
        #check similar by checking if any 3 angles of trapizoid match any 3 angles of anouther trapizoid
        if not self.has("similar", "ar3", "ar4"):
            my_trapazoid = ["a3", "b3", "c3", "d3"]
            their_trapazoid = ["a4", "b4", "c4", "d4"]
            for i in range(3):
                repeat = False
                for my_angle in my_trapazoid:
                    for their_angle in their_trapazoid:
                        if self.has("equal", my_angle, their_angle):
                            my_trapazoid.remove(my_angle)
                            their_trapazoid.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_trapazoid) == 1:
                self.set_similar("ar3", "ar4")
                self.know_ar3()
                self.know_ar4()
                self.know_sa3()
                self.know_sb3()
                self.know_sc3()
                self.know_sa4()
                self.know_sb4()
                self.know_sc4()
        #check congruent by checking if all sides are equal to any other all sides
        if not self.has("congruent", "ar3", "ar4"):
            my_trapazoid = ["sa3", "sb3", "sc3", "sd3"]
            their_trapazoid = ["sa4", "sb4", "sc4", "sd4"]
            for i in range(4):
                repeat = False
                for my_side in my_trapazoid:
                    for their_side in their_trapazoid:
                        if self.has("equal", my_side, their_side):
                            my_trapazoid.remove(my_side)
                            their_trapazoid.remove(their_side)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_trapazoid) == 0:
                self.set_similar("ar3", "ar4")
                self.set_congruent("ar3", "ar4")
                self.know_ar3()
                self.know_ar4()
                self.know_sa3()
                self.know_sb3()
                self.know_sc3()
                self.know_sa4()
                self.know_sb4()
                self.know_sc4()
        return 0

    def know_ar6(self):  # triangle a4, b2, c4
        #check similar by checking if any 2 angles of triangle match any 2 angles of anouther triangle
        if not self.has("similar", "ar1", "ar6"):
            my_triangle = ["a1", "b1", "c1"]
            their_triangle = ["a4", "b2", "c4"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar1", "ar6")
                self.know_ar1()
                self.know_ar6()
                self.know_a1()
                self.know_b1()
                self.know_c1()
                self.know_a4()
                self.know_b2()
                self.know_c4()
        if not self.has("similar", "ar2", "ar6"):
            my_triangle = ["a2", "b2", "c2"]
            their_triangle = ["a4", "b2", "c4"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar2", "ar6")
                self.know_ar2()
                self.know_ar6()
                self.know_a2()
                self.know_b2()
                self.know_c2()
                self.know_a4()
                self.know_b2()
                self.know_c4()
        if not self.has("similar", "ar6", "ar7"):
            my_triangle = ["a4", "b2", "c4"]
            their_triangle = ["a1", "b3", "c3"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar6", "ar7")
                self.know_ar6()
                self.know_ar7()
                self.know_a4()
                self.know_b2()
                self.know_c4()
                self.know_a1()
                self.know_b3()
                self.know_c3()
        #check congruent by checking if all sides are equal to any other all sides
        if not self.has("congruent", "ar6", "ar7"):
            my_triangle = ["sa6", "sb6", "sc6"]
            their_triangle = ["sa7", "sb7", "sc7"]
            for i in range(3):
                repeat = False
                for my_side in my_triangle:
                    for their_side in their_triangle:
                        if self.has("equal", my_side, their_side):
                            my_triangle.remove(my_side)
                            their_triangle.remove(their_side)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 0:
                self.set_similar("ar6", "ar7")
                self.set_congruent("ar6", "ar7")
                self.know_ar6()
                self.know_ar7()
                self.know_sa6()
                self.know_sb6()
                self.know_sc6()
                self.know_sa7()
                self.know_sb7()
                self.know_sc7()
        return 0

    def know_ar7(self):  # triangle a1, b3, c3
        #check similar by checking if any 2 angles of triangle match any 2 angles of anouther triangle
        if not self.has("similar", "ar2", "ar1"):
            my_triangle = ["a2", "b2", "c2"]
            their_triangle = ["a1", "b1", "c1"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar2", "ar1")
                self.know_ar2()
                self.know_ar1()
                self.know_a2()
                self.know_b2()
                self.know_c2()
                self.know_a1()
                self.know_b1()
                self.know_c1()
        if not self.has("similar", "ar2", "ar7"):
            my_triangle = ["a2", "b2", "c2"]
            their_triangle = ["a1", "b3", "c3"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar2", "ar7")
                self.know_ar2()
                self.know_ar7()
                self.know_a2()
                self.know_b2()
                self.know_c2()
                self.know_a1()
                self.know_b3()
                self.know_c3()
        if not self.has("similar", "ar6", "ar7"):
            my_triangle = ["a4", "b2", "c4"]
            their_triangle = ["a1", "b3", "c3"]
            for i in range(2):
                repeat = False
                for my_angle in my_triangle:
                    for their_angle in their_triangle:
                        if self.has("equal", my_angle, their_angle):
                            my_triangle.remove(my_angle)
                            their_triangle.remove(their_angle)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 1:
                self.set_similar("ar6", "ar7")
                self.know_ar6()
                self.know_ar7()
                self.know_a4()
                self.know_b2()
                self.know_c4()
                self.know_a1()
                self.know_b3()
                self.know_c3()
        #check congruent by checking if all sides are equal to any other all sides
        if not self.has("congruent", "ar6", "ar7"):
            my_triangle = ["sa6", "sb6", "sc6"]
            their_triangle = ["sa7", "sb7", "sc7"]
            for i in range(3):
                repeat = False
                for my_side in my_triangle:
                    for their_side in their_triangle:
                        if self.has("equal", my_side, their_side):
                            my_triangle.remove(my_side)
                            their_triangle.remove(their_side)
                            repeat = True
                            break
                    if repeat:
                        break
            if len(my_triangle) == 0:
                self.set_similar("ar6", "ar7")
                self.set_congruent("ar6", "ar7")
                self.know_ar6()
                self.know_ar7()
                self.know_sa6()
                self.know_sb6()
                self.know_sc6()
                self.know_sa7()
                self.know_sb7()
                self.know_sc7()
        return 0

    # calls all know functions
    def call_knows(self):
        self.know_sa6()
        self.know_sb6()
        self.know_sc6()
        self.know_sa7()
        self.know_sb7()
        self.know_sc7()
        self.know_sa1()
        self.know_sb1()
        self.know_sc1()
        self.know_sa2()
        self.know_sb2()
        self.know_sc2()
        self.know_sa3()
        self.know_sb3()
        self.know_sc3()
        self.know_sd3()
        self.know_sa4()
        self.know_sb4()
        self.know_sc4()
        self.know_sd4()
        self.know_a1()
        self.know_b1()
        self.know_c1()
        self.know_a2()
        self.know_b2()
        self.know_c2()
        self.know_a3()
        self.know_b3()
        self.know_c3()
        self.know_d3()
        self.know_a4()
        self.know_b4()
        self.know_c4()
        self.know_d4()
        self.know_a5()
        self.know_b5()
        self.know_c5()
        self.know_d5()
        self.know_ar1()
        self.know_ar2()
        self.know_ar3()
        self.know_ar4()
        self.know_ar6()
        self.know_ar7()
        return 0

    def main(self):
        # inputs base predicates that are always true
        # Takes in three initial predicates
        # Ask user how many predicates they want to enter from 2 or 3
        x = 1
        while x == 1:
            num_ = input(
                "How many Predicates are you going to enter, or enter getall() to view all "
                "dictionaries or enter 0 to exit:")
            if num_ == "0":
                x = 0
                continue
            if num_ == "getall()":
                self.set_equal("a2", "b2")
                self.set_equal("c2", "a3")
                self.set_equal("d3", "d4")
                print("Parallel: " + str(self.parallel) + "\n"
                      + "Perpendicular: " + str(self.perpendicular) + "\n"
                      + "Equal: " + str(self.equal) + "\n"
                      + "Fraction: " + str(self.fraction) + "\n"
                      + "Sum Value: " + str(self.sum_value) + "\n"
                      + "Similar: " + str(self.similar) + "\n"
                      + "Congruent: " + str(self.congruent) + "\n"
                      + "Tan: " + str(self.tan))
                print("Right Angles: " + str(self.right))
                continue
            if num_ == "2":
                tmp_1 = input("Enter Two Predicates:\n")
                tmp_2 = input()
                predicate_1 = tmp_1.split("(")
                if predicate_1[0] == "set_tan":
                    self.tan.append("Null")
                if predicate_1[0] == "set_sum_value":
                    name_ = predicate_1[1].split(",")
                    name_1 = name_[2].split(")")
                    getattr(self, predicate_1[0])(name_[0], name_[1], name_1[0])
                elif predicate_1[0] == "set_fraction":
                    print("in set fraction")
                    name_ = predicate_1[1].split(",")
                    name_1 = name_[2].split(")")
                    name_1.pop(1)
                    getattr(self, predicate_1[0])(name_[0], name_[1], name_1[0])
                else:
                    name_ = predicate_1[1].split(",")
                    name_1 = name_[1].split(")")
                    name_1.pop(1)
                    getattr(self, predicate_1[0])(name_[0], name_1[0])
                predicate_2 = tmp_2.split("(")
                if predicate_2[0] == "set_tan":
                    self.tan.append("Null")
                if predicate_2[0] == "set_sum_value":
                    name_2 = predicate_2[1].split(",")
                    name_3 = name_2[2].split(")")
                    name_3.pop(1)
                    getattr(self, predicate_2[0])(name_2[0], name_2[1], name_3[0])
                elif predicate_2[0] == "set_fraction":
                    print("in set fraction")
                    name_2 = predicate_2[1].split(",")
                    name_3 = name_2[2].split(")")
                    name_3.pop(1)
                    getattr(self, predicate_2[0])(name_2[0], name_2[1], name_3[0])
                else:
                    name_2 = predicate_2[1].split(",")
                    name_3 = name_2[1].split(")")
                    name_3.pop(1)
                    getattr(self, predicate_2[0])(name_2[0], name_3[0])
            elif num_ == "3":
                tmp_1 = input("Enter Three Predicates:\n")
                tmp_2 = input()
                tmp_3 = input()
                predicate_1 = tmp_1.split("(")
                if predicate_1[0] == "set_tan":
                    self.tan.append("Null")
                if predicate_1[0] == "set_sum_value":
                    name_ = predicate_1[1].split(",")
                    name_1 = name_[2].split(")")
                    name_1.pop(1)
                    getattr(self, predicate_1[0])(name_[0], name_[1], name_1[0])
                elif predicate_1[0] == "set_fraction":
                    print("in set fraction")
                    name_ = predicate_1[1].split(",")
                    name_1 = name_[2].split(")")
                    name_1.pop(1)
                    getattr(self, predicate_1[0])(name_[0], name_[1], name_1[0])
                else:
                    name_ = predicate_1[1].split(",")
                    name_1 = name_[1].split(")")
                    name_1.pop(1)
                    getattr(self, predicate_1[0])(name_[0], name_1[0])
                predicate_2 = tmp_2.split("(")
                if predicate_2[0] == "set_tan":
                    self.tan.append("Null")
                if predicate_2[0] == "set_sum_value":
                    name_2 = predicate_2[1].split(",")
                    name_3 = name_2[2].split(")")
                    name_3.pop(1)
                    getattr(self, predicate_2[0])(name_2[0], name_2[1], name_3[0])
                elif predicate_2[0] == "set_fraction":
                    name_2 = predicate_2[1].split(",")
                    name_3 = name_2[2].split(")")
                    name_3.pop(1)
                    getattr(self, predicate_2[0])(name_2[0], name_2[1], name_3[0])
                else:
                    name_2 = predicate_2[1].split(",")
                    name_3 = name_2[1].split(")")
                    name_3.pop(1)
                    getattr(self, predicate_2[0])(name_2[0], name_3[0])
                predicate_3 = tmp_3.split("(")
                if predicate_3[0] == "set_tan":
                    self.tan.append("Null")
                if predicate_3[0] == "set_sum_value":
                    name_4 = predicate_3[1].split(",")
                    name_5 = name_4[2].split(")")
                    name_5.pop(1)
                    getattr(self, predicate_3[0])(name_4[0], name_4[1], name_5[0])
                elif predicate_3[0] == "set_fraction":
                    name_4 = predicate_3[1].split(",")
                    name_5 = name_4[2].split(")")
                    name_5.pop(1)
                    getattr(self, predicate_3[0])(name_4[0], name_4[1], name_5[0])
                else:
                    name_4 = predicate_3[1].split(",")
                    name_5 = name_4[1].split(")")
                    name_5.pop(1)
                    getattr(self, predicate_3[0])(name_4[0], name_5[0])
            self.call_knows()
            #report findings
            print("Parallel: " + str(self.parallel) + "\n"
                  + "Perpendicular: " + str(self.perpendicular) + "\n"
                  + "Equal: " + str(self.equal) + "\n"
                  + "Fraction: " + str(self.fraction) + "\n"
                  + "Sum Value: " + str(self.sum_value) + "\n"
                  + "Similar: " + str(self.similar) + "\n"
                  + "Congruent: " + str(self.congruent) + "\n"
                  + "Tan: " + str(self.tan))
            print("Right Angles: " + str(self.right))


test = MainClass()
test.main()
