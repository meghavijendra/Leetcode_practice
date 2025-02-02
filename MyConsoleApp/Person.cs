 using System;

    namespace MyConsoleApp
    {
        public class Person
        {
            public string Name { get; set; }

            public Person(string name)
            {
                this.Name = name;
            }
            public void Introduction(string person)
            {
                Console.WriteLine("hello {0} my name is {1}", person, Name);
            }
        }
    }