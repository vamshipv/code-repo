using System;
class HelloWorld {
  static void Main() {
    int testcase;
    testcase = Convert.ToInt32(Console.ReadLine());
    // Console.WriteLine(testcase);
    while (testcase > 0)
    {
        string[] tokens = Console.ReadLine().Split();
        int D = int.Parse(tokens[0]);
        int d = int.Parse(tokens[1]);
        int P = int.Parse(tokens[2]);
        int Q = int.Parse(tokens[3]);
        // Console.WriteLine(a);
        int days = D/d;
        int reamning = D%d;
        int prod = 0;
        int heist = 0;
        int temp = days - 1;
        heist = (days * P) + ((((temp)*(temp + 1))/2)*Q);
        heist = heist * d;
        
        if ( reamning >= 1)
        {
            heist = heist + ((P + ((days) * Q))*reamning);
        }
        Console.WriteLine(heist);
        
        testcase = testcase - 1;
    }
  }
}
