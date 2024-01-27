// See https://aka.ms/new-console-template for more information

/* The HASH algorithm is a way to turn any string of characters into a single number in the range 0 to 255. To run the HASH algorithm on a string, start with a current value of 0. Then, for each character in the string starting from the beginning:

Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.
After following these steps for each character in the string in order, the current value is the output of the HASH algorithm. */

//my first C# task!

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
                        total_value = (total_value *17) % 256;
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




