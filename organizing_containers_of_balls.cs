using System;

class Solution
{
    static string organizingContainers(int[][] container)
    {
        int n = container.Length;
        int[] rowSum = new int[n];
        int[] colSum = new int[n];
        for (int i = 0; i < n; i++)
        {
            rowSum[i] = 0;
            colSum[i] = 0;
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                rowSum[i] += container[i][j];
                colSum[j] += container[i][j];
            }
        }
        Array.Sort(rowSum);
        Array.Sort(colSum);
        for (int i = 0; i < n; i++)
        {
            if (rowSum[i] != colSum[i])
                return "Impossible";
        }
        return "Possible";
    }

    static void Main()
    {
        string line = Console.ReadLine();
        int q = int.Parse(line);
        for (int t = 0; t < q; t++)
        {
            int n = int.Parse(Console.ReadLine());
            int[][] container = new int[n][];
            for (int i = 0; i < n; i++)
            {
                string[] parts = Console.ReadLine().Split(' ');
                container[i] = new int[n];
                for (int j = 0; j < n; j++)
                    container[i][j] = int.Parse(parts[j]);
            }
            string result = organizingContainers(container);
            Console.WriteLine(result);
        }
    }
}
