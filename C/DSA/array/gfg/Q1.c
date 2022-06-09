// Find the element that appears once in an array where every other element appears twice
// approch 1 (using xor )
#include <stdio.h>

int main(){
    int res;
    int arr[]= {7,3,5,5,3};
    for(int i=0;i<5;i++){
        res = res ^ arr[i]; 
    }
    printf("%d",res);
}


// approch 2 (using maths) 
// find the sum of the array then find the sum of array without duplication then 
// 2*(sum_of_array_without_dupplicates) - (sum_of_array)

