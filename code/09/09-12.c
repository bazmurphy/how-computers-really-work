// Calculate the factorial of n.
int factorial(int n)
{
  int result = n;
  while(--n > 0)
  {
    result = result * n;
  }
  return result;
}