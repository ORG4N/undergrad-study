using System;
using System.Collections.Generic;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class Review
    {
        public int ReviewId { get; set; }
        public int CompanyId { get; set; }
        public int UserId { get; set; }
        public string RevMessage { get; set; }
        public int Rating { get; set; }
    }
}
