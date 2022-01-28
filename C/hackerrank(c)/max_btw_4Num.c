#include <stdio.h>

int max_of_four(int a, int b, int c, int d);

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
int max_of_four(int a,int b , int c, int d)
{
    int k=0;
    if (a>=k){
        k = a;
    }
    if (b>=k) {
        k = b;
    }
    if (c>=k){
        k =c; 
    }
    if (d>=k){
        k =d;
    }
    return k;
}s