#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* addStrings(char* num1, char* num2) {
    
    //inizializzo lunghezze, contatori e variabili per calcolare le somme
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int k=0;
    int i=len1-1;
    int j=len2-1;
    int carry=0;
    int n1=0;
    int n2=0;
    
    int max_len=0;      

    if(len1 > len2){            //controllo la stringa più lunga 
        max_len = len1 +1;
    }
    else{
        max_len = len2 +1;
    }

    char* strSum;                       //alloco memoria
    strSum = malloc((max_len+1)*sizeof(char)); 

    while(i>=0 || j>=0 || carry){       //faccio le somme, mentre i contatori sono ancora nel range della len, gestendo anche l'ultimo riporto

        if(i>=0){               //mentre l'indice i è positivo (in range len(num1)) faccio la conversione
            n1 = num1[i] -'0';
        }
        else
            n1 = 0;
        
        if(j>=0){               //stessa cosa per num2
            n2 = num2[j] - '0';
        }
        else
            n2 = 0;

        int sum = n1 + n2+ carry;       //sommo i valori più il riporto
        carry = (sum) / 10;             //calcolo il riporto 
        strSum[k] = (sum % 10) + '0';  // inserisco nell'array la somma castata in carattere
        
        if(i >= 0)
            i--;
        
        if(j >= 0)
            j--;
        
        k++; 
    }

    strSum[k] = '\0';
    
    int start=0;
    int end=k-1;
    
    //giro i caratteri della stringa, sono partito dalla fine della stringa per calcolare la somma
    
    while(start<end){           
        char temp = strSum[start];
        strSum[start] = strSum[end];
        strSum[end] = temp;
        start++;
        end--;
    }

    return strSum;
    }

int main(){
    char num1[]="11";
    char num2[]="123";


    char* result;
    result = addStrings(num1,num2);
    printf("%s",result);
    free(result);
}   
