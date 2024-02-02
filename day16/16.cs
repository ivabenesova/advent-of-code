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
        {
            case '.':
                new_dir.Add(dict_direction[dir_index]);
                break;
            case '/':
                {
                    if ((direction == 'e') || (direction == 'w'))
                    {
                        new_dir.Add(dict_direction[(dir_index + 3) % 4]);
                    }
                    else
                    {
                        new_dir.Add(dict_direction[(dir_index + 1) % 4]);
                    }
                }
                break;
            case '\\':
                {
                    if ((direction == 'e') || (direction == 'w'))
                    {
                        new_dir.Add(dict_direction[(dir_index + 1) % 4]);
                    }
                    else
                    {
                        new_dir.Add(dict_direction[(dir_index + 3) % 4]);
                    }
                }
                break;
            case '-':
                {
                    if ((direction == 'e') || (direction == 'w'))
                    {
                        new_dir.Add(dict_direction[dir_index]);
                    }
                    else
                    {
                        new_dir.Add(dict_direction[(dir_index + 1) % 4]);
                        new_dir.Add(dict_direction[(dir_index + 3) % 4]);
                    }
                    break;
                }
            case '|':
                {
                    if ((direction == 's') || (direction == 'n'))
                    {
                        new_dir.Add(dict_direction[dir_index]);
                    }
                    else
                    {
                        new_dir.Add(dict_direction[(dir_index + 1) % 4]);
                        new_dir.Add(dict_direction[(dir_index + 3) % 4]);
                    }
                    break;

                }
        }
        return new_dir;
    }


    public static int[] NextPos(char direction, int[] position)
    {
        switch (direction)
        {
            case 'e':
                {
                    position[1] += +1;
                    break;
                }
            case 'w':
                {
                    position[1] -= 1;
                    break;
                }
            case 'n':
                {
                    position[0] -= 1;
                    break;
                }

            case 's':
                {
                    position[0] += 1;
                    break;
                }
        }

        return (position);
    }


    static void Main(string[] args)
    {
        string filePath = @"data/16.txt";

        string[] lines = File.ReadAllLines(filePath);

        int lineLength = lines[0].Length;

        char[,] energized = Create_array(lines.Length, lineLength);
        energized[0, 0] = '#';

        List<int> energy = new List<int>();
        int energySum;

        int[] position = new int[2] { 0, 0 };

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

            for (int i = 0; i < directions.Count; i++)
            {
                char symbol = lines[positions[i][0]][positions[i][1]];
                List<char> results = NextDirections(symbol, directions[i]);

                foreach (char val in results)
                {
                    try
                    {
                        int[] pos = { positions[i][0], positions[i][1] };
                        List<int[]> assignedPos = new List<int[]>();
                        int[] new_pos = NextPos(val, pos);
                        energized[new_pos[0], new_pos[1]] = '#';
                        nextpos.Add(new_pos);
                        nextdir.Add(val);
                    }
                    catch (Exception)
                    {
                    }
                }
            }
            positions = new List<int[]>(nextpos);
            directions = new List<char>(nextdir);

            energySum = 0;

            for (int y = 0; y < lines.Length; y++)
            {
                for (int x = 0; x < lineLength; x++)
                {
                    if (energized[y, x] == '#')
                    {
                        energySum += 1;

                    }
                }
            }

            energy.Add(energySum);

            if (energy.Count >= 10)
            {
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
        }

        int res = 0;

        for (int yy = 0; yy < lines.Length; yy++)
        {
            for (int xx = 0; xx < lineLength; xx++)
            {
                if (energized[yy, xx] == '#')
                {
                    res += 1;
                }
            }
        }
        Console.WriteLine(res);
    }
}

// part2 TBD