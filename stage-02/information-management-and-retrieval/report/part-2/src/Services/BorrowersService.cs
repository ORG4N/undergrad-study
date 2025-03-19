using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.IO;

using COMP2001_Task2.Models;

namespace COMP2001_Task2.Services
{
    public class BorrowersService
    {
        private static List<Borrower> data = new List<Borrower>();

        public static void Init()
        {
            BorrowersService service = new BorrowersService();

            List<string> lines = new List<string>();

            try
            {
                using (FileStream fs = File.Open("wwwroot/data/library-users.csv", FileMode.Open, FileAccess.Read))
                {
                    using (StreamReader sr = new StreamReader(fs))
                    {
                        while (!sr.EndOfStream)
                        {
                            lines.Add(sr.ReadLine());
                        }
                    }
                }
            }

            catch (IOException) { }

            // Create each object by reading each field from each line in from the users.csv file
            foreach (string field in lines)
            {
                string[] split = field.Split(',');

                Borrower borrower = new Borrower();

                borrower.Library = split[0];
                borrower.Age0to4 = split[1];
                borrower.Age5to11 = split[2];
                borrower.Age12to17 = split[3];
                borrower.Age18to59 = split[4];
                borrower.Age60to100 = split[5].Replace("/r", "");


                data.Add(borrower);
            }
        }

        public static List<Borrower> GetData()
        {
            return data;
        }

    }
}