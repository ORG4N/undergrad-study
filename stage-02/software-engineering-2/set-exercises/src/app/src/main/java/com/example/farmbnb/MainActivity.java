package com.example.farmbnb;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
    }

    public void createAccount(View v){
        Intent intent = new Intent (this, CreateAccountActivity.class);
        startActivity(intent);
    }

    public void goToHome(View v){

        EditText username   = (EditText)findViewById(R.id.username);
        EditText password   = (EditText)findViewById(R.id.password);

        if (username.getText().toString().trim().length() == 0  || password.getText().toString().trim().length() == 0){

            Context context = this;
            CharSequence text = "Inputs are missing";
            int duration = Toast.LENGTH_LONG;

            Toast toast = Toast.makeText(context, text, duration);

            toast.show();

        }
        else {
            Intent intent = new Intent(this, HomeActivity.class);
            startActivity(intent);
        }

    }
}