#include <stdio.h>
#include <math.h>
#include <stdbool.h> 
#include <time.h>


bool isInteger(double val) {
    int truncated = (int)val;
    return (val == truncated);
}

int getPentagonal (int n) {
    if (n < 1) {
        return -1;
    }
    int res = (n * (3*n - 1))/2;
    return res;
}

bool isPentagonal (int k) {
    double n = (1 + sqrt(1 + 24*k)) / 6;
    return isInteger(n);
}

int main (int argc, char *argv[]) {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    int printInterv = 1000;
    bool found = false;
    for (int n = 1; n < 3000; n++) {
        for (int i = n+1; i < 3000; i++) {
            int j = getPentagonal(n);
            int k = getPentagonal(i);
            if (i % printInterv == 0) {
                printf("\rChecking: n = %d, i = %d", n, i);
                fflush(stdout);
            }
            if (isPentagonal(k - j) && isPentagonal(k + j)){
                printf("\nj, k, d :>> %d, %d, %d\n", j, k, k-j);
                found = true;
                break;
            }

        }
        if (found) {
            break;
        }
        
    }

    end = clock();
    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Time taken: %f seconds\n", cpu_time_used);

    return 0;
}