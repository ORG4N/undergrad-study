package com.example.projectapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class ViewAllActivity extends AppCompatActivity {

    private ArrayList<Projects> projectsList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_all);

        projectsList = new ArrayList<>();

        String url ="http://web.socem.plymouth.ac.uk/COMP2000/api/students";

        RequestQueue queue = Volley.newRequestQueue(ViewAllActivity.this);
        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(Request.Method.GET, url, null, new Response.Listener<JSONArray>() {
            @Override
            public void onResponse(JSONArray response) {
                for (int i = 0; i < response.length(); i++) {
                    try {
                        JSONObject responseObj = response.getJSONObject(i);

                        String projectID = responseObj.getString("projectID");
                        String studentID = responseObj.getString("studentID");
                        String title = responseObj.getString("title");
                        String description = responseObj.getString("description");
                        String year = responseObj.getString("year");
                        String fname = responseObj.getString("first_Name");
                        String lname = responseObj.getString("second_Name");
                        String photo = responseObj.getString("photo");

                        projectsList.add(new Projects(projectID, studentID, title, description, year, fname, lname, photo));

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                buildView();
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println("Error: " + error);
            }
        });
        queue.add(jsonArrayRequest);
    }

    public void buildView(){
        final TextView textView = (TextView) findViewById(R.id.box);

        for (int i=0; i<projectsList.size(); i++){
            String text = "";

            text += "Project ID: " + projectsList.get(i).getProjectID() + "\n";
            text += "Student ID: " + projectsList.get(i).getStudentID() + "\n";
            text += "Title: " + projectsList.get(i).getTitle() + "\n";
            text += "Description: " + projectsList.get(i).getDescription() + "\n";
            text += "Year: " + projectsList.get(i).getYear() + "\n";
            text += "First Name: " + projectsList.get(i).getFirstName() + "\n";
            text += "Last Name: " + projectsList.get(i).getLastName() + "\n\n";

            textView.append(text);
        }
    }

    public void homeButton(View v){
        Intent intent = new Intent (this, HomeActivity.class);
        startActivity(intent);
    }
}