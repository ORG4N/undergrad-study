using System;
using System.Collections.Generic;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class User
    {
        public int UserId { get; set; }
        public string Forename { get; set; }
        public string Surname { get; set; }
        public byte[] UserImg { get; set; }
    }
}
