package com.example.projectapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.Image;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

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

public class StudentActivity extends AppCompatActivity {

    private ArrayList<Projects> projectsList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_student);

        Intent intent = getIntent();
        String id = intent.getStringExtra("id");

        projectsList = new ArrayList<>();

        String url ="http://web.socem.plymouth.ac.uk/COMP2000/api/students";

        RequestQueue queue = Volley.newRequestQueue(StudentActivity.this);
        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(Request.Method.GET, url, null, new Response.Listener<JSONArray>() {
            @Override
            public void onResponse(JSONArray response) {
                for (int i = 0; i < response.length(); i++) {
                    try {
                        JSONObject responseObj = response.getJSONObject(i);

                        String studentID = responseObj.getString("studentID");

                        if (id.trim().equals(studentID)) {
                            String projectID = responseObj.getString("projectID");
                            String title = responseObj.getString("title");
                            String description = responseObj.getString("description");
                            String year = responseObj.getString("year");
                            String fname = responseObj.getString("first_Name");
                            String lname = responseObj.getString("second_Name");
                            String photo = responseObj.getString("photo");

                            projectsList.add(new Projects(projectID, studentID, title, description, year, fname, lname, photo));
                        }
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
        final ImageView imageView = (ImageView) findViewById(R.id.image);

        if (projectsList.size()!=0) {

            final TextView fname_top = (TextView) findViewById(R.id.forename);
            final TextView lname_top = (TextView) findViewById(R.id.surname);
            final TextView student_top = (TextView) findViewById(R.id.studentID);

            student_top.append(projectsList.get(0).getStudentID());
            fname_top.append(projectsList.get(0).getFirstName());
            lname_top.append(projectsList.get(0).getLastName());

            for (int i = 0; i < projectsList.size(); i++) {
                String text = "";

                text += "Project ID: " + projectsList.get(i).getProjectID() + "\n";
                text += "Title: " + projectsList.get(i).getTitle() + "\n";
                text += "Description: " + projectsList.get(i).getDescription() + "\n";
                text += "Year: " + projectsList.get(i).getYear() + "\n";

                textView.append(text);

                String image = projectsList.get(i).getPhoto();

                //if the image is not null load the image
                if (image != null){

                    byte[] getImage = Base64.decode(image, Base64.DEFAULT);
                    Bitmap bmp = BitmapFactory.decodeByteArray(getImage, 0, getImage.length);
                    imageView.setImageBitmap(bmp);
                }
            }
        }
    }

    public void homeButton(View v){
        Intent intent = new Intent (this, HomeActivity.class);
        startActivity(intent);
    }

    public void createButton(View v){
        Intent intent = new Intent (this, CreateActivity.class);

        TextView text1 = findViewById(R.id.studentID);
        intent.putExtra("id", text1.getText().toString());

        TextView text2 = findViewById(R.id.forename);
        intent.putExtra("firstname", text2.getText().toString());

        TextView text3 = findViewById(R.id.surname);
        intent.putExtra("lastname", text3.getText().toString());

        startActivity(intent);
    }

    public void deleteButton(View v){
        TextView text = findViewById(R.id.inputID);
        String id = text.getText().toString();

        for(int i=0; i<projectsList.size(); i++){
            if(id.equals(projectsList.get(i).getProjectID())){
                String url ="http://web.socem.plymouth.ac.uk/COMP2000/api/students/" + id.toString();
                RequestQueue queue = Volley.newRequestQueue(StudentActivity.this);
                StringRequest deleteRequest = new StringRequest(Request.Method.DELETE, url,
                        response -> { /* response code here */},
                        error -> {   /* error code here */});

                queue = Volley.newRequestQueue(StudentActivity.this);
                queue.add(deleteRequest);
                break;
            }
        }

        Toast toast=Toast.makeText(getApplicationContext(),"Project deleted",Toast.LENGTH_SHORT);
        toast.show();
    }

    public void updateButton(View v){
        Intent intent = new Intent (this, UpdateActivity.class);

        TextView text1 = findViewById(R.id.studentID);
        intent.putExtra("id", text1.getText().toString());

        TextView text2 = findViewById(R.id.forename);
        intent.putExtra("firstname", text2.getText().toString());

        TextView text3 = findViewById(R.id.surname);
        intent.putExtra("lastname", text3.getText().toString());

        EditText text4 = findViewById(R.id.inputID);
        intent.putExtra("id_project", text4.getText().toString());

        startActivity(intent);
    }
}