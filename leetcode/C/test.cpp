#include <stdio.h>
class Solution
{
public:
    int maximum69Number(int num)
    {
        int w[4] = {0};
        for (int i = 0; i < 4; i++)
        {
            w[i] = num % 10;
            num = num / 10;
        }
        for (int i = 3; i >= 0; i--)
        {
            if (w[i] == 6)
            {
                w[i] = 9;
                break;
            }
        }
        int result = w[3];
        for (int i = 2; i >= 0; i--)
        {
            result = result * 10 + w[i];
        }
        printf("%d", result);
        return result;
    };
};

int main()
{
    Solution so;
    int input = 9666;
    so.maximum69Number(input);
}
