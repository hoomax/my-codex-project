using System;
using CalculatorLib;

namespace CalculatorConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length != 3)
            {
                Console.WriteLine("Usage: dotnet run <add|sub|mul|div> <a> <b>");
                return;
            }

            var calc = new Calculator();
            double a = double.Parse(args[1]);
            double b = double.Parse(args[2]);
            double result = args[0] switch
            {
                "add" => calc.Add(a, b),
                "sub" => calc.Subtract(a, b),
                "mul" => calc.Multiply(a, b),
                "div" => calc.Divide(a, b),
                _ => throw new ArgumentException("Unknown operation")
            };

            Console.WriteLine(result);
        }
    }
}
