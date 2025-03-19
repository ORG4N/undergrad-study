package com.example.farmbnb;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class CreateAccountActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_account);
    }

    public void backToLogin(View v){
        Intent intent = new Intent (this, MainActivity.class);
        startActivity(intent);
    }

    public void goToHome(View v){

        EditText username   = (EditText)findViewById(R.id.username);
        EditText email   = (EditText)findViewById(R.id.email);
        EditText password   = (EditText)findViewById(R.id.password);
        EditText password2   = (EditText)findViewById(R.id.confpassword);


        if (username.getText().toString().trim().length() == 0  || email.getText().toString().trim().length() == 0 || password.getText().toString().trim().length() == 0 || password2.getText().toString().trim().length() == 0){

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
