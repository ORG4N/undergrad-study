using System;
using System.Collections.Generic;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class UserConsumer
    {
        public int RoleId { get; set; }
        public int CustomerScore { get; set; }

        public virtual UserAdmin Role { get; set; }
    }
}
