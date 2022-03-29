using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Beecrowd_1008
{
    internal class Beecrowd1008
    {
        static void Main(string[] args)
        {
            int numero = int.Parse(Console.ReadLine());
            int horas = int.Parse(Console.ReadLine());
            double salario = double.Parse(Console.ReadLine());

            Console.WriteLine($"NUMBER = {numero}");
            Console.WriteLine($"SALARY = U$ {(salario * horas).ToString("0.00")}");

            Console.ReadLine();
        }
    }
}
