package com.example.projectapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
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

import java.util.HashMap;
import java.util.Map;

public class CreateActivity extends AppCompatActivity {

    String studentID = "";
    String title = "";
    String desc = "";
    String year = "";
    String forename = "";
    String surname = "";
    String photo = "xd";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create);

        Intent intent = getIntent();
        studentID = intent.getStringExtra("id");
        forename = intent.getStringExtra("firstname");
        surname = intent.getStringExtra("lastname");
    }

    public void homeButton(View v){
        Intent intent = new Intent (this, HomeActivity.class);
        startActivity(intent);
    }

    public void getValues(){
        EditText text1 = findViewById(R.id.inputTitle);
        EditText text2 = findViewById(R.id.inputDesc);
        EditText text3 = findViewById(R.id.inputYear);

        title = text1.getText().toString();
        desc = text2.getText().toString();
        year = text3.getText().toString();
    }

    public void createNew(View v){

        String url ="http://web.socem.plymouth.ac.uk/COMP2000/api/students";

        getValues();

        Map<String, Object>  params = new HashMap<String, Object>();
        params.put("studentID", Integer.parseInt(studentID));
        params.put("title", title);
        params.put("description",desc );
        params.put("year", Integer.parseInt(year));
        params.put("first_Name",forename );
        params.put("second_Name", surname);
        params.put("photo", null);

        JSONObject object = new JSONObject(params);

        RequestQueue queue = Volley.newRequestQueue(CreateActivity.this);
        JsonObjectRequest postRequest = new JsonObjectRequest(Request.Method.POST, url, object,
                response -> { },
                error -> {   /* error code here */});

        queue = Volley.newRequestQueue(CreateActivity.this);
        queue.add(postRequest);
        Intent intent = new Intent (this, HomeActivity.class);
        startActivity(intent);
    }
}