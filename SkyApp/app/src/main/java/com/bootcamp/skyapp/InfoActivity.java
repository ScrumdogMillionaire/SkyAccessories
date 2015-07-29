package com.bootcamp.skyapp;

import android.app.Activity;
import android.graphics.Typeface;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;


public class InfoActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);

        String fontPath = "skymed.ttf";
        Typeface tf = Typeface.createFromAsset(getAssets(), fontPath);

        TextView title = (TextView) findViewById(R.id.infotitle);
        title.setTypeface(tf);

        TextView star = (TextView) findViewById(R.id.starText);
        star.setTypeface(tf);

        TextView loc = (TextView) findViewById(R.id.locationText);
        loc.setTypeface(tf);

        TextView user = (TextView) findViewById(R.id.userText);
        user.setTypeface(tf);

        TextView info = (TextView) findViewById(R.id.infoText);
        info.setTypeface(tf);

        TextView log = (TextView) findViewById(R.id.logoutText);
        log.setTypeface(tf);

        TextView ver = (TextView) findViewById(R.id.versionText);
        ver.setTypeface(tf);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_info, menu);
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
