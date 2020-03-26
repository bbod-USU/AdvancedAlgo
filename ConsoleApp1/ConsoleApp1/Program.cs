using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        private static readonly Random random = new Random();

        static void Main(string[] args)
        {

            Console.WriteLine("Hello Austin!");
            Console.WriteLine("Do Your Math...You can't cheat now. HAHAHA");
            var multiplicaiton = MakeRandomNumbers(10, 10);
            var addition = MakeRandomNumbers(10, 50);
            var subtraction = MakeRandomNumbers(10, 50);
            var ltgt = MakeRandomNumbers(20, 100);
            var algebra = MakeRandomNumbers(10, 10);
            SolveMultiplicationProblems(multiplicaiton);
            SolveAdditionProblems(addition);
            SolveSubtractionProblems(subtraction);
            SolveLTGTProblems(ltgt);
            SolveAlgebraProblems(algebra);




            Console.WriteLine("Austin Finished His Math Like A BOSS!!!");
        }


        private static List<Tuple<int, int>> MakeRandomNumbers(int count, int maxNum)
        {
            var rList = new List<Tuple<int, int>>();
            for (var i = 0; i < count; i++)
            {
                var value = random.Next(0, maxNum);
                var value2 = random.Next(0, maxNum);
                rList.Add(new Tuple<int, int>(value, value2));
            }

            return rList;
        }

        private static void SolveMultiplicationProblems(List<Tuple<int, int>> multiplicaiton)
        {
            var cArray = new bool[multiplicaiton.Count];
            while (cArray.Count(x => x == false) != 0)
            {
                foreach (var t in multiplicaiton)
                {
                    if (cArray[multiplicaiton.IndexOf(t)])
                        continue;
                    Console.WriteLine($"Solve {t.Item1}x{t.Item2}=");

                    Int32.TryParse(Console.ReadLine(), out int input);
                    if (input == t.Item1 * t.Item2)
                    {
                        cArray[multiplicaiton.IndexOf(t)] = true;
                        Console.WriteLine();
                    }
                    else
                    {
                        Console.WriteLine("Wrong Answer!");
                        Console.WriteLine();
                    }
                }
            }

        }

        private static void SolveAdditionProblems(List<Tuple<int, int>> addition)
        {
            var cArray = new bool[addition.Count];
            while (cArray.Count(x => x == false) != 0)
            {
                foreach (var t in addition)
                {
                    if (cArray[addition.IndexOf(t)])
                        continue;
                    Console.WriteLine($"Solve {t.Item1}+{t.Item2}=");
                    Int32.TryParse(Console.ReadLine(), out int input);
                    if (input == t.Item1 + t.Item2)
                        cArray[addition.IndexOf(t)] = true;
                    else
                    {
                        Console.WriteLine("Wrong Answer!");
                        Console.WriteLine();
                    }
                }
            }
        }

        private static void SolveSubtractionProblems(List<Tuple<int, int>> subtraction)
        {
            var cArray = new bool[subtraction.Count];
            while (cArray.Count(x => x == false) != 0)
            {
                foreach (var t in subtraction)
                {
                    if (cArray[subtraction.IndexOf(t)])
                        continue;
                    Console.WriteLine(t.Item1 > t.Item2
                        ? $"Solve {t.Item1}-{t.Item2}="
                        : $"Solve {t.Item2}-{t.Item1}=");

                    Int32.TryParse(Console.ReadLine(), out int input);
                    if (input == Math.Abs(t.Item1 - t.Item2))
                    {
                        cArray[subtraction.IndexOf(t)] = true;
                        Console.WriteLine();

                    }
                    else
                    {
                        Console.WriteLine("Wrong Answer!");
                        Console.WriteLine();

                    }
                }
            }
        }




        private static void SolveLTGTProblems(List<Tuple<int, int>> ltgt)
        {
            var cArray = new bool[ltgt.Count];
            while (cArray.Count(x => x == false) != 0)
            {
                foreach (var t in ltgt)
                {
                    if (cArray[ltgt.IndexOf(t)])
                        continue;
                    var rand = random.Next(100);
                    var max = Math.Max(t.Item1, t.Item2);
                    if (rand % 2 == 1)
                    {
                        Console.WriteLine($"(1 is true 0 is false) Solve: {t.Item1} >= {t.Item2}");
                        int.TryParse(Console.ReadLine(), out var ans);
                        if (t.Item1 == max)
                        {
                            if (ans != 1) continue;
                            cArray[ltgt.IndexOf(t)] = true;
                            Console.WriteLine();
                        }
                        else if (t.Item2 == max)
                        {
                            if (ans != 0) continue;
                            cArray[ltgt.IndexOf(t)] = true;
                            Console.WriteLine();
                        }
                        else
                        {
                            Console.WriteLine("Wrong Answer!");
                            Console.WriteLine();
                        }
                    }
                    else
                    {
                        Console.WriteLine($"(1 is true 0 is false) Solve: {t.Item1} <= {t.Item2}");
                        int.TryParse(Console.ReadLine(), out var ans);
                        if (t.Item2 == max)
                        {
                            if (ans != 1) continue;
                            cArray[ltgt.IndexOf(t)] = true;
                            Console.WriteLine();
                        }
                        else if (t.Item1 == max)
                        {
                            if (ans != 0) continue;
                            cArray[ltgt.IndexOf(t)] = true;
                            Console.WriteLine();
                        }
                        else
                        {
                            Console.WriteLine("Wrong Answer!");
                            Console.WriteLine();

                        }
                    }

                }
            }
        }
        private static void SolveAlgebraProblems(List<Tuple<int, int>> algebra)
        {
            var cArray = new bool[algebra.Count];
            while (cArray.Count(x => x == false) != 0)
            {
                foreach (var t in algebra0
                )
                {
                    if (cArray[algebra.IndexOf(t)])
                        continue;
                    var multiplier = random.Next(10);
                    Console.WriteLine($"Solve for x: {t.Item1}x = {t.Item1*multiplier}");
                    int.TryParse(Console.ReadLine(), out var ans);
                    if (ans == multiplier)
                    {
                        cArray[algebra.IndexOf(t)] = true;
                        Console.WriteLine();
                    }
                    else
                    {
                        Console.WriteLine("Wrong Answer!");
                        Console.WriteLine();
                    }

                }
            }
        }
    }
}