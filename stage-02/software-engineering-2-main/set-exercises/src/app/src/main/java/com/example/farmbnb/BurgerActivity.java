package com.example.farmbnb;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class BurgerActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_burger);
    }

    public void button_logout(View v){
        Intent intent = new Intent (this, MainActivity.class);
        startActivity(intent);
    }

    public void button_bookings(View v){
        Intent intent = new Intent (this, BookingsActivity.class);
        startActivity(intent);
    }

    public void button_account(View v){
        Intent intent = new Intent (this, AccountActivity.class);
        startActivity(intent);
    }
}
