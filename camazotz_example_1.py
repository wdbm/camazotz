#!/usr/bin/env python

import camazotz

def main():

    library = camazotz.C(
        """
        #include <stdio.h>
        
        int factorial(int x){
            int result = 1;
            while (x > 1){
                result *= x;
                x--;
            }
        
            return result;
        }
        """
    )

    function_factorial = library["factorial"]
    print("5! =", function_factorial(5))
    print("4! =", function_factorial(4))

if __name__ == "__main__":

    main()
