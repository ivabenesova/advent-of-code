using System;
using System.IO;

class Program
{
    static void Main()
    {
        string filePath = @"data/15.txt";
        int total_sum = 0;
        try
        {
            string[] lines = File.ReadAllLines(filePath);

            foreach (string line in lines)
            {
                // Split the line by comma
                string[] expressions = line.Split(',');

                foreach (string expression in expressions)
                {
                    int total_value = 0;
                    if (expression.Length > 0)
                    {
                        string processedExpression = expression.Replace("\\n", "\n").Replace("\\t", "\t").Replace("\\r", "\r");
                        foreach (int letter in expression)
                        {
                            total_value += letter;
                            total_value = (total_value * 17) % 256;
                        }
                        total_sum += total_value;
                    }
                }
                Console.WriteLine(total_sum);
            }
        }
        catch (Exception e)
        {
            Console.WriteLine("An error occurred:");
            Console.WriteLine(e.Message);
        }
    }
}




