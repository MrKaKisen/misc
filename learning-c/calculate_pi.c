#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double double_rand()
{
    double min = 0;
    double max = 1;

    double scale = rand() / (double) RAND_MAX; /* [0, 1.0] */
    return min + scale * ( max - min );      /* [min, max] */
}

double distance_from_origio(double x, double y)
{
    double distance = pow((pow(x, 2) + pow(y, 2)), 0.5);
    return distance;
}

int is_point_in_circle(double x, double y) {
    double distance = distance_from_origio(x, y);
    if (distance <= 1) {
        return 1;
    }

    return 0;
}


int main()
{
    // how many to test with
    long sum = 1000000;

    // how many that are in the circle
    long in_circle = 0;

    // generate random coordinates and test how many are in the circle
    long i;
    for (i = 0; i <= sum; ++i)
    {
        double random_x = double_rand();
        double random_y = double_rand();

        if (is_point_in_circle(random_x, random_y) == 1)
        {
            in_circle++;
        }
    }

    // pi!
    long outside_circle = sum - in_circle;

    printf("IN\tOUT\tTOT\n");
    printf("%d\t%d\t%d\n", in_circle, outside_circle, sum);

    // area fraction
    double af = (double) in_circle / (double) outside_circle;

    // calculate pi estimate
    double pi = (4 * af) / (1 + af);

    printf("pi: %lf\n", pi);

    return 0;
}
