class Universty : 


    def humans (self ):
        print("universty students ") 
        print("universty teachers ")

    def faculty  (self,x,y  ):
        print("teachers ",x )
        print("students",y)

   
    def students_timings_1_7  (self):
        studentnames:list [str] = [ "meerab", "minahil" , "areesha" ,"hamza" ,"ali" ,"iqra" ]
        print("students timing from 1_7 ", studentnames)
    

    def classes_from_2_6 (self):
        teachers:list [str] = ["dr amin ", "dr tariq ", "dr khalid "]
        st:list [str] = ["sulsabeel","haram","annaya ","mobin"]
        print("teachers list from 2_6 ", teachers )
        print("students list from 2_6  ", st)

alpa = Universty ()
alpa.humans()
alpa.faculty (10,20)

alpa.students_timings_1_7()
alpa.classes_from_2_6()                                                                                                                                        