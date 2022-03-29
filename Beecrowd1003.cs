using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Beecrowd_1003
{
    internal class Beecrowd1003
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());

            int soma = SomarNumeros(a, b);
            Console.WriteLine($"SOMA = {soma}");

            Console.ReadLine();
        }
        public static int SomarNumeros(int x, int y)
        {
            return x + y;
        }
    }
}
