package com.bootcamp.skyapp;

import android.app.Activity;
import android.graphics.Typeface;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;


public class AccountPage extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_account_page);

        String fontPath = "skymed.ttf";
        Typeface tf = Typeface.createFromAsset(getAssets(), fontPath);

        TextView username = (TextView) findViewById(R.id.usernameValue);
        username.setTypeface(tf);
        username.setText(User.getInstance().getUsername());

        TextView email = (TextView) findViewById(R.id.emailValue);
        email.setTypeface(tf);
        email.setText(User.getInstance().getEmail());

        TextView points = (TextView) findViewById(R.id.pointsValue);
        points.setTypeface(tf);
        points.setText(User.getInstance().getPoints() + "");

        TextView firstname = (TextView) findViewById(R.id.firstnameValue);
        firstname.setTypeface(tf);
        firstname.setText(User.getInstance().getFirstName());

        TextView lastname = (TextView) findViewById(R.id.lastnameValue);
        lastname.setTypeface(tf);
        lastname.setText(User.getInstance().getLastName());

        TextView user = (TextView) findViewById(R.id.username);
        user.setTypeface(tf);
        TextView em = (TextView) findViewById(R.id.email);
        em.setTypeface(tf);
        TextView point = (TextView) findViewById(R.id.points);
        point.setTypeface(tf);
        TextView fn = (TextView) findViewById(R.id.firstname);
        fn.setTypeface(tf);
        TextView ln = (TextView) findViewById(R.id.lastname);
        ln.setTypeface(tf);

        TextView title = (TextView) findViewById(R.id.accounttitle);
        title.setTypeface(tf);
        TextView editbutton = (TextView) findViewById(R.id.editButton);
        editbutton.setTypeface(tf);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_account_page, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
