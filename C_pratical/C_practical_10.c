#include <stdio.h>

int main()
{
   FILE *f1, *f2, *f3;
   int number, i;
   printf("Enter Numbers -\n");
   f1 = fopen("DATA.txt", "w");
   for (i = 1; i <= 20; i++)
   {
      scanf("%d", &number);
      putw(number, f1);
   }
   fclose(f1);
   f1 = fopen("DATA.txt", "r");
   f2 = fopen("Oddfile.txt", "w");
   f3 = fopen("Evenfile.txt", "w");

   while (getw(f1) != EOF)
   {
      number = getw(f1);
      if (number % 2 == 0){
         putw(number, f3);}
      else{
         putw(number, f2);}
   }
   fclose(f1);
   fclose(f2);
   fclose(f3);
}


