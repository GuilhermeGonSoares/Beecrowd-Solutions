using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Beecrowd_1006
{
    internal class Beecrowd1006
    {
        static void Main(string[] args)
        {   
            var a = double.Parse(Console.ReadLine());
            var b = double.Parse(Console.ReadLine());
            var c = double.Parse(Console.ReadLine());


            var media = MediaPonderada(a, b, c);
            Console.WriteLine($"MEDIA = {media.ToString("0.0")}");

            Console.ReadLine();
        }
        static double MediaPonderada(double a, double b, double c)
        {
            return (a * 2 + b * 3 + c * 5)/(10.0);
        }
    }
}
