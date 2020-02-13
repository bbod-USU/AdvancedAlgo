using System;
using System.CodeDom;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Xml.Schema;

namespace DNA_Alignment
{
    internal class Program
    {
        /// <summary>
        /// Cost Matrix
        /// </summary>
        static readonly int[,] AlignmentMatrix =
            new int[5, 5] {
                {5, -1, -2, -1, -3}, 
                {-1, 5, -3, -2, -4},
                {-2, -3, 5, -2, -2}, 
                {-1, -2, -2, 5, -1}, 
                {-3, -4, -2, -1, 0}
            };
        /// <summary>
        /// Letter LookUP
        /// </summary>
        static readonly Dictionary<char, int> LetterLookUp=
            new Dictionary<char, int>
            {
                {'a', 0},
                {'c', 1},
                {'g', 2},
                {'t', 3},
                {'-', 4}
            };
        
        /// <summary>
        /// Calculates the chage  score given two chars.
        /// </summary>
        /// <param name="i"></param>
        /// <param name="j"></param>
        /// <returns></returns>
        private static int score(char i, char j)
        {
            return AlignmentMatrix[LetterLookUp[i], LetterLookUp[j]];
        }
        /// <summary>
        /// takes a string and reverses it.
        /// </summary>
        /// <param name="s"></param>
        /// <returns></returns>
        private static string ReverseString(string s)
        {
            char[] arr = s.ToCharArray();
            Array.Reverse(arr);
            return new string(arr);
        }
        
        /// <summary>
        /// Takes M and reverses the process.
        /// </summary>
        /// <param name="M"></param>
        /// <param name="writeFile"></param>
        /// <param name="score"></param>
        /// <returns></returns>
        private static Tuple<string, string> Traceback(int[,] M, string writeFile, string score)
        {
            var xAlign = "";
            var yAlign = "";
            var i = A.Length;
            var j = B.Length;
            var r = new List<string>();
            r.Add(score);

            while (i > 0 || j > 0)
            {
                var up = M[i - 1, j];
                var left = M[i, j - 1];
                var diag = M[i - 1, j - 1];
                if (i > 0 && up == Math.Max(Math.Max(up, left), diag))//up
                {
                    r.Add($"{A[i - 1]} => -");
                //    Console.WriteLine(A[j - 1]+" => -");

                    xAlign += A[i - 1];
                    yAlign += '-';
                    i -= 1;
                }
                else if (j > 0 && left == Math.Max(Math.Max(up, left), diag))//left
                {
                    r.Add($"- => {B[j - 1]}");
                 //   Console.WriteLine("- => "+B[i - 1]);

                    xAlign += '-';
                    yAlign += B[j - 1];
                    j -= 1;
                }else//diag
                {
                    r.Add($"{A[i - 1]} = {B[j - 1]}");
                 //   Console.WriteLine(A[j - 1]+" = "+B[i - 1]);
                    xAlign += A[i - 1];
                    yAlign += B[j - 1];
                    i -= 1;
                    j -= 1;
                }
            }
            File.WriteAllLines(writeFile, r);
            //reverse the strings
            xAlign = ReverseString(xAlign);
            yAlign = ReverseString(yAlign);
            return new Tuple<string, string>(xAlign, yAlign);
        } 

        /// <summary>
        /// Creates the array M
        /// </summary>
        /// <returns></returns>
        private static int[,] DPmed()
        {
            var m = A.Length+1;
            var n = B.Length+1;
            var M = new int [m, n];

            for (var x = 1; x < m; x++)
            {
                M[x, 0] = M[x-1, 0] + AlignmentMatrix[LetterLookUp[A[x-1]], LetterLookUp['-']];
            }

            for (var y = 1; y < n; y++)
            {
                M[0, y] = M[0, y-1] + AlignmentMatrix[LetterLookUp['-'], LetterLookUp[B[y-1]]];
            }

            for (var x = 1; x < m; x++)
            {
                for (var y = 1; y < n; y++)
                {
                    //sets up the cache
                    M[x, y] = Math.Max(Math.Max(M[x-1, y-1] + score(A[x - 1], B[y - 1]),
                            M[x-1, y] + score(A[x-1], '-')),
                        M[x, y-1] + score('-', B[y-1]));
                }
            }

            return M;
        }




        public static void Main(string[] args)
        {
            // Debug mode from ../DNA_Alignment/bin/Debug/
            // Release mode from ../DNA_Alignment/bin/Release/
            var f1 = File.ReadAllText(Path.Combine(Environment.CurrentDirectory, args[0]));
            var f2 = File.ReadAllText(Path.Combine(Environment.CurrentDirectory, args[1]));
            A = Regex.Replace(f1, @"(\r\n|\r|\n)|n|[ ]|[1234567890]", "");
            B = Regex.Replace(f2, @"(\r\n|\r|\n)|n|[ ]", "");
            var M = DPmed();
            var writeFile = Path.Combine(Environment.CurrentDirectory, $"{args[0]}_vs_{args[1]}.txt");
            Console.WriteLine("Score: " + M[A.Length,B.Length]);
            var results = Traceback(M, writeFile, $"Score: {M[A.Length,B.Length].ToString()}");
            
            
        }
        
        /// <summary>
        /// String 1
        /// </summary>
        public static string A { get; set; }
        
        /// <summary>
        /// String 2
        /// </summary>
        public static string B { get; set; }
    }
}