package com.example.projectapp;

import android.provider.ContactsContract;

public class Projects {
    private String ProjectID;
    private String StudentID;
    private String Title;
    private String Description;
    private String Year;
    //private String ThumbnailURL;
    //private String PosterURL;
    private String FirstName;
    private String LastName;
    private String Photo;

    public Projects(String ProjectID, String StudentID, String Title, String Description, String Year, String FirstName, String LastName, String Photo){
        this.ProjectID = ProjectID;
        this.StudentID = StudentID;
        this.Title = Title;
        this.Description = Description;
        this.Year = Year;
        this.FirstName = FirstName;
        this.LastName = LastName;
        this.Photo = Photo;
    }

    public String getProjectID() { return ProjectID; }
    public String getStudentID() { return StudentID; }
    public String getTitle() { return Title; }
    public String getDescription() { return Description; }
    public String getYear() { return Year; }
    //public String getThumbnailURL() { return ThumbnailURL; }
    //public String getPosterURL() { return PosterURL; }
    public String getFirstName() { return FirstName; }
    public String getLastName() { return LastName; }
    public String getPhoto() { return Photo; }
}
