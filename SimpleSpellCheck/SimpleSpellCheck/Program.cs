using System;

namespace SimpleSpellCheck
{
    internal class Program
    {
        
        public int MED(int i, int j)
        {
            if (i == 0)
                return j;
            if (j == 0)
                return i;
            return Math.Min((uint) (MED(i - 1, j) + 1), (uint)MED(i, j - 1) + 1, (uint)MED(i - 1, j - 1));
        }
        public static void Main(string[] args)
        {
            A = " igigig";
            B = " gigigi";
        }

        public static string A { get; set; }
        public static string B { get; set; }
    }
}