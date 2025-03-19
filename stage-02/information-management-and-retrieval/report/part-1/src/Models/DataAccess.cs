using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.Data.SqlClient;
using Microsoft.Extensions.Configuration;
using Microsoft.AspNetCore.Hosting;
using System.Data;


// Code scaffolded by EF Core assumes nullable reference types (NRTs) are not used or disabled.
// If you have enabled NRTs for your project, then un-comment the following line:
// #nullable disable

namespace COMP2001_Task1.Models
{
    public partial class DataAccess : DbContext
    {

        private readonly string _connection;
        public DbSet<Programme> Programmes { get; set; }

        public DataAccess(DbContextOptions<DataAccess> options) : base(options)
        {
            _connection = Database.GetDbConnection().ConnectionString;
        }

        public void Create(Programme prog, out string responseMessage)
        {
            using (SqlConnection sql = new SqlConnection(_connection))
            {
                using (SqlCommand cmd = new SqlCommand("CW2.Create_Programme", sql))
                {
                    cmd.CommandType = System.Data.CommandType.StoredProcedure;

                    cmd.Parameters.Add(new SqlParameter("@Programme_Code", prog.ProgrammeCode));
                    cmd.Parameters.Add(new SqlParameter("@Title", prog.ProgrammeTitle));

                    SqlParameter output = new SqlParameter("@ResponseMessage", SqlDbType.NVarChar, 250);
                    output.Direction = ParameterDirection.Output;

                    cmd.Parameters.Add(output);

                    sql.Open();
                    cmd.ExecuteNonQuery();

                    responseMessage = output.Value.ToString();
                }
            }
        }

        public void Update(Programme prog)
        {
            using (SqlConnection sql = new SqlConnection(_connection))
            {
                using (SqlCommand cmd = new SqlCommand("CW2.Update_Programme", sql))
                {
                    cmd.CommandType = System.Data.CommandType.StoredProcedure;

                    cmd.Parameters.Add(new SqlParameter("@Programme_Code", prog.ProgrammeCode));
                    cmd.Parameters.Add(new SqlParameter("@Title", string.IsNullOrEmpty(prog.ProgrammeTitle) ? (object)DBNull.Value : prog.ProgrammeTitle));

                    sql.Open();
                    cmd.ExecuteNonQuery();
                }
            }
        }

        public void Delete(string code)
        {
            using (SqlConnection sql = new SqlConnection(_connection))
            {
                using (SqlCommand cmd = new SqlCommand("CW2.Delete_Programme", sql))
                {
                    cmd.CommandType = System.Data.CommandType.StoredProcedure;
                    cmd.Parameters.Add(new SqlParameter("@Programme_Code", code));

                    sql.Open();
                    cmd.ExecuteNonQuery();
                }
            }
        }


        public virtual DbSet<Programme> Programme { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {/*
                #warning To protect potentially sensitive information in your connection string, you should move it out of source code. See http://go.microsoft.com/fwlink/?LinkId=723263 for guidance on storing connection strings.
                optionsBuilder.UseSqlServer("Server=socem1.uopnet.plymouth.ac.uk;Database=COMP2001_COrgan;User Id=COrgan;Password=PdaH660+;");*/
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Programme>(entity =>
            {
                entity.HasKey(e => e.ProgrammeCode)
                    .HasName("pk_programme");

                entity.ToTable("Programme", "CW2");

                entity.Property(e => e.ProgrammeCode)
                    .HasMaxLength(10)
                    .IsUnicode(false);

                entity.Property(e => e.ProgrammeTitle)
                    .HasMaxLength(255)
                    .IsUnicode(false);
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
