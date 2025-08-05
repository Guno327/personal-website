## Assignment Description

You will write a C++ program in a file CA.cpp (CA is a common abbreviation for
cellular automata).

The program will:

- Ask a user for a rule set number from 0 to 255. If a value outside that range
  is input, an explanatory message should be output and the program ended
  (returning from main with a 0). You can assume that the input is a number.
- The rule set number should be converted into a binary number and stored in a
  rule set array. This array specifies what new value should be produced given a
  value and its neighbors. The conversion is just turning the rule set integer
  number into a binary number.
- A starting generation array of length 64 should be made of all 0 except a
  single 1 at index 32. This array should be displayed. Then, 49 new generations
  should be computed and displayed using the rule set array to compute each new
  generation. This makes a total of 50 rows of output.

## Example Output

```
Please enter a number 0-255: 126
                                #                               
                               ###                              
                              ## ##                             
                             #######                            
                            ##     ##                           
                           ####   ####                          
                          ##  ## ##  ##                         
                         ###############                        
                        ##             ##                       
                       ####           ####                      
                      ##  ##         ##  ##                     
                     ########       ########                    
                    ##      ##     ##      ##                   
                   ####    ####   ####    ####                  
                  ##  ##  ##  ## ##  ##  ##  ##                 
                 ###############################                
                ##                             ##               
               ####                           ####              
              ##  ##                         ##  ##             
             ########                       ########            
            ##      ##                     ##      ##           
           ####    ####                   ####    ####          
          ##  ##  ##  ##                 ##  ##  ##  ##         
         ################               ################        
        ##              ##             ##              ##       
       ####            ####           ####            ####      
      ##  ##          ##  ##         ##  ##          ##  ##     
     ########        ########       ########        ########    
    ##      ##      ##      ##     ##      ##      ##      ##   
   ####    ####    ####    ####   ####    ####    ####    ####  
  ##  ##  ##  ##  ##  ##  ##  ## ##  ##  ##  ##  ##  ##  ##  ## 
 ############################################################## 
 #                                                            # 
 ##                                                          ## 
 ###                                                        ### 
 # ##                                                      ## # 
 #####                                                    ##### 
 #   ##                                                  ##   # 
 ## ####                                                #### ## 
 ####  ##                                              ##  #### 
 #  ######                                            ######  # 
 ####    ##                                          ##    #### 
 #  ##  ####                                        ####  ##  # 
 ########  ##                                      ##  ######## 
 #      ######                                    ######      # 
 ##    ##    ##                                  ##    ##    ## 
 ###  ####  ####                                ####  ####  ### 
 # ####  ####  ##                              ##  ####  #### # 
 ###  ####  ######                            ######  ####  ### 
 # ####  ####    ##                          ##    ####  #### #
```

## Code

[Download](/static/file/CA.cpp)
