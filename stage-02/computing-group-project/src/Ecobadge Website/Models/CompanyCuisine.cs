using System;
using System.Collections.Generic;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class CompanyCuisine
    {
        public int CompanyCuisinesId { get; set; }
        public int? CompanyId { get; set; }
        public int? CuisineId { get; set; }

        public virtual Company Company { get; set; }
        public virtual Cuisine Cuisine { get; set; }
    }
}
