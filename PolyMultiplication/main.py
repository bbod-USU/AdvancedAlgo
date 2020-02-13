import time
import problemGenerator
import highSchool
import divideConcur

def main():
    count = 1
    while True:
        highTime = 0
        dcTime = 0
        highTimeStart = 0
        dcTimeStart = 0
        for i in range(0, 10):
            P = problemGenerator.GenerateProblem(count)
            Q = problemGenerator.GenerateProblem(count)
            highTimeStart = time.time()
            highSchool.HighSchool(count*32, P, Q)
            highTime+=(time.time()-highTimeStart)

            dcTimeStart = time.time()
            divideConcur.DivideConcur(count*32, P, Q)
            dcTime+=(time.time()-dcTimeStart)
            print(i)
        count += 1
        print("Highschool Time: ", highTime/10)
        print("DC Time: ", dcTime/10)

main()