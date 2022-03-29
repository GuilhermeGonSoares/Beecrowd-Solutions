using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Beecrowd_1004
{
    internal class Beecrowd1004
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());

            var prod = a * b;
            Console.WriteLine($"PROD = {prod}");
            Console.ReadLine();
        }
    }
}
