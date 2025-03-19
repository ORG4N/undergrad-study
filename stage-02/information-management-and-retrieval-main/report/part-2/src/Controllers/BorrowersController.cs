using Microsoft.AspNetCore.Mvc;
using COMP2001_Task2.Models;
using COMP2001_Task2.Services;
using System.Collections.Generic;

namespace COMP2001_Task2.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class BorrowersController : ControllerBase
    {
        [HttpGet]
        public IEnumerable<Borrower> Get()
        {
            return BorrowersService.GetData().ToArray();
        }
    }
}
