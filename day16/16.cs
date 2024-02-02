using System.Diagnostics.CodeAnalysis;
using System.Linq.Expressions;

namespace day16;

class Program
{
    public static char[,] Create_array(int a, int b)
    { 
        char[,] new_array = new char[a, b];
        for (int i = 0; i < a; i++)
        {
            for (int j = 0; j < b; j++)
            {
            new_array[i, j] = '.';
            }
        }
    return new_array;
    }

    public static List<char> NextDirections(char symbol, char direction)
    {
        Dictionary<int, char> dict_direction = new Dictionary<int, char>();
                dict_direction[0] = 'n';
                dict_direction[1] = 'e';
                dict_direction[2] = 's';
                dict_direction[3] = 'w';

        List<char> new_dir = new List<char>();

        int dir_index = 0;
                
        foreach (var dir in dict_direction)
        {
            if (dir.Value == direction)
            {
                dir_index = dir.Key;
                break; 
            }
        }
                
            switch (symbol)
            {case '.':
                new_dir.Add(dict_direction[dir_index]);
                break;
            case '/':
                  {
                    if ((direction == 'e') || (direction == 'w'))
                    {
                        new_dir.Add(dict_direction[(dir_index+3)%4]);
                    }
                    else
                    {
                        new_dir.Add(dict_direction[(dir_index+1)%4]); 
                    }
                }
                break;
            case '\\':
                {
                    if ((direction == 'e') || (direction == 'w'))
                    {
                        new_dir.Add(dict_direction[(dir_index+1)%4]);
                    }
                    else
                    {
                        new_dir.Add(dict_direction[(dir_index+3)%4]); 
                    }
                }
                break;
            case '-':
                {if ((direction == 'e') || (direction == 'w'))
                {
                    new_dir.Add(dict_direction[dir_index]);
                }
                else
                {
                    new_dir.Add(dict_direction[(dir_index+1)%4]);
                    new_dir.Add(dict_direction[(dir_index+3)%4]);
                }
                break;
                }
            case '|':
                {if ((direction == 's') || (direction == 'n'))
                {
                    new_dir.Add(dict_direction[dir_index]);
                }
                else
                {
                    new_dir.Add(dict_direction[(dir_index+1)%4]);
                    new_dir.Add(dict_direction[(dir_index+3)%4]);
                }
                break;
                  
                }
            }
        return new_dir;
    }



    /*public static (List<int[,]>, List<char>) move(List<int[,]> positions, List<char> directories)
    { 
        
        
    return (newPositions, newDirectories);
    } */
    


    static void Main(string[] args)
    {
        string filePath = @"data/16.txt";
        string[] lines = File.ReadAllLines(filePath);

        int lineLength = lines[0].Length;
       
        char[,] energized = Create_array(lines.Length, lineLength);
        energized[0,0] = '#';

        List<int> energy = new List<int>();
        int energySum;


        // start
        int[] position = new int[2] {0,0};
        List<int[]> positions = new List<int[]>();
        positions.Add(position);
        
        char direction = 'e';
        List<char> directions = new List<char>();
        directions.Add(direction);

        bool finish = false;
        List<char> nextdir = new List<char>();
        List<int[]> nextpos = new List<int[]>();



        while (finish == false)
        { 
        nextdir.Clear(); 
        nextpos.Clear();

        // iterujeme listy directories/positions
        for (int i = 0; i < directions.Count ; i ++)  
            {
                // next directions
                char symbol = lines[positions[i][0]][positions[i][1]];
                List<char> results = NextDirections(symbol, directions[i]);    

                foreach (char val in results)
                
                    try
                    {
                    switch (val) 
                    {
                        case 'e':
                            {
                                int[] pos = {positions[i][0], positions[i][1] + 1};
                                energized[pos[0], pos[1]] = '#';
                                nextpos.Add(pos);
                                nextdir.Add(val);
                                break;
                            }
                        case 'w':
                            {
                                int[] pos = {positions[i][0], positions[i][1] - 1};
                                energized[pos[0], pos[1]] = '#';
                                nextpos.Add(pos);
                                nextdir.Add(val);
                                break;
                            }
                        case 'n':
                            {
                                int[] pos = {positions[i][0] - 1, positions[i][1]};
                                energized[pos[0], pos[1]] = '#';
                                nextpos.Add(pos);
                                nextdir.Add(val);
                                break;
                            }
                           
                        case 's':
                            {   
                                int[] pos = {positions[i][0] + 1, positions[i][1]};
                                energized[pos[0], pos[1]] = '#';
                                nextpos.Add(pos);
                                nextdir.Add(val);
                                break;
                            }
                    
                    }
                    }
                    catch (Exception ex)
                        {
                        Console.WriteLine("out of map");
                        }
                }    
                   
               
            positions = new List<int[]>(nextpos);
            directions = new List<char>(nextdir); 
            
            energySum = 0;

            for (int y = 0; y < lines.Length; y ++ )
                {
                for (int x = 0; x < lineLength; x ++ )
                {
                    if (energized[y, x] == '#')
                        {energySum += 1;
                }
                }
                }

            energy.Add(energySum);
            
           

            if (energy.Count >= 10)
            {             
                Console.WriteLine("here");

                var last10 = energy.GetRange(energy.Count - 10, 10);
                bool allSame = true;

                for (int e = 1; e < last10.Count; e++)
                {
                    if (last10[e] != last10[0])
                    {
                        allSame = false;
                        break; 
                        
                    }
                }

                if (allSame)
                {
                    finish = true;
                }

            }
            Console.WriteLine(finish);

     }

    // write array in Console
    for (int c = 0; c < lines.Length; c ++ )
    {
        for (int d = 0; d < lineLength; d ++ )
        {
            Console.Write(energized[c, d]);
        }
        Console.WriteLine();

     }
    int res = 0;

    for (int yy = 0; yy < lines.Length; yy ++ )
        {
        for (int xx = 0; xx < lineLength; xx ++ )
        {
            if (energized[yy, xx] == '#')
                {res += 1;
        }
        }
        }
        Console.WriteLine(res);

    }
    }

// part2 TBA