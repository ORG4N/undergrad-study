using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

#nullable disable

namespace Ecobadge_Website.Models
{
    public partial class COMP2003_AContext : DbContext
    {
        public COMP2003_AContext()
        {
        }

        public COMP2003_AContext(DbContextOptions<COMP2003_AContext> options)
            : base(options)
        {
        }

        public virtual DbSet<Company> Companies { get; set; }
        public virtual DbSet<CompanyCuisine> CompanyCuisines { get; set; }
        public virtual DbSet<Cuisine> Cuisines { get; set; }
        public virtual DbSet<Login> Logins { get; set; }
        public virtual DbSet<Review> Reviews { get; set; }
        public virtual DbSet<User> Users { get; set; }
        public virtual DbSet<UserAdmin> UserAdmins { get; set; }
        public virtual DbSet<UserCompanyMember> UserCompanyMembers { get; set; }
        public virtual DbSet<UserConsumer> UserConsumers { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see http://go.microsoft.com/fwlink/?LinkId=723263.
                optionsBuilder.UseSqlServer("Server=socem1.uopnet.plymouth.ac.uk;Database=COMP2003_A;User Id=COMP2003A;Password=YtfN673*;");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.HasAnnotation("Relational:Collation", "Latin1_General_CI_AS");

            modelBuilder.Entity<Company>(entity =>
            {
                entity.ToTable("Company", "ecobadge");

                entity.Property(e => e.CompanyId)
                    .ValueGeneratedNever()
                    .HasColumnName("CompanyID");

                entity.Property(e => e.Address)
                    .IsRequired()
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.Biography)
                    .IsRequired()
                    .HasMaxLength(255)
                    .IsUnicode(false);

                entity.Property(e => e.CityOrTown)
                    .IsRequired()
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.CompanyEmail)
                    .IsRequired()
                    .HasMaxLength(80)
                    .IsUnicode(false);

                entity.Property(e => e.CompanyName)
                    .IsRequired()
                    .HasMaxLength(100)
                    .IsUnicode(false);

                entity.Property(e => e.County)
                    .IsRequired()
                    .HasMaxLength(30)
                    .IsUnicode(false);

                entity.Property(e => e.Cuisine)
                    .IsRequired()
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.EcobadgeTier)
                    .IsRequired()
                    .HasMaxLength(12)
                    .IsUnicode(false);

                entity.Property(e => e.Postcode)
                    .IsRequired()
                    .HasMaxLength(8)
                    .IsUnicode(false);

                entity.Property(e => e.WebsiteLink)
                    .HasMaxLength(255)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<CompanyCuisine>(entity =>
            {
                entity.HasKey(e => e.CompanyCuisinesId)
                    .HasName("PK_CompanyCuisinesPK");

                entity.ToTable("CompanyCuisines", "ecobadge");

                entity.Property(e => e.CompanyCuisinesId)
                    .ValueGeneratedNever()
                    .HasColumnName("CompanyCuisinesID");

                entity.Property(e => e.CompanyId).HasColumnName("CompanyID");

                entity.Property(e => e.CuisineId).HasColumnName("CuisineID");

                entity.HasOne(d => d.Company)
                    .WithMany(p => p.CompanyCuisines)
                    .HasForeignKey(d => d.CompanyId)
                    .HasConstraintName("FK_Cui1FK");

                entity.HasOne(d => d.Cuisine)
                    .WithMany(p => p.CompanyCuisines)
                    .HasForeignKey(d => d.CuisineId)
                    .HasConstraintName("FK_Cui2FK");
            });

            modelBuilder.Entity<Cuisine>(entity =>
            {
                entity.ToTable("Cuisines", "ecobadge");

                entity.Property(e => e.CuisineId)
                    .ValueGeneratedNever()
                    .HasColumnName("CuisineID");

                entity.Property(e => e.CuisineName)
                    .IsRequired()
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Login>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("Login", "ecobadge");

                entity.Property(e => e.UserEmail)
                    .IsRequired()
                    .HasMaxLength(80)
                    .IsUnicode(false);

                entity.Property(e => e.UserId).HasColumnName("UserID");

                entity.Property(e => e.UserPassword)
                    .IsRequired()
                    .HasMaxLength(30)
                    .IsUnicode(false);

                entity.HasOne(d => d.User)
                    .WithMany()
                    .HasForeignKey(d => d.UserId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_LoginFK");
            });

            modelBuilder.Entity<Review>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("Reviews", "ecobadge");

                entity.Property(e => e.CompanyId).HasColumnName("CompanyID");

                entity.Property(e => e.RevMessage)
                    .HasMaxLength(255)
                    .IsUnicode(false);

                entity.Property(e => e.ReviewId).HasColumnName("ReviewID");

                entity.Property(e => e.UserId).HasColumnName("UserID");
            });

            modelBuilder.Entity<User>(entity =>
            {
                entity.ToTable("User", "ecobadge");

                entity.Property(e => e.UserId)
                    .ValueGeneratedNever()
                    .HasColumnName("UserID");

                entity.Property(e => e.Forename)
                    .IsRequired()
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.Surname)
                    .IsRequired()
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<UserAdmin>(entity =>
            {
                entity.HasKey(e => e.RoleId)
                    .HasName("PK_UAD");

                entity.ToTable("UserAdmin", "ecobadge");

                entity.Property(e => e.RoleId)
                    .ValueGeneratedNever()
                    .HasColumnName("RoleID");
            });

            modelBuilder.Entity<UserCompanyMember>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("UserCompanyMember", "ecobadge");

                entity.Property(e => e.CompanyId).HasColumnName("CompanyID");

                entity.Property(e => e.RoleId).HasColumnName("RoleID");

                entity.HasOne(d => d.Company)
                    .WithMany()
                    .HasForeignKey(d => d.CompanyId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_UCM2FK");

                entity.HasOne(d => d.Role)
                    .WithMany()
                    .HasForeignKey(d => d.RoleId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_UCM1FK");
            });

            modelBuilder.Entity<UserConsumer>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("UserConsumer", "ecobadge");

                entity.Property(e => e.RoleId).HasColumnName("RoleID");

                entity.HasOne(d => d.Role)
                    .WithMany()
                    .HasForeignKey(d => d.RoleId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_UrCFK");
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
