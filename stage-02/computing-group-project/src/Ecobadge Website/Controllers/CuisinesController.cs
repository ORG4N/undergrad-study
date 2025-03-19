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
    public class CuisinesController : ControllerBase
    {
        private readonly COMP2003_AContext _context;

        public CuisinesController(COMP2003_AContext context)
        {
            _context = context;
        }

        // GET: api/Cuisines
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Cuisine>>> GetCuisines()
        {
            return await _context.Cuisines.ToListAsync();
        }

        // GET: api/Cuisines/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Cuisine>> GetCuisine(int id)
        {
            var cuisine = await _context.Cuisines.FindAsync(id);

            if (cuisine == null)
            {
                return NotFound();
            }

            return cuisine;
        }

        // PUT: api/Cuisines/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutCuisine(int id, Cuisine cuisine)
        {
            if (id != cuisine.CuisineId)
            {
                return BadRequest();
            }

            _context.Entry(cuisine).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!CuisineExists(id))
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

        // POST: api/Cuisines
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Cuisine>> PostCuisine(Cuisine cuisine)
        {
            _context.Cuisines.Add(cuisine);
            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateException)
            {
                if (CuisineExists(cuisine.CuisineId))
                {
                    return Conflict();
                }
                else
                {
                    throw;
                }
            }

            return CreatedAtAction("GetCuisine", new { id = cuisine.CuisineId }, cuisine);
        }

        // DELETE: api/Cuisines/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteCuisine(int id)
        {
            var cuisine = await _context.Cuisines.FindAsync(id);
            if (cuisine == null)
            {
                return NotFound();
            }

            _context.Cuisines.Remove(cuisine);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool CuisineExists(int id)
        {
            return _context.Cuisines.Any(e => e.CuisineId == id);
        }
    }
}
