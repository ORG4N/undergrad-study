using System;
using System.Collections.Generic;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class Login
    {
        public int UserId { get; set; }
        public string UserEmail { get; set; }
        public string UserPassword { get; set; }

        public virtual User User { get; set; }
    }
}
