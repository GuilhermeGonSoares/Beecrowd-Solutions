using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Beecrowd_2143
{
    internal class Beecrowd2143
    {

        static void Main(string[] args)
        {
            int t = -1;

            while(t != 0)
            {
                t = int.Parse(Console.ReadLine());
                for(int i = 0; i < t; i++)
                {
                    int pedidos = 0;
                    int quantidadeDePessoas = int.Parse(Console.ReadLine());
                    if (VerificarPar(quantidadeDePessoas))
                    {
                        pedidos += 2 + (quantidadeDePessoas - 2) * 2;
                    }
                    else
                    {
                        pedidos += 1 + (quantidadeDePessoas - 1) * 2;
                    }
                    Console.WriteLine(pedidos);
                }
            }
        }
        static bool VerificarPar(int n)
        {
            if (n % 2 == 0) return true;
            return false;
        }
    }
}
