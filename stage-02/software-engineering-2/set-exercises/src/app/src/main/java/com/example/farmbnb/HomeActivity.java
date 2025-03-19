package com.example.farmbnb;

import android.app.Activity;
import android.app.assist.AssistStructure;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

public class HomeActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        TableLayout tableLayout = findViewById(R.id.table);

        for(int i = 0; i < tableLayout.getChildCount(); i++){
            TableRow tableRow = (TableRow) tableLayout.getChildAt(i);
            tableRow.setId(i);
        }
    }

    public void goToVenue(View v){
        Intent intent = new Intent (this, VenueActivity.class);
        startActivity(intent);
    }

    public void burgermenu(View v){
        Intent intent = new Intent (this, BurgerActivity.class);
        startActivity(intent);
    }

}
