#include <stdio.h>

int main(int argc, char** argv)
{
    int i = 20;
    while (i%2  || i%3  || i%4  || i%5  || 
           i%6  || i%7  || i%8  || i%9  ||
           i%10 || i%11 || i%12 || i%13 ||
           i%14 || i%15 || i%16 || i%17 ||
           i%18 || i%19 || i%20)
        i += 20;
    printf("%d\n",i);
}

