using System;
using System.Text;

class Solution
{
    static string Encryption(string s)
    {
        //  vosluklari kaldir
        s = s.Replace(" ", "");
        int L = s.Length;

        //  satir ve sutun sayisini hesapla
        int rows = (int)Math.Floor(Math.Sqrt(L));   // karekokun altina yuvarla
        int cols = (int)Math.Ceiling(Math.Sqrt(L)); // karekokun ustune yuvarla
        if (rows * cols < L) rows++;                // yeterli degilse satiri artir

        //  gridi olustur
        string[] grid = new string[rows];
        for (int i = 0; i < rows; i++)
        {
            int start = i * cols;                               // baslangic indexi
            int length = Math.Min(cols, L - start);             // kalan karakter sayisi
            grid[i] = s.Substring(start, length);               // satir stringi 
        }

        // kolonları okuyarak sifreli metni olustur
        StringBuilder result = new StringBuilder();
        for (int c = 0; c < cols; c++)
        {
            if (c > 0) result.Append(" ");                      // kolonlar arasi bosluk ekle
            for (int r = 0; r < rows; r++)
            {
                if (c < grid[r].Length)                         // satirda bu kolon var mi?
                    result.Append(grid[r][c]);                  // varsa karakter eklicez
            }
        }
        return result.ToString();
    }

    static void Main()
    {
        // girdiyi oku ve sonucu yazdir
        string input = Console.ReadLine();
        Console.WriteLine(Encryption(input));
    }
}
