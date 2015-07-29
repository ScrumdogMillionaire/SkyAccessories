package com.bootcamp.skyapp;

import android.app.Activity;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Typeface;
import android.os.AsyncTask;
import android.support.v4.app.NotificationCompat;
import android.support.v4.app.TaskStackBuilder;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;

import java.util.ArrayList;
import java.util.concurrent.ExecutionException;


public class LandingActivity extends Activity {
    TextView user;
    TextView pass;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_landing);

        String fontPath = "skymed.ttf";
        Typeface tf = Typeface.createFromAsset(getAssets(), fontPath);

        user = (TextView) findViewById(R.id.loginUser);
        user.setTypeface(tf);

        pass = (TextView) findViewById(R.id.loginPass);
        pass.setTypeface(tf);

        Button login = (Button) findViewById(R.id.loginButton);
        login.setTypeface(tf);

        Button signup = (Button) findViewById(R.id.signupButton);
        signup.setTypeface(tf);

        this.startService(new Intent(this, GeofenceService.class));


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_landing, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void loadMenu(View v){

        try {
            RetrieveJSONPost.tryLogin(user.getText().toString(), pass.getText().toString());
            Intent resultIntent = new Intent(this, MainMenu.class);
            startActivity(resultIntent);
        } catch (Exception e) {
            Log.d("This is why", "It failed", e);
            Toast toast = Toast.makeText(
                    this,
                    "Login Failed! :(",
                    Toast.LENGTH_SHORT
            );

            toast.setGravity(Gravity.CENTER_VERTICAL | Gravity.CENTER_HORIZONTAL, 0, 0);
            toast.show();
        }

    }

    public void loadSignup(View v){
        Intent resultIntent = new Intent(this, Signup.class);
        startActivity(resultIntent);
    }
}
