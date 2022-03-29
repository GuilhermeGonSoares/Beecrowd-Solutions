using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Beecrowd_2766
{
    internal class Beecrowd2766
    {
        static void Main(string[] args)
        {

            for(int i = 0; i < 10; i++)
            {
                string nome = Console.ReadLine();
                if (i == 2 || i == 6 || i == 8)
                {
                 
                    Console.WriteLine(nome);
                }
            }

            Console.ReadLine();

        }
    }
}
