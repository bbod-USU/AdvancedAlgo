import time
import problemGenerator
import highSchool
import divideConcur
import ThreeDivideConcur

def main():
    count = 32
    power = 0
    while True:
        highTime = 0
        dcTime = 0
        highTimeStart = 0
        dcTimeStart = 0
        tpTimeStart = 0
        tpTime = 0
        for i in range(0, 10):
            P = problemGenerator.GenerateProblem(count)
            Q = problemGenerator.GenerateProblem(count)
            highTimeStart = time.time()
            highSchool.HighSchool(count, P, Q)
            highTime += (time.time()-highTimeStart)

            dcTimeStart = time.time()
            divideConcur.DivideConcur(count, P, Q)
            dcTime += (time.time()-dcTimeStart)

            tpTimeStart = time.time()
            ThreeDivideConcur.threeDivideConcur(count, P, Q)
            tpTime += (time.time()-tpTimeStart)

        saveArray = [count, highTime, dcTime, tpTime]
        with open("results.txt", "a") as myfile:
            print(str(saveArray), file=myfile)
            myfile.flush()
        count += count
        print("done")
        myfile.close()

main()