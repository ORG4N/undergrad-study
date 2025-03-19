package com.example.projectapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class HomeActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
    }

    public void submitID(View v){
        Intent intent = new Intent (this, StudentActivity.class);
        EditText text = findViewById(R.id.inputID);
        intent.putExtra("id", text.getText().toString());
        startActivity(intent);
    }

    public void viewAllProjects(View v){
        Intent intent = new Intent (this, ViewAllActivity.class);
        startActivity(intent);
    }

}