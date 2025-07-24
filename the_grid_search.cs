using System;

class Solution
{
    // GridSearch fonksiyonu: Deseni (P) grid (G) içinde arar
    static string GridSearch(string[] G, string[] P)
    {
        int R = G.Length;       // Number of rows in grid
        int C = G[0].Length;    // Number of columns in grid
        int r = P.Length;       // Number of rows in pattern
        int c = P[0].Length;    // Number of columns in pattern

        // Grid icinde tum olasi baslangic noktalarini deniyoruz YANİ pattern matrisini buyuk gridin icinde kaydirarak her olasi yerde ariyoruz....
        for (int i = 0; i <= R - r; i++)
        {
            for (int j = 0; j <= C - c; j++)
            {
                bool match = true;
                // Desenin her satirini kontrol et
                for (int k = 0; k < r; k++)
                {
                    // Grid'den substring al ve desen satiri ile karsilastir
                    if (G[i + k].Substring(j, c) != P[k])
                    {
                        match = false;
                        break;
                    }
                }
                // Eger tum satirlar eslesirse YES dondur
                if (match)
                    return "YES";
            }
        }
        // Hicbir eslesme yoksa NO dondur
        return "NO";
    }

    static void Main(string[] args)
    {
        // Test sayisini oku
        int t = int.Parse(Console.ReadLine().Trim());
        for (int test = 0; test < t; test++)
        {
            // Grid boyutlarini oku
            string[] gridDims = Console.ReadLine().Trim().Split();
            int R = int.Parse(gridDims[0]);
            int C = int.Parse(gridDims[1]);
            string[] G = new string[R];
            // Read grid rows
            for (int i = 0; i < R; i++)
                G[i] = Console.ReadLine().Trim();

            // Desen boyutlarini oku
            string[] patternDims = Console.ReadLine().Trim().Split();
            int r = int.Parse(patternDims[0]);
            int c = int.Parse(patternDims[1]);
            string[] P = new string[r];
            //  Sonucu ekrana yaz
            for (int i = 0; i < r; i++)
                P[i] = Console.ReadLine().Trim();

            // Output YES or NO
            Console.WriteLine(GridSearch(G, P));
        }
    }
}
