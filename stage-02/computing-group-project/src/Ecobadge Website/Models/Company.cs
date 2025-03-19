using System;
using System.Collections.Generic;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class Company
    {
        public Company()
        {
            CompanyCuisines = new HashSet<CompanyCuisine>();
        }

        public int CompanyId { get; set; }
        public string CompanyName { get; set; }
        public string Biography { get; set; }
        public string CityOrTown { get; set; }
        public string County { get; set; }
        public string Address { get; set; }
        public string Postcode { get; set; }
        public string CompanyEmail { get; set; }
        public string WebsiteLink { get; set; }
        public byte[] CompImg { get; set; }
        public string Cuisine { get; set; }
        public int? CompanyScore { get; set; }
        public string EcobadgeTier { get; set; }
        public byte[] Menu { get; set; }
        public bool? VeganDishes { get; set; }
        public bool? SingleUsePlastic { get; set; }
        public bool? FoodWasteCollectionScheme { get; set; }
        public bool? LocalProduce { get; set; }
        public int? Tel { get; set; }

        public virtual ICollection<CompanyCuisine> CompanyCuisines { get; set; }
    }
}
