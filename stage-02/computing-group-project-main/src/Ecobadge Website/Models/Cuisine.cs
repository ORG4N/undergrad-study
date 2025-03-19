using System;
using System.Collections.Generic;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class Cuisine
    {
        public Cuisine()
        {
            CompanyCuisines = new HashSet<CompanyCuisine>();
        }

        public int CuisineId { get; set; }
        public string CuisineName { get; set; }

        public virtual ICollection<CompanyCuisine> CompanyCuisines { get; set; }
    }
}
