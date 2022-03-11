#include <stdio.h>
 
int main ()
{
 
   FILE *fp;
   int i=1, j=2, k=1, num;
   fp = fopen ("test.txt","w");
   putw(i,fp);
   putw(j,fp);
   putw(k,fp);
   fclose(fp);
 
   fp = fopen ("test.c","r");
 
   while(getw(fp)!=EOF)
   {
      num= getw(fp);
      printf("Data in test.c file is %d \n", num);
   }
   fclose(fp);
   return 0;
}