using System;
using System.Collections.Generic;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class UserCompanyMember
    {
        public int RoleId { get; set; }
        public int CompanyId { get; set; }

        public virtual Company Company { get; set; }
        public virtual UserAdmin Role { get; set; }
    }
}
