#include <stdio.h>
#include <signal.h>
int main()
{
  int points = 27;
  int year = 2020;

  // print the value of 'points' and its memory address
  printf("points is %d and is stored at %#016lx\n", points, (unsigned long)&points);
  // print the value of 'year' and its memory address
  printf("year is %d and is stored at %#016lx\n", year, (unsigned long)&year);

  raise(SIGINT);

  return 0;
}

// points is 27 and is stored at 0x7fff1af27900
// year is 2020 and is stored at 0x7fff1af27904

// 0x7fff1af27900
// 16 hexidecimal digits
// Each hexadecimal digit represents 4 bits
// (16 x 4) 64 bits in total