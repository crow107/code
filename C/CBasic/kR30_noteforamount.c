# include <stdio.h>

void main(){
    int amount ,note_2000;
    printf("kanishk rawat (BCA EA) \n");
    printf("Enter the Amount:-");
    scanf("%d",&amount);
    while(amount!=0){
        if (amount>=2000){
            note_2000 = amount/2000;
            amount = amount%2000;
            printf("There are %d Notes of 2000",note_2000);
        }
        else if(amount>=500){
            int note_500 = amount/500;
            amount = amount%500;
            printf("There are %d Notes of 500",note_500);
        }
        else if(amount>=200){
            int note_200 = amount/200;
            amount = amount%200;
            printf("There are %d Notes of 200",note_200);

        }
        else if(amount>=00){
            int note_100 = amount/100;
            amount = amount%100;
            printf("There are %d Notes of 100",note_100);

        }
        else if(amount>=50){
            int note_50 = amount/50;
            amount = amount%50;
            printf("There are %d Notes of 50",note_50);

        }
        else if(amount>=20){
            int note_20 = amount/20;
            amount = amount%20;
            printf("There are %d Notes of 20",note_20);

        }
        else if(amount>=10){
            int note_10 = amount/10;
            amount = amount%10;
            printf("There are %d Notes of 10",note_10);
        }
        else if(amount>=5){
            int note_5 = amount/5;
            amount = amount%5;
            printf("There are %d Notes of 5",note_5);
        }
        else if(amount>=2){
            int note_2 = amount/2;
            amount = amount%2;
            printf("There are %d Notes of 2",note_2);
        }
        else if(amount>=1){
            int note_1 = amount/1;
            amount = amount%1;
            printf("There are %d Notes of 1",note_1);
        }
    }

}