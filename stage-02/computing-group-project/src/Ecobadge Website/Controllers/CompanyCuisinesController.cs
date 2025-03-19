using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Ecobadge_Website.Models;

namespace Ecobadge_Website.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CompanyCuisinesController : ControllerBase
    {
        private readonly COMP2003_AContext _context;

        public CompanyCuisinesController(COMP2003_AContext context)
        {
            _context = context;
        }

        // GET: api/CompanyCuisines
        [HttpGet]
        public async Task<ActionResult<IEnumerable<CompanyCuisine>>> GetCompanyCuisines()
        {
            return await _context.CompanyCuisines.ToListAsync();
        }

        // GET: api/CompanyCuisines/5
        [HttpGet("{id}")]
        public async Task<ActionResult<CompanyCuisine>> GetCompanyCuisine(int id)
        {
            var companyCuisine = await _context.CompanyCuisines.FindAsync(id);

            if (companyCuisine == null)
            {
                return NotFound();
            }

            return companyCuisine;
        }

        // PUT: api/CompanyCuisines/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutCompanyCuisine(int id, CompanyCuisine companyCuisine)
        {
            if (id != companyCuisine.CompanyCuisinesId)
            {
                return BadRequest();
            }

            _context.Entry(companyCuisine).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!CompanyCuisineExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/CompanyCuisines
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<CompanyCuisine>> PostCompanyCuisine(CompanyCuisine companyCuisine)
        {
            _context.CompanyCuisines.Add(companyCuisine);
            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateException)
            {
                if (CompanyCuisineExists(companyCuisine.CompanyCuisinesId))
                {
                    return Conflict();
                }
                else
                {
                    throw;
                }
            }

            return CreatedAtAction("GetCompanyCuisine", new { id = companyCuisine.CompanyCuisinesId }, companyCuisine);
        }

        // DELETE: api/CompanyCuisines/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteCompanyCuisine(int id)
        {
            var companyCuisine = await _context.CompanyCuisines.FindAsync(id);
            if (companyCuisine == null)
            {
                return NotFound();
            }

            _context.CompanyCuisines.Remove(companyCuisine);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool CompanyCuisineExists(int id)
        {
            return _context.CompanyCuisines.Any(e => e.CompanyCuisinesId == id);
        }
    }
}
