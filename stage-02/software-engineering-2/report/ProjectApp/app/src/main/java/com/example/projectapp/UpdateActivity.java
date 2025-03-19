package com.example.projectapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
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

import java.util.HashMap;
import java.util.Map;

public class UpdateActivity extends AppCompatActivity {

    String projectID = "";
    String studentID = "";
    String title = "";
    String desc = "";
    String year = "";
    String forename = "";
    String surname = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_update);

        Intent intent = getIntent();
        studentID = intent.getStringExtra("id");
        forename = intent.getStringExtra("firstname");
        surname = intent.getStringExtra("lastname");

        projectID = intent.getStringExtra("id_project");

        buildView();
    }

    public void buildView(){

        final TextView fname_top = (TextView) findViewById(R.id.forename);
        final TextView lname_top = (TextView) findViewById(R.id.surname);
        final TextView student_top = (TextView) findViewById(R.id.student);

        student_top.append(studentID);
        fname_top.append(forename);
        lname_top.append(surname);
    }

    public void getValues(){
        EditText text1 = findViewById(R.id.inputTitle);
        EditText text2 = findViewById(R.id.inputDesc);
        EditText text3 = findViewById(R.id.inputYear);
        //EditText text4 = findViewById(R.id.inputImage);

        title = text1.getText().toString();
        desc = text2.getText().toString();
        year = text3.getText().toString();
    }

    public void update(){
        String url ="http://web.socem.plymouth.ac.uk/COMP2000/api/students/" + projectID.toString();

        getValues();

        Map<String, Object>  params = new HashMap<String, Object>();
        params.put("studentID", Integer.parseInt(studentID));
        params.put("title", title);
        params.put("description",desc );
        params.put("year", Integer.parseInt(year));
        params.put("first_Name",forename );
        params.put("second_Name", surname);

        JSONObject object = new JSONObject(params);

        RequestQueue queue = Volley.newRequestQueue(UpdateActivity.this);
        JsonObjectRequest putRequest = new JsonObjectRequest(Request.Method.PUT, url, object,
                response -> { /* response code here */},
                error -> {   /* error code here */});

        queue = Volley.newRequestQueue(UpdateActivity.this);
        queue.add(putRequest);
        Intent intent = new Intent (this, HomeActivity.class);
        startActivity(intent);
    }

    public void homeButton(View v){
        Intent intent = new Intent (this, HomeActivity.class);
        startActivity(intent);
    }

    public void submitUpdate(View v){
        Intent intent = new Intent (this, HomeActivity.class);

        update();

        startActivity(intent);
    }

}