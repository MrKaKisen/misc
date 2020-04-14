#include <stdio.h>

double multiply_array(double arr1[ 5 ], double arr2 [5])
{
    int i;
    double sum = 0.0;

    for (i = 0; i < 5; ++i)
    {
        sum = sum + arr1[i] * arr2[i];
    };

    return sum;
}

int main()
{
    // two arbitrary five-dimensional vectors
    double vector1[ 5 ] = { 7, 4, 3, 2, 9.3 };
    double vector2[ 5 ] = { 8, 2, 1, -3, 2 };
    printf("%lf\n", multiply_array(vector1, vector2));

    return 0;
}
