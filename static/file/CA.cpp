/*Gunnar Hovik, Assignment 1: This program generates a 1D cellular automata based on an input ruleset between 0-255.*/

#include <iostream>

/*Converts setNumber to an 8-digit binary number and stores it in storage. Assumes setNumber between 0-255*/
void convertRuleSetNumberToRuleSetArray(int setNumber, int storage[8]){
    //set every value to 0 to make sure there is no funny bussiness
    for(int i = 0; i < 8; i++)
        storage[i] = 0;

    //convert setNumber to binary and store
    int index = 7;
    for(int i = 128; i > 0; i /= 2){
        if(setNumber >= i){
            storage[index] = 1;
            setNumber -= i;
        }
        index--;
    }
}

/*Outputs the storage array using the format 0=" " and 1="#". Assumes that the array contains
    only 1s and 0s and that the size parameter is the size of the storage array.*/
void displayGeneration(int storage[], int size){
    for(int i = 0; i < size; i++){
        if(storage[i] == 0)
            std::cout << " ";
        else
            std::cout << "#";
    }
    std::cout << std::endl;
}

/*Converts the binary number made by lcr to base 10 and returns.
    Assumes l,c,r are either 1 or 0.*/
int convertNeighborhoodToIndex(int l, int c, int r){
    return l*4 + c*2 + r*1;
}

/*Computes the next generation of the CA and stores it in the next array.
    Assumes cur contains the current generation, size is the size of both cur and next
    and rule is a valid 8 digit CA ruleset.*/
void computeNextGeneration(int cur[], int next[], int size, int rule[8]){
    //copy first and last
    next[0] = cur[0];
    next[size - 1] = cur[size - 1];
    //use rule set for rest
    for(int i = 1; i < size - 1; i++)
        next[i] = rule[convertNeighborhoodToIndex(cur[i-1], cur[i], cur[i+1])];
}

/*Copys one int array into another. Assumes both dst and src are of length size.*/
void copyArray(int dst[], int src[], int size){
    for(int i = 0; i < size; i++)
        dst[i] = src[i];
}

int main(){
    int test[8];
    convertRuleSetNumberToRuleSetArray(3, test);
    for(int x : test)
        std::cout << x;
    std::cout << std::endl;

    //vars
    int ruleNum = -1;
    int rule[8];
    int gen[64]{};

    //Get the rule number
    std::cout << "Please enter a number 0-255: ";
    std::cin >> ruleNum;
    //Must be 0-255
    if(ruleNum < 0 || ruleNum > 255) {
        std::cout << "That is an invalid number." << std::endl;
        return 0;
    }

    //Calculate and store ruleset
    convertRuleSetNumberToRuleSetArray(ruleNum, rule);

    //Make starting gen
    gen[32] = 1;
    displayGeneration(gen, 64);

    //Calculate 49 more
    for(int i = 0; i < 49; i++){
        int temp[64];
        computeNextGeneration(gen, temp, 64, rule);
        copyArray(gen, temp, 64);
        displayGeneration(gen, 64);
    }
}