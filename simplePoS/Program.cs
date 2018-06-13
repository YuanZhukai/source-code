using System;
using System.Collections.Generic;

namespace pofPrototype
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            for (int i = 0; i < 2; i++)
            {
                //create the simController telling it the number of peer nodes
                //and the total latency between nodes
                simController sc = new simController(2, 20);

                //run the simulation by telling it the number of transactions
                sc.runSimulation(10);
                sc.report();
            }
        }
    }
}