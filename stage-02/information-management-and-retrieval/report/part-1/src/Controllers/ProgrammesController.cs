using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using COMP2001_Task1.Models;

namespace COMP2001_Task1.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProgrammesController : ControllerBase
    {
        private readonly DataAccess _context;

        public ProgrammesController(DataAccess context)
        {
            _context = context;
        }

        // GET: api/Programmes
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Programme>>> GetProgramme()
        {
            return await _context.Programme.ToListAsync();
        }

        // GET: api/Programmes/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Programme>> GetProgramme(string id)
        {
            var programme = await _context.Programme.FindAsync(id);

            if (programme == null)
            {
                return NotFound();
            }

            return programme;
        }

        [HttpPost]
        public IActionResult Post([FromBody] Programme prog)
        {
            string responseMessage = "";
            try
            {
                _context.Create(prog, out responseMessage);
            }
            catch (Exception e)
            {
                responseMessage = e.ToString();
                return Ok(new string[] { "Error", responseMessage });
            }
            return StatusCode(201);
        }



        [HttpPut("{id}")]
        public IActionResult PutProgramme(string id, [FromBody] Programme programme)
        {
            string responseMessage = "";

            try
            {
                programme.ProgrammeCode = id;
                _context.Update(programme);
            }
            catch (Exception e)
            {
                responseMessage = e.ToString();
                return Ok(new string[] { "Error", responseMessage });
            }

            return NoContent();
        }

        // DELETE: api/Programmes/5
        [HttpDelete("{id}")]
        public IActionResult DeleteProgramme(string id)
        {
            _context.Delete(id);
            return NoContent();
        }

        private bool ProgrammeExists(string id)
        {
            return _context.Programme.Any(e => e.ProgrammeCode == id);
        }
    }
}
