// how many square and rectangle is in chees board

// 1,4,9,25,36,49,64

#include <stdio.h>
int main(){
    int i,j,square=0;
    for(i=1;i<9;i++){
        square += i*i;
    }
    printf("Number of the Squares in cheese board = %d",square);
     

}