// Insert Bits – Given two 32-bit numbers N and M, and bit positions i to j,
// insert M into N such that M occupies bits i...j 
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// 0xAABBCCDD
// 0x11445566

// 0b 1010 1010 1011 1011 1100 1100 1101 1101 //M
// 0b 0001 0001 0100 0100 0101 0101 0110 0110 //N
//                           12          5
 
// i = 5 j = 12;



uint32_t insertBits(uint32_t M, uint32_t N, int i , int j)
{
    int width = (j-i+1);
    uint32_t mask = (width==32)? ~0U:((1U<<width)-1);
    uint32_t M_loc = M&mask;
    uint32_t clear_mask = ~(mask<<i);
    N = N&clear_mask;

    return N|(M_loc<<i);

}





