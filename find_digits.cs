using System;

class Program
{
    static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        while (t-- > 0)
        {
            int n = int.Parse(Console.ReadLine());
            int count = 0, x = n;
            while (x > 0)
            {
                int d = x % 10;
                if (d != 0 && n % d == 0)
                    count++;
                x /= 10;
            }
            Console.WriteLine(count);
        }
    }
}
