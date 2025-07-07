using System;

class Solution
{
    static int AlternatingCharacters(string s)
    {
        int deletions = 0;
        for (int i = 1; i < s.Length; i++)
        {
            if (s[i] == s[i - 1])
                deletions++;
        }
        return deletions;
    }

    static void Main(string[] args)
    {
        int q = int.Parse(Console.ReadLine());
        for (int i = 0; i < q; i++)
        {
            string s = Console.ReadLine();
            int result = AlternatingCharacters(s);
            Console.WriteLine(result);
        }
    }
}
