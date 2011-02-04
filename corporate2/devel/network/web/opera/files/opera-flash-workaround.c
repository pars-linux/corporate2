#include <stdio.h>

void __attribute__((constructor)) init()
{
    return 0;
    //printf("using workaround for opera inconsistency\n");
}

