import time
import problemGenerator
import highSchool
import divideConcur

def main():
    count = 32
    power = 0
    while True:
        highTime = 0
        dcTime = 0
        highTimeStart = 0
        dcTimeStart = 0
        for i in range(0, 10):
            P = problemGenerator.GenerateProblem(count)
            Q = problemGenerator.GenerateProblem(count)
            highTimeStart = time.time()
            highSchool.HighSchool(count, P, Q)
            highTime += (time.time()-highTimeStart)

            dcTimeStart = time.time()
            divideConcur.DivideConcur(count, P, Q)
            dcTime += (time.time()-dcTimeStart)
            print(i)

        print("Highschool Time: ", highTime/10)
        print("DC Time: ", dcTime/10)
        saveArray = [count, highTime/10, dcTime/10]
        print(saveArray)
        with open("results.txt", "a") as myfile:
            print(str(saveArray), file=myfile)
            myfile.flush()
        count += count
        myfile.close()

main()