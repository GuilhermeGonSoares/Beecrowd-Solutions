using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Beecrowd_2949
{
    internal class Beecrowd2949
    {
        static void Main(string[] args)
        {
   
           int numeroDePessoas = int.Parse(Console.ReadLine());

            var raca = new Dictionary<string, int>()
            {
                { "A", 0},
                { "E", 0},
                { "H", 0},
                { "M", 0},
                { "X", 0}
            };

            for(int i = 0; i < numeroDePessoas; i++)
            {
                string[] entrada = Console.ReadLine().Split(' ');
                var tipoDaRaca = entrada[1];
                raca[tipoDaRaca]++;
            }
            Console.WriteLine($"{raca["X"]} Hobbit(s)");
            Console.WriteLine($"{raca["H"]} Humano(s)");
            Console.WriteLine($"{raca["E"]} Elfo(s)");
            Console.WriteLine($"{raca["A"]} Anao(s)");
            Console.WriteLine($"{raca["M"]} Mago(s)");

        }
    }
}
