using System;
using MyConsoleApp;

namespace MyConsoleApp
{
   
    class Program
    {
        static void Main(string[] args)
        {
            Person p = new Person("John");
            Console.WriteLine(p.Name);
            p.Introduction("Summit");
        }
    }
}