using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Beecrowd_2554
{
    internal class Beecrowd2554
    {
        static void Main(string[] args)
        {
            while (true)
            {
                string entrada = Console.ReadLine();
                if (string.IsNullOrEmpty(entrada)) break;
                string[] testes = entrada.Split(' ');

                bool dataValida = false;
                for (int i = 0; i < int.Parse(testes[1]); i++)
                {
                    string[] dataPresenca = Console.ReadLine().Split(' ');
                    int contador = 0;
                    for(int pos = 1; pos <= int.Parse(testes[0]) && !dataValida; pos++)
                    {
                        if (int.Parse(dataPresenca[pos]) == 1) contador++;
 
                        else break;
                    }
                    if (contador == int.Parse(testes[0])){
                        dataValida = true;
                        Console.WriteLine(dataPresenca[0]);
                    }
                }
                if (!dataValida) Console.WriteLine("Pizza antes de FdI");

            }

        }
    }
}
